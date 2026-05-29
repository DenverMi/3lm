![](_page_0_Picture_0.jpeg)

# **Matter Device Library Specification Version 1.5.1**

Document: 23-27351-009\_Matter-1.5.1-Device-Library-Specification.pdf

March 16,2026

Sponsored by: Connectivity Standards Alliance

Accepted by: This document has been accepted for release by the Connectivity

Standards Alliance Board of Directors on **March 16,2026**

Abstract: The Matter Device Library Specification defines fundamental

requirements for Matter Device Types.

Keywords: Referenced in Chapter 1.

Copyright © 2022-2026 Connectivity Standards Alliance, Inc. 508 Second Street, Suite 109B Davis, CA 95616 - USA www.csa-iot.org All rights reserved.

Permission is granted to members of the Connectivity Standards Alliance to reproduce this document for their own use or the use of other Connectivity Standards Alliance members only, provided this notice is included. All other rights reserved. Duplication for sale, or for commercial or for-profit use is strictly prohibited without the prior written consent of the Connectivity Standards Alliance.

![](_page_2_Picture_0.jpeg)

# Matter Device Library

Version 1.5.1, 2026-03-10 23:04:42 -0700: Approved

# <span id="page-4-0"></span>**Copyright Notice, License and Disclaimer**

Copyright © Connectivity Standards Alliance (2021-2025). All rights reserved. The information within this document is the property of the Connectivity Standards Alliance and its use and disclosure are restricted, except as expressly set forth herein.

Connectivity Standards Alliance hereby grants you a fully-paid, non-exclusive, nontransferable, worldwide, limited and revocable license (without the right to sublicense), under Connectivity Standards Alliance's applicable copyright rights, to view, download, save, reproduce and use the document solely for your own internal purposes and in accordance with the terms of the license set forth herein. This license does not authorize you to, and you expressly warrant that you shall not: (a) permit others (outside your organization) to use this document; (b) post or publish this document; (c) modify, adapt, translate, or otherwise change this document in any manner or create any derivative work based on this document; (d) remove or modify any notice or label on this document, including this Copyright Notice, License and Disclaimer. The Connectivity Standards Alliance does not grant you any license hereunder other than as expressly stated herein.

Elements of this document may be subject to third party intellectual property rights, including without limitation, patent, copyright or trademark rights, and any such third party may or may not be a member of the Connectivity Standards Alliance. Connectivity Standards Alliance members grant other Connectivity Standards Alliance members certain intellectual property rights as set forth in the Connectivity Standards Alliance IPR Policy. Connectivity Standards Alliance members do not grant you any rights under this license. The Connectivity Standards Alliance is not responsible for, and shall not be held responsible in any manner for, identifying or failing to identify any or all such third party intellectual property rights. Please visit www.csa-iot.org for more information on how to become a member of the Connectivity Standards Alliance.

This document and the information contained herein are provided on an "AS IS" basis and the Connectivity Standards Alliance DISCLAIMS ALL WARRANTIES EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO (A) ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OF THIRD PARTIES (INCLUDING WITHOUT LIMITATION ANY INTELLEC-TUAL PROPERTY RIGHTS INCLUDING PATENT, COPYRIGHT OR TRADEMARK RIGHTS); OR (B) ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NONINFRINGEMENT. IN NO EVENT WILL THE CONNECTIVITY STANDARDS ALLIANCE BE LIABLE FOR ANY LOSS OF PROFITS, LOSS OF BUSINESS, LOSS OF USE OF DATA, INTERRUPTION OF BUSI-NESS, OR FOR ANY OTHER DIRECT, INDIRECT, SPECIAL OR EXEMPLARY, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL DAMAGES OF ANY KIND, IN CONTRACT OR IN TORT, IN CONNECTION WITH THIS DOCUMENT OR THE INFORMATION CONTAINED HEREIN, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE.

All company, brand and product names in this document may be trademarks that are the sole property of their respective owners.

This notice and disclaimer must be included on all copies of this document.

Connectivity Standards Alliance 508 Second Street, Suite 206 Davis, CA 95616, USA

# <span id="page-6-0"></span>**Revision History**

| Revision | Date               | Details       | Editor          |
|----------|--------------------|---------------|-----------------|
| 1        | September 23, 2022 | Version 1.0   | Robert Szewczyk |
| 2        | May 17, 2023       | Version 1.1   | Robert Szewczyk |
| 3        | October 18, 2023   | Version 1.2   | Robert Szewczyk |
| 4        | April 17, 2024     | Version 1.3   | Robert Szewczyk |
| 5        | November 4, 2024   | Version 1.4   | Robert Szewczyk |
| 6        | March 17, 2025     | Version 1.4.1 | Robert Szewczyk |
| 7        | July 16, 2025      | Version 1.4.2 | Robert Szewczyk |
| 8        | November 10, 2025  | Version 1.5   | Robert Szewczyk |
| 9        | March 16, 2026     | Version 1.5.1 | Robert Szewczyk |

# **Table of Contents**

| Copyright Notice, License and Disclaimer            | 1  |
|-----------------------------------------------------|----|
| Revision History                                    | 3  |
| References                                          | 20 |
| Connectivity Standards Alliance Reference Documents | 20 |
| Provisional.                                        | 20 |
| List of Provisional Items                           | 20 |
| 1. Base Device Type                                 | 21 |
| 1.1. Base Device Type                               | 21 |
| 1.1.1. Revision History                             | 21 |
| 1.1.2. Overview                                     | 21 |
| 1.1.3. Conditions                                   | 21 |
| 1.1.4. Common Capability Conditions                 | 22 |
| 1.1.5. Device Type Class Conditions                 | 22 |
| 1.1.6. Endpoint Type Class Conditions               | 23 |
| 1.1.7. Cluster Requirements                         | 23 |
| 1.1.8. Element Requirements                         | 23 |
| 2. Utility Device Types                             | 25 |
| 2.1. Root Node Device Type                          | 25 |
| 2.1.1. Revision History                             | 25 |
| 2.1.2. Classification                               | 26 |
| 2.1.3. Conditions                                   | 26 |
| 2.1.4. Device Type Requirements                     | 27 |
| 2.1.5. Cluster Requirements                         |    |
| 2.1.6. Element Requirements                         | 28 |
| 2.1.7. Endpoint Composition                         | 29 |
| 2.2. Power Source Device Type                       | 29 |
| 2.2.1. Revision History                             | 30 |
| 2.2.2. Classification                               | 30 |
| 2.2.3. Cluster Requirements                         | 30 |
| 2.3. OTA Requestor Device Type                      |    |
| 2.3.1. Revision History                             |    |
| 2.3.2. Classification                               |    |
| 2.3.3. Cluster Requirements                         |    |
| 2.4. OTA Provider Device Type                       |    |
| 2.4.1. Revision History                             |    |
| 2.4.2. Classification                               |    |
| 2.4.3. Cluster Requirements                         |    |
| 2.5. Bridged Node Device Type                       |    |
|                                                     |    |

| 2.5.1. Revision History       3         2.5.2. Classification       3         2.5.3. Conditions       3         2.5.4. Device Type Requirements       3         2.5.5. Cluster Requirements       3         2.5.6. Endopoint Composition       3         2.6. Electrical Sensor Device Type       3         2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3         2.9.1. Joint Fabric Architecture       3 |    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| 2.5.3. Conditions       3         2.5.4. Device Type Requirements       3         2.5.5. Cluster Requirements       3         2.5.6. Endpoint Composition       3         2.6. Electrical Sensor Device Type       3         2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.8.9. Joint Fabric Administrator Device Type       3          3       2.9. Joint Fabric Administrator Device Type       3                                                          | 1  |
| 2.5.4. Device Type Requirements       3         2.5.5. Cluster Requirements       3         2.5.6. Endpoint Composition       3         2.6. Electrical Sensor Device Type       3         2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                   | 2  |
| 2.5.5. Cluster Requirements       3         2.5.6. Endpoint Composition       3         2.6. Electrical Sensor Device Type       3         2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                   | 2  |
| 2.5.6. Endpoint Composition       3         2.6. Electrical Sensor Device Type       3         2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                               | 2  |
| 2.6. Electrical Sensor Device Type       3         2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                                        | 2  |
| 2.6.1. Revision History       3         2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                              | 3  |
| 2.6.2. Classification       3         2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                                                                      | 4  |
| 2.6.3. Cluster Requirements       3         2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                                                                                                            | 4  |
| 2.7. Device Energy Management       3         2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 5  |
| 2.7.1. Revision History       3         2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 5  |
| 2.7.2. Classification       3         2.7.3. Conditions       3         2.7.4. Cluster Requirements       3         2.7.5. Element Requirements       3         2.8. Secondary Network Interface Device Type       3         2.8.1. Revision History       3         2.8.2. Classification       3         2.8.3. Cluster Requirements       3         2.9. Joint Fabric Administrator Device Type       3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 5  |
| 2.7.3. Conditions32.7.4. Cluster Requirements32.7.5. Element Requirements32.8. Secondary Network Interface Device Type32.8.1. Revision History32.8.2. Classification32.8.3. Cluster Requirements32.9. Joint Fabric Administrator Device Type3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 5  |
| 2.7.4. Cluster Requirements32.7.5. Element Requirements32.8. Secondary Network Interface Device Type32.8.1. Revision History32.8.2. Classification32.8.3. Cluster Requirements32.9. Joint Fabric Administrator Device Type3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 5  |
| 2.7.5. Element Requirements 3 2.8. Secondary Network Interface Device Type 3 2.8.1. Revision History 3 2.8.2. Classification 3 2.8.3. Cluster Requirements 3 2.9. Joint Fabric Administrator Device Type 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 6  |
| 2.8. Secondary Network Interface Device Type 3 2.8.1. Revision History 3 2.8.2. Classification 3 2.8.3. Cluster Requirements 3 2.9. Joint Fabric Administrator Device Type 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 6  |
| 2.8.1. Revision History32.8.2. Classification32.8.3. Cluster Requirements32.9. Joint Fabric Administrator Device Type3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 6  |
| 2.8.2. Classification32.8.3. Cluster Requirements32.9. Joint Fabric Administrator Device Type3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 7  |
| 2.8.3. Cluster Requirements32.9. Joint Fabric Administrator Device Type3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 7  |
| 2.9. Joint Fabric Administrator Device Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 7  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 7  |
| 2.9.1. Joint Fabric Architecture 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 8  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 8  |
| 2.9.2. Revision History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 8  |
| 2.9.3. Classification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 8  |
| 2.9.4. Cluster Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 8  |
| 3. Application Device Types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :1 |
| 4. Lighting Device Types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :5 |
| 4.1. On/Off Light Device Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :5 |
| 4.1.1. Revision History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :5 |
| 4.1.2. Classification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :5 |
| 4.1.3. Conditions 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :5 |
| 4.1.4. Cluster Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :5 |
| 4.1.5. Element Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 6  |
| 4.2. Dimmable Light Device Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 6  |
| 4.2.1. Revision History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :7 |
| 4.2.2. Classification 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | .7 |
| 4.2.3. Conditions 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :7 |
| 4.2.4. Cluster Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :7 |
| 4.2.5. Element Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :7 |
| 4.3. Color Temperature Light Device Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 8  |
| 4.3.1. Revision History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 8  |

| 4     | 4.3.2. Classification                       | 48 |
|-------|---------------------------------------------|----|
| 4     | 4.3.3. Conditions                           | 48 |
| 4     | 4.3.4. Cluster Requirements                 | 49 |
| 4     | 4.3.5. Element Requirements                 | 49 |
| 4.4   | . Extended Color Light Device Type          | 50 |
| 4     | 4.4.1. Revision History                     | 50 |
| 4     | 4.4.2. Classification                       | 50 |
| 4     | 1.4.3. Conditions                           | 50 |
| 4     | 1.4.4. Cluster Requirements                 | 50 |
| 4     | 1.4.5. Element Requirements                 | 51 |
| 5. Sm | art Plugs/Outlets and other Actuators       | 53 |
| 5.1   | . On/Off Plug-in Unit Device Type           | 53 |
| !     | 5.1.1. Revision History                     | 53 |
| !     | 5.1.2. Classification                       | 54 |
| ļ     | 5.1.3. Conditions                           | 54 |
| ļ     | 5.1.4. Cluster Requirements                 | 54 |
|       | 5.1.5. Element Requirements                 |    |
|       | . Dimmable Plug-In Unit Device Type         |    |
|       | 5.2.1. Revision History                     |    |
| ļ     | 5.2.2. Classification                       | 56 |
| ļ     | 5.2.3. Conditions                           | 56 |
| ļ     | 5.2.4. Cluster Requirements                 | 57 |
|       | 5.2.5. Element Requirements                 |    |
| 5.3   | . Mounted On/Off Control Device Type        | 57 |
|       | 5.3.1. Revision History                     |    |
|       | 5.3.2. Classification                       |    |
|       | 5.3.3. Conditions                           |    |
| ļ     | 5.3.4. Cluster Requirements                 | 58 |
|       | 5.3.5. Element Requirements                 |    |
|       | . Mounted Dimmable Load Control Device Type |    |
|       | 5.4.1. Revision History                     |    |
|       | 5.4.2. Classification                       |    |
|       | 5.4.3. Conditions                           |    |
|       | 5.4.4. Cluster Requirements                 |    |
|       | 5.4.5. Element Requirements                 |    |
|       | . Pump Device Type                          |    |
|       | 5.5.1. Revision History                     |    |
|       | 5.5.2. Classification                       |    |
|       | 5.5.3. Conditions                           |    |
|       | 5.5.4. Cluster Requirements                 |    |
|       | 5.5.5. Cluster Restrictions                 |    |
| •     | J.J. CIUSTOI INCOLLICUOLIS                  | UΖ |

| 5.6. Water Valve Device Type                 | 63 |
|----------------------------------------------|----|
| 5.6.1. Revision History                      |    |
| 5.6.2. Classification                        |    |
| 5.6.3. Conditions                            | 64 |
| 5.6.4. Cluster Requirements                  | 64 |
| 5.6.5. Device implementation recommendations | 64 |
| 5.7. Irrigation System Device Type           | 65 |
| 5.7.1. Irrigation System Architecture        | 65 |
| 5.7.2. Revision History                      | 65 |
| 5.7.3. Classification                        | 65 |
| 5.7.4. Conditions                            | 66 |
| 5.7.5. Device Type Requirements              | 66 |
| 5.7.6. Cluster Requirements                  | 66 |
| 6. Switches and Controls Device Types        | 69 |
| 6.1. On/Off Light Switch Device type         | 69 |
| 6.1.1. Revision History                      | 69 |
| 6.1.2. Classification                        | 69 |
| 6.1.3. Conditions                            | 69 |
| 6.1.4. Cluster Requirements                  | 70 |
| 6.2. Dimmer Switch Device Type               | 70 |
| 6.2.1. Revision History                      | 70 |
| 6.2.2. Classification                        | 70 |
| 6.2.3. Conditions                            | 70 |
| 6.2.4. Cluster Requirements                  | 70 |
| 6.3. Color Dimmer Switch Device Type         | 71 |
| 6.3.1. Revision History                      | 71 |
| 6.3.2. Classification                        | 71 |
| 6.3.3. Conditions                            | 71 |
| 6.3.4. Cluster Requirements                  | 71 |
| 6.4. Control Bridge Device Type              | 72 |
| 6.4.1. Revision History                      | 72 |
| 6.4.2. Classification                        | 72 |
| 6.4.3. Conditions                            | 72 |
| 6.4.4. Cluster Requirements                  | 72 |
| 6.5. Pump Controller Device Type             | 73 |
| 6.5.1. Revision History                      | 73 |
| 6.5.2. Classification                        | 73 |
| 6.5.3. Conditions                            | 73 |
| 6.5.4. Cluster Requirements                  | 73 |
| 6.6. Generic Switch Device Type              | 74 |
| 6.6.1. Revision History                      | 74 |

| · · · · · · · · · · · · · · · · · · ·                        | ,  |
|--------------------------------------------------------------|----|
| 6.6.2. Classification                                        | 74 |
| 6.6.3. Conditions                                            | 75 |
| 6.6.4. Cluster Requirements                                  | 75 |
| 6.6.5. Relation with other Switch device types (informative) | 77 |
| 7. Sensor Device Types                                       | 79 |
| 7.1. Contact Sensor Device Type                              | 79 |
| 7.1.1. Revision History                                      | 79 |
| 7.1.2. Classification                                        |    |
| 7.1.3. Conditions                                            |    |
| 7.1.4. Cluster Requirements                                  |    |
| 7.2. Light Sensor Device Type                                | 80 |
| 7.2.1. Revision History                                      | 80 |
| 7.2.2. Classification                                        | 80 |
| 7.2.3. Conditions                                            | 80 |
| 7.2.4. Cluster Requirements                                  | 80 |
| 7.3. Occupancy Sensor Device Type                            | 81 |
| 7.3.1. Revision History                                      |    |
| 7.3.2. Classification                                        | 81 |
| 7.3.3. Conditions                                            | 81 |
| 7.3.4. Cluster Requirements                                  | 81 |
| 7.3.5. Multi-modality sensors                                | 82 |
| 7.4. Temperature Sensor Device Type                          | 82 |
| 7.4.1. Revision History                                      | 82 |
| 7.4.2. Classification                                        | 82 |
| 7.4.3. Conditions                                            | 83 |
| 7.4.4. Cluster Requirements                                  | 83 |
| 7.4.5. Element Requirements                                  | 83 |
| 7.5. Pressure Sensor Device Type                             | 83 |
| 7.5.1. Revision History                                      | 84 |
| 7.5.2. Classification                                        |    |
| 7.5.3. Conditions                                            | 84 |
| 7.5.4. Cluster Requirements                                  | 84 |
| 7.6. Flow Sensor Device Type                                 | 84 |
| 7.6.1. Revision History                                      | 84 |
| 7.6.2. Classification                                        | 84 |
| 7.6.3. Conditions                                            | 85 |
| 7.6.4. Cluster Requirements                                  | 85 |
| 7.7. Humidity Sensor Device Type                             | 85 |
| 7.7.1. Revision History                                      |    |
| 7.7.2. Classification                                        | 85 |
| 7.7.3. Conditions                                            | 85 |
|                                                              |    |

| 7.7.4. Cluster Requirements             |    |
|-----------------------------------------|----|
| 7.8. On/Off Sensor Device Type.         |    |
| 7.8.1. Revision History                 |    |
| 7.8.2. Classification                   |    |
| 7.8.3. Conditions                       |    |
| 7.8.4. Cluster Requirements             |    |
| 7.9. Smoke CO Alarm Device Type         |    |
| 7.9.1. Revision History                 |    |
| 7.9.2. Classification                   |    |
| 7.9.3. Conditions                       |    |
| 7.9.4. Device Type Requirements         |    |
| 7.9.5. Cluster Requirements             | 87 |
| 7.10. Air Quality Sensor Device Type.   |    |
| 7.10.1. Revision History                |    |
| 7.10.2. Classification                  |    |
| 7.10.3. Conditions                      |    |
| 7.10.4. Cluster Requirements            |    |
| 7.11. Water Freeze Detector Device Type |    |
| 7.11.1. Revision History                |    |
| 7.11.2. Classification                  |    |
| 7.11.3. Conditions                      | 90 |
| 7.11.4. Cluster Requirements            | 90 |
| 7.11.5. Element Requirements            | 91 |
| 7.12. Water Leak Detector Device Type   | 91 |
| 7.12.1. Revision History                | 91 |
| 7.12.2. Classification                  | 91 |
| 7.12.3. Conditions                      | 91 |
| 7.12.4. Cluster Requirements            | 91 |
| 7.12.5. Element Requirements            | 92 |
| 7.13. Rain Sensor Device Type.          | 92 |
| 7.13.1. Revision History                | 92 |
| 7.13.2. Classification                  | 92 |
| 7.13.3. Conditions                      | 92 |
| 7.13.4. Cluster Requirements            | 93 |
| 7.13.5. Element Requirements            | 93 |
| 7.14. Soil Sensor Device Type           | 93 |
| 7.14.1. Revision History                |    |
| 7.14.2. Classification                  | 94 |
| 7.14.3. Conditions                      | 94 |
| 7.14.4. Cluster Requirements            |    |
| 8. Entry Control Device Types           | 95 |

| 8.1   | . Door Lock Device Type                   | . 95 |
|-------|-------------------------------------------|------|
|       | 8.1.1. Revision History                   | . 95 |
|       | 8.1.2. Classification                     | . 95 |
|       | 8.1.3. Conditions                         | . 95 |
|       | 8.1.4. Condition Requirements             | . 95 |
|       | 8.1.5. Cluster Requirements               | . 96 |
| 8.2   | 2. Door Lock Controller Device Type       | . 96 |
|       | 8.2.1. Revision History                   | . 96 |
|       | 8.2.2. Classification                     | . 96 |
|       | 8.2.3. Conditions                         | . 96 |
|       | 8.2.4. Condition Requirements             | . 96 |
|       | 8.2.5. Cluster Requirements               | . 97 |
| 8.3   | 3. Window Covering Device Type            | . 97 |
|       | 8.3.1. Revision History                   | . 97 |
|       | 8.3.2. Classification                     | . 97 |
|       | 8.3.3. Conditions                         | . 97 |
|       | 8.3.4. Cluster Requirements               | . 97 |
| 8.4   | l. Window Covering Controller Device Type | . 98 |
|       | 8.4.1. Revision History                   | . 98 |
|       | 8.4.2. Classification                     | . 98 |
|       | 8.4.3. Conditions                         | . 98 |
|       | 8.4.4. Cluster Requirements               | . 98 |
| 8.5   | S. Closure Device Type                    | . 99 |
|       | 8.5.1. Closure Architecture               | . 99 |
|       | 8.5.2. Revision History                   | 101  |
|       | 8.5.3. Classification                     | 101  |
|       | 8.5.4. Device Type Requirements           | 101  |
|       | 8.5.5. Cluster Requirements               | 102  |
|       | 8.5.6. Element Requirements               | 102  |
| 8.6   | S. Closure Panel Device Type              | 103  |
|       | 8.6.1. Revision History                   | 103  |
|       | 8.6.2. Classification                     | 103  |
|       | 8.6.3. Cluster Requirements               | 103  |
|       | 8.6.4. Element Requirements               | 103  |
| 8.7   | 7. Closure Controller Device Type         | 104  |
|       | 8.7.1. Introduction                       |      |
|       | 8.7.2. Revision History                   | 104  |
|       | 8.7.3. Classification                     | 105  |
|       | 8.7.4. Conditions                         | 105  |
|       | 8.7.5. Cluster Requirements               | 105  |
| 9. HV | AC Device Types                           | 107  |

| 9.1. Thermostat Device Type 107                                             |  |
|-----------------------------------------------------------------------------|--|
| 9.1.1. Revision History 107                                                 |  |
| 9.1.2. Classification 107                                                   |  |
| 9.1.3. Conditions 107                                                       |  |
| 9.1.4. Cluster Requirements 107                                             |  |
| 9.2. Fan Device Type 108                                                    |  |
| 9.2.1. Revision History 108                                                 |  |
| 9.2.2. Classification 108                                                   |  |
| 9.2.3. Conditions 108                                                       |  |
| 9.2.4. Device Type Requirements 109                                         |  |
| 9.2.5. Cluster Requirements 109                                             |  |
| 9.2.6. Cluster Restrictions 109                                             |  |
| 9.3. Air Purifier Device Type 109                                           |  |
| 9.3.1. Revision History 110                                                 |  |
| 9.3.2. Classification 110                                                   |  |
| 9.3.3. Conditions 110                                                       |  |
| 9.3.4. Device Type Requirements 110                                         |  |
| 9.3.5. Cluster Requirements 110                                             |  |
| 9.3.6. Cluster Restrictions 111                                             |  |
| 9.4. Thermostat Controller Device Type 111                                  |  |
| 9.4.1. Revision History 111                                                 |  |
| 9.4.2. Classification 111                                                   |  |
| 9.4.3. Conditions 111                                                       |  |
| 9.4.4. Cluster Requirements 111                                             |  |
| 10. Media Device Types 113                                                  |  |
| 10.1. Video Player Architecture 113                                         |  |
| 10.1.1. Introduction 113                                                    |  |
| 10.1.2. Clients of a Casting Video Player 114                               |  |
| 10.1.3. Endpoint Composition for Content Apps of a Casting Video Player 114 |  |
| 10.1.4. Commissioning 115                                                   |  |
| 10.1.5. Determining Context 117                                             |  |
| 10.1.6. Basic Video Player Features 118                                     |  |
| 10.1.7. Content Launching Features 119                                      |  |
| 10.2. Basic Video Player Device Type 120                                    |  |
| 10.2.1. Revision History 120                                                |  |
| 10.2.2. Classification 120                                                  |  |
| 10.2.3. Conditions 120                                                      |  |
| 10.2.4. Cluster Requirements 121                                            |  |
| 10.3. Casting Video Player Device Type 121                                  |  |
| 10.3.1. Revision History 121                                                |  |
| 10.3.2. Classification 122                                                  |  |

| 10.3.3. Conditions.                      | 122 |
|------------------------------------------|-----|
| 10.3.4. Cluster Requirements             | 122 |
| 10.3.5. Element Requirements             | 123 |
| 10.4. Speaker Device Type                | 123 |
| 10.4.1. Revision History                 | 123 |
| 10.4.2. Classification                   | 123 |
| 10.4.3. Conditions                       | 124 |
| 10.4.4. Cluster Requirements             | 124 |
| 10.5. Content App Device Type            | 124 |
| 10.5.1. Revision History                 | 124 |
| 10.5.2. Classification                   | 124 |
| 10.5.3. Conditions                       | 124 |
| 10.5.4. Cluster Requirements             | 125 |
| 10.5.5. Element Requirements             | 125 |
| 10.5.6. Endpoint Composition             | 125 |
| 10.5.7. Disambiguation                   | 125 |
| 10.6. Casting Video Client Device Type   | 125 |
| 10.6.1. Revision History                 | 126 |
| 10.6.2. Classification                   | 126 |
| 10.6.3. Conditions                       | 126 |
| 10.6.4. Cluster Requirements             | 126 |
| 10.7. Video Remote Control Device Type   | 127 |
| 10.7.1. Revision History                 | 127 |
| 10.7.2. Classification                   | 127 |
| 10.7.3. Conditions                       | 127 |
| 10.7.4. Cluster Requirements             | 127 |
| 11. Generic Device Types                 | 129 |
| 11.1. Mode Select Device Type            | 129 |
| 11.1.1. Revision History                 | 129 |
| 11.1.2. Classification                   | 129 |
| 11.1.3. Conditions                       | 129 |
| 11.1.4. Cluster Requirements             | 129 |
| 11.2. Aggregator Device Type             | 129 |
| 11.2.1. Revision History                 | 129 |
| 11.2.2. Classification                   | 130 |
| 11.2.3. Conditions                       | 130 |
| 11.2.4. Cluster Requirements             | 130 |
| 11.2.5. Endpoint Composition             | 130 |
| 11.2.6. Disambiguation                   | 132 |
| 12. Robotic Device Types                 | 135 |
| 12.1. Robotic Vacuum Cleaner Device Type | 135 |

| 12.1.1. Revision History 135                         |  |
|------------------------------------------------------|--|
| 12.1.2. Classification 135                           |  |
| 12.1.3. Conditions 135                               |  |
| 12.1.4. Cluster Requirements 135                     |  |
| 12.1.5. Element Requirements 136                     |  |
| 12.1.6. Cluster Usage 136                            |  |
| 13. Appliances Device Types 139                      |  |
| 13.1. Laundry Washer Device Type 139                 |  |
| 13.1.1. Revision History 139                         |  |
| 13.1.2. Classification 139                           |  |
| 13.1.3. Conditions 139                               |  |
| 13.1.4. Cluster Requirements 139                     |  |
| 13.1.5. Cluster Restrictions 140                     |  |
| 13.1.6. Element Requirements 140                     |  |
| 13.2. Refrigerator Device Type 141                   |  |
| 13.2.1. Refrigerator Architecture 141                |  |
| 13.2.2. Revision History 142                         |  |
| 13.2.3. Classification 142                           |  |
| 13.2.4. Conditions 142                               |  |
| 13.2.5. Condition Requirements 142                   |  |
| 13.2.6. Device Type Requirements 143                 |  |
| 13.2.7. Cluster Requirements 143                     |  |
| 13.2.8. Element Requirements 143                     |  |
| 13.3. Room Air Conditioner Device Type 144           |  |
| 13.3.1. Room Air Conditioner Architecture 144        |  |
| 13.3.2. Revision History 145                         |  |
| 13.3.3. Classification 145                           |  |
| 13.3.4. Conditions 145                               |  |
| 13.3.5. Device Type Requirements 145                 |  |
| 13.3.6. Cluster Requirements 145                     |  |
| 13.3.7. Cluster Restrictions 146                     |  |
| 13.3.8. Element Requirements 146                     |  |
| 13.4. Temperature Controlled Cabinet Device Type 147 |  |
| 13.4.1. Revision History 147                         |  |
| 13.4.2. Classification 147                           |  |
| 13.4.3. Conditions 147                               |  |
| 13.4.4. Cluster Requirements 148                     |  |
| 13.4.5. Element Requirements 148                     |  |
| 13.5. Dishwasher Device Type 149                     |  |
| 13.5.1. Revision History 149                         |  |
| 13.5.2. Classification 149                           |  |

| 13.5.3. Conditions                | 149 |
|-----------------------------------|-----|
| 13.5.4. Cluster Requirements      | 150 |
| 13.5.5. Cluster Restrictions      | 150 |
| 13.5.6. Element Requirements      | 151 |
| 13.6. Laundry Dryer Device Type.  | 151 |
| 13.6.1. Revision History          | 151 |
| 13.6.2. Classification            | 151 |
| 13.6.3. Conditions                | 152 |
| 13.6.4. Cluster Requirements      | 152 |
| 13.6.5. Cluster Restrictions      | 152 |
| 13.6.6. Element Requirements      | 153 |
| 13.7. Cook Surface Device Type    | 153 |
| 13.7.1. Revision History          | 153 |
| 13.7.2. Classification            | 154 |
| 13.7.3. Conditions.               | 154 |
| 13.7.4. Cluster Requirements      | 154 |
| 13.7.5. Cluster Restrictions      | 154 |
| 13.7.6. Element Requirements      | 154 |
| 13.8. Cooktop Device Type         | 155 |
| 13.8.1. Revision History          | 155 |
| 13.8.2. Classification            | 155 |
| 13.8.3. Conditions                | 155 |
| 13.8.4. Device Type Requirements  | 155 |
| 13.8.5. Cluster Requirements      | 156 |
| 13.8.6. Cluster Restrictions      | 156 |
| 13.8.7. Element Requirements      | 156 |
| 13.9. Oven Device Type.           | 156 |
| 13.9.1. Oven Architecture         | 156 |
| 13.9.2. Revision History          | 157 |
| 13.9.3. Classification            | 157 |
| 13.9.4. Conditions                | 157 |
| 13.9.5. Condition Requirements    | 157 |
| 13.9.6. Device Type Requirements. | 158 |
| 13.9.7. Cluster Requirements      | 158 |
| 13.10. Extractor Hood Device Type | 158 |
| 13.10.1. Revision History         | 159 |
| 13.10.2. Classification           | 159 |
| 13.10.3. Conditions               | 159 |
| 13.10.4. Device Type Requirements | 159 |
| 13.10.5. Cluster Requirements     | 159 |
| 13.10.6. Element Requirements     | 160 |

| 13.11. Microwave Oven Device Type 160    |  |
|------------------------------------------|--|
| 13.11.1. Microwave Oven Architecture 160 |  |
| 13.11.2. Revision History 161            |  |
| 13.11.3. Classification 161              |  |
| 13.11.4. Conditions 161                  |  |
| 13.11.5. Device Type Requirements 161    |  |
| 13.11.6. Cluster Requirements 162        |  |
| 13.11.7. Element Requirements 162        |  |
| 13.11.8. Cluster Usage 162               |  |
| 14. Energy Device Types 165              |  |
| 14.1. EVSE Device Type 165               |  |
| 14.1.1. EVSE Architecture 165            |  |
| 14.1.2. Revision History 166             |  |
| 14.1.3. Classification 166               |  |
| 14.1.4. Conditions 166                   |  |
| 14.1.5. Cluster Requirements 166         |  |
| 14.1.6. Device Type Requirements 167     |  |
| 14.2. Water Heater Device Type 168       |  |
| 14.2.1. Water Heater Architecture 168    |  |
| 14.2.2. Revision History 169             |  |
| 14.2.3. Classification 169               |  |
| 14.2.4. Conditions 169                   |  |
| 14.2.5. Cluster Requirements 169         |  |
| 14.2.6. Element Requirements 170         |  |
| 14.2.7. Device Type Requirements 170     |  |
| 14.3. Solar Power Device Type 171        |  |
| 14.3.1. Solar Power Architecture 171     |  |
| 14.3.2. Revision History 173             |  |
| 14.3.3. Classification 173               |  |
| 14.3.4. Conditions 173                   |  |
| 14.3.5. Cluster Requirements 173         |  |
| 14.3.6. Device Type Requirements 173     |  |
| 14.4. Battery Storage Device Type 176    |  |
| 14.4.1. Battery Storage Architecture 176 |  |
| 14.4.2. Revision History 177             |  |
| 14.4.3. Classification 178               |  |
| 14.4.4. Conditions 178                   |  |
| 14.4.5. Cluster Requirements 178         |  |
| 14.4.6. Device Type Requirements 178     |  |
| 14.5. Heat Pump Device Type 183          |  |
| 14.5.1. Heat Pump Architecture 183       |  |

| 14.5.2. Revision History 183                         |  |
|------------------------------------------------------|--|
| 14.5.3. Classification 184                           |  |
| 14.5.4. Conditions 184                               |  |
| 14.5.5. Cluster Requirements 184                     |  |
| 14.5.6. Device Type Requirements 184                 |  |
| 14.6. Meter Reference Point Device Type 187          |  |
| 14.6.1. Revision History 187                         |  |
| 14.6.2. Classification 187                           |  |
| 14.6.3. Conditions 187                               |  |
| 14.6.4. Condition Requirements 187                   |  |
| 14.6.5. Cluster Requirements 188                     |  |
| 14.6.6. Device Type Requirements 188                 |  |
| 14.6.7. Meter Reference Point Topology 188           |  |
| 14.7. Electrical Energy Tariff Device Type 193       |  |
| 14.7.1. Revision History 193                         |  |
| 14.7.2. Classification 193                           |  |
| 14.7.3. Conditions 193                               |  |
| 14.7.4. Cluster Requirements 193                     |  |
| 14.7.5. Element Requirements 193                     |  |
| 14.7.6. Semantic Tag Requirements 194                |  |
| 14.8. Electrical Meter Device Type 194               |  |
| 14.8.1. Revision History 194                         |  |
| 14.8.2. Classification 194                           |  |
| 14.8.3. Device Type Requirements 194                 |  |
| 14.8.4. Cluster Requirements 194                     |  |
| 14.9. Electrical Utility Meter Device Type 195       |  |
| 14.9.1. Revision History 195                         |  |
| 14.9.2. Classification 195                           |  |
| 14.9.3. Conditions 195                               |  |
| 14.9.4. Condition Requirements 195                   |  |
| 14.9.5. Cluster Requirements 195                     |  |
| 14.9.6. Electrical Utility Meter Topology 196        |  |
| 15. Network Infrastructure Device Types 201          |  |
| 15.1. Introduction 201                               |  |
| 15.2. Common Requirements 201                        |  |
| 15.2.1. Minimum Number of Devices to Support 201     |  |
| 15.3. Network Infrastructure Manager Device Type 201 |  |
| 15.3.1. Revision History 202                         |  |
| 15.3.2. Classification 202                           |  |
| 15.3.3. Conditions 202                               |  |
| 15.3.4. Cluster Requirements 202                     |  |
|                                                      |  |

| 15.3.5. Condition Requirements 202                         |  |
|------------------------------------------------------------|--|
| 15.3.6. Other Requirements 203                             |  |
| 15.4. Thread Border Router Device Type 205                 |  |
| 15.4.1. Revision History 205                               |  |
| 15.4.2. Classification 206                                 |  |
| 15.4.3. Conditions 206                                     |  |
| 15.4.4. Device Type Requirements 206                       |  |
| 15.4.5. Cluster Requirements 206                           |  |
| 15.4.6. Other Requirements 206                             |  |
| 15.4.7. Cluster Usage 207                                  |  |
| 16. Camera Device Types 211                                |  |
| 16.1. Camera Device Type 211                               |  |
| 16.1.1. Revision History 211                               |  |
| 16.1.2. Classification 211                                 |  |
| 16.1.3. Conditions 211                                     |  |
| 16.1.4. Device Type Requirements 211                       |  |
| 16.1.5. Condition Requirements 211                         |  |
| 16.1.6. Cluster Requirements 212                           |  |
| 16.1.7. Element Requirements 213                           |  |
| 16.2. Floodlight Camera Device Type 213                    |  |
| 16.2.1. Revision History 213                               |  |
| 16.2.2. Classification 213                                 |  |
| 16.2.3. Conditions 213                                     |  |
| 16.2.4. Device Type Requirements 213                       |  |
| 16.3. Video Doorbell Device Type 214                       |  |
| 16.3.1. Revision History 214                               |  |
| 16.3.2. Classification 214                                 |  |
| 16.3.3. Device Type Requirements 214                       |  |
| 16.4. Intercom Device Type 214                             |  |
| 16.4.1. Revision History 215                               |  |
| 16.4.2. Classification 215                                 |  |
| 16.4.3. Conditions 215                                     |  |
| 16.4.4. Device Type Requirements 215                       |  |
| 16.4.5. Condition Requirements 215                         |  |
| 16.4.6. Cluster Requirements 216                           |  |
| 16.4.7. Element Requirements 216                           |  |
| 16.4.8. Element Requirements on Component Device Types 217 |  |
| 16.5. Audio Doorbell Device Type 217                       |  |
| 16.5.1. Revision History 217                               |  |
| 16.5.2. Classification 217                                 |  |
| 16.5.3. Condition Requirements 218                         |  |
|                                                            |  |

| Matter Device Library | Connectivity Standards Alliance Document 23-27351 March 16, 2026 |
|-----------------------|------------------------------------------------------------------|
|                       | 16.5.4. Cluster Requirements 218                                 |
|                       | 16.5.5. Element Requirements 218                                 |
|                       | 16.6. Snapshot Camera Device Type 219                            |
|                       | 16.6.1. Revision History 219                                     |
|                       | 16.6.2. Classification 219                                       |
|                       | 16.6.3. Conditions 219                                           |
|                       | 16.6.4. Device Type Requirements 219                             |
|                       | 16.6.5. Condition Requirements 220                               |
|                       | 16.6.6. Cluster Requirements 220                                 |
|                       | 16.6.7. Element Requirements 220                                 |
|                       | 16.7. Chime Device Type 221                                      |
|                       | 16.7.1. Revision History 221                                     |
|                       | 16.7.2. Classification 221                                       |
|                       | 16.7.3. Conditions 221                                           |
|                       | 16.7.4. Cluster Requirements 221                                 |
|                       | 16.7.5. Element Requirements 221                                 |
|                       | 16.8. Camera Controller Device Type 222                          |
|                       | 16.8.1. Revision History 222                                     |
|                       | 16.8.2. Classification 222                                       |
|                       | 16.8.3. Cluster Requirements 222                                 |
|                       | 16.9. Doorbell Device Type 223                                   |
|                       | 16.9.1. Revision History 223                                     |
|                       | 16.9.2. Classification 223                                       |

# <span id="page-23-0"></span>**References**

The following standards and specifications contain provisions, which through reference in this document constitute provisions of this specification. All the standards and specifications listed are normative references. At the time of publication, the editions indicated were valid. All standards and specifications are subject to revision, and parties to agreements based on this specification are encouraged to investigate the possibility of applying the most recent editions of the standards and specifications indicated below.

#### <span id="page-23-1"></span>**Connectivity Standards Alliance Reference Documents**

<span id="page-23-6"></span><span id="page-23-5"></span><span id="page-23-4"></span>

| Reference                 | Reference Location/URL                                           | Description                                                  |
|---------------------------|------------------------------------------------------------------|--------------------------------------------------------------|
| [Alliance<br>PNP]         | https://groups.csa-iot.org/wg/<br>members/document/21624         | Alliance Organizational Processes and Procedures,<br>13-0625 |
| [Certification<br>Policy] | https://groups.csa-iot.org/wg/<br>members-all/document/125       | Alliance Certification Policy, 15-0288                       |
| [MatterCore]              | https://groups.csa-iot.org/wg/<br>members-all/document/<br>27349 | Matter Core Specification                                    |
| [MatterApp<br>Clusters]   | https://groups.csa-iot.org/wg/<br>members-all/document/<br>27350 | Matter Application Cluster Specification                     |

# <span id="page-23-2"></span>**Provisional**

Per [\[Alliance-PNP\],](#page-23-4) when a specification is completed there may be sections of specification text (or smaller pieces of a section) that are not certifiable at this stage. These sections (or smaller pieces of a section) are marked as provisional prior to publishing the specification. This specification uses well-defined notation to mark Provisional Conformance (see [\[MatterCore\]](#page-23-5), Section 7.3) or notes a section of text with the term "provisional".

### <span id="page-23-3"></span>**List of Provisional Items**

The following is a list of provisional items.

# <span id="page-24-0"></span>**Chapter 1. Base Device Type**

This chapter describes the [base device type.](#page-24-1)

# <span id="page-24-1"></span>**1.1. Base Device Type**

#### <span id="page-24-2"></span>**1.1.1. Revision History**

Because this document defines common requirements for all device types, changes to this document does affect all device types. Therefore, all device type definitions SHALL have its revision number incremented, with a new entry added to its history with a description that matches the description here, or state that the base device type is updated.

| Revision | Description                                     |
|----------|-------------------------------------------------|
| 1        | Initial revision                                |
| 2        | Duplicate condition replaces Multiple condition |
| 3        | Removed certification program conditions        |

#### <span id="page-24-3"></span>**1.1.2. Overview**

This defines common conformance for all device types depending on, but not limited to:

- Underlying protocol stack (e.g. 802.15.4, Wi-Fi, Thread, Zigbee PRO, IPv6, TCP/IP)
- Regional regulations
- Interfaces (UI, cloud, etc.)
- Scale (e.g. residential vs commercial)
- Other common limitations or capabilities (e.g. battery powered or sleepy nodes).
- etc.

#### <span id="page-24-4"></span>**1.1.3. Conditions**

Each section below is a category of conditions, each defining a list of conformance condition names and unique tags. The separation into categories is for reading purposes only.

#### **1.1.3.1. Protocol Conditions**

| Protocol Tag |  |
|--------------|--|
| Ethernet     |  |
| Wi-Fi        |  |
| Thread       |  |
| TCP          |  |
| UDP          |  |

| Protocol Tag |  |
|--------------|--|
| IP           |  |
| IPv4         |  |
| IPv6         |  |

#### **1.1.3.2. Interface Conditions**

| Interface Tag  | Description                                                                  |
|----------------|------------------------------------------------------------------------------|
| LanguageLocale | The node supports localization for conveying<br>text to the user             |
| TimeLocale     | The node supports localization for conveying<br>time to the user             |
| UnitLocale     | The node supports localization for conveying<br>units of measure to the user |

Note that "supports localization" in the table above refers to supporting update of localization via cluster interactions.

### <span id="page-25-0"></span>**1.1.4. Common Capability Conditions**

This category is for common limitations or capabilities of a node.

| Capability Tag | Description                                                       |
|----------------|-------------------------------------------------------------------|
| SIT            | The node is a short idle time intermittently con<br>nected device |
| LIT            | The node is a long idle time intermittently con<br>nected device  |
| Active         | The node is always able to communicate                            |

# <span id="page-25-1"></span>**1.1.5. Device Type Class Conditions**

This category is for classifications of device type. Some of these classifications are dependent on other conditions.

| Class Tag | Summary                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------|
| Node      | the device type is classified as a Node device<br>type (see Data Model specification)         |
| App       | the device type is classified as an Application<br>device type (see Data Model specification) |
| Simple    | the device type is classified as a Simple device<br>type (see Data Model specification)       |

| Class Tag | Summary                                                                                   |
|-----------|-------------------------------------------------------------------------------------------|
| Dynamic   | the device type is classified as a Dynamic device<br>type (see Data Model specification)  |
| Composed  | the device type is composed of 2 or more device<br>types (see System Model specification) |

#### <span id="page-26-0"></span>**1.1.6. Endpoint Type Class Conditions**

This category is for classifications of endpoints. Some of these classifications are dependent on other conditions.

| Class Tag              | Summary                                                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Client                 | there exists a client application cluster on the<br>endpoint                                                                         |
| Server                 | there exists a server application cluster on the<br>endpoint                                                                         |
| Duplicate              | the endpoint and at least one of its siblings have<br>overlap in application device type(s)                                          |
| BridgedPowerSourceInfo | the endpoint represents a Bridged Device, for<br>which information about the state of its power<br>source is available to the Bridge |

#### <span id="page-26-3"></span>**1.1.6.1. Duplicate Condition**

The endpoint and at least one of its sibling endpoints have an overlap in application device type(s), as defined in the "Disambiguation" section in the System Model specification. This condition triggers requirements for providing additional information about the endpoints in order to disambiguate between the endpoints (see "Disambiguation" section in the System Model specification).

# <span id="page-26-1"></span>**1.1.7. Cluster Requirements**

Each Matter device type implementation SHALL include these clusters, as a minimum set, based on the conformance defined below. This conformance table SHALL assume the Matter conformance condition is TRUE (in Conformance column).

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance     |
|------------|--------------|---------------|---------|-----------------|
| 0x001D     | Descriptor   | Server        |         | M               |
| 0x001E     | Binding      | Server        |         | Simple & Client |
| 0x0040     | Fixed Label  | Server        |         | O               |
| 0x0041     | User Label   | Server        |         | O               |

## <span id="page-26-2"></span>**1.1.8. Element Requirements**

The table below lists qualities and conformance that override the cluster specification require-

ments. A blank entry means no change.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------|------------|--------|-----------------|
| 0x001D     | Descriptor      | Feature | TagList |            |        | Duplicate       |

# <span id="page-28-0"></span>**Chapter 2. Utility Device Types**

This chapter describes the utility device types. The utility device types are summarized in the table below:

| Device ID | Device name                 |
|-----------|-----------------------------|
| 0x0016    | Root Node                   |
| 0x0011    | Power Source                |
| 0x0012    | OTA Requestor               |
| 0x0014    | OTA Provider                |
| 0x0013    | Bridged Node                |
| 0x0510    | Electrical Sensor           |
| 0x050D    | Device Energy Management    |
| 0x0019    | Secondary Network Interface |
| 0x0130    | Joint Fabric Administrator  |

# <span id="page-28-1"></span>**2.1. Root Node Device Type**

This defines conformance for a root node endpoint (see System Model specification). This endpoint is akin to a "read me first" endpoint that describes itself and the other endpoints that make up the node.

- Device types with Endpoint scope SHALL NOT be supported on the same endpoint as this device type.
- Clusters with an Application role SHALL NOT be supported on the same endpoint as this device type.
- Other device types with Node scope MAY be supported on the same endpoint as this device type.

### <span id="page-28-2"></span>**2.1.1. Revision History**

| Revision | Description                                                                                |
|----------|--------------------------------------------------------------------------------------------|
| 1        | Initial revision                                                                           |
| 2        | Added Power Source to device type; Deprecated<br>Power Source Configuration                |
| 3        | Added restriction on Managed Device feature of<br>Access Control cluster                   |
| 4        | Added conditions and cluster requirements for<br>Time Sync, TLS, and Power Source clusters |

#### <span id="page-29-0"></span>**2.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class | Scope |
|----------------|---------------------|-------------|-------|-------|
| 0x0016         | Root Node           |             | Node  | Node  |

#### <span id="page-29-1"></span>**2.1.3. Conditions**

The following table lists conditions that MAY be defined for this device type. This is used by device types which need certain clusters or features thereof to be present on this device type (Root Node). See [Section 1.1.3, "Base Type Conditions"](#page-24-4) for additional conformance tags.

<span id="page-29-7"></span><span id="page-29-6"></span><span id="page-29-5"></span><span id="page-29-4"></span><span id="page-29-3"></span><span id="page-29-2"></span>

| Condition              | Description                                                                                                                                                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CustomNetworkConfig    | The node only supports out-of-band-configured<br>networking (e.g. rich user interface, manufac<br>turer-specific means, custom commissioning<br>flows, or future IP-compliant network technol<br>ogy not yet directly supported by NetworkCommis<br>sioning cluster). |
| ManagedAclAllowed      | The node has at least one endpoint where some<br>Device Type present on the endpoint has a<br>Device Library element requirement table entry<br>that sets this condition to true.                                                                                     |
| TimeSyncCond           | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>use Time Synchronization support.                                                                                                                                    |
| TimeSyncWithClientCond | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>use Time Synchronization support with Client<br>cluster support, and the TimeSyncClient feature.                                                                     |
| TimeSyncWithNTPCCond   | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>use Time Synchronization support with the NTP<br>Client feature.                                                                                                     |
| TimeSyncWithTZCond     | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>use Time Synchronization support with the<br>TimeZone feature.                                                                                                       |
| TLSCertificatesCond    | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>use TLS Certificate Management. Since TLS<br>requires basic Time Sync support, this will<br>include that dependency.                                                 |

<span id="page-30-4"></span><span id="page-30-3"></span>

| Condition        | Description                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TLSClientCond    | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>use TLS Client Management. Since TLS requires<br>basic Time Sync support, this will include that<br>dependency. |
| PowerSourceCond  | The node has at least one endpoint where some<br>Device Type present on the endpoint needs to<br>have Power Source be on the Root Node.                                                                          |
| ACLExtensionCond | The node has at least one endpoint where some<br>Device Type present on the endpoint needs the<br>Access Control instance to have the Extension<br>attribute.                                                    |

#### <span id="page-30-2"></span><span id="page-30-0"></span>**2.1.4. Device Type Requirements**

The table lists other device types to be implemented along with this device type based on conformance.

| Device Type ID | Device Type Name | Constraint | Conformance        |
|----------------|------------------|------------|--------------------|
| 0x0011         | Power Source     |            | PowerSourceCond, O |

#### <span id="page-30-1"></span>**2.1.5. Cluster Requirements**

| Cluster ID | Cluster Name                   | Client/Server | Quality | Conformance              |
|------------|--------------------------------|---------------|---------|--------------------------|
| 0x001F     | Access Control                 | Server        | I       | M                        |
| 0x0028     | Basic Information              | Server        | I       | M                        |
| 0x002B     | Localization Con<br>figuration | Server        | I       | LanguageLocale           |
| 0x002C     | Time Format<br>Localization    | Server        | I       | TimeLocale               |
| 0x002D     | Unit Localization              | Server        | I       | UnitLocale               |
| 0x002E     | Power Source Con<br>figuration | Server        | I       | O, D                     |
| 0x0030     | General Commis<br>sioning      | Server        | I       | M                        |
| 0x0031     | Network Commis<br>sioning      | Server        |         | !CustomNetwork<br>Config |
| 0x0032     | Diagnostic Logs                | Server        | I       | O                        |

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance                                                                                                                                        |
|------------|---------------------------------|---------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0033     | General Diagnos<br>tics         | Server        | I       | M                                                                                                                                                  |
| 0x0034     | Software Diagnos<br>tics        | Server        | I       | O                                                                                                                                                  |
| 0x0035     | Thread Network<br>Diagnostics   | Server        |         | [Thread]                                                                                                                                           |
| 0x0036     | Wi-Fi Network<br>Diagnostics    | Server        |         | [Wi-Fi]                                                                                                                                            |
| 0x0037     | Ethernet Network<br>Diagnostics | Server        |         | [Ethernet]                                                                                                                                         |
| 0x0038     | Time Synchroniza<br>tion        | Server        | I       | TimeSyncCond,<br>TimeSyncWith<br>ClientCond, Time<br>SyncWithNTPC<br>Cond, Time<br>SyncWithTZCond,<br>TLSClientCond,<br>TLSCertifi<br>catesCond, O |
| 0x0038     | Time Synchroniza<br>tion        | Client        | I       | TimeSyncWith<br>ClientCond, O                                                                                                                      |
| 0x003C     | Administrator<br>Commissioning  | Server        | I       | M                                                                                                                                                  |
| 0x003E     | Operational Cre<br>dentials     | Server        | I       | M                                                                                                                                                  |
| 0x003F     | Group Key Man<br>agement        | Server        | I       | M                                                                                                                                                  |
| 0x0046     | ICD Management                  | Server        | I       | SIT   LIT                                                                                                                                          |
| 0x0801     | TLS Certificate<br>Management   | Server        | I       | TLSCertifi<br>catesCond, O                                                                                                                         |
| 0x0802     | TLS Client Man<br>agement       | Server        | I       | TLSClientCond, O                                                                                                                                   |

**NOTE**

The Network Diagnostics clusters present on the Root Node SHALL serve the primary network interface as specified in the Network Commissioning cluster if it exists, or the out-of-band-configured networking interfaces.

### <span id="page-31-0"></span>**2.1.6. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name          | Element   | Name                    | Constraint | Access | Confor<br>mance                                                                           |
|------------|--------------------------|-----------|-------------------------|------------|--------|-------------------------------------------------------------------------------------------|
| 0x001F     | Access Con<br>trol       | Feature   | MNGD                    | desc       |        | [ManagedA<br>clAllowed]                                                                   |
| 0x001F     | Access Con<br>trol       | Attribute | Extension               |            |        | ACLExten<br>sionCond                                                                      |
| 0x0038     | Time Syn<br>chronization | Feature   | TimeSync<br>Client      |            |        | Time<br>SyncWith<br>ClientCond,<br>[TLSCertifi<br>catesCond  <br>TLSClient<br>Cond].a+, O |
| 0x0038     | Time Syn<br>chronization | Feature   | NTPClient               |            |        | Time<br>SyncWithNT<br>PCCond,<br>[TLSCertifi<br>catesCond  <br>TLSClient<br>Cond].a+, O   |
| 0x0038     | Time Syn<br>chronization | Feature   | TimeZone                |            |        | Time<br>SyncWithTZ<br>Cond, O                                                             |
| 0x0046     | ICD Manage<br>ment       | Feature   | LongIdle<br>TimeSupport |            |        | LIT                                                                                       |

#### **2.1.6.1. Access Control MNGD Conformance**

The MNGD (Managed Device) feature of the Access Control Cluster on the device's Root Node endpoint is restricted to devices that contain an Application Endpoint type that explicitly permits its use, such as the Network Infrastructure Manager device type (Device Type ID 0x0090).

### <span id="page-32-0"></span>**2.1.7. Endpoint Composition**

A Root Node endpoint's Descriptor cluster PartsList attribute SHALL contain a list of all other endpoints on the node, i.e. the full-family pattern defined in the System Model specification.

# <span id="page-32-1"></span>**2.2. Power Source Device Type**

A Power Source device type provides information about the source of power.

#### <span id="page-33-0"></span>**2.2.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-33-1"></span>**2.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class   | Scope |
|----------------|---------------------|-------------|---------|-------|
| 0x0011         | Power Source        |             | Utility | Node  |

#### <span id="page-33-2"></span>**2.2.3. Cluster Requirements**

This device SHALL support the clusters listed in the following table.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x002F     | Power Source | Server        |         | M           |

# <span id="page-33-3"></span>**2.3. OTA Requestor Device Type**

An OTA Requestor is a device that is capable of receiving an OTA software update.

#### <span id="page-33-4"></span>**2.3.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-33-5"></span>**2.3.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class   | Scope |
|----------------|---------------------|-------------|---------|-------|
| 0x0012         | OTA Requestor       |             | Utility | Node  |

### <span id="page-33-6"></span>**2.3.3. Cluster Requirements**

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0029     | OTA Software<br>Update Provider  | Client        |         | M           |
| 0x002A     | OTA Software<br>Update Requestor | Server        |         | M           |

# <span id="page-34-0"></span>**2.4. OTA Provider Device Type**

An OTA Provider is a node that is capable of providing an OTA software update to other nodes on the same fabric.

#### <span id="page-34-1"></span>**2.4.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-34-2"></span>**2.4.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class   | Scope |
|----------------|---------------------|-------------|---------|-------|
| 0x0014         | OTA Provider        |             | Utility | Node  |

### <span id="page-34-3"></span>**2.4.3. Cluster Requirements**

Each node supporting this device type SHALL include these clusters based on the conformance defined below. A node SHALL only ever have, at most, one instance of the OTA Provider's required clusters.

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0029     | OTA Software<br>Update Provider  | Server        |         | M           |
| 0x002A     | OTA Software<br>Update Requestor | Client        |         | O           |

# <span id="page-34-4"></span>**2.5. Bridged Node Device Type**

This defines conformance for a Bridged Node root endpoint. This endpoint is akin to a "read me first" endpoint that describes itself and any other endpoints that make up the Bridged Node. A Bridged Node endpoint represents a device on a foreign network, but is not the root endpoint of the bridge itself.

## <span id="page-34-5"></span>**2.5.1. Revision History**

| Revision | Description                                                                   |
|----------|-------------------------------------------------------------------------------|
| 1        | Initial revision                                                              |
| 2        | Added Power Source to device type; Deprecated<br>Power Source Configuration   |
| 3        | Added Ecosystem Information Cluster and Fab<br>ricSynchronizedNode Condition. |

#### <span id="page-35-0"></span>**2.5.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class   | Scope    |
|----------------|---------------------|-------------|---------|----------|
| 0x0013         | Bridged Node        |             | Utility | Endpoint |

#### <span id="page-35-1"></span>**2.5.3. Conditions**

This device type MAY support the following conformance conditions as defined below.

| Condition              | Description            |
|------------------------|------------------------|
| FabricSynchronizedNode | See description below. |

See the Base Device Type definition for additional conformance tags.

#### **2.5.3.1. FabricSynchronizedNode Condition**

The FabricSynchronizedNode condition applies to a Bridged Node endpoint when all of the following are true:

- There is a Commissioner Control Cluster on an Aggregator which has this endpoint as a descendant.
- The Commissioner Control Cluster has a SupportedDeviceCategories attribute with the Fabric-Synchronization bit set.
- The bridged node is a Matter Node.

### <span id="page-35-2"></span>**2.5.4. Device Type Requirements**

This device type SHALL only be indicated on endpoints which are listed in the Descriptor cluster PartsList of another endpoint with an Aggregator device type.

The table lists other device types to be implemented along with this device type based on conformance.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0011         | Power Source     |            | O           |

### <span id="page-35-3"></span>**2.5.5. Cluster Requirements**

| Cluster ID | Cluster Name                   | Client/Server | Quality | Conformance                   |
|------------|--------------------------------|---------------|---------|-------------------------------|
| 0x002E     | Power Source Con<br>figuration | Server        |         | BridgedPower<br>SourceInfo, D |

| Cluster ID | Cluster Name                        | Client/Server | Quality | Conformance                   |
|------------|-------------------------------------|---------------|---------|-------------------------------|
| 0x002F     | Power Source                        | Server        |         | BridgedPower<br>SourceInfo    |
| 0x0039     | Bridged Device<br>Basic Information | Server        |         | M                             |
| 0x003C     | Administrator<br>Commissioning      | Server        |         | FabricSynchro<br>nizedNode    |
| 0x0750     | Ecosystem Infor<br>mation           | Server        |         | FabricSynchro<br>nizedNode, O |

### <span id="page-36-0"></span>**2.5.6. Endpoint Composition**

A Bridged Node endpoint SHALL support one of the following composition patterns:

- **Separate Endpoints**: All application device types are supported on separate descendant endpoints, and SHALL NOT be hosted on the Bridged Node endpoint. The Bridged Node endpoint's Descriptor cluster PartsList attribute SHALL indicate a list of all endpoints representing the functionality of the bridged device, including the endpoints supporting the application device types, i.e. the full-family pattern defined in the System Model specification. This is used for the following cases:
  - Exposing a compound device the child endpoints each have a part of the functionality of the bridged device. See endpoints 31-34 in the example below; the bridged device is a PIR sensor which also has temperature and illuminance measurement. Endpoints 32-34 host the associated application device types and clusters. Endpoint 31 (the endpoint with the Bridged Node device type) functions as parent for these endpoints and has no application device types.
  - Exposing a composed device type a child endpoint of the endpoint with the Bridged Node device type has the composed device type; this endpoint with the composed device type has child endpoints for the device type(s) that are mandatory or optional for the composed device type. See endpoints 41-43 in the example below; this is a refrigerator, which is a composed device type, hosted on endpoint 42, with the associated temperature controlled cabinet device type on child endpoint 43. Endpoint 41 (the endpoint with the Bridged Node device type) functions as parent for the endpoint hosting the composed device type and has no application clusters.
  - Combinations of the above.
- **One Endpoint**: Both the Bridged Node and one or more application device types are supported on the same endpoint (following application device type rules). The PartsList attribute in the Descriptor cluster SHALL be empty.
  - Since compound devices and composed device types each need more than one endpoint to expose their functionality, they cannot use the "One Endpoint" pattern and need to use the "Separate Endpoints" model described above.
    - Example in the figure below: endpoint 21 hosts the Bridged Node utility device type, plus the application device type for a dimmable light on same endpoint. Since the dimmable light device type is a superset of on/off light, that subset device type MAY be added here as well.

In all these composition patterns, endpoint composition SHALL conform to the application device type(s) definition.

![](_page_37_Figure_3.jpeg)

*Figure 1. examples of composition for bridged nodes*

# <span id="page-37-0"></span>**2.6. Electrical Sensor Device Type**

An Electrical Sensor device measures the electrical power and/or energy being imported and/or exported.

### <span id="page-37-1"></span>**2.6.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-38-0"></span>**2.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class   | Scope    |
|----------------|---------------------|-------------|---------|----------|
| 0x0510         | Electrical Sensor   |             | Utility | Endpoint |

### <span id="page-38-1"></span>**2.6.3. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0090     | Electrical Power<br>Measurement  | Server        |         | O.a+        |
| 0x0091     | Electrical Energy<br>Measurement | Server        |         | O.a+        |
| 0x009C     | Power Topology                   | Server        |         | M           |

**NOTE**

Electrical measurements made by either the Electrical Power Measurement cluster, the Electrical Energy Measurement cluster, or both SHALL apply to the endpoints indicated by the Power Topology cluster.

# <span id="page-38-2"></span>**2.7. Device Energy Management**

A Device Energy Management device provides reporting and optionally adjustment of the electrical power planned on being consumed or produced by the device.

## <span id="page-38-3"></span>**2.7.1. Revision History**

| Revision | Description                                               |
|----------|-----------------------------------------------------------|
| 1        | Initial revision                                          |
| 2        | Updated description of when DEM Mode is to be<br>included |
| 3        | Updated to include Electrical Grid Conditions             |

#### <span id="page-38-4"></span>**2.7.2. Classification**

| Device Type ID | Device Type<br>Name         | Superset Of | Class   | Scope    |
|----------------|-----------------------------|-------------|---------|----------|
| 0x050D         | Device Energy<br>Management |             | Utility | Endpoint |

#### <span id="page-39-0"></span>**2.7.3. Conditions**

See the Base Device Type definition for conformance tags.

| Condition       | Description                                  |  |
|-----------------|----------------------------------------------|--|
| ControllableESA | The DEM cluster on this endpoint accepts com |  |
|                 | mands to adjust its energy operation.        |  |

A ControllableESA device is one that allows a client to request either a change in power (PowerAdjustment feature), a change in the start time (StartTimeAdjustment feature), to be paused and resumed (Pausable feature), or to have its power or state forecast adjusted (ForecastAdjustment or ConstraintBasedAdjustment features).

Simple reporting of the Forecast as a single capability on its own (PowerForecastReporting or State-ForecastReporting feature support) does not require the ControllableESA condition.

#### <span id="page-39-1"></span>**2.7.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                        | Client/Server | Quality | Conformance        |
|------------|-------------------------------------|---------------|---------|--------------------|
| 0x0098     | Device Energy<br>Management         | Server        |         | M                  |
| 0x009F     | Device Energy<br>Management<br>Mode | Server        |         | ControllableESA, O |
| 0x00A0     | Electrical Grid<br>Conditions       | Client        |         | O                  |

### <span id="page-39-2"></span>**2.7.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                 | Element | Name                              | Constraint | Access | Confor<br>mance          |
|------------|---------------------------------|---------|-----------------------------------|------------|--------|--------------------------|
| 0x0098     | Device<br>Energy Man<br>agement | Feature | PowerAd<br>justment               |            |        | [Control<br>lableESA].a+ |
| 0x0098     | Device<br>Energy Man<br>agement | Feature | StartTimeAd<br>justment           |            |        | [Control<br>lableESA].a+ |
| 0x0098     | Device<br>Energy Man<br>agement | Feature | Pausable                          |            |        | [Control<br>lableESA].a+ |
| 0x0098     | Device<br>Energy Man<br>agement | Feature | ForecastAd<br>justment            |            |        | [Control<br>lableESA].a+ |
| 0x0098     | Device<br>Energy Man<br>agement | Feature | Constraint<br>BasedAdjust<br>ment |            |        | [Control<br>lableESA].a+ |

# <span id="page-40-0"></span>**2.8. Secondary Network Interface Device Type**

A Secondary Network Interface device provides an additional network interface supported by the Node, supplementing the primary interface hosted by the Root Node endpoint.

A Node supporting multiple network interfaces SHALL include the primary interface on the Root Node endpoint, along with secondary interfaces on other endpoints. The priorities of these network interfaces are determined by the order of their endpoints, where interfaces with smaller endpoint numbers are higher priority.

### <span id="page-40-1"></span>**2.8.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-40-2"></span>**2.8.2. Classification**

| Device Type ID | Device Type<br>Name             | Superset Of | Class   | Scope    |
|----------------|---------------------------------|-------------|---------|----------|
| 0x0019         | Secondary Net<br>work Interface |             | Utility | Endpoint |

### <span id="page-40-3"></span>**2.8.3. Cluster Requirements**

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance |
|------------|---------------------------------|---------------|---------|-------------|
| 0x0031     | Network Commis<br>sioning       | Server        |         | M           |
| 0x0035     | Thread Network<br>Diagnostics   | Server        |         | [Thread]    |
| 0x0036     | Wi-Fi Network<br>Diagnostics    | Server        |         | [Wi-Fi]     |
| 0x0037     | Ethernet Network<br>Diagnostics | Server        |         | [Ethernet]  |

**NOTE**

The Network Diagnostics cluster present in this device type SHALL serve the secondary network interface as specified in the Network Commissioning cluster.

# <span id="page-41-0"></span>**2.9. Joint Fabric Administrator Device Type**

A Joint Fabric Administrator device provides capabilities to manage the Joint Fabric Datastore and issue an ICAC signed by the Joint Fabric Anchor Root CA.

A client wanting to access the capabilities of the Joint Fabric Administrator MAY use the Joint Commissioning Method (as specified in the [Matter core specification](#page-23-5)) to be commissioned onto the Joint Fabric. Once commissioned, a client MAY access the capabilities of the Joint Fabric Administrator.

### <span id="page-41-1"></span>**2.9.1. Joint Fabric Architecture**

See the Joint Fabric section of the Multiple Fabrics chapter in the [Matter core specification](#page-23-5) for more information on the Joint Fabric architecture.

### <span id="page-41-2"></span>**2.9.2. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-41-3"></span>**2.9.3. Classification**

| Device Type ID | Device Type<br>Name           | Superset Of | Class   | Scope    |
|----------------|-------------------------------|-------------|---------|----------|
| 0x0130         | Joint Fabric<br>Administrator |             | Utility | Endpoint |

## <span id="page-41-4"></span>**2.9.4. Cluster Requirements**

Each endpoint supporting the Joint Fabric Administrator device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                  | Client/Server | Quality | Conformance |
|------------|-------------------------------|---------------|---------|-------------|
| 0x0752     | Joint Fabric Datas<br>tore    | Server        |         | M           |
| 0x0753     | Joint Fabric<br>Administrator | Server        |         | M           |

# <span id="page-44-0"></span>**Chapter 3. Application Device Types**

The following chapters list the application device types defined in this version of the Device Library. They are grouped per functional area in a chapter and are summarized in the table below:

| Device ID                               | Device name                   |  |  |  |
|-----------------------------------------|-------------------------------|--|--|--|
| lighting                                |                               |  |  |  |
| 0x0100                                  | On/Off Light                  |  |  |  |
| 0x0101                                  | Dimmable Light                |  |  |  |
| 0x010C                                  | Color Temperature Light       |  |  |  |
| 0x010D                                  | Extended Color Light          |  |  |  |
| smart plugs/outlets and other actuators |                               |  |  |  |
| 0x010A                                  | On/Off Plug-in Unit           |  |  |  |
| 0x010B                                  | Dimmable Plug-In Unit         |  |  |  |
| 0x010F                                  | Mounted On/Off Control        |  |  |  |
| 0x0110                                  | Mounted Dimmable Load Control |  |  |  |
| 0x0303                                  | Pump                          |  |  |  |
| 0x0042                                  | Water Valve                   |  |  |  |
| 0x0040                                  | Irrigation System             |  |  |  |
| switches and controls                   |                               |  |  |  |
| 0x0103                                  | On/Off Light Switch           |  |  |  |
| 0x0104                                  | Dimmer Switch                 |  |  |  |
| 0x0105                                  | Color Dimmer Switch           |  |  |  |
| 0x0840                                  | Control Bridge                |  |  |  |
| 0x0304                                  | Pump Controller               |  |  |  |
| 0x000F                                  | Generic Switch                |  |  |  |
|                                         | sensors                       |  |  |  |
| 0x0015                                  | Contact Sensor                |  |  |  |
| 0x0106                                  | Light Sensor                  |  |  |  |
| 0x0107                                  | Occupancy Sensor              |  |  |  |
| 0x0302                                  | Temperature Sensor            |  |  |  |
| 0x0305                                  | Pressure Sensor               |  |  |  |
| 0x0306                                  | Flow Sensor                   |  |  |  |
| 0x0307                                  | Humidity Sensor               |  |  |  |
| 0x0850                                  | On/Off Sensor                 |  |  |  |

| Device ID  | Device name                |  |  |
|------------|----------------------------|--|--|
| 0x0076     | Smoke CO Alarm             |  |  |
| 0x002C     | Air Quality Sensor         |  |  |
| 0x0041     | Water Freeze Detector      |  |  |
| 0x0043     | Water Leak Detector        |  |  |
| 0x0044     | Rain Sensor                |  |  |
| 0x0045     | Soil Sensor                |  |  |
|            | Entry Control              |  |  |
| 0x000A     | Door Lock                  |  |  |
| 0x000B     | Door Lock Controller       |  |  |
| 0x0202     | Window Covering            |  |  |
| 0x0203     | Window Covering Controller |  |  |
| 0x0230     | Closure                    |  |  |
| 0x0231     | Closure Panel              |  |  |
| 0x023E     | Closure Controller         |  |  |
|            | HVAC                       |  |  |
| 0x0301     | Thermostat                 |  |  |
| 0x002B     | Fan                        |  |  |
| 0x002D     | Air Purifier               |  |  |
| 0x030A     | Thermostat Controller      |  |  |
|            | media                      |  |  |
| 0x0028     | Basic Video Player         |  |  |
| 0x0023     | Casting Video Player       |  |  |
| 0x0022     | Speaker                    |  |  |
| 0x0024     | Content App                |  |  |
| 0x0029     | Casting Video Client       |  |  |
| 0x002A     | Video Remote Control       |  |  |
|            | generic                    |  |  |
| 0x0027     | Mode Select                |  |  |
| 0x000E     | Aggregator                 |  |  |
|            | robotic devices            |  |  |
| 0x0074     | Robotic Vacuum Cleaner     |  |  |
| appliances |                            |  |  |
| 0x0070     | Refrigerator               |  |  |

| Device ID | Device name                    |  |  |  |
|-----------|--------------------------------|--|--|--|
| 0x0071    | Temperature Controlled Cabinet |  |  |  |
| 0x0072    | Room Air Conditioner           |  |  |  |
| 0x0073    | Laundry Washer                 |  |  |  |
| 0x0075    | Dishwasher                     |  |  |  |
| 0x0077    | Cook Surface                   |  |  |  |
| 0x0078    | Cooktop                        |  |  |  |
| 0x0079    | Microwave Oven                 |  |  |  |
| 0x007A    | Extractor Hood                 |  |  |  |
| 0x007B    | Oven                           |  |  |  |
| 0x007C    | Laundry Dryer                  |  |  |  |
| energy    |                                |  |  |  |
| 0x050C    | EVSE                           |  |  |  |
| 0x050F    | Water Heater                   |  |  |  |
| 0x0017    | Solar Power                    |  |  |  |
| 0x0018    | Battery Storage                |  |  |  |
| 0x0309    | Heat Pump                      |  |  |  |
| 0x0512    | Meter Reference Point          |  |  |  |
| 0x0513    | Electrical Energy Tariff       |  |  |  |
| 0x0514    | Electrical Meter               |  |  |  |
| 0x0511    | Electrical Utility Meter       |  |  |  |
|           | network infrastructure         |  |  |  |
| 0x0090    | Network Infrastructure Manager |  |  |  |
| 0x0091    | Thread Border Router           |  |  |  |
|           | cameras                        |  |  |  |
| 0x0142    | Camera                         |  |  |  |
| 0x0144    | Floodlight Camera              |  |  |  |
| 0x0143    | Video Doorbell                 |  |  |  |
| 0x0140    | Intercom                       |  |  |  |
| 0x0141    | Audio Doorbell                 |  |  |  |
| 0x0145    | Snapshot Camera                |  |  |  |
| 0x0146    | Chime                          |  |  |  |
| 0x0147    | Camera Controller              |  |  |  |
| 0x0148    | Doorbell                       |  |  |  |

# <span id="page-48-0"></span>**Chapter 4. Lighting Device Types**

# <span id="page-48-1"></span>**4.1. On/Off Light Device Type**

The On/Off Light is a lighting device that is capable of being switched on or off by means of a bound controller device such as an On/Off Light Switch or a Dimmer Switch. In addition, an on/off light is also capable of being switched by means of a bound occupancy sensor.

#### <span id="page-48-2"></span>**4.1.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-48-3"></span>**4.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0100         | On/Off Light        |             | Simple | Endpoint |

### <span id="page-48-4"></span>**4.1.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-48-5"></span>**4.1.4. Cluster Requirements**

*Table 1. On/Off Light Cluster Requirements*

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | O           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

The inclusion of the Level Control cluster on this device is recommended to provide a consistent user experience when the device is grouped with additional dimmable lights and the "with on/off" commands are used. For this device, since its only states are on or off, if the Level Control cluster is implemented, it SHALL NOT have any effect on the actual light level except for those commands that cause an on/off state change, that is, the "with on/off" commands. In addition, if the Level Control cluster is implemented, the device SHALL accept and process Level Control cluster commands, adjusting the value of the CurrentLevel attribute accordingly and, where necessary, adjusting the On/Off cluster OnOff attribute.

#### <span id="page-49-0"></span>**4.1.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |

As the TriggerEffect command of the Identify cluster and the OffWithEffect command of the On/Off cluster specify light effects that require dimming of the light output, and such is not possible on this device type, the specified light effects MAY be replaced by pure on/off light effects.

# <span id="page-49-1"></span>**4.2. Dimmable Light Device Type**

A Dimmable Light is a lighting device that is capable of being switched on or off and the intensity of its light adjusted by means of a bound controller device such as a Dimmer Switch or a Color Dimmer Switch. In addition, a Dimmable Light device is also capable of being switched by means of a bound occupancy sensor or other device(s).

#### <span id="page-50-0"></span>**4.2.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-50-1"></span>**4.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of  | Class  | Scope    |
|----------------|---------------------|--------------|--------|----------|
| 0x0101         | Dimmable Light      | On/Off Light | Simple | Endpoint |

### <span id="page-50-2"></span>**4.2.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-50-3"></span>**4.2.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

## <span id="page-50-4"></span>**4.2.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name          | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------------|------------|--------|-----------------|
| 0x0003     | Identify        | Command | TriggerEffect |            |        | M               |
| 0x0006     | On/Off          | Feature | Lighting      |            |        | M               |

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |

# <span id="page-51-0"></span>**4.3. Color Temperature Light Device Type**

A Color Temperature Light is a lighting device that is capable of being switched on or off, the intensity of its light adjusted, and its color temperature adjusted by means of a bound controller device such as a Color Dimmer Switch.

### <span id="page-51-1"></span>**4.3.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Added optional occupancy sensing                                            |
| 4        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-51-2"></span>**4.3.2. Classification**

| Device Type ID | Device Type<br>Name         | Superset Of    | Class  | Scope    |
|----------------|-----------------------------|----------------|--------|----------|
| 0x010C         | Color Tempera<br>ture Light | Dimmable Light | Simple | Endpoint |

#### <span id="page-51-3"></span>**4.3.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-52-0"></span>**4.3.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

*Table 2. Color Temperature Light Cluster Requirements*

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0300     | Color Control         | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

#### <span id="page-52-1"></span>**4.3.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |
| 0x0300     | Color Con<br>trol     | Feature   | ColorTem<br>perature  |            |        | M               |

| Cluster ID | Cluster<br>Name   | Element   | Name              | Constraint | Access | Confor<br>mance |
|------------|-------------------|-----------|-------------------|------------|--------|-----------------|
| 0x0300     | Color Con<br>trol | Attribute | Remaining<br>Time |            |        | M               |

# <span id="page-53-0"></span>**4.4. Extended Color Light Device Type**

An Extended Color Light is a lighting device that is capable of being switched on or off, the intensity of its light adjusted, and its color adjusted by means of a bound controller device such as a Color Dimmer Switch or Control Bridge. The device supports adjustment of color by means of hue/saturation, enhanced hue, color looping, XY coordinates, and color temperature. In addition, the extended color light is also capable of being switched by means of a bound occupancy sensor.

#### <span id="page-53-1"></span>**4.4.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation; integrate<br>DM CCB 3501                |
| 3        | Added optional occupancy sensing                                            |
| 4        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-53-2"></span>**4.4.2. Classification**

| Device Type ID | Device Type<br>Name     | Superset Of                 | Class  | Scope    |
|----------------|-------------------------|-----------------------------|--------|----------|
| 0x010D         | Extended Color<br>Light | Color Tempera<br>ture Light | Simple | Endpoint |

#### <span id="page-53-3"></span>**4.4.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-53-4"></span>**4.4.4. Cluster Requirements**

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | M           |
| 0x0004     | Groups       | Server        |         | M           |
| 0x0006     | On/Off       | Server        |         | M           |

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0008     | Level Control         | Server        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0300     | Color Control         | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

#### <span id="page-54-0"></span>**4.4.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |
| 0x0300     | Color Con<br>trol     | Feature   | HueSatura<br>tion     |            |        | O               |
| 0x0300     | Color Con<br>trol     | Feature   | Enhanced<br>Hue       |            |        | O               |
| 0x0300     | Color Con<br>trol     | Feature   | ColorLoop             |            |        | O               |
| 0x0300     | Color Con<br>trol     | Feature   | XY                    |            |        | M               |
| 0x0300     | Color Con<br>trol     | Feature   | ColorTem<br>perature  |            |        | M               |

| Cluster ID | Cluster<br>Name   | Element   | Name              | Constraint | Access | Confor<br>mance |
|------------|-------------------|-----------|-------------------|------------|--------|-----------------|
| 0x0300     | Color Con<br>trol | Attribute | Remaining<br>Time |            |        | M               |

# <span id="page-56-0"></span>**Chapter 5. Smart Plugs/Outlets and other Actuators**

# <span id="page-56-1"></span>**5.1. On/Off Plug-in Unit Device Type**

An On/Off Plug-in Unit is a device that provides power to another device that is plugged into it, and is capable of switching that provided power on or off.

The [Mounted On/Off Control](#page-60-2) (added in Matter 1.4) has identical cluster requirements as the On/Off Plug-In Unit, and is marked as superset of this device type (since Matter 1.4.2). For devices intended to be mounted permanently, the [Mounted On/Off Control](#page-60-2) device type SHALL be used, with the On/Off Plug-In Unit device type optionally added in the DeviceTypeList of the Descriptor cluster in addition to the On/Off Plug-In Unit device type (see [Mounted On/Off Control server guidance](#page-61-4) section).

<span id="page-56-3"></span>Before Matter 1.4, mounted units typically used the On/Off Plug-In Unit device type. Clients can encounter devices which were made before or after these specification updates. Therefore, clients SHOULD use the following heuristic to distinguish the type of physical device based on the device type revision found on an endpoint ("--" means the device type is not listed).

| On/Off Plug-In Unit (device<br>type revision) | Mounted On/Off Control<br>(device type revision) | Device Type                                                                  |  |  |
|-----------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------------|--|--|
| 3 or lower                                    | —                                                | On/Off Plug-in Unit or Mounted<br>On/Off Control (could be both)             |  |  |
| 4 or higher                                   | —                                                | On/Off Plug-in Unit                                                          |  |  |
| 4 or higher                                   | 2 or higher                                      | Mounted On/Off Control                                                       |  |  |
| —                                             | 2 or higher                                      | Mounted On/Off Control (manu<br>facturer not interested in older<br>clients) |  |  |
| —                                             | 1                                                | Mounted On/Off Control (Matter<br>1.4 did not have superset mark<br>ing)     |  |  |
| 3                                             | 1                                                | Mounted On/Off Control (CCB<br>4128 for a Matter 1.4/1.4.1<br>device)        |  |  |

### <span id="page-56-2"></span>**5.1.1. Revision History**

| Revision | Description                        |  |
|----------|------------------------------------|--|
| 1        | Initial Zigbee 3.0 revision        |  |
| 2        | New data model format and notation |  |

| Revision | Description                                                                         |
|----------|-------------------------------------------------------------------------------------|
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062         |
| 4        | Add Mounted On/Off Control as superset, add<br>usage guidance for both device types |

#### <span id="page-57-0"></span>**5.1.2. Classification**

| Device Type ID | Device Type<br>Name    | Superset Of | Class  | Scope    |
|----------------|------------------------|-------------|--------|----------|
| 0x010A         | On/Off Plug-in<br>Unit |             | Simple | Endpoint |

#### <span id="page-57-1"></span>**5.1.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-57-2"></span>**5.1.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

*Table 3. On/Off Plug-in Unit Cluster Requirements*

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | O           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

The inclusion of the Level Control cluster on this device is recommended to provide a consistent user experience when the device is grouped with additional dimmable lights and the "with on/off" commands are used. For this device, since its only states are on or off, if the Level Control cluster is implemented, it SHALL NOT have any effect on the actual light level except for those commands that cause an on/off state change, that is, the "with on/off" commands. In addition, if the Level Control cluster is implemented, the device SHALL accept and process Level Control cluster commands, adjusting the value of the CurrentLevel attribute accordingly and, where necessary, adjusting the On/Off cluster OnOff attribute.

#### <span id="page-58-0"></span>**5.1.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |

As the TriggerEffect command of the Identify cluster and the OffWithEffect command of the On/Off cluster specify light effects that require dimming of the light output, and such is not possible on this device type, the specified light effects MAY be replaced by pure on/off light effects.

# <span id="page-58-1"></span>**5.2. Dimmable Plug-In Unit Device Type**

A Dimmable Plug-In Unit is a device that provides power to another device that is plugged into it, and is capable of being switched on or off and have its level adjusted. The Dimmable Plug-in Unit is typically used to control a conventional non-communicating light through its mains connection using phase cutting.

The [Mounted Dimmable Load Control](#page-62-1) (added in Matter 1.4) has identical cluster requirements as the Dimmable Plug-In Unit, and is marked as a superset of this device type (since Matter 1.4.2). For devices intended to be mounted permanently, the [Mounted Dimmable Load Control](#page-62-1) device type SHALL be used, with the Dimmable Plug-In Unit device type optionally added to the DeviceTypeList of the Descriptor cluster in addition to the Mounted Dimmable Load Control device type (see [Mounted Dimmable Load Control server guidance](#page-63-4) section).

<span id="page-58-2"></span>Before Matter 1.4, mounted dimmable load control units typically used the Dimmable Plug-In Unit device type. Clients can encounter devices which were made before or after these specification updates. Therefore, clients SHOULD use the following heuristic to distinguish the type of physical device based on the device type revision found on an endpoint ("--" means the device type is not listed).

| Dimmable Plug-In Unit<br>(device type revision) | Mounted Dimmable Load Con<br>trol (device type revision) | Device Type                                                                          |
|-------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| 4 or lower                                      | —                                                        | Dimmable Plug-in Unit or<br>Mounted Dimmable Load Con<br>trol (could be both)        |
| 5 or higher                                     | —                                                        | Dimmable Plug-in Unit                                                                |
| 5 or higher                                     | 2 or higher                                              | Mounted Dimmable Load Con<br>trol                                                    |
| —                                               | 2 or higher                                              | Mounted Dimmable Load Con<br>trol (manufacturer not inter<br>ested in older clients) |
| —                                               | 1                                                        | Mounted Dimmable Load Con<br>trol (Matter 1.4 did not have<br>superset marking)      |
| 4                                               | 1                                                        | Mounted Dimmable Load Con<br>trol (CCB 4128 for a Matter<br>1.4/1.4.1 device)        |

#### <span id="page-59-0"></span>**5.2.1. Revision History**

| Revision | Description                                                                                 |
|----------|---------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                                 |
| 2        | New data model format and notation                                                          |
| 3        | Added optional occupancy sensing                                                            |
| 4        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062                 |
| 5        | Add Mounted Dimmable Load Control as super<br>set, add usage guidance for both device types |

#### <span id="page-59-1"></span>**5.2.2. Classification**

| Device Type ID | Device Type<br>Name      | Superset Of | Class  | Scope    |
|----------------|--------------------------|-------------|--------|----------|
| 0x010B         | Dimmable Plug-In<br>Unit |             | Simple | Endpoint |

#### <span id="page-59-2"></span>**5.2.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-60-0"></span>**5.2.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

#### <span id="page-60-1"></span>**5.2.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |

# <span id="page-60-2"></span>**5.3. Mounted On/Off Control Device Type**

A Mounted On/Off Control is a fixed device that provides power to another device or power circuit that is connected to it, and is capable of switching that provided power on or off.

<span id="page-61-4"></span>This device type is intended for any wall-mounted or hardwired load controller, while [On/Off Plug](#page-56-1)[in Unit](#page-56-1) is intended only for smart plugs and other power switching devices that are not permanently connected, and which can be unplugged from their power source.

**NOTE**

Since this device type was added in Matter 1.4, for endpoints using this device type it is RECOMMENDED to add the subset device type [On/Off Plug-in Unit](#page-56-1) to the Device-TypeList of the Descriptor cluster on the same endpoint for backward compatibility with existing clients.

See [On/Off Plug-in Unit client guidance](#page-56-3) for additional information, regarding the inclusion of these two device types.

#### <span id="page-61-0"></span>**5.3.1. Revision History**

| Revision | Description                                                             |
|----------|-------------------------------------------------------------------------|
| 1        | Initial release                                                         |
| 2        | Add superset classification and usage guidance<br>for both device types |

#### <span id="page-61-1"></span>**5.3.2. Classification**

| Device Type ID | Device Type<br>Name       | Superset Of            | Class  | Scope    |
|----------------|---------------------------|------------------------|--------|----------|
| 0x010F         | Mounted On/Off<br>Control | On/Off Plug-in<br>Unit | Simple | Endpoint |

#### <span id="page-61-2"></span>**5.3.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-61-3"></span>**5.3.4. Cluster Requirements**

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | O           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

The inclusion of the Level Control cluster on this device is recommended to provide a consistent user experience when the device is grouped with additional dimmable lights and the "with on/off" commands are used. For this device, since its only states are on or off, if the Level Control cluster is implemented, it SHALL NOT have any effect on the actual light level except for those commands that cause an on/off state change, that is, the "with on/off" commands. In addition, if the Level Control cluster is implemented, the device SHALL accept and process Level Control cluster commands, adjusting the value of the CurrentLevel attribute accordingly and, where necessary, adjusting the On/Off cluster OnOff attribute.

#### <span id="page-62-0"></span>**5.3.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |

As the TriggerEffect command of the Identify cluster and the OffWithEffect command of the On/Off cluster specify light effects that require dimming of the light output, and such is not possible on this device type, the specified light effects MAY be replaced by pure on/off light effects.

# <span id="page-62-1"></span>**5.4. Mounted Dimmable Load Control Device Type**

A Mounted Dimmable Load Control is a fixed device that provides power to a load connected to it, and is capable of being switched on or off and have its level adjusted. The Mounted Dimmable Load Control is typically used to control a conventional non-communicating light through its mains connection using phase cutting.

This device type is intended for any wall-mounted or hardwired dimmer-capable load controller, while [Dimmable Plug-In Unit](#page-58-1) is intended only for dimmer-capable smart plugs that are not perma<span id="page-63-4"></span>nently connected, and which can be unplugged from their power source.

**NOTE**

Since this device type was added in Matter 1.4, for endpoints using this device type it is RECOMMENDED to add the subset device type [Dimmable Plug-In Unit](#page-58-1) to the DeviceTypeList of the Descriptor cluster on the same endpoint for backward compatibility with existing clients.

See [Dimmable Plug-In Unit client guidance](#page-58-2) for additional information, regarding the inclusion of these two device types.

#### <span id="page-63-0"></span>**5.4.1. Revision History**

| Revision | Description                                                             |
|----------|-------------------------------------------------------------------------|
| 1        | Initial release                                                         |
| 2        | Add superset classification and usage guidance<br>for both device types |

#### <span id="page-63-1"></span>**5.4.2. Classification**

| Device Type ID | Device Type<br>Name               | Superset Of              | Class  | Scope    |
|----------------|-----------------------------------|--------------------------|--------|----------|
| 0x0110         | Mounted Dimma<br>ble Load Control | Dimmable Plug-In<br>Unit | Simple | Endpoint |

#### <span id="page-63-2"></span>**5.4.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-63-3"></span>**5.4.4. Cluster Requirements**

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | M           |
| 0x0006     | On/Off                | Server        |         | M           |
| 0x0008     | Level Control         | Server        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | M           |
| 0x0406     | Occupancy Sens<br>ing | Client        |         | O           |

#### <span id="page-64-0"></span>**5.4.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name       | Element   | Name                  | Constraint | Access | Confor<br>mance |
|------------|-----------------------|-----------|-----------------------|------------|--------|-----------------|
| 0x0003     | Identify              | Command   | TriggerEffect         |            |        | M               |
| 0x0006     | On/Off                | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | OnOff                 |            |        | M               |
| 0x0008     | Level Con<br>trol     | Feature   | Lighting              |            |        | M               |
| 0x0008     | Level Con<br>trol     | Attribute | CurrentLevel 1 to 254 |            |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MinLevel              | 1          |        |                 |
| 0x0008     | Level Con<br>trol     | Attribute | MaxLevel              | 254        |        |                 |
| 0x0062     | Scenes Man<br>agement | Command   | CopyScene             |            |        | M               |

# <span id="page-64-1"></span>**5.5. Pump Device Type**

A Pump device is a pump that may have variable speed. It may have optional built-in sensors and a regulation mechanism. It is typically used for pumping fluids like water.

## <span id="page-64-2"></span>**5.5.1. Revision History**

This is the revision history for this device type. The highest revision number in the table below is the revision for this device type.

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-64-3"></span>**5.5.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0303         | Pump                |             | Simple | Endpoint |

#### <span id="page-65-0"></span>**5.5.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-65-1"></span>**5.5.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                       | Client/Server | Quality | Conformance |
|------------|------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                           | Server        |         | M           |
| 0x0004     | Groups                             | Server        |         | O           |
| 0x0006     | On/Off                             | Server        |         | M           |
| 0x0008     | Level Control                      | Server        |         | O           |
| 0x0062     | Scenes Manage<br>ment              | Server        |         | O           |
| 0x0200     | Pump Configura<br>tion and Control | Server        |         | M           |
| 0x0402     | Temperature Mea<br>surement        | Server        |         | O           |
| 0x0402     | Temperature Mea<br>surement        | Client        |         | O           |
| 0x0403     | Pressure Measure<br>ment           | Server        |         | O           |
| 0x0403     | Pressure Measure<br>ment           | Client        |         | O           |
| 0x0404     | Flow Measure<br>ment               | Server        |         | O           |
| 0x0404     | Flow Measure<br>ment               | Client        |         | O           |
| 0x0406     | Occupancy Sens<br>ing              | Client        |         | O           |

#### <span id="page-65-2"></span>**5.5.5. Cluster Restrictions**

#### **5.5.5.1. On/Off Cluster (Server) Clarifications**

The actions carried out by a Pump device on receipt of commands are shown in the following.

*Table 4. Pump Actions on Receipt for On/Off Commands*

| Command | Action on Receipt                                                                                                                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off     | If the pump is powered on, store the current<br>level then immediately power it off.                                                                                                                                   |
| On      | If the pump is powered off, power it on and<br>move immediately to the level stored by a previ<br>ous Off command. If no such level has been<br>stored, move immediately to the maximum level<br>allowed for the pump. |
| Toggle  | If the pump is powered on, proceed as for the<br>Off command. If the device is powered off, pro<br>ceed as for the On command.                                                                                         |

#### **5.5.5.2. Level Control Cluster (Server) Clarifications**

The Level Control cluster SHALL allow controlling the pump setpoints. However, the transition time is always ignored.

The setpoint of the pump is a percentage related to the level according to the following table.

*Table 5. Relationship between Level and Setpoint*

| Level   | Setpoint               | Meaning                   |
|---------|------------------------|---------------------------|
| 0       | N/A                    | Pump is stopped.          |
| 1–200   | Level / 2 (0.5–100.0%) | Pump setpoint in percent. |
| 201–255 | 100.0%                 | Pump setpoint is 100.0%   |

# <span id="page-66-0"></span>**5.6. Water Valve Device Type**

This defines conformance to the Water Valve device type.

### <span id="page-66-1"></span>**5.6.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-66-2"></span>**5.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0042         | Water Valve         |             | Simple | Endpoint |

#### <span id="page-67-0"></span>**5.6.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-67-1"></span>**5.6.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                        | Client/Server | Quality | Conformance |
|------------|-------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                            | Server        |         | M           |
| 0x0081     | Valve Configura<br>tion and Control | Server        |         | M           |
| 0x0404     | Flow Measure<br>ment                | Server        |         | O           |
| 0x0404     | Flow Measure<br>ment                | Client        |         | O           |

#### **5.6.4.1. Identify Cluster**

This cluster is used to identify the device.

#### **5.6.4.2. Valve Configuration and Control Cluster**

This cluster is used to configure and control (Open/Close) the valve.

#### **5.6.4.3. Flow Measurement Cluster**

The cluster server, if present, SHALL be used to report the measured flow through the valve.

The cluster client, if present, MAY be used via binding to close a control loop of flow through the valve.

#### <span id="page-67-2"></span>**5.6.5. Device implementation recommendations**

#### **5.6.5.1. Start Up Behavior**

The start up behavior of a device with this device type, is currently not specified and is considered manufacturer specific. This means that the start up behavior and what is considered the "safe state", most suitable for the specific device, is defined by the manufacturer.

#### **5.6.5.2. Firmware Update**

When a device with this device type needs to update its firmware (or restart for another reason), it is strongly recommended to only perform the update/restart when the valve is in its closed state, as well as ignoring any open request during this update/restart, given the chance a valve can unintentionally be left in the open state, for longer periods of time.

# <span id="page-68-0"></span>**5.7. Irrigation System Device Type**

This defines conformance to the Irrigation System device type. An irrigation system is used to control a group of irrigation zones to water landscape. Irrigation systems are also commonly referred to as "Sprinkler Controllers" since they are often used in residential and commercial settings to control and schedule in-ground sprinkler systems for lawns. A physical irrigation system typically has a set of electrical terminals to which in-ground water valves are connected so that the system can actuate them.

#### <span id="page-68-1"></span>**5.7.1. Irrigation System Architecture**

An irrigation system is always defined via endpoint composition. Irrigation system manufacturers determine how many watering "zone" terminals are present on the physical device. Each zone is represented by a disambiguated Water Valve endpoint:

![](_page_68_Figure_6.jpeg)

*Figure 2. Example of an Irrigation System*

### **5.7.2. Revision History**

<span id="page-68-2"></span>

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-68-3"></span>**5.7.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0040         | Irrigation System   |             | Simple | Endpoint |

#### <span id="page-69-0"></span>**5.7.4. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-69-1"></span>**5.7.5. Device Type Requirements**

An irrigation system SHALL be composed of at least one endpoint with the Water Valve device type. Any instance of the Valve Configuration and Control Cluster on an endpoint is scoped to the valve on that endpoint and not the whole node.

If more than one instance of the Water Valve device type is present, each instance SHALL include semantic tags from the common namespaces in the TagList attribute of the Descriptor cluster to disambiguate which watering zone on the device each valve endpoint represents.

Some irrigation systems include a master valve installed at the main water supply line. When a master valve is present, the physical system is responsible for opening it first when receiving a command to open a downstream watering valve. In addition, the physical system is responsible for closing the master valve when the last open watering valve is closed. Since the master valve is orchestrated by the device, it is not represented as a Water Valve endpoint.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0042         | Water Valve      | min 1      | M           |

### <span id="page-69-2"></span>**5.7.6. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name         | Client/Server | Quality | Conformance |
|------------|----------------------|---------------|---------|-------------|
| 0x0003     | Identify             | Server        |         | O           |
| 0x0060     | Operational State    | Server        |         | O           |
| 0x0404     | Flow Measure<br>ment | Server        |         | O           |
| 0x0404     | Flow Measure<br>ment | Client        |         | O           |

#### **5.7.6.1. Identify Cluster**

This cluster is used to identify the entire irrigation system device.

#### **5.7.6.2. Operational State Cluster**

This cluster, if present, is used to denote the current state of the irrigation system. An irrigation system MAY report the general operational states "Running" when at least one of the composed water valves is open for any reason, and "Stopped" when all water valves are closed. In addition, the system MAY support operational state commands "Pause" and "Resume" as well as the operational state "Paused" if it supports temporarily pausing a water valve that is currently open for a known duration. In this case, it SHOULD report the CountdownTime attribute to denote the remaining open duration of a currently open valve.

#### **5.7.6.3. Flow Measurement Cluster**

This cluster, if present, is used to measure the net flow through the irrigation system. When present, the cluster SHALL report the total flow through the irrigation system and not any individual valve.

If present, the flow measurement client cluster is used via binding to measure flow from external flow sensors.

# <span id="page-72-0"></span>**Chapter 6. Switches and Controls Device Types**

This Chapter specifies a number of "controller" device types like On/Off Light Switch and Dimmer Switch. Some products implementing these device types are intended to replace legacy switches or dimmers that directly control the power to a load. For such products, manufacturers are encouraged to implement an additional endpoint on the same product holding an "actuator" device type like an On/Off Light (or On/Off Plug-in Unit) or Dimmable Light (or Dimmable Plug-in Unit), consistent with the type of control it can provide to the load. In case product can control multiple loads separately, multiple such endpoints to each hold a device type for each load.

Additionally, having a central control function allows much richer automation triggered by a press of a switch. In such case, a switch works more like a sensor. For this, the Generic Switch device type is defined. See [Section 6.6, "Generic Switch".](#page-77-0) Manufacturers are encouraged to implement the Generic Switch device type as well in products that are generically referred to as switches. See [Sec](#page-80-0)[tion 6.6.5, "Relation with other Switch device types \(informative\)"](#page-80-0) for examples how these device types can be combined.

# <span id="page-72-1"></span>**6.1. On/Off Light Switch Device type**

An On/Off Light Switch is a controller device that, when bound to a lighting device such as an On/Off Light, is capable of being used to switch the device on or off.

#### <span id="page-72-2"></span>**6.1.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

### <span id="page-72-3"></span>**6.1.2. Classification**

| Device Type ID | Device Type<br>Name    | Superset Of | Class  | Scope    |
|----------------|------------------------|-------------|--------|----------|
| 0x0103         | On/Off Light<br>Switch |             | Simple | Endpoint |

#### <span id="page-72-4"></span>**6.1.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-73-0"></span>**6.1.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

*Table 6. On/Off Light Switch Cluster Requirements*

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0003     | Identify              | Client        |         | M           |
| 0x0004     | Groups                | Client        |         | O           |
| 0x0006     | On/Off                | Client        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Client        |         | O           |

# <span id="page-73-1"></span>**6.2. Dimmer Switch Device Type**

A Dimmer Switch is a controller device that, when bound to a lighting device such as a Dimmable Light, is capable of being used to switch the device on or off and adjust the intensity of the light being emitted.

#### <span id="page-73-2"></span>**6.2.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-73-3"></span>**6.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of            | Class  | Scope    |
|----------------|---------------------|------------------------|--------|----------|
| 0x0104         | Dimmer Switch       | On/Off Light<br>Switch | Simple | Endpoint |

#### <span id="page-73-4"></span>**6.2.3. Conditions**

See the Base Device Type definition for conformance tags.

# <span id="page-73-5"></span>**6.2.4. Cluster Requirements**

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0003     | Identify              | Client        |         | M           |
| 0x0004     | Groups                | Client        |         | O           |
| 0x0006     | On/Off                | Client        |         | M           |
| 0x0008     | Level Control         | Client        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Client        |         | O           |

# <span id="page-74-0"></span>**6.3. Color Dimmer Switch Device Type**

A Color Dimmer Switch is a controller device that, when bound to a lighting device such as an Extended Color Light, is capable of being used to adjust the color of the light being emitted.

#### <span id="page-74-1"></span>**6.3.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-74-2"></span>**6.3.2. Classification**

| Device Type ID | Device Type<br>Name    | Superset Of   | Class  | Scope    |
|----------------|------------------------|---------------|--------|----------|
| 0x0105         | Color Dimmer<br>Switch | Dimmer Switch | Simple | Endpoint |

#### <span id="page-74-3"></span>**6.3.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-74-4"></span>**6.3.4. Cluster Requirements**

*Table 7. Color Dimmer Switch Cluster Requirements*

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | M           |
| 0x0003     | Identify     | Client        |         | M           |

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0004     | Groups                | Client        |         | O           |
| 0x0006     | On/Off                | Client        |         | M           |
| 0x0008     | Level Control         | Client        |         | M           |
| 0x0062     | Scenes Manage<br>ment | Client        |         | O           |
| 0x0300     | Color Control         | Client        |         | M           |

# <span id="page-75-0"></span>**6.4. Control Bridge Device Type**

A Control Bridge is a controller device that, when bound to a lighting device such as an Extended Color Light, is capable of being used to switch the device on or off, adjust the intensity of the light being emitted and adjust the color of the light being emitted. In addition, a Control Bridge device is capable of being used for setting scenes.

#### <span id="page-75-1"></span>**6.4.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-75-2"></span>**6.4.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0840         | Control Bridge      |             | Simple | Endpoint |

#### <span id="page-75-3"></span>**6.4.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-75-4"></span>**6.4.4. Cluster Requirements**

*Table 8. Control Bridge Cluster Requirements*

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | M           |
| 0x0003     | Identify     | Client        |         | M           |

| Cluster ID | Cluster Name                | Client/Server | Quality | Conformance |
|------------|-----------------------------|---------------|---------|-------------|
| 0x0004     | Groups                      | Client        |         | M           |
| 0x0006     | On/Off                      | Client        |         | M           |
| 0x0008     | Level Control               | Client        |         | M           |
| 0x0062     | Scenes Manage<br>ment       | Client        |         | M           |
| 0x0300     | Color Control               | Client        |         | M           |
| 0x0400     | Illuminance Mea<br>surement | Client        |         | O           |
| 0x0406     | Occupancy Sens<br>ing       | Client        |         | O           |

# <span id="page-76-0"></span>**6.5. Pump Controller Device Type**

A Pump Controller device is capable of configuring and controlling a Pump device.

### <span id="page-76-1"></span>**6.5.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |
| 4        | Remove Binding client as a result of review of<br>CCB4058                   |

#### <span id="page-76-2"></span>**6.5.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0304         | Pump Controller     |             | Simple | Endpoint |

#### <span id="page-76-3"></span>**6.5.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-76-4"></span>**6.5.4. Cluster Requirements**

| Cluster ID | Cluster Name                       | Client/Server | Quality | Conformance |
|------------|------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                           | Server        |         | M           |
| 0x0003     | Identify                           | Client        |         | O           |
| 0x0004     | Groups                             | Client        |         | O           |
| 0x0006     | On/Off                             | Client        |         | M           |
| 0x0008     | Level Control                      | Client        |         | O           |
| 0x0062     | Scenes Manage<br>ment              | Client        |         | O           |
| 0x0200     | Pump Configura<br>tion and Control | Client        |         | M           |
| 0x0402     | Temperature Mea<br>surement        | Client        |         | O           |
| 0x0403     | Pressure Measure<br>ment           | Client        |         | O           |
| 0x0404     | Flow Measure<br>ment               | Client        |         | O           |

# <span id="page-77-0"></span>**6.6. Generic Switch Device Type**

This defines conformance for the Generic Switch device type.

### <span id="page-77-1"></span>**6.6.1. Revision History**

| Revision | Description                                                                                                                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Initial revision                                                                                                                                                                                                          |
| 2        | Removed requirement for Fixed Label cluster<br>(instead use TagList which was added in<br>Descriptor cluster)                                                                                                             |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062; note that this clus<br>ter is not used in this device type (only men<br>tioned in the informative section related to<br>On/Off Light Switch) |

#### <span id="page-77-2"></span>**6.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x000F         | Generic Switch      |             | Simple | Endpoint |

#### <span id="page-78-0"></span>**6.6.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-78-1"></span>**6.6.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | M           |
| 0x003B     | Switch       | Server        |         | M           |

#### **6.6.4.1. Instantaneous reporting**

The generic mechanism for subscriptions and events might not ensure that detected interactions with the switch will be delivered "instantaneously" to the Switch client cluster in the interested party (they might be sent only after some time, e.g. due to batching of events and the Min Interval behavior for subscriptions). In order to achieve a good user experience, a device of this device type SHALL send updates of attributes and events defined in the Switch cluster without delay to subscribed parties.

#### **6.6.4.2. Labeling for multi-switch devices**

A Node which contains multiple switches will need to expose multiple endpoints each hosting an instance of this device type and the associated Switch cluster. This means the [Duplicate](#page-26-3) condition in Matter base device requirements applies, so a TagList SHALL be included in the Descriptor cluster on each such endpoint. The tag(s) in this TagList are used to indicate orientation (e.g. left and right for a two-button switch) or labeling (e.g. "dim up" and "dim down" icons printed on the buttons) relevant to the user. A client SHOULD use these tags to convey such information to the user (e.g. showing it in a user interface), to help the user identify which endpoint maps to a certain orientation or labeling.

For the case where a server indicates tags from the Common Number Namespace, and the client presents entities related to the endpoints (e.g. icons for the various switches), it SHOULD present them in numerical order as indicated by the tags from the Common Number Namespace.

For a Node which has only one endpoint hosting an instance of this device type and the associated Switch cluster, a TagList MAY be used. This can be beneficial in cases where the switch has some user-recognizable labeling.

The TagList can contain a combination of tags from the namespaces defined in the Matter Semantic Tag Namespaces, including the namespace for switches as well as tags from a manufacturer-specific namespace.

In case the buttons have an intended function (e.g. engraved icon), the semantic tags from the Switches Namespace SHALL be used where applicable. If there is no corresponding tag, a manufacturer-specific tag with a string Label SHOULD be used (see Example 2 below).

To identify the location of a button on the device (e.g. top button of a two-button device), the semantic tags from the Common Position Namespace SHALL be used where applicable.

For devices where these are not applicable or not sufficient (e.g. a switch device with four buttons in a row), the semantic tags from the Common Number Namespace SHALL be used to enumerate the position of the buttons on the device, in left to right, top to bottom order, starting with Number.One for the first button.

For devices to control a Closure (e.g. Window Covering), the semantic tags from the Switches Namespace SHALL be used where applicable.

Example 1: a device with two rocker switches (mounted side by side), which has two endpoints (11,12) for the switch-related functionality

- endpoint 11 has device type Generic Switch and contains
  - cluster Switch (feature flags: LS) exposing the state and events of the left button
  - cluster Descriptor with its TagList containing two tags: Position.Left and Number.One
- endpoint 12 has device type Generic Switch and contains
  - cluster Switch (feature flags: LS) exposing the state and events of the right button
  - cluster Descriptor with its TagList containing two tags: Position.Right and Number.Two

If this device were to have labeling on the buttons like an "up" and "down" icon, the TagList would have a third tag (from the Switches Namespace) with values Switches.Up and Switches.Down respectively.

Example 2: a device with four push buttons (mounted in a square), each labeled with an icon for a certain scene setting, which has four endpoints (21,22,23,24) for the switch-related functionality

- endpoint 21 has device type Generic Switch and contains
  - cluster Switch (feature flags: MS) exposing the events of the top-left button
  - cluster Descriptor with its TagList containing four tags: Position.Top, Position.Left, Number.One and (Tag=Switches.Custom, Label="watch tv")
    - This last tag is a Switches.Custom tag accompanied with a label (the other three tags do not need a Label field).
- endpoint 22 has device type Generic Switch and contains
  - cluster Switch (feature flags: MS) exposing the events of the top-right button
  - cluster Descriptor with its TagList containing four tags: Position.Top, Position.Right, Number.Two and (Tag=Switches.Custom, Label="dinner")
- endpoint 23 has device type Generic Switch and contains
  - cluster Switch (feature flags: MS) exposing the events of the bottom-left button
  - cluster Descriptor with its TagList containing four tags: Position.Bottom, Position.Left, Number.Three and (Tag=Switches.Custom, Label="reading")
- endpoint 24 has device type Generic Switch and contains

- cluster Switch (feature flags: MS) exposing the events of the bottom-right button
- cluster Descriptor with its TagList containing four tags: Position.Bottom, Position.Right, Number.Four and (Tag=Switches.Custom, Label="nightlight")

#### <span id="page-80-0"></span>**6.6.5. Relation with other Switch device types (informative)**

The Generic Switch device type and the On/Off Light Switch device type both convey information about interactions with a switch to another device.

- The On/Off Light Switch will send On/Off/Toggle commands from its On/Off (client) cluster to a device implementing the On/Off (server) cluster to control the on/off functionality of that device. An On/Off Light Switch device can also implement Groups and Scenes Management clusters and thus send group and scene commands. Basically, it is targeted at directly sending control commands to other devices. The binding table is used to tell the device where to send the commands.
- The Generic Switch device type will send updates of attributes (for Latching Switch only) and events to subscribed parties which implement the Switch client cluster, as indications of interaction with the switch - leaving the interpretation (e.g. which device should be actuated because of the interaction) to the subscribed party. So it can be compared to a sensor-type device. This allows a more comprehensive controller to combine the information from the switch with other inputs or information sources (e.g. time of day, user presence) to determine which control commands (e.g. on/off, scene recall, attribute change) are sent to other devices in the network.

A device manufacturer MAY implement both device types on the same switch device, to allow it to be used for both types of control, as in this example for a rocker switch which implements:

- endpoint 31 with device type On/Off Light Switch which contains
  - (client) cluster On/Off exposing the On/Off/Toggle commands
- endpoint 32 with device type Generic Switch which contains
  - (server) cluster Switch (feature flags: LS) exposing the state and events of the switch

When this device is used in a particular setup, binding tables and subscriptions can be used to determine how it is used:

- used as an On/Off Light Switch (no subscriptions to endpoint 32)
- used as a Generic Switch (no bindings on endpoint 31)
- used as both at the same time. In this case, an interaction with the switch would result in an On/Off/Toggle command being sent to devices listed in the binding table of endpoint 31, as well as attribute update and events being sent towards devices having a subscription with endpoint 32.

# <span id="page-82-0"></span>**Chapter 7. Sensor Device Types**

# <span id="page-82-1"></span>**7.1. Contact Sensor Device Type**

This defines conformance to the Contact Sensor device type.

#### <span id="page-82-2"></span>**7.1.1. Revision History**

| Revision | Description                                            |  |
|----------|--------------------------------------------------------|--|
| 1        | Initial revision                                       |  |
| 2        | Add Boolean State Configuration as optional<br>cluster |  |

#### <span id="page-82-3"></span>**7.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0015         | Contact Sensor      |             | Simple | Endpoint |

#### <span id="page-82-4"></span>**7.1.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-82-5"></span>**7.1.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance |
|------------|---------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                        | Server        |         | M           |
| 0x0045     | Boolean State                   | Server        |         | M           |
| 0x0080     | Boolean State Con<br>figuration | Server        |         | O           |

#### **7.1.4.1. Identify Cluster**

This is used to identify the endpoint.

#### **7.1.4.2. Boolean State Cluster**

This is used to indicate the state of the sensor/detector.

The state of the Boolean State cluster SHALL reflect the sensor detection using this scheme:

| Value | State              |  |
|-------|--------------------|--|
| True  | Closed or contact  |  |
| False | Open or no contact |  |

#### **7.1.4.3. Boolean State Configuration Cluster**

This is used to configure the sensor/detector and is for this device type linked to the configuration of the Boolean State cluster.

# <span id="page-83-0"></span>**7.2. Light Sensor Device Type**

A Light Sensor device is a measurement and sensing device that is capable of measuring and reporting the intensity of light (illuminance) to which the sensor is being subjected.

#### <span id="page-83-1"></span>**7.2.1. Revision History**

| Revision | Description                          |  |
|----------|--------------------------------------|--|
| 1        | Initial Zigbee 3.0 revision          |  |
| 2        | New data model format and notation   |  |
| 3        | Restricting Groups client to Zigbee. |  |
| 4        | Removed Zigbee related elements      |  |

#### <span id="page-83-2"></span>**7.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0106         | Light Sensor        |             | Simple | Endpoint |

#### <span id="page-83-3"></span>**7.2.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-83-4"></span>**7.2.4. Cluster Requirements**

*Table 9. Light Sensor Cluster Requirements*

| Cluster ID | Cluster Name                | Client/Server | Quality | Conformance |
|------------|-----------------------------|---------------|---------|-------------|
| 0x0003     | Identify                    | Server        |         | M           |
| 0x0400     | Illuminance Mea<br>surement | Server        |         | M           |

# <span id="page-84-0"></span>**7.3. Occupancy Sensor Device Type**

An Occupancy Sensor is a measurement and sensing device that is capable of measuring and reporting the occupancy state in a designated area.

#### <span id="page-84-1"></span>**7.3.1. Revision History**

| Revision | Description                                                                               |
|----------|-------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                               |
| 2        | New data model format and notation                                                        |
| 3        | Restricting Groups client to Zigbee                                                       |
| 4        | Add Boolean State Configuration as optional<br>cluster and remove Zigbee related elements |

#### <span id="page-84-2"></span>**7.3.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0107         | Occupancy Sensor    |             | Simple | Endpoint |

### <span id="page-84-3"></span>**7.3.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-84-4"></span>**7.3.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance |
|------------|---------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                        | Server        |         | M           |
| 0x0080     | Boolean State Con<br>figuration | Server        |         | O           |
| 0x0406     | Occupancy Sens<br>ing           | Server        |         | M           |

#### **7.3.4.1. Identify Cluster**

This is used to identify the endpoint.

#### **7.3.4.2. Boolean State Configuration Cluster**

This is used to configure the sensor/detector (e.g. sensitivity) and is for this device type linked to the configuration of the Occupancy Sensing cluster on the same endpoint.

#### **7.3.4.3. Occupancy Sensing Cluster**

This is used to indicate occupancy as well as the type of occupancy sensor used for detection and configuring the delays related to the occupied and unoccupied transitions.

#### <span id="page-85-0"></span>**7.3.5. Multi-modality sensors**

The Occupancy Sensing cluster defines multiple modalities that can be employed to sense occupancy. A device implementing multiple such modalities (exposed in the feature flags) can be implemented in two ways:

- A single endpoint with an Occupancy Sensing cluster which has two or more of these feature bits set to 1.
  - This requires reporting the combination the sensing results as a single bit in the Occupancy attribute (and the OccupancyChanged event, when supported), with a single set of timing parameters applied.
  - Sensitivity setting (via a Boolean State Configuration cluster on the same endpoint) applies to all the sensing modalities together via a manufacturer-specific mapping.
- Multiple endpoints each hosting an Occupancy Sensing cluster (each with one feature bit set):
  - The sensing result of each modality is reported separately in the Occupancy attribute (and the OccupancyChanged event, when supported) of each endpoint, governed by the set of timing parameters provided in the cluster on that endpoint.
    - This implies some of these attributes can have a different values than their counterparts on other endpoints and that a client MAY have to combine these values if it wants to derive a single value.
  - Each modality can be provided with an independent sensitivity setting via a Boolean State Configuration cluster located on one or more of the endpoints.

# <span id="page-85-1"></span>**7.4. Temperature Sensor Device Type**

A Temperature Sensor device reports measurements of temperature.

### <span id="page-85-2"></span>**7.4.1. Revision History**

| Revision | Description                                                                                  |
|----------|----------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                                  |
| 2        | New data model format and notation                                                           |
| 3        | Added Thermostat User Interface Configuration<br>cluster and removed Zigbee related elements |

#### <span id="page-85-3"></span>**7.4.2. Classification**

| Device Type ID | Device Type<br>Name    | Superset Of | Class  | Scope    |
|----------------|------------------------|-------------|--------|----------|
| 0x0302         | Temperature Sen<br>sor |             | Simple | Endpoint |

#### <span id="page-86-0"></span>**7.4.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-86-1"></span>**7.4.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                                   | Client/Server | Quality | Conformance |
|------------|------------------------------------------------|---------------|---------|-------------|
| 0x0402     | Temperature Mea<br>surement                    | Server        |         | M           |
| 0x0003     | Identify                                       | Server        |         | M           |
| 0x0204     | Thermostat User<br>Interface Configu<br>ration | Server        |         | O           |

#### **7.4.4.1. Thermostat User Interface Configuration Cluster**

This cluster provides an interface to allow configuration of the user interface for a temperature sensor that supports keypad or screen.

### <span id="page-86-2"></span>**7.4.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                                    | Element   | Name              | Constraint | Access | Confor<br>mance |
|------------|----------------------------------------------------|-----------|-------------------|------------|--------|-----------------|
| 0x0204     | Thermostat<br>User Inter<br>face Configu<br>ration | Attribute | KeypadLock<br>out |            |        | O               |

# <span id="page-86-3"></span>**7.5. Pressure Sensor Device Type**

A Pressure Sensor device measures and reports the pressure of a fluid.

#### <span id="page-87-0"></span>**7.5.1. Revision History**

| Revision | Description                        |
|----------|------------------------------------|
| 1        | Initial Zigbee 3.0 revision        |
| 2        | New data model format and notation |
| 3        | Removed Zigbee related elements    |

### <span id="page-87-1"></span>**7.5.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0305         | Pressure Sensor     |             | Simple | Endpoint |

#### <span id="page-87-2"></span>**7.5.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-87-3"></span>**7.5.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0003     | Identify                 | Server        |         | M           |
| 0x0403     | Pressure Measure<br>ment | Server        |         | M           |

# <span id="page-87-4"></span>**7.6. Flow Sensor Device Type**

A Flow Sensor device measures and reports the flow rate of a fluid.

### <span id="page-87-5"></span>**7.6.1. Revision History**

| Revision | Description                        |
|----------|------------------------------------|
| 1        | Initial Zigbee 3.0 revision        |
| 2        | New data model format and notation |
| 3        | Removed Zigbee related elements    |

#### <span id="page-87-6"></span>**7.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0306         | Flow Sensor         |             | Simple | Endpoint |

#### <span id="page-88-0"></span>**7.6.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-88-1"></span>**7.6.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name         | Client/Server | Quality | Conformance |
|------------|----------------------|---------------|---------|-------------|
| 0x0003     | Identify             | Server        |         | M           |
| 0x0404     | Flow Measure<br>ment | Server        |         | M           |

# <span id="page-88-2"></span>**7.7. Humidity Sensor Device Type**

A humidity sensor (in most cases a Relative humidity sensor) reports humidity measurements.

#### <span id="page-88-3"></span>**7.7.1. Revision History**

| Revision | Description                        |
|----------|------------------------------------|
| 1        | Initial Zigbee 3.0 revision        |
| 2        | New data model format and notation |
| 3        | Removed Zigbee related elements    |

#### <span id="page-88-4"></span>**7.7.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0307         | Humidity Sensor     |             | Simple | Endpoint |

#### <span id="page-88-5"></span>**7.7.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-88-6"></span>**7.7.4. Cluster Requirements**

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                         | Server        |         | M           |
| 0x0405     | Relative Humidity<br>Measurement | Server        |         | M           |

# <span id="page-89-0"></span>**7.8. On/Off Sensor Device Type**

An On/Off Sensor is a measurement and sensing device that, when bound to a lighting device such as a Dimmable Light, is capable of being used to switch the device on or off.

#### <span id="page-89-1"></span>**7.8.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |

#### <span id="page-89-2"></span>**7.8.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0850         | On/Off Sensor       |             | Simple | Endpoint |

### <span id="page-89-3"></span>**7.8.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-89-4"></span>**7.8.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

*Table 10. On/Off Sensor Cluster Requirements*

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0003     | Identify              | Client        |         | M           |
| 0x0004     | Groups                | Client        |         | O           |
| 0x0006     | On/Off                | Client        |         | M           |
| 0x0008     | Level Control         | Client        |         | O           |
| 0x0062     | Scenes Manage<br>ment | Client        |         | O           |
| 0x0300     | Color Control         | Client        |         | O           |

# <span id="page-89-5"></span>**7.9. Smoke CO Alarm Device Type**

A Smoke CO Alarm device is capable of sensing smoke, carbon monoxide or both. It is capable of

issuing a visual and audible alert to indicate elevated concentration of smoke or carbon monoxide.

Smoke CO Alarms are capable of monitoring themselves and issuing visual and audible alerts for hardware faults, critical low battery conditions, and end of service. Optionally, some of the audible alerts can be temporarily silenced. Smoke CO Alarms are capable of performing a self-test which performs a diagnostic of the primary sensor and issuing a cycle of the audible and visual life safety alarm indications.

Some smoke alarms MAY be capable of adjusting sensitivity. Smoke CO Alarm MAY have the ability to detect and report humidity levels, temperature levels, and contamination levels.

#### <span id="page-90-0"></span>**7.9.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-90-1"></span>**7.9.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0076         | Smoke CO Alarm      |             | Simple | Endpoint |

#### <span id="page-90-2"></span>**7.9.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-90-3"></span>**7.9.4. Device Type Requirements**

A Smoke CO Alarm device type SHALL support an instance of a Power Source device type on some endpoint. See the Power Source cluster for more information.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0011         | Power Source     | min 1      | M           |

## <span id="page-90-4"></span>**7.9.5. Cluster Requirements**

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                         | Server        |         | M           |
| 0x0004     | Groups                           | Server        |         | O           |
| 0x005C     | Smoke CO Alarm                   | Server        |         | M           |
| 0x0405     | Relative Humidity<br>Measurement | Server        |         | O           |

| Cluster ID | Cluster Name                                    | Client/Server | Quality | Conformance |
|------------|-------------------------------------------------|---------------|---------|-------------|
| 0x0402     | Temperature Mea<br>surement                     | Server        |         | O           |
| 0x040C     | Carbon Monoxide<br>Concentration<br>Measurement | Server        |         | O           |

# <span id="page-91-0"></span>**7.10. Air Quality Sensor Device Type**

This defines conformance for the Air Quality Sensor device type.

An air quality sensor is a device designed to monitor and measure various parameters related to the quality of ambient air in indoor or outdoor environments.

#### <span id="page-91-1"></span>**7.10.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

### <span id="page-91-2"></span>**7.10.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x002C         | Air Quality Sensor  |             | Simple | Endpoint |

#### <span id="page-91-3"></span>**7.10.3. Conditions**

See the Base Device Type definition for conformance tags.

## <span id="page-91-4"></span>**7.10.4. Cluster Requirements**

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                         | Server        |         | M           |
| 0x005B     | Air Quality                      | Server        |         | M           |
| 0x0402     | Temperature Mea<br>surement      | Server        |         | O           |
| 0x0405     | Relative Humidity<br>Measurement | Server        |         | O           |

| Cluster ID | Cluster Name                                                          | Client/Server | Quality | Conformance |
|------------|-----------------------------------------------------------------------|---------------|---------|-------------|
| 0x040C     | Carbon Monoxide<br>Concentration<br>Measurement                       | Server        |         | O           |
| 0x040D     | Carbon Dioxide<br>Concentration<br>Measurement                        | Server        |         | O           |
| 0x0413     | Nitrogen Dioxide<br>Concentration<br>Measurement                      | Server        |         | O           |
| 0x0415     | Ozone Concentra<br>tion Measurement                                   | Server        |         | O           |
| 0x042A     | PM2.5 Concentra<br>tion Measurement                                   | Server        |         | O           |
| 0x042B     | Formaldehyde<br>Concentration<br>Measurement                          | Server        |         | O           |
| 0x042C     | PM1 Concentra<br>tion Measurement                                     | Server        |         | O           |
| 0x042D     | PM10 Concentra<br>tion Measurement                                    | Server        |         | O           |
| 0x042E     | Total Volatile<br>Organic Com<br>pounds Concentra<br>tion Measurement | Server        |         | O           |
| 0x042F     | Radon Concentra<br>tion Measurement                                   | Server        |         | O           |

# <span id="page-92-0"></span>**7.11. Water Freeze Detector Device Type**

This defines conformance to the Water Freeze Detector device type.

### <span id="page-92-1"></span>**7.11.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-92-2"></span>**7.11.2. Classification**

| Device Type ID | Device Type<br>Name      | Superset Of | Class  | Scope    |
|----------------|--------------------------|-------------|--------|----------|
| 0x0041         | Water Freeze<br>Detector |             | Simple | Endpoint |

#### <span id="page-93-0"></span>**7.11.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-93-1"></span>**7.11.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance |
|------------|---------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                        | Server        |         | M           |
| 0x0045     | Boolean State                   | Server        |         | M           |
| 0x0080     | Boolean State Con<br>figuration | Server        |         | O           |

#### **7.11.4.1. Identify Cluster**

This is used to identify the endpoint.

#### **7.11.4.2. Boolean State Cluster**

This is used to indicate the state of the sensor/detector.

The state of the Boolean State cluster SHALL reflect the sensor detection using this scheme of:

| Value | State                                                                 |
|-------|-----------------------------------------------------------------------|
| True  | Water could potentially freeze in the current<br>ambient conditions   |
| False | Water is very unlikely to freeze in the current<br>ambient conditions |

Due to the difficulty in quantifying the risk of freezing based on the dependency on external factors such as temperature, humidity, pressure, etc, the actual triggering of a detector of this type depends on the physical construction and characteristics of the device and is therefore considered manufacturer specific.

#### **7.11.4.3. Boolean State Configuration Cluster**

This is used to configure the sensor/detector and is for this device type linked to the configuration of the Boolean State cluster.

#### <span id="page-94-0"></span>**7.11.5. Element Requirements**

The following table lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name  | Element | Name        | Constraint | Access | Confor<br>mance |
|------------|------------------|---------|-------------|------------|--------|-----------------|
| 0x0045     | Boolean<br>State | Event   | StateChange |            |        | M               |

# <span id="page-94-1"></span>**7.12. Water Leak Detector Device Type**

This defines conformance to the Water Leak Detector device type.

#### <span id="page-94-2"></span>**7.12.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

### <span id="page-94-3"></span>**7.12.2. Classification**

| Device Type ID | Device Type<br>Name     | Superset Of | Class  | Scope    |
|----------------|-------------------------|-------------|--------|----------|
| 0x0043         | Water Leak Detec<br>tor |             | Simple | Endpoint |

#### <span id="page-94-4"></span>**7.12.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-94-5"></span>**7.12.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance |
|------------|---------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                        | Server        |         | M           |
| 0x0045     | Boolean State                   | Server        |         | M           |
| 0x0080     | Boolean State Con<br>figuration | Server        |         | O           |

#### **7.12.4.1. Identify Cluster**

This is used to identify the endpoint.

#### **7.12.4.2. Boolean State Cluster**

This is used to indicate the state of the sensor/detector.

The state of the Boolean State cluster SHALL reflect the sensor detection using this scheme of:

| Value | State                  |
|-------|------------------------|
| True  | Water leak detected    |
| False | No water leak detected |

#### **7.12.4.3. Boolean State Configuration Cluster**

This is used to configure the sensor/detector and is for this device type linked to the configuration of the Boolean State cluster.

#### <span id="page-95-0"></span>**7.12.5. Element Requirements**

The following table lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name  | Element | Name        | Constraint | Access | Confor<br>mance |
|------------|------------------|---------|-------------|------------|--------|-----------------|
| 0x0045     | Boolean<br>State | Event   | StateChange |            |        | M               |

# <span id="page-95-1"></span>**7.13. Rain Sensor Device Type**

This defines conformance to the Rain Sensor device type.

### <span id="page-95-2"></span>**7.13.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-95-3"></span>**7.13.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0044         | Rain Sensor         |             | Simple | Endpoint |

#### <span id="page-95-4"></span>**7.13.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-96-0"></span>**7.13.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                    | Client/Server | Quality | Conformance |
|------------|---------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                        | Server        |         | M           |
| 0x0045     | Boolean State                   | Server        |         | M           |
| 0x0080     | Boolean State Con<br>figuration | Server        |         | O           |

#### **7.13.4.1. Identify Cluster**

This is used to identify the endpoint.

#### **7.13.4.2. Boolean State Cluster**

This is used to indicate the state of the sensor/detector.

The state of the Boolean State cluster SHALL reflect the sensor detection using this scheme of:

| Value | State            |
|-------|------------------|
| True  | Rain detected    |
| False | No rain detected |

#### **7.13.4.3. Boolean State Configuration Cluster**

This is used to configure the sensor/detector and is for this device type linked to the configuration of the Boolean State cluster.

## <span id="page-96-1"></span>**7.13.5. Element Requirements**

The following table lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name  | Element | Name        | Constraint | Access | Confor<br>mance |
|------------|------------------|---------|-------------|------------|--------|-----------------|
| 0x0045     | Boolean<br>State | Event   | StateChange |            |        | M               |

# <span id="page-96-2"></span>**7.14. Soil Sensor Device Type**

A Soil Sensor device reports measurements of soil values, such as moisture and (optionally) temperature.

#### <span id="page-97-0"></span>**7.14.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-97-1"></span>**7.14.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0045         | Soil Sensor         |             | Simple | Endpoint |

#### <span id="page-97-2"></span>**7.14.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-97-3"></span>**7.14.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                | Client/Server | Quality | Conformance |
|------------|-----------------------------|---------------|---------|-------------|
| 0x0003     | Identify                    | Server        |         | M           |
| 0x0402     | Temperature Mea<br>surement | Server        |         | O           |
| 0x0430     | Soil Measurement            | Server        |         | M           |

#### **7.14.4.1. Identify Cluster**

This is used to identify the endpoint.

#### **7.14.4.2. Temperature Measurement Cluster**

This is used to provide the temperature of the soil. Measurements SHOULD be done either in the soil or very close to the soil, in order to NOT provide ambient temperature measurements.

#### **7.14.4.3. Soil Measurement Cluster**

This is used to provide the humidity of the soil.

# <span id="page-98-0"></span>**Chapter 8. Entry Control Device Types**

Entry Control device types are device types that control entry to a space, e.g. by people, pets, sun, wind, or rain.

# <span id="page-98-1"></span>**8.1. Door Lock Device Type**

A Door Lock is a device used to secure a door. It is possible to actuate a door lock either by means of a manual or a remote method.

#### <span id="page-98-2"></span>**8.1.1. Revision History**

| Revision | Description                                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                                                                                            |
| 2        | Initial Matter revision                                                                                                                                |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062; as noted below,<br>this cluster remains disallowed in this device<br>type |
| 4        | Removed Zigbee related elements                                                                                                                        |

#### <span id="page-98-3"></span>**8.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x000A         | Door Lock           |             | Simple | Endpoint |

#### <span id="page-98-4"></span>**8.1.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-98-5"></span>**8.1.4. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition                  | Conformance |
|----------|----------------|---------------------|----------------------------|-------------|
| Root     | 0x0016         | Root Node           | ACLExtension<br>Cond       | M           |
| Root     | 0x0016         | Root Node           | TimeSyncCond               | O           |
| Root     | 0x0016         | Root Node           | TimeSyncWith<br>ClientCond | O           |

#### <span id="page-99-0"></span>**8.1.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Server        |         | M           |
| 0x0004     | Groups                | Server        |         | X           |
| 0x0062     | Scenes Manage<br>ment | Server        |         | X           |
| 0x0101     | Door Lock             | Server        |         | M           |

# <span id="page-99-1"></span>**8.2. Door Lock Controller Device Type**

A Door Lock Controller is a device capable of controlling a door lock.

### <span id="page-99-2"></span>**8.2.1. Revision History**

| Revision | Description                                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                                                       |
| 2        | Initial Matter revision                                                                                           |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 and remove Zigbee<br>related elements |

#### <span id="page-99-3"></span>**8.2.2. Classification**

| Device Type ID | Device Type<br>Name      | Superset Of | Class  | Scope    |
|----------------|--------------------------|-------------|--------|----------|
| 0x000B         | Door Lock Con<br>troller |             | Simple | Endpoint |

### <span id="page-99-4"></span>**8.2.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-99-5"></span>**8.2.4. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition    | Conformance |
|----------|----------------|---------------------|--------------|-------------|
| Root     | 0x0016         | Root Node           | TimeSyncCond | O           |

#### <span id="page-100-0"></span>**8.2.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0004     | Groups                | Client        |         | O           |
| 0x0062     | Scenes Manage<br>ment | Client        |         | O           |
| 0x0101     | Door Lock             | Client        |         | M           |

# <span id="page-100-1"></span>**8.3. Window Covering Device Type**

This defines conformance to the Window Covering device type.

#### <span id="page-100-2"></span>**8.3.1. Revision History**

| Revision | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                 |
| 2        | New data model format and notation                                          |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062 |
| 4        | Scenes Management cluster was removed from<br>Cluster Requirements          |
| 5        | Introduced conditions on Closure clusters                                   |
| 6        | Removed Zigbee related elements                                             |

#### <span id="page-100-3"></span>**8.3.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0202         | Window Covering     |             | Simple | Endpoint |

#### <span id="page-100-4"></span>**8.3.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-100-5"></span>**8.3.4. Cluster Requirements**

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0003     | Identify                 | Server        |         | M           |
| 0x0004     | Groups                   | Server        |         | Active, O   |
| 0x0102     | Window Covering          | Server        |         | M           |
| 0x0104     | Closure Control          | Server        |         | X           |
| 0x0105     | Closure Dimension Server |               |         | X           |

Furthermore, in revision at or before revision 5 for this device type, either or both of the Closure Control cluster and the Closure Dimension cluster SHALL NOT appear on the same endpoint. This is to avoid potential future usage of the closely related Closure Control cluster in this device type from interfering with non-standard usage of that cluster until proper data dependency language can be introduced, if any.

# <span id="page-101-0"></span>**8.4. Window Covering Controller Device Type**

A Window Covering Controller is a device that controls an automatic window covering.

#### <span id="page-101-1"></span>**8.4.1. Revision History**

| Revision | Description                                                                                               |
|----------|-----------------------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                                               |
| 2        | New data model format and notation                                                                        |
| 3        | Updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062                               |
| 4        | Removed Zigbee related elements and Scenes<br>Management cluster was removed from Cluster<br>Requirements |

#### <span id="page-101-2"></span>**8.4.2. Classification**

| Device Type ID | Device Type<br>Name           | Superset Of | Class  | Scope    |
|----------------|-------------------------------|-------------|--------|----------|
| 0x0203         | Window Covering<br>Controller |             | Simple | Endpoint |

#### <span id="page-101-3"></span>**8.4.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-101-4"></span>**8.4.4. Cluster Requirements**

| Cluster ID | Cluster Name    | Client/Server | Quality | Conformance |
|------------|-----------------|---------------|---------|-------------|
| 0x0003     | Identify        | Server        |         | O           |
| 0x0003     | Identify        | Client        |         | O           |
| 0x0004     | Groups          | Client        |         | Active, O   |
| 0x0102     | Window Covering | Client        |         | M           |

# <span id="page-102-0"></span>**8.5. Closure Device Type**

A Closure is an element that seals an opening (such as a window, door, cabinet, wall, facade, ceiling, or roof). It MAY contain one or more instances of a [Closure Panel](#page-106-0) device type on separate child endpoints of the Closure parent. Each Closure Panel is a sub-component of a Closure, capable of some change in state, primarily through a movement.

All the common characteristics of a Closure are gathered within Closure Control Cluster. Moving parts or other physical aspects of the device are exposed using Closure Dimension Cluster.

#### <span id="page-102-1"></span>**8.5.1. Closure Architecture**

A Closure is a composed device type that MAY include additional device types on separate child endpoints. See the Device Type Requirements section below for details.

A Closure SHALL use exactly one semantic tag from the Closure namespace in the TagList attribute of the Descriptor cluster to describe the primary function of the device, e.g., "Window", "Covering", or "Cabinet". Semantic tags from the Closure Window, Closure Covering and Closure Cabinet namespaces, in addition to the Common namespaces, MAY be used to convey additional configuration information.

An example of a Closure device with multiple Closure Panel devices on separate child endpoints is illustrated below.

![](_page_103_Figure_2.jpeg)

*Figure 3. Example of a Closure with multiple panels*

An example of a Closure with a single panel on a separate child endpoint is illustrated below.

![](_page_103_Figure_5.jpeg)

*Figure 4. Example of a Closure with single panel*

An example of a Closure as a standalone device type is illustrated below.

*Figure 5. Example of a Closure as standalone device type*

#### <span id="page-104-0"></span>**8.5.2. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-104-1"></span>**8.5.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0230         | Closure             |             | Simple | Endpoint |

### <span id="page-104-2"></span>**8.5.4. Device Type Requirements**

A Closure device MAY be composed of other device types listed in the table below subject to the conformance column of the table. All devices used in compositions SHALL adhere to the disambiguation and superset requirements of the System Model.

Note that the On/Off Light listed in the table below is part of a Superset Device Type relationship as defined by the System Model (see Superset Device Types in [\[MatterCore\]\)](#page-23-5), and so the rules defined in that section apply to the use of an On/Off Light or its Superset device types when included on separate child endpoints.

The use of semantic tags in the Descriptor cluster TagList SHALL adhere to the disambiguation and superset requirements of the System Model. Other semantic tags from other namespaces MAY be used to convey additional configuration information.

All instances of Closure Panel devices included in a composition SHALL reflect the current state of the associated panels, and operate in relation to the ClosureControl cluster at the top of the hierarchy. In other words, successfully opening/closing the closure via the ClosureControl cluster SHALL be followed by appropriate attribute updates in the ClosureDimension cluster that reflect the panels being in the state requested. Similarly, operating the ClosureDimension cluster instances SHALL cause the attributes of the ClosureControl instance at the top of the hierarchy to reflect the correct state of opening and closing at the same time.

Additional device types not listed in this table MAY also be included in device compositions.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x000A         | Door Lock        |            | O           |
| 0x0100+        | On/Off Light+    |            | O           |
| 0x0231         | Closure Panel    |            | O           |

#### <span id="page-105-0"></span>**8.5.5. Cluster Requirements**

Each endpoint supporting the Closure device type MAY include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0003     | Identify                 | Server        |         | M           |
| 0x0102     | Window Covering          | Server        |         | X           |
| 0x0104     | Closure Control          | Server        |         | M           |
| 0x0105     | Closure Dimension Server |               |         | X           |

In revision 1 of this device type, the Window Covering cluster SHALL NOT be present on the same endpoint. This restriction prevents conflicts between future standardized uses of the Window Covering cluster and any current non-standard implementations, until appropriate data dependency language is defined.

### <span id="page-105-1"></span>**8.5.6. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance |  |
|------------|-----------------|---------|---------|------------|--------|-----------------|--|
| 0x001D     | Descriptor      | Feature | TagList |            |        | M               |  |

The TagList in the Descriptor cluster of an endpoint with this device type SHALL meet the following constraints:

- There SHALL be exactly one tag from the Closure namespace (namespace 0x44) to identify the type of closure device.
- There SHALL NOT be any tag from the ClosurePanel namespace (namespace 0x45), among all the other tags.

# <span id="page-106-0"></span>**8.6. Closure Panel Device Type**

A Closure Panel SHALL ONLY exist as a part (child) of a [Closure](#page-102-0) device type. It represents a single panel aspect (e.g. position of a blind, tilt of slats, etc) within that Closure.

This panel can be used to express the following:

- Translation : panel translates along one axis
- Rotation : panel rotates around an axis of rotation
- Modulation : panel modifies its aspect to modulate a flow

A Closure Panel SHALL use exactly one semantic tag from the ClosurePanel namespace (0x45) in the TagList attribute of the Descriptor cluster to describe the spatial aspect of the dimension, e.g., "Lift", "Tilt", etc.

### <span id="page-106-1"></span>**8.6.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-106-2"></span>**8.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0231         | Closure Panel       |             | Simple | Endpoint |

### <span id="page-106-3"></span>**8.6.3. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0102     | Window Covering          | Server        |         | X           |
| 0x0104     | Closure Control          | Server        |         | X           |
| 0x0105     | Closure Dimension Server |               |         | M           |

In revision 1 of this device type, the Window Covering cluster SHALL NOT appear on the same endpoint. This restriction prevents conflicts between potential future standardized use of the Window Covering cluster and any existing non-standard implementations, until appropriate data dependency language is defined.

### <span id="page-106-4"></span>**8.6.4. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------|------------|--------|-----------------|
| 0x001D     | Descriptor      | Feature | TagList |            |        | M               |

The TagList in the Descriptor cluster of an endpoint with this device type SHALL meet the following constraints:

- There SHALL be exactly one tag from the ClosurePanel namespace (namespace 0x45).
- There SHALL NOT be any tag from the Closure namespace (namespace 0x44).

# <span id="page-107-0"></span>**8.7. Closure Controller Device Type**

A Closure Controller is capable of controlling a [Closure.](#page-102-0)

#### <span id="page-107-1"></span>**8.7.1. Introduction**

Two levels of control are available:

- Basic Level (Closure Control Cluster):
  - Used for simple controller with buttons like wall switches.
  - Also all the general status and information remain at this level.
- Advanced Level (Closure Dimension Cluster):
  - Provides advanced information, controls and settings.
  - Used for advanced controller.

![](_page_107_Figure_17.jpeg)

*Figure 6. Closure Levels View*

#### <span id="page-107-2"></span>**8.7.2. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-108-0"></span>**8.7.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x023E         | Closure Controller  |             | Simple | Endpoint |

#### <span id="page-108-1"></span>**8.7.4. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-108-2"></span>**8.7.5. Cluster Requirements**

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0003     | Identify                 | Client        |         | O           |
| 0x0004     | Groups                   | Client        |         | O           |
| 0x0104     | Closure Control          | Client        |         | M           |
| 0x0105     | Closure Dimension Client |               |         | O           |

# <span id="page-110-0"></span>**Chapter 9. HVAC Device Types**

# <span id="page-110-1"></span>**9.1. Thermostat Device Type**

A Thermostat device is capable of having either built-in or separate sensors for temperature, humidity or occupancy. It allows the desired temperature to be set either remotely or locally. The thermostat is capable of sending heating and/or cooling requirement notifications to a heating/cooling unit (for example, an indoor air handler) or is capable of including a mechanism to control a heating or cooling unit directly.

#### <span id="page-110-2"></span>**9.1.1. Revision History**

| Revision | Description                                                                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Initial Zigbee 3.0 revision                                                                                                                         |
| 2        | New data model format and notation, added<br>Clusters required for Matter support, restricted<br>legacy elements to Zigbee only                     |
| 3        | Addition of Energy Preference cluster and<br>updated the Scenes cluster to Scenes Manage<br>ment with Cluster ID: 0x0062                            |
| 4        | Remove Time Synchronization cluster, Scenes<br>Management and Zigbee only clusters, remove<br>provisional marking from Energy Preference<br>cluster |
| 5        | Moved disallowed element conformance to<br>Thermostat cluster.                                                                                      |

#### <span id="page-110-3"></span>**9.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0301         | Thermostat          |             | Simple | Endpoint |

#### <span id="page-110-4"></span>**9.1.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-110-5"></span>**9.1.4. Cluster Requirements**

| Cluster ID | Cluster Name                                   | Client/Server | Quality | Conformance |
|------------|------------------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                                       | Server        |         | M           |
| 0x0004     | Groups                                         | Server        |         | Active      |
| 0x009B     | Energy Preference                              | Server        |         | O           |
| 0x0201     | Thermostat                                     | Server        |         | M           |
| 0x0202     | Fan Control                                    | Client        |         | O           |
| 0x0204     | Thermostat User<br>Interface Configu<br>ration | Server        |         | O           |
| 0x0402     | Temperature Mea<br>surement                    | Client        |         | O           |
| 0x0405     | Relative Humidity<br>Measurement               | Client        |         | O           |
| 0x0406     | Occupancy Sens<br>ing                          | Client        |         | O           |

# <span id="page-111-0"></span>**9.2. Fan Device Type**

A Fan device is typically standalone or mounted on a ceiling or wall and is used to circulate air in a room.

### <span id="page-111-1"></span>**9.2.1. Revision History**

| Revision | Description                                                         |
|----------|---------------------------------------------------------------------|
| 1        | Initial revision                                                    |
| 2        | Added ability to be composed with a Thermostat<br>for fan heaters   |
| 3        | Added On/Off cluster                                                |
| 4        | Moved FanModeSequence element requirement<br>to Fan Control cluster |

#### <span id="page-111-2"></span>**9.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x002B         | Fan                 |             | Simple | Endpoint |

### <span id="page-111-3"></span>**9.2.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-112-0"></span>**9.2.4. Device Type Requirements**

A fan MAY expose elements of its functionality through one or more additional device types on different endpoints. All devices used in compositions SHALL adhere to the disambiguation requirements of the System Model. Other device types, not explicitly listed in the table, MAY also be included in device compositions but are not considered part of the core functionality of the device.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0301         | Thermostat       |            | O           |

#### <span id="page-112-1"></span>**9.2.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | server        |         | M           |
| 0x0004     | Groups       | server        |         | M           |
| 0x0006     | On/Off       | server        |         | O           |
| 0x0202     | Fan Control  | server        |         | M           |

#### <span id="page-112-2"></span>**9.2.6. Cluster Restrictions**

#### **9.2.6.1. On/Off Cluster (Server) Clarifications**

The On/Off cluster is independent from the Fan Control Cluster's FanMode attribute, which also includes an Off setting.

If the FanMode attribute of the Fan Control cluster is set to a value other than Off when the OnOff attribute of the On/Off cluster transitions from TRUE to FALSE, it may be desirable to restore the FanMode, SpeedSetting and PercentSetting attribute values of the Fan Control cluster when the OnOff attribute of the On/Off cluster later transitions from FALSE to TRUE. If the FanMode is set to Off when the device is turned off, this information is lost, as the SpeedSetting and PercentSetting will be set to zero. Using the On/Off cluster alongside the Fan Control cluster allows the FanMode, SpeedSetting and PercentSetting to remain unchanged when the device is turned off. In this case, the On/Off cluster would be set to Off, and the SpeedCurrent and PercentCurrent set to zero, without changing FanMode, SpeedSetting and PercentSetting.

# <span id="page-112-3"></span>**9.3. Air Purifier Device Type**

An Air Purifier is a standalone device that is designed to clean the air in a room.

It is a device that has a fan to control the air speed while it is operating. Optionally, it can report on the condition of its filters.

#### <span id="page-113-0"></span>**9.3.1. Revision History**

| Revision | Description          |
|----------|----------------------|
| 1        | Initial revision     |
| 2        | Added On/Off cluster |

#### <span id="page-113-1"></span>**9.3.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x002D         | Air Purifier        |             | Simple | Endpoint |

#### <span id="page-113-2"></span>**9.3.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-113-3"></span>**9.3.4. Device Type Requirements**

An Air Purifier MAY expose elements of its functionality through one or more additional device types on different endpoints. All devices used in compositions SHALL adhere to the disambiguation requirements of the System Model. Other device types, not explicitly listed in the table, MAY also be included in device compositions but are not considered part of the core functionality of the device.

| Device Type ID | Device Type Name   | Constraint | Conformance |
|----------------|--------------------|------------|-------------|
| 0x002C         | Air Quality Sensor |            | O           |
| 0x0301         | Thermostat         |            | O           |
| 0x0302         | Temperature Sensor |            | O           |
| 0x0307         | Humidity Sensor    |            | O           |

### <span id="page-113-4"></span>**9.3.5. Cluster Requirements**

| Cluster ID | Cluster Name                          | Client/Server | Quality | Conformance |
|------------|---------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                              | Server        |         | M           |
| 0x0004     | Groups                                | Server        |         | O           |
| 0x0006     | On/Off                                | Server        |         | O           |
| 0x0071     | HEPA Filter Moni<br>toring            | Server        |         | O           |
| 0x0072     | Activated Carbon<br>Filter Monitoring | Server        |         | O           |

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0202     | Fan Control  | Server        |         | M           |

#### <span id="page-114-0"></span>**9.3.6. Cluster Restrictions**

#### **9.3.6.1. On/Off Cluster (Server) Clarifications**

The On/Off cluster is independent from the Fan Control Cluster's FanMode attribute, which also includes an Off setting.

If the FanMode attribute of the Fan Control cluster is set to a value other than Off when the OnOff attribute of the On/Off cluster transitions from TRUE to FALSE, it may be desirable to restore the FanMode, SpeedSetting and PercentSetting attribute values of the Fan Control cluster when the OnOff attribute of the On/Off cluster later transitions from FALSE to TRUE. If the FanMode is set to Off when the device is turned off, this information is lost, as the SpeedSetting and PercentSetting will be set to zero. Using the On/Off cluster alongside the Fan Control cluster allows the FanMode, SpeedSetting and PercentSetting to remain unchanged when the device is turned off. In this case, the On/Off cluster would be set to Off, and the SpeedCurrent and PercentCurrent set to zero, without changing FanMode, SpeedSetting and PercentSetting.

# <span id="page-114-1"></span>**9.4. Thermostat Controller Device Type**

A Thermostat Controller is a device capable of controlling a Thermostat.

### <span id="page-114-2"></span>**9.4.1. Revision History**

| Revision | Description             |
|----------|-------------------------|
| 1        | Initial Matter revision |

#### <span id="page-114-3"></span>**9.4.2. Classification**

| Device Type ID | Device Type<br>Name       | Superset Of | Class  | Scope    |
|----------------|---------------------------|-------------|--------|----------|
| 0x030A         | Thermostat Con<br>troller |             | Simple | Endpoint |

#### <span id="page-114-4"></span>**9.4.3. Conditions**

Please see the Base Device Type definition for conformance tags.

### <span id="page-114-5"></span>**9.4.4. Cluster Requirements**

| Cluster ID | Cluster Name          | Client/Server | Quality | Conformance |
|------------|-----------------------|---------------|---------|-------------|
| 0x0003     | Identify              | Client        |         | O           |
| 0x0004     | Groups                | Client        |         | O           |
| 0x0062     | Scenes Manage<br>ment | Client        |         | O           |
| 0x0201     | Thermostat            | Client        |         | M           |

# <span id="page-116-0"></span>**Chapter 10. Media Device Types**

# <span id="page-116-1"></span>**10.1. Video Player Architecture**

#### <span id="page-116-2"></span>**10.1.1. Introduction**

A Video Player endpoint (either Casting Video Player or Basic Video Player) represents a device that is able to play media to a physical output or to a display screen which is part of the device. For example, a Video Player can be a traditional TV device, a physical media playback device such as a DVD Player, a TV Set Top Box, or a content streaming device that provides input to another device like a TV or computer monitor.

Video Player features can be categorized into **basic** and **content launching**.

The **basic** features include (conceptually): On/Off, Volume Control, Playback Control, Channel Change, Input Control, Output Control, Sleep/Wake, Target Navigation and Keypad Navigation.

The **content launching** features include: discovery and launch of Content Apps, search and launch of content by content name and by URL.

A Basic Video Player is a **commissionable node** and supports these basic features which include, at a minimum, media playback controls (Media Playback cluster server) and remote controls (Keypad Input cluster server).

A Casting Video Player is a **commissioner** and supports both the Basic Video Player features and content launching features which include, at a minimum, the ability to launch content (Content Launcher cluster server).

A Content App is usually an application built by a Content Provider and exists as a separate endpoint on a Casting Video Player with a Content App Platform.

When a Casting Video Player includes a Content App Platform, it can launch Content Apps (Application Launcher cluster server) and represent these apps as separate endpoints on the Node.

A Video Remote Control is a **commissionable node** used to control basic features including, at a minimum, the ability to initiate keypad navigation (Keypad Input cluster client) and media playback (Media Playback cluster client).

A Casting Video Client is a **commissionable node** which extends the Video Remote Control features with the ability to initiate content launching (Content Launcher cluster client). A Casting Video Client is often associated with a Content App built by a specific Content Provider - for example, the Vendor Id of the Content App's Application Basic cluster will match the Vendor Id of the Casting Video Client.

![](_page_117_Picture_2.jpeg)

*Figure 7. Video Player Device Types*

### <span id="page-117-0"></span>**10.1.2. Clients of a Casting Video Player**

The clients for a Video Player device can be categorized into 2 high-level groups.

- 1. Clients controlling the Video Player endpoint, such as a remote control (e.g.: Video Remote device type)
- 2. Clients controlling specific Content App(s) such as a Phone App casting to a corresponding Content App (e.g.: Casting Video Client device type)

### <span id="page-117-1"></span>**10.1.3. Endpoint Composition for Content Apps of a Casting Video Player**

A Casting Video Player with a Content App Platform SHALL represent each Content App as its own dedicated endpoint where each is identified using the Device ID 0x0024 for "Content App".

The requirements for allocating and deallocating an endpoint address for a Content App SHALL be as described in the System Model specification (see "Dynamic Endpoint allocation").

The following diagram shows a Video Player device containing 3 separate Content Apps:

![](_page_118_Figure_2.jpeg)

*Figure 8. Endpoint Composition for Video Player Device*

### <span id="page-118-0"></span>**10.1.4. Commissioning**

A Basic Video Player SHALL be commissioned like any commissionable node.

A Casting Video Player SHALL be a Commissioner. The primary reason for this requirement is to enable the Casting Video Player to verify, using device attestation, the vendor of a Client for the purpose of controlling content on the Casting Video Player, and to ensure that only clients authorized by a Content App can control it. In this way, a Commissionee associated with a Content App on the Casting Video Player can be commissioned by the Casting Video Player and granted access to the endpoint associated with that Content App.

When a Casting Video Player commissions a Client, such as a Video Remote Control or a Casting Video Client, the Casting Video Player SHALL determine the Content App access for the given Client following the rules defined in this section. Since the Client is being commissioned by the Casting Video Player, the Client, which may be a phone app, SHALL include attestation credentials which are used by the Casting Video Player to determine its Vendor ID.

1. A Casting Video Player SHOULD allow each Content App to specify which clusters it implements, and reflect these clusters in the corresponding endpoint for the given Content App. The method for conveying this information between the Content App and the Casting Video Player is specific to the vendor of the Casting Video Player.

- 2. A Casting Video Player SHALL allow each Content App to specify values for fields in the Application Basic cluster, such as Vendor ID and Application Name. A Casting Video Player SHALL also use this information to determine access control for Clients commissioned by the Casting Video Player. The method for conveying this information between the Content App and the Casting Video Player is specific to the vendor of the Casting Video Player.
- 3. A Casting Video Player device SHALL allow each Content App to provide an Allowed Controller Vendor ID list. The Allowed Controller Vendor ID list specifies a list of Vendor IDs for Clients that SHALL be granted access to the endpoint for the given Content App. The Casting Video Player device SHALL use the Allowed Controller Vendor ID list to determine access control for Clients commissioned by the Casting Video Player. Only Clients with a Vendor ID in the Allowed Controller Vendor ID list SHALL be granted access to the given Content App endpoint. The method for conveying this information between the Content App and the Casting Video Player is specific to the vendor of the Casting Video Player. When a Client is commissioned, its attested Vendor ID is used to determine access to Content App endpoints. The Allowed Controller Vendor ID list is contained in the AllowedVendorList attribute of the Application Basic cluster.

A Casting Video Player MAY enable a commissioning flow, which avoids Setup PIN entry by the user, when the following conditions are met:

- 1. The Client's Vendor ID and a Rotating ID (used as a TempAccountIdentifier) are present in its commissionable node advertisement, or present in a User Directed Commissioning message sent by the Client to initiate commissioning with the Casting Video Player.
- 2. The Casting Video Player is able to determine an endpoint corresponding to the given Vendor ID which contains the Account Login cluster (for example, a Content App endpoint).
- 3. The Account Login cluster's GetSetupPIN command returns a SetupPIN which is then used successfully to commission the Client.

A Casting Video Player MAY enable a Content App account login flow, which avoids login name and password entry by the user, when the following conditions are met:

- 1. The Client's Vendor ID and a Rotating ID (used as a TempAccountIdentifier) are present in its commissionable node advertisement, or present in a User Directed Commissioning message sent by the Client to initiate commissioning with the Casting Video Player.
- 2. The Casting Video Player is able to determine an endpoint corresponding to the given Vendor ID which contains the Account Login cluster (for example, a Content App endpoint).
- 3. The Account Login cluster's Login command returns successfully.

In these flows, when the Account Login cluster is located on a Content App endpoint, the Account Login cluster will often be implemented by a different vendor from the Casting Video Player itself. See AccountLoginCluster for further details on the use of these commands.

Since a Client commissioned by the Casting Video Player will only have access to one or more Content App endpoints and the Speaker endpoint (when present), it will not have the ability to access the Application Launcher cluster on the Casting Video Player endpoint. If they do not already exist, the Casting Video Player device SHALL create endpoints for each Content App to which the Client has access and notify the Client of such access by adding an entry for each Content App to the Binding cluster of the Client. The Casting Video Player device SHALL automatically launch the Content App upon commands targeted to a Content App endpoint.

The following steps are performed by a Casting Video Player when granting and removing Client access to Content App endpoints:

- 1. Upon commissioning a Client and granting it access to a Content App endpoint, the Casting Video Player SHALL invoke the Login command of the AccountLogin cluster on the Content App endpoint (when implemented by the Content App) in order to notify the Content App endpoint of the Client.
  - a. If the Client is a Casting Video Client and it implements the Content App Observer server cluster, and if the Content App endpoint implements both the Binding server cluster and the Content App Observer client cluster, then the Casting Video Player SHALL create a binding on the Content App endpoint which specifies the Node and Endpoint of the Casting Video Client's Content App Observer server cluster. The Casting Video Player SHALL provide a way for the Content App to send a Content App Observer cluster ContentAppMessage command to the Casting Video Client and to receive a ContentAppMessageResponse in return.
- 2. Upon removing access to a Content App endpoint for a Client, the Casting Video Player SHALL invoke the Logout command of the AccountLogin cluster on the Content App endpoint (when implemented by the Content App) in order to notify the Content App endpoint that Client access has been removed.
  - a. If the Casting Video Player created a binding on the Content App endpoint corresponding to the Casting Video Client's Content App Observer server cluster, then the Casting Video Player SHALL remove this binding.

When the Content App endpoint generates a LoggedOut event, the Casting Video Player SHALL remove access to the Node specified to the given Content App endpoint.

**NOTE**

A Client commissioned by the Casting Video Player is able to determine if the corresponding Content App is visible to the user using the **Status** attribute on the Application Basic cluster for the Content App endpoint. This ensures that the Client cannot access foreground Content App information about any other Content App to which it does not have access. It also ensures that such a client will only need access to specific Content App endpoints and the Speaker endpoint (when present).

#### <span id="page-120-0"></span>**10.1.5. Determining Context**

A client that controls multiple aspects of the Video Player functionality (like a voice assistant) may have access to multiple endpoints on the Video Player. To determine the current context on the Video Player when the user interacts with the client (for example, when the user interacts with the device using voice), the client can look at the state in the various clusters on the Casting Video Player.

#### Specifically:

- 1. Media Input cluster (when CurrentInput does NOT have type INTERNAL, then Video Player is displaying content from a physical input)
- 2. Application Launcher cluster (CurrentApp indicates the current application endpoint which

may be the Video Player endpoint when no Content App is in the foreground).

3. Target Navigator cluster on current application endpoint (indicates which navigation target the user is in)

The Video Player SHOULD provide a way for the user to view the list of clients with access to control the screen and SHOULD provide a way for the user to revoke this access.

#### <span id="page-121-0"></span>**10.1.6. Basic Video Player Features**

#### **10.1.6.1. On/Off/Toggle**

This feature turns on/off the user-visible power state of the device, corresponding to the on/off/toggle button usually found on a remote or button on the device.

An On/Off cluster on the Video Player endpoint SHALL be used for this feature.

#### **10.1.6.2. Volume Control**

This feature controls the speaker volume of the device.

A Speaker endpoint SHALL be used for this feature when the device controls a speaker.

#### **10.1.6.3. Media Playback Control**

This feature controls media playback on the device which includes functionality such as Play, Pause, Stop, Rewind, and Fast Forward.

The Media Playback cluster SHALL be used for this functionality.

#### **10.1.6.4. Channel Change**

This feature controls channel control functionality on the device which includes functionality such as lineup discovery, change and skip channels.

The Channel cluster SHALL be used for this functionality.

#### **10.1.6.5. Media Input Control**

This feature controls the input selection on the device which includes functionality such as input discovery, selection and naming.

The Media Input cluster SHALL be used for this functionality.

#### **10.1.6.6. Audio Output Control**

This feature controls audio output selection on the device which includes functionality such as output discovery, selection and naming.

The Audio Output cluster SHALL be used for this functionality.

Note that when the current output is set to an output of type HDMI, adjustments to volume via a

Speaker endpoint on the same node MAY cause HDMI volume up/down commands to be sent to the given HDMI output.

#### **10.1.6.7. Sleep/Wake**

This feature controls low power mode on the device which includes functionality such as sleep, and declaration of protocols supported for Wakeup.

The Low Power cluster SHALL be used for putting a device into low power (sleep) mode.

The WakeOnLAN cluster SHALL be used for declaring that a device supports the WakeOnLAN protocol.

#### **10.1.6.8. Target Navigation**

This feature controls on-screen navigation to custom-named targets, for example, "Settings", "On Demand" and "Search". A list of named targets can be provided for the Video Player endpoint itself, as well as for Content App represented as endpoints.

The Target Navigator cluster SHALL be used for listing navigation targets, invoking navigation to a target, and tracking the current target.

#### **10.1.6.9. Keypad Navigation**

This feature controls on-screen navigation, commonly referred to as D-Pad navigation, and includes navigation commands such as UP, DOWN, LEFT, RIGHT, SELECT, BACK, EXIT, MENU.

The Keypad Input cluster SHALL be used for this functionality.

#### **10.1.6.10. Account Login**

This cluster provides commands that facilitate user account login on an application or a node.

The Account Login cluster SHALL be used for this functionality.

#### <span id="page-122-0"></span>**10.1.7. Content Launching Features**

Many Video Player devices (traditional TVs, Set Top Boxes, Content Streamers) have advanced features that MAY include any of the following:

- the ability to search for and playback content such as movies and TV shows
- a platform for Content Apps that can themselves be launched, and instructed to search and playback content such as movies and TV shows
- the ability to download and playback basic content referenced by URL

#### **10.1.7.1. Discover and Launch Content App from another Device**

This feature allows a client to discover the Content App identification catalogs supported by a Video Player device, and launch an Application based upon a Content App identifier within a given catalog. An example Content App identification catalog is the DIAL registry [\(http://www.dial-](http://www.dial-multiscreen.org/) [multiscreen.org/\)](http://www.dial-multiscreen.org/).

The Application Launcher cluster SHALL be used for this functionality.

#### **10.1.7.2. Launch Content from another Device**

Content search and launch is defined by the Content Launcher cluster which includes feature flags for Content Search and URL Playback which are used to indicate which of these features is supported.

The Content Launcher cluster SHALL be used for this functionality.

# <span id="page-123-0"></span>**10.2. Basic Video Player Device Type**

This defines conformance to the Basic Video Player device type.

A Video Player (either Basic or Casting) represents a device that is able to play media to a physical output or to a display screen which is part of the device.

A Basic Video Player has playback controls (play, pause, etc.) and keypad remote controls (up, down, number input), but is not able to launch content and is not a content app platform (the Casting Video Player device type is used for these functions).

For example, a Basic Video Player can be a traditional TV device a physical media playback device such as a DVD Player, or a device that provides input to another device like a TV or computer monitor.

See [Section 10.1, "Video Player Architecture"](#page-116-1) for additional Basic Video Player requirements relating to Video Player device endpoint composition, commissioning, feature representation in clusters, and UI context.

#### <span id="page-123-1"></span>**10.2.1. Revision History**

| Revision | Description                                 |
|----------|---------------------------------------------|
| 1        | Initial revision                            |
| 2        | Added Messages and Content Control clusters |

#### <span id="page-123-2"></span>**10.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0028         | Basic Video Player  |             | Simple | Endpoint |

#### <span id="page-123-3"></span>**10.2.3. Conditions**

This device type SHALL support the following conformance conditions as defined below.

| Condition      | Description                               |
|----------------|-------------------------------------------|
| PhysicalInputs | The device has physical inputs for media. |

See the Base Device Type definition for additional conformance tags.

#### <span id="page-124-0"></span>**10.2.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name     | Client/Server | Quality | Conformance    |
|------------|------------------|---------------|---------|----------------|
| 0x0006     | On/Off           | Server        |         | M              |
| 0x0097     | Messages         | Server        |         | O              |
| 0x0503     | Wake On LAN      | Server        |         | O              |
| 0x0504     | Channel          | Server        |         | O              |
| 0x0505     | Target Navigator | Server        |         | O              |
| 0x0506     | Media Playback   | Server        |         | M              |
| 0x0507     | Media Input      | Server        |         | PhysicalInputs |
| 0x0508     | Low Power        | Server        |         | O              |
| 0x0509     | Keypad Input     | Server        |         | M              |
| 0x050B     | Audio Output     | Server        |         | O              |
| 0x050F     | Content Control  | Server        |         | P, O           |

# <span id="page-124-1"></span>**10.3. Casting Video Player Device Type**

This defines conformance to the Casting Video Player device type.

A Video Player (either Basic or Casting) represents a device that is able to play media to a physical output or to a display screen which is part of the device.

A Casting Video Player has basic controls for playback (play, pause, etc.) and keypad input (up, down, number input), and is able to launch content.

For example, a Casting Video Player can be a smart TV device, a TV Set Top Box, or a content streaming device that provides input to another device like a TV or computer monitor.

See [Section 10.1, "Video Player Architecture"](#page-116-1) for additional Casting Video Player requirements relating to Video Player device endpoint composition, commissioning, feature representation in clusters, and UI context.

### <span id="page-124-2"></span>**10.3.1. Revision History**

| Revision | Description                                 |
|----------|---------------------------------------------|
| 1        | Initial revision                            |
| 2        | Added Messages and Content Control clusters |

#### <span id="page-125-0"></span>**10.3.2. Classification**

| Device Type ID | Device Type<br>Name     | Superset Of | Class  | Scope    |
|----------------|-------------------------|-------------|--------|----------|
| 0x0023         | Casting Video<br>Player |             | Simple | Endpoint |

#### <span id="page-125-1"></span>**10.3.3. Conditions**

This device type SHALL support the following conformance conditions as defined below.

| Condition          | Description                                                                                                                                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ContentAppPlatform | The device includes a Content App Platform. A<br>Content App is usually an application built by a<br>Content Provider. A Casting Video Player with a<br>Content App Platform is able to launch Content<br>Apps and represent these apps as separate end<br>points. |
| PhysicalInputs     | The device has physical inputs for media.                                                                                                                                                                                                                          |

See the Base Device Type definition for additional conformance tags.

### <span id="page-125-2"></span>**10.3.4. Cluster Requirements**

| Cluster ID | Cluster Name     | Client/Server | Quality | Conformance    |
|------------|------------------|---------------|---------|----------------|
| 0x0006     | On/Off           | Server        |         | M              |
| 0x0097     | Messages         | Server        |         | O              |
| 0x0503     | Wake On LAN      | Server        |         | O              |
| 0x0504     | Channel          | Server        |         | O              |
| 0x0505     | Target Navigator | Server        |         | O              |
| 0x0506     | Media Playback   | Server        |         | M              |
| 0x0507     | Media Input      | Server        |         | PhysicalInputs |
| 0x0508     | Low Power        | Server        |         | O              |
| 0x0509     | Keypad Input     | Server        |         | M              |

| Cluster ID | Cluster Name            | Client/Server | Quality | Conformance            |
|------------|-------------------------|---------------|---------|------------------------|
| 0x050A     | Content Launcher        | Server        |         | M                      |
| 0x050B     | Audio Output            | Server        |         | O                      |
| 0x050C     | Application<br>Launcher | Server        |         | ContentAppPlat<br>form |
| 0x050E     | Account Login           | Server        |         | O                      |
| 0x050F     | Content Control         | Server        |         | P, O                   |

#### <span id="page-126-0"></span>**10.3.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank entry means no change.

| Cluster ID | Cluster<br>Name         | Element | Name                    | Constraint | Access | Confor<br>mance |
|------------|-------------------------|---------|-------------------------|------------|--------|-----------------|
| 0x050C     | Application<br>Launcher | Feature | Application<br>Platform |            |        | M               |

# <span id="page-126-1"></span>**10.4. Speaker Device Type**

This defines conformance to the Speaker device type.

This feature controls the speaker volume of the device.

To control unmute/mute, the On/Off cluster SHALL be used. A value of TRUE for the OnOff attribute SHALL represent the volume on (not muted) state, while a value of FALSE SHALL represent the volume off (muted) state. For volume level control, the Level cluster SHALL be used.

A dedicated endpoint is needed because the On/Off cluster can also be used for other purposes, such as for power control.

The decision to use Level and On/Off clusters for volume (rather than defining a new audio control cluster) was made in order to treat volume in a fashion consistent with lighting which also uses these clusters and has matching functional requirements.

### <span id="page-126-2"></span>**10.4.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-126-3"></span>**10.4.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0022         | Speaker             |             | Simple | Endpoint |

#### <span id="page-127-0"></span>**10.4.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-127-1"></span>**10.4.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name  | Client/Server | Quality | Conformance |
|------------|---------------|---------------|---------|-------------|
| 0x0006     | On/Off        | Server        |         | M           |
| 0x0008     | Level Control | Server        |         | M           |

# <span id="page-127-2"></span>**10.5. Content App Device Type**

This defines conformance to the Content App device type.

A Content App is usually an application built by a Content Provider. A Casting Video Player with a Content App Platform is able to launch Content Apps and represent these apps as separate endpoints.

### <span id="page-127-3"></span>**10.5.1. Revision History**

| Revision | Description                        |  |
|----------|------------------------------------|--|
| 1        | Initial revision                   |  |
| 2        | Added Content App Observer cluster |  |

#### <span id="page-127-4"></span>**10.5.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0024         | Content App         |             | Simple | Endpoint |

#### <span id="page-127-5"></span>**10.5.3. Conditions**

| Condition      | Description                                   |  |  |
|----------------|-----------------------------------------------|--|--|
| ObserverClient | The node is a client for ContentAppObservers. |  |  |

See the Base Device Type definition for additional conformance tags.

#### <span id="page-128-0"></span>**10.5.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name            | Client/Server | Quality | Conformance    |
|------------|-------------------------|---------------|---------|----------------|
| 0x0504     | Channel                 | Server        |         | O              |
| 0x0505     | Target Navigator        | Server        |         | O              |
| 0x0506     | Media Playback          | Server        |         | O              |
| 0x0509     | Keypad Input            | Server        |         | M              |
| 0x050A     | Content Launcher        | Server        |         | O              |
| 0x050C     | Application<br>Launcher | Server        |         | M              |
| 0x050D     | Application Basic       | Server        |         | M              |
| 0x050E     | Account Login           | Server        |         | O              |
| 0x0510     | Content App<br>Observer | Client        |         | ObserverClient |

### <span id="page-128-1"></span>**10.5.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank entry means no change.

| Cluster ID | Cluster<br>Name         | Element | Name                    | Constraint | Access | Confor<br>mance |
|------------|-------------------------|---------|-------------------------|------------|--------|-----------------|
| 0x050C     | Application<br>Launcher | Feature | Application<br>Platform |            |        | X               |

### <span id="page-128-2"></span>**10.5.6. Endpoint Composition**

Endpoints with this device type SHALL support Dynamic Endpoint Allocation as specified in the System Model specification.

## <span id="page-128-3"></span>**10.5.7. Disambiguation**

When there is more than one sibling endpoint with this device type in a PartsList, disambiguation information SHALL be provided by having a unique value in the ApplicationName attribute of the Application Basic cluster on each of these endpoints.

# <span id="page-128-4"></span>**10.6. Casting Video Client Device Type**

This defines conformance to the Casting Video Client device type.

A Casting Video Client is a client that can launch content on a Casting Video Player, for example, a

Smart Speaker or a Content Provider phone app.

#### <span id="page-129-0"></span>**10.6.1. Revision History**

| Revision | Description                                                          |
|----------|----------------------------------------------------------------------|
| 1        | Initial revision                                                     |
| 2        | Added Content App Observer, Messages and<br>Content Control Clusters |

#### <span id="page-129-1"></span>**10.6.2. Classification**

| Device Type ID | Device Type<br>Name     | Superset Of | Class  | Scope    |
|----------------|-------------------------|-------------|--------|----------|
| 0x0029         | Casting Video<br>Client |             | Simple | Endpoint |

#### <span id="page-129-2"></span>**10.6.3. Conditions**

See the Base Device Type definition for additional conformance tags.

#### <span id="page-129-3"></span>**10.6.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

See [Section 1.1.7, "Cluster Requirements"](#page-26-1) for additional clusters including the Binding cluster.

| Cluster ID | Cluster Name     | Client/Server | Quality | Conformance |
|------------|------------------|---------------|---------|-------------|
| 0x0006     | On/Off           | Client        |         | M           |
| 0x0008     | Level Control    | Client        |         | O           |
| 0x0097     | Messages         | Client        |         | O           |
| 0x0503     | Wake On LAN      | Client        |         | O           |
| 0x0504     | Channel          | Client        |         | O           |
| 0x0505     | Target Navigator | Client        |         | O           |
| 0x0506     | Media Playback   | Client        |         | O           |
| 0x0507     | Media Input      | Client        |         | O           |
| 0x0508     | Low Power        | Client        |         | O           |
| 0x0509     | Keypad Input     | Client        |         | M           |
| 0x050A     | Content Launcher | Client        |         | M           |
| 0x050B     | Audio Output     | Client        |         | O           |

| Cluster ID | Cluster Name            | Client/Server | Quality | Conformance |
|------------|-------------------------|---------------|---------|-------------|
| 0x050C     | Application<br>Launcher | Client        |         | O           |
| 0x050D     | Application Basic       | Client        |         | M           |
| 0x050E     | Account Login           | Client        |         | O           |
| 0x050F     | Content Control         | Client        |         | P, O        |
| 0x0510     | Content App<br>Observer | Server        |         | O           |

# <span id="page-130-0"></span>**10.7. Video Remote Control Device Type**

This defines conformance to the Video Remote Control device type.

A Video Remote Control is a client that can control a Video Player, for example, a traditional universal remote control.

#### <span id="page-130-1"></span>**10.7.1. Revision History**

| Revision | Description                   |
|----------|-------------------------------|
| 1        | Initial revision              |
| 2        | Added Content Control cluster |

#### <span id="page-130-2"></span>**10.7.2. Classification**

| Device Type ID | Device Type<br>Name      | Superset Of | Class  | Scope    |
|----------------|--------------------------|-------------|--------|----------|
| 0x002A         | Video Remote Con<br>trol |             | Simple | Endpoint |

#### <span id="page-130-3"></span>**10.7.3. Conditions**

See the Base Device Type definition for additional conformance tags.

#### <span id="page-130-4"></span>**10.7.4. Cluster Requirements**

| Cluster ID | Cluster Name  | Client/Server | Quality | Conformance |
|------------|---------------|---------------|---------|-------------|
| 0x0006     | On/Off        | Client        |         | M           |
| 0x0008     | Level Control | Client        |         | O           |
| 0x0503     | Wake On LAN   | Client        |         | O           |

| Cluster ID | Cluster Name            | Client/Server | Quality | Conformance |
|------------|-------------------------|---------------|---------|-------------|
| 0x0504     | Channel                 | Client        |         | O           |
| 0x0505     | Target Navigator        | Client        |         | O           |
| 0x0506     | Media Playback          | Client        |         | M           |
| 0x0507     | Media Input             | Client        |         | O           |
| 0x0508     | Low Power               | Client        |         | O           |
| 0x0509     | Keypad Input            | Client        |         | M           |
| 0x050A     | Content Launcher        | Client        |         | O           |
| 0x050B     | Audio Output            | Client        |         | O           |
| 0x050C     | Application<br>Launcher | Client        |         | O           |
| 0x050E     | Account Login           | Client        |         | O           |
| 0x050F     | Content Control         | Client        |         | P, O        |

# <span id="page-132-0"></span>**Chapter 11. Generic Device Types**

# <span id="page-132-1"></span>**11.1. Mode Select Device Type**

This defines conformance to the Mode Select device type.

#### <span id="page-132-2"></span>**11.1.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

### <span id="page-132-3"></span>**11.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0027         | Mode Select         |             | Simple | Endpoint |

### <span id="page-132-4"></span>**11.1.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-132-5"></span>**11.1.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0050     | Mode Select  | Server        |         | M           |

# <span id="page-132-6"></span>**11.2. Aggregator Device Type**

This device type aggregates endpoints as a collection. Clusters on the endpoint indicating this device type provide functionality for the collection of descendant endpoints present in the PartsList of the endpoint's descriptor, for example the Actions cluster.

The purpose of this device type is to aggregate functionality for a collection of endpoints. The definition of the collection or functionality is not defined here.

When using this device type as a collection of bridged nodes, please see the "Bridge" section in the System Model specification.

### <span id="page-132-7"></span>**11.2.1. Revision History**

| Revision | Description                                                                 |  |
|----------|-----------------------------------------------------------------------------|--|
| 1        | Initial revision                                                            |  |
| 2        | Added Commissioner Control Cluster and Fabric<br>Synchronization Condition. |  |

#### <span id="page-133-0"></span>**11.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x000E         | Aggregator          |             | Simple | Endpoint |

#### <span id="page-133-1"></span>**11.2.3. Conditions**

This device type MAY support the following conformance conditions as defined below.

| Condition             | Description            |  |
|-----------------------|------------------------|--|
| FabricSynchronization | See description below. |  |

See the Base Device Type definition for additional conformance tags.

#### **11.2.3.1. FabricSynchronization Condition**

The FabricSynchronization condition applies when there is a Commissioner Control Cluster on this endpoint with a SupportedDeviceCategories attribute with the FabricSynchronization bit set.

### <span id="page-133-2"></span>**11.2.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name            | Client/Server | Quality | Conformance               |
|------------|-------------------------|---------------|---------|---------------------------|
| 0x0025     | Actions                 | Server        |         | O                         |
| 0x0003     | Identify                | Server        |         | O                         |
| 0x0751     | Commissioner<br>Control | Server        |         | FabricSynchro<br>nization |

The Identify cluster SHOULD be used in case this device type is used to represent a Bridge which has a mechanism to identify itself to the user (e.g. blinking LED on the bridge itself).

For the Identify-functionality of the individual bridged devices, see the Identify cluster on the endpoint for a bridged device.

# <span id="page-133-3"></span>**11.2.5. Endpoint Composition**

An Aggregator endpoint's Descriptor cluster PartsList attribute SHALL list the collection of all end-

points aggregated by the Aggregator device type, i.e. the full-family pattern defined in the System Model specification.

#### **11.2.5.1. Multiple aggregators**

When a Node has multiple instances of the Aggregator device type, the composition SHALL comply with one of the following two patterns for any given pair (A,B) of endpoints with the Aggregator device type:

- **No overlap**: The endpoints in the PartsList attribute of Aggregator A do not appear in the PartsList attribute of Aggregator B, and vice versa.
  - Example: A Node which bridges to two non-Matter independent technologies (e.g. Zigbee and Z-Wave), see the aggregators on endpoints 11 and 31 in the figure below - their lists of endpoints (12-14, 21-23 versus 32-33) do not overlap.
- **Strict subset**: The endpoint where aggregator B is exposed and all endpoints in its PartsList attribute (the subset) are included in the PartsList attribute of Aggregator A (the superset).
  - This maintains the rule that there SHALL be a single path from the Root Node to each endpoint (see [System Model\)](#page-23-5).
  - Example: A Node which implements a bridge to Zigbee, and one of those Zigbee devices is connected to a string of DALI lights, which can be addressed individually and thus this Zigbee/DALI device functions as a bridge from Zigbee to DALI; in the figure below one can see that the endpoints for the Zigbee/DALI bridge listed in the PartsList of the aggregator on endpoint 14 (21-23) form a strict subset of the endpoints for the Zigbee bridge in the PartsList of the aggregator on endpoint 11 (12-14, 21-23), and the endpoint 14 of the "subset" aggregator is included in the PartsList of the "superset" aggregator on endpoint 11.

![](_page_135_Figure_2.jpeg)

*Figure 9. examples of multiple aggregators*

### <span id="page-135-0"></span>**11.2.6. Disambiguation**

If the Duplicate condition applies to child endpoints of an Aggregator endpoint that represent multiple independent bridged devices, the endpoints SHOULD make available metadata to allow a client to disambiguate distinct bridged devices with an overlap in application device types.

Typically this is done using the NodeLabel attribute of the Bridged Device Basic Information cluster

- thus reusing the naming information which the bridge already has to allow disambiguation to the user when using a direct user interface to the bridge.

Example: the Aggregator in this figure (copied from the "Bridge for non-Matter devices" section in the Core Specification) exposes several Color Temperature Lights (endpoints 13 and 22) which are disambiguated with their NodeLabel. Note that the compound device at endpoints 24, 25 and 26 also uses a TagList (for information rather than disambiguation) since, for this case, the bridge knows the lighting direction of both elements of the compound device.

![](_page_136_Figure_4.jpeg)

*Figure 10. use of NodeLabel and TagList for disambiguation*

# <span id="page-138-0"></span>**Chapter 12. Robotic Device Types**

# <span id="page-138-1"></span>**12.1. Robotic Vacuum Cleaner Device Type**

This defines conformance for the Robotic Vacuum Cleaner device type.

#### <span id="page-138-2"></span>**12.1.1. Revision History**

| Revision | Description                                                                                                                                                                  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Initial revision                                                                                                                                                             |
| 2        | Add cluster usage constraints and informative<br>data. Remove the element requirements section,<br>after moving all constraints to the respective<br>cluster specifications. |
| 3        | Add support for the Service Area cluster                                                                                                                                     |
| 4        | Mandate OperationCompletion Event                                                                                                                                            |

#### <span id="page-138-3"></span>**12.1.2. Classification**

| Device Type ID | Device Type<br>Name       | Superset Of | Class  | Scope    |
|----------------|---------------------------|-------------|--------|----------|
| 0x0074         | Robotic Vacuum<br>Cleaner |             | Simple | Endpoint |

#### <span id="page-138-4"></span>**12.1.3. Conditions**

See the Base Device Type definition for conformance tags.

## <span id="page-138-5"></span>**12.1.4. Cluster Requirements**

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0003     | Identify                 | Server        |         | M           |
| 0x0054     | RVC Run Mode             | Server        |         | M           |
| 0x0055     | RVC Clean Mode           | Server        |         | O           |
| 0x0061     | RVC Operational<br>State | Server        |         | M           |
| 0x0150     | Service Area             | Server        |         | O           |

#### <span id="page-139-0"></span>**12.1.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name           | Element | Name                        | Constraint | Access | Confor<br>mance |
|------------|---------------------------|---------|-----------------------------|------------|--------|-----------------|
| 0x0061     | RVC Opera<br>tional State | Event   | Opera<br>tionComple<br>tion |            |        | M               |

#### <span id="page-139-1"></span>**12.1.6. Cluster Usage**

This section describes how to control and monitor the operation of a Robotic Vacuum Cleaner device. This information is meant to clarify how the data dependencies within the device type's cluster composition are to be used.

Note that the device operations may also be the result of, or affected by, out-of-band actions such as robot physical button presses, internally scheduled events, vendor application requests, commands sent from other fabrics, internal device timeouts, etc. For example, a user may pause the robot during cleaning by using a Matter client and then resume cleaning by using a physical button of the device, or a robot may stop cleaning after an internal timeout occurs, and so forth.

The RVC Operational State cluster's OperationalState attribute SHALL be updated according to the state of the device, and therefore it SHOULD be used for monitoring purposes. Note that while the robot is in a cleaning cycle it may automatically seek the charger, recharge, and then resume cleaning.

The sections below describe various operational flows with preconditions and actions. The behavior in case the preconditions are not met is described in the corresponding cluster descriptions.

#### **12.1.6.1. Starting Cleaning**

#### **12.1.6.1.1. Preconditions**

If the DirectModeChange feature is not present, cleaning can only be started when the RVC Run Mode cluster's CurrentMode attribute is set to a mode that has the Idle mode tag associated with it, and the RVC Operational State cluster's OperationalState attribute is set to the Stopped, Paused, Docked or Charging state.

Note that if the RVC Clean Mode cluster is implemented, it determines the type of cleaning.

#### **12.1.6.1.2. Actions**

To attempt starting a cleaning operation, the RVC Run Mode cluster can be sent a ChangeToMode command with the NewMode field set to a mode that has the Cleaning mode tag associated with it.

#### **12.1.6.2. Pausing Cleaning**

#### **12.1.6.2.1. Preconditions**

Cleaning can only be paused when the RVC Operational State cluster's OperationalState attribute is set to a Pause-compatible state. See the Pause Compatibility table and the RVC Pause Compatibility Table.

Note that even if the Pause command is not implemented, the RVC Operational State cluster's OperationalState attribute MAY report that the device is in the Paused state due to an out-of-band action, such as the user pressing a physical button on the device.

#### **12.1.6.2.2. Actions**

To attempt pausing a cleaning operation, the RVC Operational State cluster can be sent a Pause command.

#### **12.1.6.3. Resuming Cleaning**

#### **12.1.6.3.1. Preconditions**

Cleaning can only be resumed if the RVC Operational State cluster's OperationalState attribute is set to a Resume-compatible state (see Resume Compatibility table and the RVC Resume Compatibility table), and the RVC Run Mode cluster's CurrentMode is set to a mode with the Cleaning mode tag.

Note that even if the Resume command is not implemented, the RVC Operational State cluster's OperationalState attribute MAY indicate that the device transitioned from the Paused state to the Running state due to an out-of-band action, such as the user pressing a physical button on the device.

#### **12.1.6.3.2. Actions**

To attempt resuming a cleaning operation, the RVC Operational State cluster can be sent a Resume command.

#### **12.1.6.4. Stopping Cleaning**

#### **12.1.6.4.1. Preconditions**

Stopping cleaning can only happen if the RVC Run Mode cluster's CurrentMode attribute is set to a mode that has the Cleaning mode tag associated with it.

#### **12.1.6.4.2. Actions**

To attempt stopping a cleaning operation, the RVC Run Mode cluster can be sent a ChangeToMode command with the NewMode field set to a mode that has the Idle mode tag associated with it.

#### **12.1.6.4.3. Side Effects**

Note that the device MAY seek the charger after successfully switching the RVC Run Mode cluster to an Idle mode. The OperationalState attribute indicates whether the device is seeking the charger, stopped, charging, docked etc.

#### **12.1.6.5. Other Device Operations**

The RVC Run Mode cluster's SupportedModes attribute list MAY include modes that have neither the Idle nor the Cleaning mode tags, for example the Mapping mode tag.

Starting, pausing, resuming and stopping these other operations have similar preconditions, actions and side effects as those described above for the cleaning operations.

#### **12.1.6.6. Device Error Handling**

When in an error condition, as indicated by the RVC Operational State cluster's OperationalState attribute, out-of-band action will be required to clear that condition.

If an error occurs while the device operates, such as while cleaning or while mapping, the device MAY pause and set the RVC Operational State cluster's OperationalState attribute to Error. If the operation can be resumed after the error is cleared, the device SHALL set the RVC Operational State cluster's OperationalState attribute to Paused and MAY be resumed either via a Resume command, if implemented, or by out-of-band actions, such as by pressing the robot's physical buttons.

Note that certain errors may not pause or disable the device. For example, a dual-function device, that can both vacuum and mop, may report a WaterTankEmpty error but may still be able to be used if it has a vacuum only cleaning mode. Certain modes of the RVC Run Mode and the RVC Cleaning Mode clusters MAY become unavailable and the ChangeToModeResponse commands' Status-Code SHALL be set to InvalidInMode, when attempting to switch to those modes.

# <span id="page-142-0"></span>**Chapter 13. Appliances Device Types**

# <span id="page-142-1"></span>**13.1. Laundry Washer Device Type**

A Laundry Washer represents a device that is capable of laundering consumer items. Any laundry washer product may utilize this device type.

A Laundry Washer SHALL be composed of at least one endpoint with the Laundry Washer device type.

#### <span id="page-142-2"></span>**13.1.1. Revision History**

| Revision | Description                       |
|----------|-----------------------------------|
| 1        | Initial revision                  |
| 2        | Mandate OperationCompletion Event |

#### <span id="page-142-3"></span>**13.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0073         | Laundry Washer      |             | Simple | Endpoint |

#### <span id="page-142-4"></span>**13.1.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-142-5"></span>**13.1.4. Cluster Requirements**

| Cluster ID | Cluster Name               | Client/Server | Quality | Conformance |
|------------|----------------------------|---------------|---------|-------------|
| 0x0003     | Identify                   | Server        |         | O           |
| 0x0006     | On/Off                     | Server        |         | O           |
| 0x0051     | Laundry Washer<br>Mode     | Server        |         | O           |
| 0x0053     | Laundry Washer<br>Controls | Server        |         | O           |
| 0x0056     | Temperature Con<br>trol    | Server        |         | O           |
| 0x0060     | Operational State          | Server        |         | M           |

#### <span id="page-143-0"></span>**13.1.5. Cluster Restrictions**

#### **13.1.5.1. Temperature Control Cluster (Server) Clarifications**

Given that different markets have different customary methods of providing temperature settings (e.g. North America often prefers levels, whereas many other markets provide temperatures in °C), it is RECOMMENDED that when the Temperature Control cluster is present, the TemperatureLevel or TemperatureNumber feature of that cluster is chosen to follow the most widely applied convention for the market where the product is sold.

#### **13.1.5.2. On/Off Cluster (Server) Clarifications**

As indicated in the Element Requirements section below, the DF (Dead Front) feature is required for the On/Off cluster in this device type. See the "DeadFrontBehavior feature" section in the On/Off cluster description for detailed requirements. The "dead front" state is linked to the OnOff attribute in the On/Off cluster having the value False. Thus, the Off command of the On/Off cluster SHALL move the device into the "dead front" state, the On command of the On/Off cluster SHALL bring the device out of the "dead front" state, and the device SHALL adhere with the associated requirements on subscription handling and event reporting.

#### **13.1.5.3. Best Effort Attribute Values in "Dead Front" State**

When in "dead front", should the operational values of the cluster attributes not be available or accessible, the following are the RECOMMENDED best effort values for per cluster attributes when responding to a new subscription request or a read request. Attributes not listed have no change in their defined or expected values.

| Cluster Name            | Attribute        | Fallback |
|-------------------------|------------------|----------|
| Laundry Washer Mode     | CurrentMode      | MS       |
| Laundry Washer Controls | SpinSpeedCurrent | null     |
|                         | NumberOfRinses   | null     |
|                         | SpinSpeeds       | null     |
|                         | MaxRinses        | null     |
| Temperature Control     | All attributes   | MS       |
| Identify                | All attributes   | MS       |
| Operational State       | PhaseList        | null     |
|                         | CurrentPhase     | null     |
|                         | CountdownTime    | null     |
|                         | OperationalState | Stopped  |
|                         | OperationalError | No Error |

#### <span id="page-143-1"></span>**13.1.6. Element Requirements**

The table below lists qualities and conformance that override the cluster specification require-

ments. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name           | Element   | Name                        | Constraint | Access | Confor<br>mance |
|------------|---------------------------|-----------|-----------------------------|------------|--------|-----------------|
| 0x0006     | On/Off                    | Feature   | DeadFront<br>Behavior       |            |        | M               |
| 0x0051     | Laundry<br>Washer<br>Mode | Feature   | OnOff                       |            |        | X               |
| 0x0051     | Laundry<br>Washer<br>Mode | Attribute | StartUpMode                 |            |        | X               |
| 0x0060     | Operational<br>State      | Event     | Opera<br>tionComple<br>tion |            |        | M               |

# <span id="page-144-0"></span>**13.2. Refrigerator Device Type**

A refrigerator represents a device that contains one or more cabinets that are capable of chilling or freezing food. Examples of consumer products that MAY make use of this device type include refrigerators, freezers, and wine coolers.

### <span id="page-144-1"></span>**13.2.1. Refrigerator Architecture**

A Refrigerator is always defined via endpoint composition. See [Section 13.2.6, "Device Type](#page-146-0) [Requirements"](#page-146-0) for more details.

A Refrigerator MAY include a semantic tag in the TagList attribute of the Descriptor cluster to describe the primary function of the device, e.g., "Refrigerator" or "Freezer".

An example of a Refrigerator with multiple cabinets is illustrated below.

*Figure 11. Example of a Refrigerator*

#### <span id="page-145-0"></span>**13.2.2. Revision History**

| Revision | Description              |
|----------|--------------------------|
| 1        | Initial revision         |
| 2        | Added Cooler requirement |

#### <span id="page-145-1"></span>**13.2.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0070         | Refrigerator        |             | Simple | Endpoint |

#### <span id="page-145-2"></span>**13.2.4. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-145-3"></span>**13.2.5. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location   | Device Type<br>ID | Device Type<br>Name                   | Condition | Conformance | Constraint |
|------------|-------------------|---------------------------------------|-----------|-------------|------------|
| Descendant | 0x0071            | Temperature<br>Controlled Cab<br>inet | Cooler    | M           | min 1      |

#### <span id="page-146-0"></span>**13.2.6. Device Type Requirements**

A Refrigerator SHALL be composed of at least one endpoint with the Temperature Controlled Cabinet device type as defined by the conformance below. There MAY be more endpoints with other device types existing in the Refrigerator.

If the Refrigerator contains more than one instance of a Temperature Controlled Cabinet, those instances SHALL include a semantic tag in the TagList attribute of the Descriptor cluster to disambiguate the cabinet, e.g., "freezer" or "refrigerator". Such a semantic tag SHALL be from either the defined Common or Refrigerator namespaces.

| Device Type ID | Device Type Name                   | Constraint | Conformance |
|----------------|------------------------------------|------------|-------------|
| 0x0071         | Temperature Con<br>trolled Cabinet | min 1      | M           |

#### <span id="page-146-1"></span>**13.2.7. Cluster Requirements**

Each endpoint supporting the refrigerator device type MAY include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                                                   | Client/Server | Quality | Conformance |
|------------|----------------------------------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                                                       | Server        |         | O           |
| 0x0052     | Refrigerator And<br>Temperature Con<br>trolled Cabinet<br>Mode | Server        |         | O           |
| 0x0057     | Refrigerator<br>Alarm                                          | Server        |         | O           |

## <span id="page-146-2"></span>**13.2.8. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                                                     | Element | Name  | Constraint | Access | Confor<br>mance |
|------------|---------------------------------------------------------------------|---------|-------|------------|--------|-----------------|
| 0x0052     | Refrigerator<br>And Temper<br>ature Con<br>trolled Cabi<br>net Mode | Feature | OnOff |            |        | X               |

| Cluster ID | Cluster<br>Name                                                     | Element   | Name        | Constraint | Access | Confor<br>mance |
|------------|---------------------------------------------------------------------|-----------|-------------|------------|--------|-----------------|
| 0x0052     | Refrigerator<br>And Temper<br>ature Con<br>trolled Cabi<br>net Mode | Attribute | StartUpMode |            |        | X               |

# <span id="page-147-0"></span>**13.3. Room Air Conditioner Device Type**

This defines conformance to the Room Air Conditioner device type.

A Room Air Conditioner is a device with the primary function of controlling the air temperature in a single room.

#### <span id="page-147-1"></span>**13.3.1. Room Air Conditioner Architecture**

A Room Air Conditioner is a device which at a minimum is capable of being turned on and off and of controlling the temperature in the living space.

A Room Air Conditioner MAY also support additional capabilities via endpoint composition. See [Sec](#page-148-3)[tion 13.3.5, "Device Type Requirements"](#page-148-3) for typical device types.

The following diagram shows an example Room Air Conditioner consisting of a parent endpoint that is the Room Air Conditioner device type and several child endpoints providing additional capabilities. Note that two of the child endpoints are of the same device type, Temperature Sensor, which are being disambiguated via the requirements of endpoint composition defined in the system model.

![](_page_147_Figure_11.jpeg)

*Figure 12. Example of a Room Air Conditioner*

#### <span id="page-148-0"></span>**13.3.2. Revision History**

| Revision | Description                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Initial revision                                                                                                                     |
| 2        | Thermostat User Interface Configuration cluster<br>added; Updated the Scenes cluster to Scenes<br>Management with Cluster ID: 0x0062 |
| 3        | Added filter monitoring clusters                                                                                                     |
| 4        |                                                                                                                                      |

### <span id="page-148-1"></span>**13.3.3. Classification**

| Device Type ID | Device Type<br>Name      | Superset Of | Class  | Scope    |
|----------------|--------------------------|-------------|--------|----------|
| 0x0072         | Room Air Condi<br>tioner |             | Simple | Endpoint |

#### <span id="page-148-2"></span>**13.3.4. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-148-3"></span>**13.3.5. Device Type Requirements**

A Room Air Conditioner MAY have zero or more of each device type listed in this table subject to the conformance column of the table. All devices used in compositions SHALL adhere to the disambiguation requirements of the System Model. Additional device types not listed in this table MAY also be included in device compositions.

| Device Type ID | Device Type Name   | Constraint | Conformance |
|----------------|--------------------|------------|-------------|
| 0x0302         | Temperature Sensor |            | O           |
| 0x0307         | Humidity Sensor    |            | O           |

### <span id="page-148-4"></span>**13.3.6. Cluster Requirements**

| Cluster ID | Cluster Name           | Client/Server | Conformance |
|------------|------------------------|---------------|-------------|
| 0x0003     | Identify               | Server        | M           |
| 0x0004     | Groups                 | Server        | O           |
| 0x0006     | On/Off                 | Server        | M           |
| 0x0062     | Scenes Management      | Server        | O           |
| 0x0071     | HEPA Filter Monitoring | Server        | O           |

| Cluster ID | Cluster Name                                | Client/Server | Conformance |
|------------|---------------------------------------------|---------------|-------------|
| 0x0072     | Activated Carbon Filter<br>Monitoring       | Server        | O           |
| 0x0201     | Thermostat                                  | Server        | M           |
| 0x0202     | Fan Control                                 | Server        | O           |
| 0x0204     | Thermostat User Inter<br>face Configuration | Server        | O           |
| 0x0402     | Temperature Measure<br>ment                 | Server        | O           |
| 0x0405     | Relative Humidity Mea<br>surement           | Server        | O           |

#### <span id="page-149-0"></span>**13.3.7. Cluster Restrictions**

#### **13.3.7.1. On/Off Cluster (Server) Clarifications**

As indicated in the Element Requirements section below, the DF (Dead Front) feature is required for the On/Off cluster in this device type. See the "DeadFrontBehavior feature" section in the On/Off cluster description for detailed requirements. The "dead front" state is linked to the OnOff attribute in the On/Off cluster having the value False. Thus, the Off command of the On/Off cluster SHALL move the device into the "dead front" state, the On command of the On/Off cluster SHALL bring the device out of the "dead front" state, and the device SHALL adhere with the associated requirements on subscription handling and event reporting.

#### **13.3.7.2. Best Effort Attribute Values in "Dead Front" State**

When in "dead front", should the operational values of the cluster attributes not be available or accessible, the following are the RECOMMENDED best effort values for per cluster attributes when responding to a new subscription request or a read request. Attributes not listed have no change in their defined or expected values.

| Cluster Name                      | Attribute        | Fallback |
|-----------------------------------|------------------|----------|
| Thermostat                        | LocalTemperature | null     |
| Temperature Measurement           | MeasuredValue    | null     |
| Relative Humidity Measure<br>ment | MeasuredValue    | null     |
| Fan Control                       | SpeedSetting     | null     |
|                                   | PercentSetting   | null     |

### <span id="page-149-1"></span>**13.3.8. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                                       | Element   | Name                  | Constraint | Access | Confor<br>mance | Fallback |
|------------|-------------------------------------------------------|-----------|-----------------------|------------|--------|-----------------|----------|
| 0x0006     | On/Off                                                | Feature   | DeadFront<br>Behavior |            |        | M               |          |
| 0x0204     | Thermo<br>stat User<br>Interface<br>Configura<br>tion | Attribute | Keypad<br>Lockout     |            |        | O               |          |

# <span id="page-150-0"></span>**13.4. Temperature Controlled Cabinet Device Type**

A Temperature Controlled Cabinet only exists composed as part of another device type. It represents a single cabinet that is capable of having its temperature controlled. Such a cabinet may be chilling or freezing food, for example as part of a refrigerator, freezer, wine chiller, or other similar device. Equally, such a cabinet may be warming or heating food, for example as part of an oven, range, or similar device.

#### <span id="page-150-1"></span>**13.4.1. Revision History**

| Revision | Description                                                                    |
|----------|--------------------------------------------------------------------------------|
| 1        | Initial revision                                                               |
| 2        | Extension to heating cabinets                                                  |
| 3        | Added exclusivity for conditions                                               |
| 4        | Mandate OperationCompletion Event for Oven<br>Cavity Operational State cluster |
| 5        | Made TemperatureNumber (TN) the only valid<br>temperature control mode         |

#### <span id="page-150-2"></span>**13.4.2. Classification**

| Device Type ID | Device Type<br>Name                | Superset Of | Class  | Scope    |
|----------------|------------------------------------|-------------|--------|----------|
| 0x0071         | Temperature Con<br>trolled Cabinet |             | Simple | Endpoint |

#### <span id="page-150-3"></span>**13.4.3. Conditions**

This device type SHALL support the following conformance conditions as defined below.

<span id="page-150-5"></span><span id="page-150-4"></span>

| Condition | Description                           |
|-----------|---------------------------------------|
| Cooler    | The device has cooling functionality. |
| Heater    | The device has heating functionality. |

Endpoints SHALL support at most one condition.

See the Base Device Type definition for conformance tags.

#### <span id="page-151-0"></span>**13.4.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                                                   | Client/Server | Quality | Conformance |
|------------|----------------------------------------------------------------|---------------|---------|-------------|
| 0x0056     | Temperature Con<br>trol                                        | Server        |         | M           |
| 0x0402     | Temperature Mea<br>surement                                    | Server        |         | O           |
| 0x0052     | Refrigerator And<br>Temperature Con<br>trolled Cabinet<br>Mode | Server        |         | [Cooler]    |
| 0x0049     | Oven Mode                                                      | Server        |         | [Heater]    |
| 0x0048     | Oven Cavity Oper<br>ational State                              | Server        |         | [Heater]    |

### <span id="page-151-1"></span>**13.4.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                                                     | Element   | Name        | Constraint | Access | Confor<br>mance |
|------------|---------------------------------------------------------------------|-----------|-------------|------------|--------|-----------------|
| 0x0052     | Refrigerator<br>And Temper<br>ature Con<br>trolled Cabi<br>net Mode | Attribute | StartUpMode |            |        | X               |
| 0x0052     | Refrigerator<br>And Temper<br>ature Con<br>trolled Cabi<br>net Mode | Feature   | OnOff       |            |        | X               |
| 0x0049     | Oven Mode                                                           | Attribute | StartUpMode |            |        | X               |
| 0x0049     | Oven Mode                                                           | Feature   | OnOff       |            |        | X               |

| Cluster ID | Cluster<br>Name                     | Element | Name                        | Constraint | Access | Confor<br>mance |
|------------|-------------------------------------|---------|-----------------------------|------------|--------|-----------------|
| 0x0048     | Oven Cavity<br>Operational<br>State | Command | Pause                       |            |        | X               |
| 0x0048     | Oven Cavity<br>Operational<br>State | Command | Resume                      |            |        | X               |
| 0x0048     | Oven Cavity<br>Operational<br>State | Event   | Opera<br>tionComple<br>tion |            |        | M               |
| 0x0056     | Temperature<br>Control              | Feature | Tempera<br>tureNumber       |            |        | M               |
| 0x0056     | Temperature<br>Control              | Feature | Tempera<br>tureLevel        |            |        | X               |

Temperature Controlled cabinets only allow the Temperature Control cluster to use the TemperatureNumber feature (i.e. actual temperature in °C). This is because using qualitative temperature levels (e.g. Low/Medium/High) does not allow the behavior expected by the majority of clients. Clients would be trying to "set the temperature" of a cabinet using that cluster, such as an oven's cooking temperature, or a refrigerator's internal cabinet temperature setpoint.

# <span id="page-152-0"></span>**13.5. Dishwasher Device Type**

A dishwasher is a device that is generally installed in residential homes and is capable of washing dishes, cutlery, and other items associate with food preparation and consumption. The device can be permanently installed or portable and can have variety of filling and draining methods.

### <span id="page-152-1"></span>**13.5.1. Revision History**

| Revision | Description                       |
|----------|-----------------------------------|
| 1        | Initial revision                  |
| 2        | Mandate OperationCompletion Event |

#### <span id="page-152-2"></span>**13.5.2. Classification**

| ID     | Device Name | Superset Of | Class  | Scope    |
|--------|-------------|-------------|--------|----------|
| 0x0075 | Dishwasher  |             | Simple | Endpoint |

#### <span id="page-152-3"></span>**13.5.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-153-0"></span>**13.5.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| ID     | Cluster             | Client/Server | Conformance |
|--------|---------------------|---------------|-------------|
| 0x0003 | Identify            | Server        | O           |
| 0x0006 | On/Off              | Server        | O           |
| 0x0056 | Temperature Control | Server        | O           |
| 0x0059 | Dishwasher Mode     | Server        | O           |
| 0x005D | Dishwasher Alarm    | Server        | O           |
| 0x0060 | Operational State   | Server        | M           |

**NOTE**

A dishwasher cycle is a combination of a mode (if supported) and a temperature (if supported). The operational state cluster is then used to start the cycle once these selections have been made via the client.

### <span id="page-153-1"></span>**13.5.5. Cluster Restrictions**

#### **13.5.5.1. Temperature Control Cluster (Server) Clarifications**

Given that different markets have different customary methods of providing temperature settings (e.g. North America often prefers levels, whereas many other markets provide temperatures in °C), it is RECOMMENDED that when the Temperature Control cluster is present, the TemperatureLevel or TemperatureNumber feature of that cluster is chosen to follow the most widely applied convention for the market where the product is sold.

#### **13.5.5.2. On/Off Cluster (Server) Clarifications**

As indicated in the Element Requirements section below, the DF (Dead Front) feature is required for the On/Off cluster in this device type. See the "DeadFrontBehavior feature" section in the On/Off cluster description for detailed requirements. The "dead front" state is linked to the OnOff attribute in the On/Off cluster having the value False. Thus, the Off command of the On/Off cluster SHALL move the device into the "dead front" state, the On command of the On/Off cluster SHALL bring the device out of the "dead front" state, and the device SHALL adhere with the associated requirements on subscription handling and event reporting.

#### **13.5.5.3. Best Effort Attribute Values in "Dead Front" State**

When in "dead front", should the operational values of the cluster attributes not be available or accessible, the following are the RECOMMENDED best effort values for per cluster attributes when responding to a new subscription request or a read request. Attributes not listed have no change in their defined or expected values.

| Cluster Name                 | Attribute        | Fallback |
|------------------------------|------------------|----------|
| Dishwasher Mode              | CurrentMode      | MS       |
| Temperature Control          | All attributes   | MS       |
| Dishwasher Operational State | PhaseList        | null     |
|                              | CurrentPhase     | null     |
|                              | CountdownTime    | null     |
|                              | OperationalState | Stopped  |
|                              | OperationalError | No Error |

#### <span id="page-154-0"></span>**13.5.6. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| ID     | Cluster              | Element   | Name                        | Constraint | Access | Confor<br>mance |
|--------|----------------------|-----------|-----------------------------|------------|--------|-----------------|
| 0x0006 | On/Off               | Feature   | DeadFront<br>Behavior       |            |        | M               |
| 0x0059 | Dishwasher<br>Mode   | Attribute | StartUpMode                 |            |        | X               |
| 0x0059 | Dishwasher<br>Mode   | Feature   | OnOff                       |            |        | X               |
| 0x0060 | Operational<br>State | Event     | Opera<br>tionComple<br>tion |            |        | M               |

# <span id="page-154-1"></span>**13.6. Laundry Dryer Device Type**

A Laundry Dryer represents a device that is capable of drying laundry items.

### <span id="page-154-2"></span>**13.6.1. Revision History**

| Revision | Description                       |  |
|----------|-----------------------------------|--|
| 1        | Initial revision                  |  |
| 2        | Mandate OperationCompletion Event |  |

#### <span id="page-154-3"></span>**13.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x007C         | Laundry Dryer       |             | Simple | Endpoint |

#### <span id="page-155-0"></span>**13.6.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-155-1"></span>**13.6.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name              | Client/Server | Quality | Conformance |
|------------|---------------------------|---------------|---------|-------------|
| 0x0003     | Identify                  | Server        |         | O           |
| 0x0051     | Laundry Washer<br>Mode    | Server        |         | O           |
| 0x0006     | On/Off                    | Server        |         | O           |
| 0x004A     | Laundry Dryer<br>Controls | Server        |         | O           |
| 0x0056     | Temperature Con<br>trol   | Server        |         | O           |
| 0x0060     | Operational State         | Server        |         | M           |

#### <span id="page-155-2"></span>**13.6.5. Cluster Restrictions**

#### **13.6.5.1. Temperature Control Cluster (Server) Clarifications**

Given that different markets have different customary methods of providing temperature settings (e.g. North America often prefers levels, whereas many other markets provide temperatures in °C), it is RECOMMENDED that when the Temperature Control cluster is present, the TemperatureLevel or TemperatureNumber feature of that cluster is chosen to follow the most widely applied convention for the market where the product is sold.

#### **13.6.5.2. On/Off Cluster (Server) Clarifications**

The actions carried out by a Laundry Dryer device on receipt of specific commands are shown below. As indicated in the Element Requirements section below, the DF (Dead Front) feature is required for the On/Off cluster in this device type. See the "DeadFrontBehavior feature" section in the On/Off cluster description for detailed requirements. The "dead front" state is linked to the OnOff attribute in the On/Off cluster having the value False. Thus, the Off command of the On/Off cluster SHALL move the device into the "dead front" state, the On command of the On/Off cluster SHALL bring the device out of the "dead front" state, and the device SHALL adhere with the associated requirements on subscription handling and event reporting.

#### **13.6.5.3. Best Effort Attribute Values in "Dead Front" State**

When in "dead front", should the operational values of the cluster attributes not be available or accessible, the following are the RECOMMENDED best effort values for per cluster attributes when responding to a new subscription request or a read request. Note that some of these attributes may be missing for the clusters not implemented on the endpoint due to optionality.

| Cluster Name           | Attribute            | Value                 |  |
|------------------------|----------------------|-----------------------|--|
| Laundry Dryer Mode     | CurrentMode          | Manufacturer Specific |  |
| Laundry Dryer Controls | TemperatureLevel     | Null                  |  |
|                        | DrynessLevel         | Null                  |  |
| Temperature Control    | All attributes       | Manufacturer Specific |  |
| Operational State      | PhaseList            | Null                  |  |
|                        | CurrentPhase         | Null                  |  |
|                        | CountdownTime        | Null                  |  |
|                        | OperationalStateList | Fully populated       |  |
|                        | OperationalState     | Stopped               |  |
|                        | OperationalError     | No Error              |  |

### <span id="page-156-0"></span>**13.6.6. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name           | Element   | Name                        | Constraint | Access | Confor<br>mance |
|------------|---------------------------|-----------|-----------------------------|------------|--------|-----------------|
| 0x0006     | On/Off                    | Feature   | DeadFront<br>Behavior       |            |        | M               |
| 0x0051     | Laundry<br>Washer<br>Mode | Feature   | OnOff                       |            |        | X               |
| 0x0051     | Laundry<br>Washer<br>Mode | Attribute | StartUpMode                 |            |        | X               |
| 0x0060     | Operational<br>State      | Event     | Opera<br>tionComple<br>tion |            |        | M               |

# <span id="page-156-1"></span>**13.7. Cook Surface Device Type**

A Cook Surface device type represents a heating object on a cooktop or other similar device. It SHALL only be used when composed as part of another device type.

### <span id="page-156-2"></span>**13.7.1. Revision History**

| Revision | Description                                                            |
|----------|------------------------------------------------------------------------|
| 1        | Initial revision                                                       |
| 2        | Made TemperatureLevel (TL) the only valid tem<br>perature control mode |

#### <span id="page-157-0"></span>**13.7.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0077         | Cook Surface        |             | Simple | Endpoint |

#### <span id="page-157-1"></span>**13.7.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-157-2"></span>**13.7.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                | Client/Server | Quality | Conformance |
|------------|-----------------------------|---------------|---------|-------------|
| 0x0006     | On/Off                      | Server        |         | O           |
| 0x0056     | Temperature Con<br>trol     | Server        |         | O.a+        |
| 0x0402     | Temperature Mea<br>surement | Server        |         | O.a+        |

#### <span id="page-157-3"></span>**13.7.5. Cluster Restrictions**

#### **13.7.5.1. On/Off Cluster (Server) Clarifications**

The OffOnly feature is required for the On/Off cluster in this device type due to safety requirements.

## <span id="page-157-4"></span>**13.7.6. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------|------------|--------|-----------------|
| 0x0006     | On/Off          | Feature | OffOnly |            |        | M               |

| Cluster ID | Cluster<br>Name        | Element | Name                  | Constraint | Access | Confor<br>mance |
|------------|------------------------|---------|-----------------------|------------|--------|-----------------|
| 0x0056     | Temperature<br>Control | Feature | Tempera<br>tureLevel  |            |        | M               |
| 0x0056     | Temperature<br>Control | Feature | Tempera<br>tureNumber |            |        | X               |

Whenever the Temperature Control cluster is included on a Cook Surface, the Temperature Control cluster SHALL use the TemperatureLevel feature rather than the TemperatureNumber feature. This is because users are usually in the loop for controlling the temperature of the food being cooked within a heated cooking utensil. For example, while the surface temperature of a cooktop may be significantly above 100°C, an open pot of water will never exceed the boiling point of water as all excess energy transmitted is spent on the water's phase change to steam and the liquid within the pot reaches an equilibrium temperature.

# <span id="page-158-0"></span>**13.8. Cooktop Device Type**

A cooktop is a cooking surface that heats food either by transferring currents from an electromagnetic field located below the glass surface directly to the magnetic induction cookware placed above or through traditional gas or electric burners.

#### <span id="page-158-1"></span>**13.8.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-158-2"></span>**13.8.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0078         | Cooktop             |             | Simple | Endpoint |

#### <span id="page-158-3"></span>**13.8.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-158-4"></span>**13.8.4. Device Type Requirements**

A Cooktop SHALL be composed of zero or more endpoints with the Cook Surface device type as defined by the conformance below.

A cooktop falls under strict regulatory control in some regions. One of these restrictions for noninduction cooktops is that the only remote commands available are to turn off the entire device or read out the temperature setting. This one scenario for allowed remote operation is specifically to address the use case of a device that is left on after a user leaves the home. The individual cooking surfaces cannot be shut off. This leads to a model of a cooktop that has 0 controllable cooking surfaces. For example, the requirements that exist for a gas cooktop would result in zero Cook Surface instances being exposed.

If the Cooktop contains more than one instance of a Cook Surface, those instances SHALL include a semantic tag in the TagList attribute of the Descriptor cluster to disambiguate the cook surface, e.g., "front", "left", or "back". Such a semantic tag SHALL be from the Common namespaces.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0077         | Cook Surface     | min 1      | O           |

#### <span id="page-159-0"></span>**13.8.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | O           |
| 0x0006     | On/Off       | Server        |         | M           |

#### <span id="page-159-1"></span>**13.8.6. Cluster Restrictions**

#### **13.8.6.1. On/Off Cluster (Server) Clarifications**

The OffOnly feature is required for the On/Off cluster in this device type due to safety requirements.

### <span id="page-159-2"></span>**13.8.7. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------|------------|--------|-----------------|
| 0x0006     | On/Off          | Feature | OffOnly |            |        | M               |

# <span id="page-159-3"></span>**13.9. Oven Device Type**

An oven represents a device that contains one or more cabinets, and optionally a single cooktop, that are all capable of heating food. Examples of consumer products implementing this device type include ovens, wall ovens, convection ovens, etc.

#### <span id="page-159-4"></span>**13.9.1. Oven Architecture**

An oven is always defined via endpoint composition. See [Section 13.9.6, "Device Type Require](#page-161-0)[ments"](#page-161-0) for more details.

An example of an oven with two cabinets (one above the other) and a cooktop (with two cook surfaces) is illustrated below.

![](_page_160_Figure_3.jpeg)

*Figure 13. Example of an Oven*

#### <span id="page-160-0"></span>**13.9.2. Revision History**

| Revision | Description              |
|----------|--------------------------|
| 1        | Initial revision         |
| 2        | Added Heater requirement |

#### <span id="page-160-1"></span>**13.9.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x007B         | Oven                |             | Simple | Endpoint |

#### <span id="page-160-2"></span>**13.9.4. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-160-3"></span>**13.9.5. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location   | Device Type<br>ID | Device Type<br>Name                   | Condition | Conformance | Constraint |
|------------|-------------------|---------------------------------------|-----------|-------------|------------|
| Descendant | 0x0071            | Temperature<br>Controlled Cab<br>inet | Heater    | M           | min 1      |

#### <span id="page-161-0"></span>**13.9.6. Device Type Requirements**

An Oven SHALL be composed of at least one endpoint with Temperature Controlled Cabinet device type. There MAY be more endpoints with other device types existing in the Oven. Note that any instance of the TemperatureControl cluster on an endpoint is scoped to the device type on that endpoint, and not the whole node.

If the Oven contains more than one instance of a Temperature Controlled Cabinet, those instances SHALL include a semantic tag in the TagList attribute of the Descriptor cluster to disambiguate the cabinet, e.g., "Top" or "Bottom". Such a semantic tag SHALL be from the defined Common Position namespaces.

Regional restrictions and safety regulations may dictate which aspects of a Temperature Controlled Cabinet may be remotely accessible. In such cases, clusters exposed by an instance of a Temperature Controlled Cabinet MAY have limitations on what commands are supported or what attributes are mutable.

| Device Type ID | Device Type Name                   | Constraint | Conformance |
|----------------|------------------------------------|------------|-------------|
| 0x0071         | Temperature Con<br>trolled Cabinet | min 1      | M           |
| 0x0078         | Cooktop                            | max 1      | O           |

### <span id="page-161-1"></span>**13.9.7. Cluster Requirements**

Each endpoint supporting this device type MAY include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | O           |

# <span id="page-161-2"></span>**13.10. Extractor Hood Device Type**

An Extractor Hood is a device that is generally installed above a cooking surface in residential kitchens. An Extractor Hood's primary purpose is to reduce odors that arise during the cooking process by either extracting the air above the cooking surface or by recirculating and filtering it. It may also contain a light for illuminating the cooking surface.

Extractor Hoods may also be known by the following names:

• Hoods

- Extractor Fans
- Extractors
- Range Hoods
- Telescoping Hoods
- Telescoping Extractors

#### <span id="page-162-0"></span>**13.10.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-162-1"></span>**13.10.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x007A         | Extractor Hood      |             | Simple | Endpoint |

#### <span id="page-162-2"></span>**13.10.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-162-3"></span>**13.10.4. Device Type Requirements**

An Extractor Hood is composed of other device types listed in this table subject to the conformance column of the table. All devices used in compositions SHALL adhere to the disambiguation and superset requirements of the System Model. Specifically, please note that the On/Off Light as listed is a Superset Device Type as defined by the System Model (see *Superset Device Types* in [\[Matter-](#page-23-5)[Core\]\)](#page-23-5), and so the rules defined in that section apply to the use of On/Off Light as a superset when composed in this device type. Additional device types not listed in this table MAY also be included in device compositions.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0100+        | On/Off Light+    |            | O           |

## <span id="page-162-4"></span>**13.10.5. Cluster Requirements**

| Cluster ID | Cluster Name           | Client/Server | Conformance |
|------------|------------------------|---------------|-------------|
| 0x0003     | Identify               | Server        | O           |
| 0x0071     | HEPA Filter Monitoring | Server        | O           |

| Cluster ID | Cluster Name                          | Client/Server | Conformance |
|------------|---------------------------------------|---------------|-------------|
| 0x0072     | Activated Carbon Filter<br>Monitoring | Server        | O           |
| 0x0202     | Fan Control                           | Server        | M           |

#### <span id="page-163-0"></span>**13.10.6. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name                 | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|----------------------|------------|--------|-----------------|
| 0x0202     | Fan Control     | Feature | Rocking              |            |        | X               |
| 0x0202     | Fan Control     | Feature | Wind                 |            |        | X               |
| 0x0202     | Fan Control     | Feature | AirflowDi<br>rection |            |        | X               |

# <span id="page-163-1"></span>**13.11. Microwave Oven Device Type**

This defines conformance to the Microwave Oven device type.

A Microwave Oven is a device with the primary function of heating foods and beverages using a magnetron.

#### <span id="page-163-2"></span>**13.11.1. Microwave Oven Architecture**

A Microwave Oven is a device which at a minimum is capable of being started and stopped and of setting a power level.

A Microwave Oven MAY also support additional capabilities via endpoint composition. See [Section](#page-164-3) [13.11.5, "Device Type Requirements"](#page-164-3) for typical device types.

The following diagram shows an example Microwave Oven consisting of a parent endpoint that is the Microwave Oven device type and a child endpoint providing additional capabilities.

A microwave oven placed above a thermal oven or cooktop/hob may also include a light for illuminating the cooking surface of the thermal oven or cooktop/hob and an exhaust fan for removing cooking odors.

![](_page_164_Figure_3.jpeg)

*Figure 14. Example of a Microwave Oven*

#### <span id="page-164-0"></span>**13.11.2. Revision History**

| Revision | Description                       |  |
|----------|-----------------------------------|--|
| 1        | Initial revision                  |  |
| 2        | Mandate OperationCompletion Event |  |

#### <span id="page-164-1"></span>**13.11.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0079         | Microwave Oven      |             | Simple | Endpoint |

#### <span id="page-164-2"></span>**13.11.4. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-164-3"></span>**13.11.5. Device Type Requirements**

Each endpoint supporting this device type SHALL include endpoints with these device types based on the conformance defined below.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0100+        | On/Off Light+    |            | O           |

When a light is included as part of a composed device type, it is intended to be used as surface light when the microwave oven is installed above a range in an "over the range" configuration rather than the internal light of the microwave oven cavity.

#### <span id="page-165-0"></span>**13.11.6. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name               | Client/Server | Conformance |
|------------|----------------------------|---------------|-------------|
| 0x0003     | Identify                   | Server        | O           |
| 0x0060     | Operational State          | Server        | M           |
| 0x0202     | Fan Control                | Server        | O           |
| 0x005E     | Microwave Oven Mode        | Server        | M           |
| 0x005F     | Microwave Oven Con<br>trol | Server        | M           |

When the Fan Control cluster is supported on an endpoint of this device type, it is intended to be used as a ventilation fan when the microwave oven is installed above a range in an "over the range" configuration rather than the internal fan of the microwave oven cavity.

#### <span id="page-165-1"></span>**13.11.7. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name      | Element   | Name                        | Constraint | Access | Confor<br>mance |
|------------|----------------------|-----------|-----------------------------|------------|--------|-----------------|
| 0x0060     | Operational<br>State | Attribute | Countdown<br>Time           |            |        | M               |
| 0x0060     | Operational<br>State | Event     | Opera<br>tionComple<br>tion |            |        | M               |
| 0x0202     | Fan Control          | Feature   | Wind                        |            |        | X               |
| 0x0202     | Fan Control          | Feature   | AirflowDi<br>rection        |            |        | X               |

### <span id="page-165-2"></span>**13.11.8. Cluster Usage**

This section describes how to control and monitor the operation of a Microwave Oven device. This information is meant to clarify how the data dependencies within the device type's cluster composition are to be used.

Note that the device operations may also be the result of, or affected by, out-of-band actions such as physical button presses on the device, internally scheduled events, vendor application requests, commands invoked via other fabrics, internal device timeouts, etc. For example, a user may pause the oven during operation by opening the door to check on the food.

#### **13.11.8.1. Starting the Oven**

The oven operational attributes are set by sending the SetCookingParameters command of the Microwave Oven Control cluster with the values as intended by the user via a client. Oven operation can be started by sending the Start command via the Operational State cluster or one of its derivatives, if supported, or within the SetCookingParameters command via the StartAfterSetting attribute, if supported.

Upon setting the CookTime attribute via the SetCookingParameters command, the CountdownTime attribute of the Operational State cluster or one of its derivatives , if supported, is set to the same value as the CookTime attribute.

Once oven operation is started, the values previously sent by the SetCookingParameters command are used to control the oven operation and the CountdownTime attribute of the Operational State cluster or one of its derivatives begins counting down.

#### **13.11.8.2. During Operation**

While the oven is in the Running state, the CountdownTime attribute of the Operational State cluster or one of its derivatives counts down and the CookTime attribute of the Microwave Oven Control cluster remains fixed.

#### **13.11.8.3. Stopping the Oven**

Oven operation will end when either the Stop command of the Operational State cluster or one of its derivatives, if supported, is sent, the CountdownTime value reaches zero, or the oven is stopped via an out-of-band method.

It is recommended that when the oven enters the Stopped state of the Operational State cluster or one of its derived clusters, the attribute values of the Microwave Oven Control cluster be set to their default values by the server.

#### **13.11.8.4. Adding More Time**

When time is added to the CookTime attribute using the AddMoreTime command of the Microwave Oven Control cluster, the same amount of time is also added to the CountdownTime attribute of the Operational State cluster or one of its derivatives. See the CookTime attribute constraints and AddMoreTime command for more details.

# <span id="page-168-0"></span>**Chapter 14. Energy Device Types**

# <span id="page-168-1"></span>**14.1. EVSE Device Type**

An EVSE (Electric Vehicle Supply Equipment) is a device that allows an EV (Electric Vehicle) to be connected to the mains electricity supply to allow it to be charged (or discharged in case of Vehicle to Grid / Vehicle to Home applications).

#### <span id="page-168-2"></span>**14.1.1. EVSE Architecture**

An EVSE is always defined via endpoint composition. See [Section 14.1.6, "Device Type Require](#page-170-0)[ments"](#page-170-0) for more details.

An example of an EVSE with single phase AC supply is illustrated below.

![](_page_168_Figure_8.jpeg)

*Figure 15. Example of a single phase EVSE*

The EVSE may also indicate its internal temperature using the temperature measurement cluster (not shown).

An example of an EVSE with a 3 phase AC supply is illustrated below.

![](_page_169_Figure_2.jpeg)

*Figure 16. Example of a 3 phase EVSE*

#### <span id="page-169-0"></span>**14.1.2. Revision History**

| Revision | Description                                                |
|----------|------------------------------------------------------------|
| 1        | Initial revision                                           |
| 2        | Addition of associated Device Energy Manage<br>ment device |

#### <span id="page-169-1"></span>**14.1.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x050C         | Energy EVSE         |             | Simple | Endpoint |

#### <span id="page-169-2"></span>**14.1.4. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-169-3"></span>**14.1.5. Cluster Requirements**

| Cluster ID | Cluster Name     | Client/Server | Conformance |
|------------|------------------|---------------|-------------|
| 0x0003     | Identify         | Server        | O           |
| 0x0099     | Energy EVSE      | Server        | M           |
| 0x009D     | Energy EVSE Mode | Server        | M           |

| Cluster ID | Cluster Name                | Client/Server | Conformance |
|------------|-----------------------------|---------------|-------------|
| 0x0402     | Temperature Measure<br>ment | Server        | O           |

#### <span id="page-170-0"></span>**14.1.6. Device Type Requirements**

An EVSE SHALL be composed of at least one endpoint with device types as defined by the conformance below. There MAY be more endpoints with other device types existing in the EVSE.

| Device Type ID | Device Type Name             | Constraint | Conformance |
|----------------|------------------------------|------------|-------------|
| 0x0011         | Power Source                 | min 1      | M           |
| 0x050D         | Device Energy Manage<br>ment | min 1      | M           |
| 0x0510         | Electrical Sensor            | min 1      | M           |

#### **14.1.6.1. Cluster Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster requirements for the component device types.

| Device Type<br>ID | Device Type<br>Name   | Cluster ID | Cluster Name                         | Client/Server | Conformance |
|-------------------|-----------------------|------------|--------------------------------------|---------------|-------------|
| 0x0510            | Electrical Sen<br>sor | 0x0090     | Electrical<br>Power Mea<br>surement  | Server        | M           |
| 0x0510            | Electrical Sen<br>sor | 0x0091     | Electrical<br>Energy Mea<br>surement | Server        | M           |

The Electrical Sensor device SHALL include both the Electrical Energy Measurement and Electrical Power Measurement clusters, measuring the total energy and power of the EVSE.

#### **14.1.6.2. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Device<br>Type ID        | Device<br>Type<br>Name | Cluster<br>ID | Cluster<br>Name | Element | Name | Con<br>straint | Access | Confor<br>mance |
|--------------------------|------------------------|---------------|-----------------|---------|------|----------------|--------|-----------------|
| Device Energy Management |                        |               |                 |         |      |                |        |                 |

| Device<br>Type ID | Device<br>Type<br>Name             | Cluster<br>ID | Cluster<br>Name                    | Element | Name                               | Con<br>straint | Access | Confor<br>mance |
|-------------------|------------------------------------|---------------|------------------------------------|---------|------------------------------------|----------------|--------|-----------------|
| 0x050D            | Device<br>Energy<br>Manage<br>ment | 0x0098        | Device<br>Energy<br>Manage<br>ment | Feature | Power<br>Forecas<br>tReport<br>ing |                |        | M               |
| 0x050D            | Device<br>Energy<br>Manage<br>ment | 0x0098        | Device<br>Energy<br>Manage<br>ment | Feature | PowerAd<br>justment                |                |        | desc            |

If an EVSE supports three phase power then it SHALL include three additional endpoints including an Electrical Sensor Device Type as child elements. For each child endpoint it SHALL include a semantic tag from the Electrical Measurement Namespace in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Electrical Power Measurement and Electrical Energy Measurement clusters indicating the relevant AC phase that is being measured.

If the EVSE supports the V2X feature then the Device Energy Management cluster included in the Device Energy Management device SHALL support the PowerAdjustment (PA) feature.

# <span id="page-171-0"></span>**14.2. Water Heater Device Type**

A water heater is a device that is generally installed in properties to heat water for showers, baths etc.

#### <span id="page-171-1"></span>**14.2.1. Water Heater Architecture**

A Water Heater is always defined via endpoint composition.

If a Water Heater supports multiple temperature measurement sensors as child elements, it SHALL include a separate endpoint for each sensor. Each endpoint SHALL include a semantic tag in the TagList attribute of the Descriptor cluster to describe the relevant position of the sensor. Such a semantic tag SHALL be from the defined Common Position namespace (i.e. Top, Middle, Bottom etc).

For basic control features the Water Heater re-uses the Thermostat cluster with the **HEAT** and **SCH** features. This allows it to have daily schedules set as to when the hot water heating is enabled, as well as setting the desired setpoint of the hot water.

Additional features of the Water Heater (such as reporting estimated hot water content, and smart reheating functions) are provided by the Water Heater application cluster.

In order to add energy management capability, the Device Energy Management cluster may be optionally supported, and if so, the Electrical Power Measurement and Electrical Energy Measurement clusters are supported via the Electrical Sensor device type.

An example of a Water Heater device is illustrated below.

![](_page_172_Figure_2.jpeg)

*Figure 17. Example of a Water Heater*

#### <span id="page-172-0"></span>**14.2.2. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-172-1"></span>**14.2.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x050F         | Water Heater        |             | Simple | Endpoint |

#### <span id="page-172-2"></span>**14.2.4. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-172-3"></span>**14.2.5. Cluster Requirements**

| Cluster ID | Cluster Name                | Client/Server | Conformance |
|------------|-----------------------------|---------------|-------------|
| 0x0003     | Identify                    | Server        | O           |
| 0x0094     | Water Heater Manage<br>ment | Server        | M           |
| 0x009E     | Water Heater Mode           | Server        | M           |
| 0x0201     | Thermostat                  | Server        | M           |

#### <span id="page-173-0"></span>**14.2.6. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance | Fallback |
|------------|-----------------|---------|---------|------------|--------|-----------------|----------|
| 0x0201     | Thermo<br>stat  | Feature | Heating |            |        | M               |          |

The Energy Management feature of the Water Heater cluster SHALL be supported if the Device Energy Management device type is included.

If Off is a supported SystemMode in the Thermostat cluster, setting the SystemMode of the Thermostat cluster to Off SHALL set the CurrentMode attribute of the Water Heater Mode cluster to a mode having the Off mode tag value and vice versa.

At least one entry in the SupportedModes attribute of the Water Heater Mode cluster SHALL include the Timed mode tag in the ModeTags field list.

#### <span id="page-173-1"></span>**14.2.7. Device Type Requirements**

A Water Heater SHALL be composed of at least one endpoint with device types as defined by the conformance below. There MAY be more endpoints with other device types existing in the Water Heater.

| Device Type ID | Device Type Name             | Constraint | Conformance |
|----------------|------------------------------|------------|-------------|
| 0x0011         | Power Source                 |            | O           |
| 0x0302         | Temperature Sensor           |            | O           |
| 0x050D         | Device Energy Manage<br>ment |            | O           |
| 0x0510         | Electrical Sensor            |            | desc        |

#### **14.2.7.1. Electrical Sensor Device Type**

If a Device Energy Management device type is included as part of a composition, the Electrical Sensor device type SHALL also be included.

#### **14.2.7.2. Cluster Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster requirements for the component device types.

| Device Type<br>ID | Device Type<br>Name | Cluster ID | Cluster Name | Client/Server | Conformance |  |
|-------------------|---------------------|------------|--------------|---------------|-------------|--|
| Electrical Sensor |                     |            |              |               |             |  |

| Device Type<br>ID | Device Type<br>Name   | Cluster ID | Cluster Name                         | Client/Server | Conformance |
|-------------------|-----------------------|------------|--------------------------------------|---------------|-------------|
| 0x0510            | Electrical Sen<br>sor | 0x0090     | Electrical<br>Power Mea<br>surement  | Server        | M           |
| 0x0510            | Electrical Sen<br>sor | 0x0091     | Electrical<br>Energy Mea<br>surement | Server        | M           |

If an Electrical Sensor device is included as part of a composition, it SHALL include both the Electrical Energy Measurement and Electrical Power Measurement clusters, measuring the total energy and power of the Water Heater.

#### **14.2.7.3. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Device<br>Type ID        | Device<br>Type<br>Name             | Cluster<br>ID | Cluster<br>Name                    | Element | Name                               | Con<br>straint | Access | Confor<br>mance |
|--------------------------|------------------------------------|---------------|------------------------------------|---------|------------------------------------|----------------|--------|-----------------|
| Device Energy Management |                                    |               |                                    |         |                                    |                |        |                 |
| 0x050D                   | Device<br>Energy<br>Manage<br>ment | 0x0098        | Device<br>Energy<br>Manage<br>ment | Feature | Power<br>Forecas<br>tReport<br>ing |                |        | M               |

If a Device Energy Management device type is included on a separate endpoint as part of a composition and the Device Energy Management cluster is supported on the same endpoint, the Power-ForecastReporting feature of the Device Energy Management cluster SHALL also be supported.

# <span id="page-174-0"></span>**14.3. Solar Power Device Type**

A Solar Power device is a device that allows a solar panel array, which can optionally be comprised of a set parallel strings of solar panels, and its associated controller and, if appropriate, inverter, to be monitored and controlled by an Energy Management System.

#### <span id="page-174-1"></span>**14.3.1. Solar Power Architecture**

A Solar Power device is always defined via endpoint composition. See [Section 14.3.6, "Device Type](#page-176-4) [Requirements"](#page-176-4) for more details.

An example of a Solar Power device with single phase AC output is illustrated below.

![](_page_175_Figure_2.jpeg)

*Figure 18. Example of a Solar Power device with single phase AC output*

An example of a Solar Power device with single phase AC output, but with the ability to measure the output from 4 sets of solar panels supplying the overall device is illustrated below.

![](_page_175_Figure_5.jpeg)

*Figure 19. Example of a Solar Power device with solar panel measurements*

An example of a Solar Power device with single phase AC output, but with the ability to measure the output from 4 individual solar panels, arranged as 2 strings or 2 panels each is illustrated below.

![](_page_176_Figure_2.jpeg)

*Figure 20. Example of a Solar Power device with solar panel measurements*

#### <span id="page-176-0"></span>**14.3.2. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-176-1"></span>**14.3.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0017         | Solar Power         |             | Simple | Endpoint |

#### <span id="page-176-2"></span>**14.3.4. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-176-3"></span>**14.3.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Conformance |
|------------|--------------|---------------|-------------|
| 0x0003     | Identify     | Server        | O           |

### <span id="page-176-4"></span>**14.3.6. Device Type Requirements**

A Solar Power device SHALL be composed of at least one endpoint with device types as defined by

the conformance below. There MAY be more endpoints with additional instances of these device types or additional device types existing in the Solar Power device.

| Device Type ID | Device Type Name             | Constraint | Conformance |
|----------------|------------------------------|------------|-------------|
| 0x0011         | Power Source                 | min 1      | M           |
| 0x0302         | Temperature Sensor           |            | O           |
| 0x050D         | Device Energy Manage<br>ment |            | desc        |
| 0x0510         | Electrical Sensor            | min 1      | M           |

#### **14.3.6.1. Device Energy Management Device Type**

If the Solar Power device output power can be controlled, then the Device Energy Management device SHALL be included.

#### **14.3.6.2. Cluster Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster requirements for the component device types.

| Device Type<br>ID | Device Type<br>Name   | Cluster ID | Cluster Name                         | Client/Server | Conformance |
|-------------------|-----------------------|------------|--------------------------------------|---------------|-------------|
| 0x0510            | Electrical Sen<br>sor | 0x0041     | User Label                           | Server        | desc        |
| 0x0510            | Electrical Sen<br>sor | 0x0090     | Electrical<br>Power Mea<br>surement  | Server        | M           |
| 0x0510            | Electrical Sen<br>sor | 0x0091     | Electrical<br>Energy Mea<br>surement | Server        | M           |

If a Solar Power device supports measurement of the output of individual solar panels or strings of solar panels then it MAY include additional endpoints for each such measurement, including an Electrical Sensor Device Type as child elements. For each such child endpoint:

• It SHALL include a User Label cluster to allow an installer to add identifying information for the panel or string of panels.

#### **14.3.6.3. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Device<br>Type ID | Device<br>Type<br>Name             | Cluster<br>ID | Cluster<br>Name                         | Element   | Name                | Con<br>straint | Access | Confor<br>mance |
|-------------------|------------------------------------|---------------|-----------------------------------------|-----------|---------------------|----------------|--------|-----------------|
| Power Source      |                                    |               |                                         |           |                     |                |        |                 |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                         | Feature   | Wired               |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x001D        | Descrip<br>tor                          | Feature   | TagList             |                |        | M               |
|                   | Temperature Sensor                 |               |                                         |           |                     |                |        |                 |
| 0x0302            | Tempera<br>ture Sen<br>sor         | 0x001D        | Descrip<br>tor                          | Feature   | TagList             |                |        | M               |
|                   | Device Energy Management           |               |                                         |           |                     |                |        |                 |
| 0x050D            | Device<br>Energy<br>Manage<br>ment | 0x0098        | Device<br>Energy<br>Manage<br>ment      | Feature   | PowerAd<br>justment |                |        | M               |
| Electrical Sensor |                                    |               |                                         |           |                     |                |        |                 |
| 0x0510            | Electrical<br>Sensor               | 0x0091        | Electrical<br>Energy<br>Measure<br>ment | Feature   | Exporte<br>dEnergy  |                |        | M               |
| 0x0510            | Electrical<br>Sensor               | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Attribute | Voltage             |                |        | M               |
| 0x0510            | Electrical<br>Sensor               | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Attribute | Active<br>Current   |                |        | M               |

The Electrical Sensor device SHALL also conform to the following:

- An Electrical Sensor device SHALL measure the energy and power flows of the Solar Power device at the AC grid or DC connection point.
- If the Solar Power device is connected to AC wiring, this Electrical Power Measurement cluster SHALL support the AlternatingCurrent feature, and SHALL support the PolyPhasePower feature if the Solar Power device is connected via polyphase wiring.
- If the Solar Power device is connected to DC wiring, this Electrical Power Measurement cluster SHALL support the DirectCurrent feature.
- This Electrical Power Measurement cluster SHOULD support the ReactivePower attribute if connected to AC wiring.

• This Electrical Energy Measurement cluster SHOULD support the CumulativeEnergy feature.

#### **14.3.6.4. Semantic Tag Requirements on Component Device Types**

The Descriptor cluster for the endpoint including the Power Source device SHALL include the Grid tag if it is connected to the premises wiring.

If a Solar Power device supports two or three phase power output then it MAY include two or three additional endpoints, each including an Electrical Sensor Device Type as child elements. For each such child endpoint it SHALL include a semantic tag from the Electrical Measurement Namespace in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Electrical Power Measurement and Electrical Energy Measurement clusters indicating the relevant AC phase that is being measured.

If a Solar Power device supports measurement of the output of individual solar panels or strings of solar panels then it MAY include additional endpoints for each such measurement, including an Electrical Sensor Device Type as child elements. For each such child endpoint:

• It SHALL include a semantic tag from a Common Namespace, or a Manufacturer defined Tag and Label, in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Electrical Power Measurement and Electrical Energy Measurement clusters, indicating the relevant device port, panel, or string of panels that is being measured.

Any Temperature Sensors included SHALL include Tag(s), and for non-standard Namespaces, Label(s) in the Descriptor clusters of their endpoints to identify the temperature being measured.

# <span id="page-179-0"></span>**14.4. Battery Storage Device Type**

A Battery Storage device is a device that allows a DC battery, which can optionally be comprised of a set parallel strings of battery packs and associated controller, and an AC inverter, to be monitored and controlled by an Energy Management System in order to manage the peaks and troughs of supply and demand, and/or to optimize cost of the energy consumed in premises. It is not intended to be used for a UPS directly supplying a set of appliances, nor for portable battery storage devices.

### <span id="page-179-1"></span>**14.4.1. Battery Storage Architecture**

A Battery Storage device is always defined via endpoint composition. See [Section 14.4.6, "Device](#page-181-3) [Type Requirements"](#page-181-3) for more details.

An example of a Battery Storage device with single phase AC output is illustrated below.

![](_page_180_Figure_2.jpeg)

*Figure 21. Example of a Battery Storage device with single phase AC output*

An example of a Battery Storage device which also includes a directly connected Solar Power device supplying DC power to the battery and using a single common inverter to the single phase AC input and output is illustrated below.

![](_page_180_Figure_5.jpeg)

*Figure 22. Example of a Battery Storage device with DC-connected Solar Power device*

### <span id="page-180-0"></span>**14.4.2. Revision History**

| Revision | Description                                                                        |
|----------|------------------------------------------------------------------------------------|
| 1        | Initial revision                                                                   |
| 2        | Added mandate of two Power Source and Elec<br>trical Sensor composed devices types |

#### <span id="page-181-0"></span>**14.4.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0018         | Battery Storage     |             | Simple | Endpoint |

#### <span id="page-181-1"></span>**14.4.4. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-181-2"></span>**14.4.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Conformance |
|------------|--------------|---------------|-------------|
| 0x0003     | Identify     | Server        | O           |

#### <span id="page-181-3"></span>**14.4.6. Device Type Requirements**

A Battery Storage device SHALL be composed of at least two endpoints with device types as defined by the conformance below. There MAY be more endpoints with additional instances of these device types or additional device types existing in the Battery Storage device.

| Device Type ID | Device Type Name             | Constraint | Conformance |
|----------------|------------------------------|------------|-------------|
| 0x0011         | Power Source                 | min 2      | M           |
| 0x0017         | Solar Power                  |            | O           |
| 0x0302         | Temperature Sensor           |            | O           |
| 0x050D         | Device Energy Manage<br>ment |            | M           |
| 0x0510         | Electrical Sensor            | min 2      | M           |

The Solar Power devices, if included, SHALL have separate endpoints, and include their own Power Source, Electrical Sensor, and Device Energy Management devices, as defined by the [Solar Power](#page-174-0) device.

#### **14.4.6.1. Cluster Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster requirements for the component device types.

| Device Type<br>ID       | Device Type<br>Name | Cluster ID | Cluster Name | Client/Server | Conformance |
|-------------------------|---------------------|------------|--------------|---------------|-------------|
| Electrical Sensor (1st) |                     |            |              |               |             |

| Device Type<br>ID       | Device Type<br>Name   | Cluster ID | Cluster Name                         | Client/Server | Conformance |
|-------------------------|-----------------------|------------|--------------------------------------|---------------|-------------|
| 0x0510                  | Electrical Sen<br>sor | 0x0090     | Electrical<br>Power Mea<br>surement  | Server        | M           |
| 0x0510                  | Electrical Sen<br>sor | 0x0091     | Electrical<br>Energy Mea<br>surement | Server        | M           |
| Electrical Sensor (2st) |                       |            |                                      |               |             |
| 0x0510                  | Electrical Sen<br>sor | 0x0090     | Electrical<br>Power Mea<br>surement  | Server        | M           |
| 0x0510                  | Electrical Sen<br>sor | 0x0091     | Electrical<br>Energy Mea<br>surement | Server        | M           |

**NOTE**

The use of 1st and 2nd to annotate the device types is purely to distinguish the two from each other. It does NOT specify any order or structure of the composition.

#### **14.4.6.2. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Device<br>Type ID | Device<br>Type<br>Name | Cluster<br>ID | Cluster<br>Name | Element   | Name           | Con<br>straint | Access | Confor<br>mance |
|-------------------|------------------------|---------------|-----------------|-----------|----------------|----------------|--------|-----------------|
|                   | Power Source (1st)     |               |                 |           |                |                |        |                 |
| 0x0011            | Power<br>Source        | 0x001D        | Descrip<br>tor  | Feature   | TagList        |                |        | M               |
| 0x0011            | Power<br>Source        | 0x002F        | Power<br>Source | Feature   | Wired          |                |        | M               |
|                   | Power Source (2nd)     |               |                 |           |                |                |        |                 |
| 0x0011            | Power<br>Source        | 0x001D        | Descrip<br>tor  | Feature   | TagList        |                |        | M               |
| 0x0011            | Power<br>Source        | 0x002F        | Power<br>Source | Feature   | Battery        |                |        | M               |
| 0x0011            | Power<br>Source        | 0x002F        | Power<br>Source | Attribute | BatVolt<br>age |                |        | M               |

| Device<br>Type ID | Device<br>Type<br>Name             | Cluster<br>ID | Cluster<br>Name                        | Element   | Name                            | Con<br>straint | Access | Confor<br>mance |
|-------------------|------------------------------------|---------------|----------------------------------------|-----------|---------------------------------|----------------|--------|-----------------|
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | BatPer<br>centRema<br>ining     |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | Bat<br>TimeRe<br>maining        |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | Active<br>BatFaults             |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | BatCapac<br>ity                 |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | Bat<br>TimeTo<br>FullCharg<br>e |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | BatCharg<br>ingCur<br>rent      |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                        | Attribute | Active<br>BatCharg<br>eFaults   |                |        | M               |
|                   | Temperature Sensor                 |               |                                        |           |                                 |                |        |                 |
| 0x0302            | Tempera<br>ture Sen<br>sor         | 0x001D        | Descrip<br>tor                         | Feature   | TagList                         |                |        | M               |
|                   | Device Energy Management           |               |                                        |           |                                 |                |        |                 |
| 0x050D            | Device<br>Energy<br>Manage<br>ment | 0x0098        | Device<br>Energy<br>Manage<br>ment     | Feature   | PowerAd<br>justment             |                |        | M               |
|                   | Electrical Sensor (1st)            |               |                                        |           |                                 |                |        |                 |
| 0x0510            | Electrical<br>Sensor               | 0x001D        | Descrip<br>tor                         | Feature   | TagList                         |                |        | M               |
| 0x0510            | Electrical<br>Sensor               | 0x0090        | Electrical<br>Power<br>Measure<br>ment | Feature   | Alternat<br>ingCur<br>rent      |                |        | M               |

| Device<br>Type ID | Device<br>Type<br>Name  | Cluster<br>ID | Cluster<br>Name                         | Element   | Name               | Con<br>straint | Access | Confor<br>mance |
|-------------------|-------------------------|---------------|-----------------------------------------|-----------|--------------------|----------------|--------|-----------------|
| 0x0510            | Electrical<br>Sensor    | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Attribute | Voltage            |                |        | M               |
| 0x0510            | Electrical<br>Sensor    | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Attribute | Active<br>Current  |                |        | M               |
| 0x0510            | Electrical<br>Sensor    | 0x0091        | Electrical<br>Energy<br>Measure<br>ment | Feature   | Exporte<br>dEnergy |                |        | M               |
|                   | Electrical Sensor (2nd) |               |                                         |           |                    |                |        |                 |
| 0x0510            | Electrical<br>Sensor    | 0x001D        | Descrip<br>tor                          | Feature   | TagList            |                |        | M               |
| 0x0510            | Electrical<br>Sensor    | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Feature   | DirectCur<br>rent  |                |        | M               |
| 0x0510            | Electrical<br>Sensor    | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Attribute | Voltage            |                |        | M               |
| 0x0510            | Electrical<br>Sensor    | 0x0090        | Electrical<br>Power<br>Measure<br>ment  | Attribute | Active<br>Current  |                |        | M               |
| 0x0510            | Electrical<br>Sensor    | 0x0091        | Electrical<br>Energy<br>Measure<br>ment | Feature   | Exporte<br>dEnergy |                |        | M               |

The Power Source cluster in the Power Source device SHALL support the RECHG feature if it can be charged as well as discharged through the connection to the premises wiring.

The Electrical Sensor device SHALL also conform to the following:

- An Electrical Sensor device SHALL measure the energy and power flows of the Battery Storage device at the AC grid connection point.
- The Electrical Power Measurement cluster of this Electrical Sensor device SHALL support the PolyphasePower feature if the Battery Storage device is connected via polyphase wiring, and

SHOULD support the ReactivePower attribute.

• The Electrical Energy Measurement cluster of this Electrical Sensor device SHALL support the ImportedEnergy feature if it can be charged as well as discharged through the connection to the premises wiring, and SHOULD support the CumulativeEnergy feature.

If a Battery Storage device supports two or three phase power output then it MAY include two or three additional endpoints, each including an Electrical Sensor Device Type as child elements. For each such child endpoint it SHALL include a semantic tag from the Electrical Measurement Namespace in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Electrical Power Measurement and Electrical Energy Measurement clusters indicating the relevant AC phase that is being measured.

If a Battery Storage device supports measurement of the input and output of individual batteries or sets of batteries then it MAY include additional endpoints for each such measurement, including an Electrical Sensor Device Type as child elements. For each such child endpoint: \* it SHALL include a semantic tag from the Common Number Namespace, or a Manufacturer defined Tag and Label, in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Electrical Power Measurement and Electrical Energy Measurement clusters indicating the relevant device port, battery, or set of batteries that is being measured. \* it SHOULD also include a User Label cluster to allow an installer to add identifying information if the device permits flexible connection of the actual batteries at installation time.

Any Temperature Sensors included SHALL include Tag(s), and for non-standard Namespaces, Label(s) in the Descriptor clusters of their endpoints to identify the temperature being measured.

#### **14.4.6.3. Semantic Tag Requirements on Component Device Types**

The table below lists conformance requirements for semantic tags associated with the device types listed in the table when used in a composed device.

| Device Type<br>ID       | Device Type<br>Name     | Namespace<br>ID | Namespace       | Tag ID | Tag     | Confor<br>mance |  |  |
|-------------------------|-------------------------|-----------------|-----------------|--------|---------|-----------------|--|--|
|                         | Power Source (1st)      |                 |                 |        |         |                 |  |  |
| 0x0011                  | Power<br>Source         | 0x0F            | Power<br>Source | 0x01   | Grid    | M               |  |  |
| Power Source (2nd)      |                         |                 |                 |        |         |                 |  |  |
| 0x0011                  | Power<br>Source         | 0x0F            | Power<br>Source | 0x03   | Battery | M               |  |  |
|                         | Electrical Sensor (1st) |                 |                 |        |         |                 |  |  |
| 0x0510                  | Electrical<br>Sensor    | 0x0F            | Power<br>Source | 0x01   | Grid    | M               |  |  |
| Electrical Sensor (2nd) |                         |                 |                 |        |         |                 |  |  |
| 0x0510                  | Electrical<br>Sensor    | 0x0F            | Power<br>Source | 0x03   | Battery | M               |  |  |

# <span id="page-186-0"></span>**14.5. Heat Pump Device Type**

A Heat Pump device is a device that uses electrical energy to heat either spaces or water tanks using ground, water or air as the heat source. These typically can heat the air or can pump water via central heating radiators or underfloor heating systems. It is typical to also heat hot water and store the heat in a hot water tank.

Note that the Water Heater device type can also be heated by a heat pump and has similar requirements, but that cannot be used for space heating.

#### <span id="page-186-1"></span>**14.5.1. Heat Pump Architecture**

A Heat Pump device is always defined via endpoint composition. See [Section 14.5.6, "Device Type](#page-187-3) [Requirements"](#page-187-3) for more details.

The Heat Pump device may contain Temperature Sensors for example to measure the flow and return temperatures of the water it is providing to the premises heating system.

The Heat Pump device may also include Thermostats located in the rooms that are being heated by it, which in turn may also include Temperature Sensor clusters which can report the temperatures in those rooms. These Thermostats may be included as servers within Thermostat devices within the Heat Pump device itself, or may be separate third-party Thermostat devices for which the Heat Pump has a client to use them.

An example of a Heat Pump device is illustrated below.

![](_page_186_Figure_10.jpeg)

*Figure 23. Example of a Heat Pump device*

### <span id="page-186-2"></span>**14.5.2. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-187-0"></span>**14.5.3. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0309         | Heat Pump           |             | Simple | Endpoint |

#### <span id="page-187-1"></span>**14.5.4. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-187-2"></span>**14.5.5. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Conformance |
|------------|--------------|---------------|-------------|
| 0x0003     | Identify     | Server        | O           |
| 0x0201     | Thermostat   | Client        | O           |

#### <span id="page-187-3"></span>**14.5.6. Device Type Requirements**

A Heat Pump device SHALL be composed of at least one endpoint with device types as defined by the conformance below. There MAY be more endpoints with additional instances of these device types or additional device types existing in the Heat Pump device.

| Device Type ID | Device Type Name             | Constraint | Conformance |
|----------------|------------------------------|------------|-------------|
| 0x0011         | Power Source                 |            | M           |
| 0x0301         | Thermostat                   |            | O           |
| 0x0302         | Temperature Sensor           |            | O           |
| 0x050D         | Device Energy Manage<br>ment |            | M           |
| 0x050F         | Water Heater                 |            | O           |
| 0x0510         | Electrical Sensor            | min 1      | M           |

The Heat Pump device SHALL include either one or more Thermostat devices, or include a Thermostat client.

#### **14.5.6.1. Cluster Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster requirements for the component device types.

| Device Type<br>ID | Device Type<br>Name   | Cluster ID | Cluster Name                         | Client/Server | Conformance |  |  |  |
|-------------------|-----------------------|------------|--------------------------------------|---------------|-------------|--|--|--|
| Thermostat        |                       |            |                                      |               |             |  |  |  |
| 0x0301            | Thermostat            | 0x0041     | User Label                           | Server        | M           |  |  |  |
| Electrical Sensor |                       |            |                                      |               |             |  |  |  |
| 0x0510            | Electrical Sen<br>sor | 0x0090     | Electrical<br>Power Mea<br>surement  | Server        | M           |  |  |  |
| 0x0510            | Electrical Sen<br>sor | 0x0091     | Electrical<br>Energy Mea<br>surement | Server        | M           |  |  |  |

#### **14.5.6.2. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Device<br>Type ID | Device<br>Name                     | Cluster<br>ID | Cluster<br>Name                    | Element | Name                | Con<br>straint | Access | Confor<br>mance |
|-------------------|------------------------------------|---------------|------------------------------------|---------|---------------------|----------------|--------|-----------------|
| Power Source      |                                    |               |                                    |         |                     |                |        |                 |
| 0x0011            | Power<br>Source                    | 0x002F        | Power<br>Source                    | Feature | Wired               |                |        | M               |
| 0x0011            | Power<br>Source                    | 0x001D        | Descrip<br>tor                     | Feature | TagList             |                |        | M               |
| Thermostat        |                                    |               |                                    |         |                     |                |        |                 |
| 0x0301            | Thermo<br>stat                     | 0x001D        | Descrip<br>tor                     | Feature | TagList             |                |        | M               |
|                   | Temperature Sensor                 |               |                                    |         |                     |                |        |                 |
| 0x0302            | Tempera<br>ture Sen<br>sor         | 0x001D        | Descrip<br>tor                     | Feature | TagList             |                |        | M               |
|                   | Device Energy Management           |               |                                    |         |                     |                |        |                 |
| 0x050D            | Device<br>Energy<br>Manage<br>ment | 0x0098        | Device<br>Energy<br>Manage<br>ment | Feature | PowerAd<br>justment |                |        | M               |
| Electrical Sensor |                                    |               |                                    |         |                     |                |        |                 |

| Device<br>Type ID | Device<br>Name       | Cluster<br>ID | Cluster<br>Name                        | Element   | Name                       | Con<br>straint | Access | Confor<br>mance |
|-------------------|----------------------|---------------|----------------------------------------|-----------|----------------------------|----------------|--------|-----------------|
| 0x0510            | Electrical<br>Sensor | 0x0090        | Electrical<br>Power<br>Measure<br>ment | Feature   | Alternat<br>ingCur<br>rent |                |        | M               |
| 0x0510            | Electrical<br>Sensor | 0x0090        | Electrical<br>Power<br>Measure<br>ment | Attribute | Voltage                    |                |        | M               |
| 0x0510            | Electrical<br>Sensor | 0x0090        | Electrical<br>Power<br>Measure<br>ment | Attribute | Active<br>Current          |                |        | M               |

If a Heat Pump device supports two or three phase power input then it MAY include two or three additional endpoints, each including an Electrical Sensor Device Type as child elements. For each such child endpoint it SHALL include a semantic tag from the Electrical Measurement Namespace in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Electrical Power Measurement and Electrical Energy Measurement clusters indicating the relevant AC phase that is being measured.

The Electrical Energy Measurement and Electrical Power Measurement clusters of the mandatory Electrical Sensor device SHALL measure the energy and power of the Heat Pump device at the AC grid connection point.

The Electrical Power Measurement clusters of the mandatory Electrical Sensor device SHALL support the PolyPhasePower feature if the Heat Pump device is connected via polyphase wiring.

The Electrical Energy Measurement cluster of the mandatory Electrical Sensor device SHOULD support the ImportedEnergy and CumulativeEnergy features.

Any Temperature Sensors using non-standard Namespaces for their Tags SHALL include Label(s) in the Descriptor clusters of their endpoints to identify the temperature being measured.

Any Thermostat SHALL include a semantic tag from a Common Namespace, or a Manufacturer defined Tag and Label, in the TagList attribute of the Descriptor cluster to describe the endpoint for the relevant Thermostat clusters, indicating the relevant device (or its connected port) that is being measured. It SHALL also include a User Label cluster to allow an installer to add identifying information for the rooms or spaces where the Thermostat measurement point is located.

#### **14.5.6.3. Semantic Tag Requirements on Component Device Types**

The table below lists conformance requirements for semantic tags associated with the device types listed in the table when used in a composition.

| Device Type<br>ID | Device<br>Name  | Namespace<br>ID | Namespace       | Tag ID | Tag  | Confor<br>mance |
|-------------------|-----------------|-----------------|-----------------|--------|------|-----------------|
| Power Source      |                 |                 |                 |        |      |                 |
| 0x0011            | Power<br>Source | 0x0F            | Power<br>Source | 0x01   | Grid | M               |

# <span id="page-190-0"></span>**14.6. Meter Reference Point Device Type**

A Meter Reference Point device provides details about tariffs and metering.

#### <span id="page-190-1"></span>**14.6.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

#### <span id="page-190-2"></span>**14.6.2. Classification**

| Device Type ID | Device Type<br>Name      | Superset Of | Class  | Scope    |
|----------------|--------------------------|-------------|--------|----------|
| 0x0512         | Meter Reference<br>Point |             | Simple | Endpoint |

### <span id="page-190-3"></span>**14.6.3. Conditions**

This device type MAY support the following conformance conditions as defined below.

| Condition        | Description            |
|------------------|------------------------|
| ElectricalEnergy | See description below. |

See the Base Device Type definition for additional conformance tags.

#### **14.6.3.1. ElectricalEnergy Condition**

The ElectricalEnergy condition applies to a Meter Reference Point representing a tariff for electrical energy.

### <span id="page-190-4"></span>**14.6.4. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition    | Conformance |
|----------|----------------|---------------------|--------------|-------------|
| Root     | 0x0016         | Root Node           | TimeSyncCond | M           |

#### <span id="page-191-0"></span>**14.6.5. Cluster Requirements**

Each endpoint supporting the Meter Reference Point device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0003     | Identify     | Server        |         | M           |

#### <span id="page-191-1"></span>**14.6.6. Device Type Requirements**

A Meter Reference Point is composed of other endpoints with device types listed in this table, subject to the conformance column of the table. Additional device types not listed in this table MAY also be included in device compositions.

| Device Type ID | Device Type Name         | Constraint | Conformance           |  |
|----------------|--------------------------|------------|-----------------------|--|
| 0x0513         | Electrical Energy Tariff | min 1      | [ElectricalEnergy].a+ |  |
| 0x0514         | Electrical Meter         | min 1      | [ElectricalEnergy].a+ |  |

#### **14.6.6.1. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Device<br>Type ID        | Device<br>Type<br>Name         | Cluster<br>ID | Cluster<br>Name      | Element   | Name       | Con<br>straint | Access | Confor<br>mance |
|--------------------------|--------------------------------|---------------|----------------------|-----------|------------|----------------|--------|-----------------|
| Electrical Energy Tariff |                                |               |                      |           |            |                |        |                 |
| 0x0513                   | Electrical<br>Energy<br>Tariff | 0x700         | Commod<br>ity Tariff | Attribute | TariffUnit | kWh  <br>kVAh  |        | M               |

### <span id="page-191-2"></span>**14.6.7. Meter Reference Point Topology**

#### **14.6.7.1. Basic Electrical Meter Reference Point**

A basic electrical Meter Reference Point device type has a simple import tariff endpoint for grid power, tagged as Grid, Import, AC, and Current.

Optionally, this endpoint may have a child endpoint representing an upcoming tariff, if available, tagged as Grid, Import, AC, and Upcoming.

![](_page_192_Figure_2.jpeg)

*Figure 24. Example of a basic Meter Reference Point*

Optionally, the tariff endpoint may have child endpoints representing tariffs for individual phases of a polyphase power supply.

![](_page_192_Figure_5.jpeg)

*Figure 25. Example of a Meter Reference Point with multiple phases*

#### **14.6.7.2. Separate EV Rate**

Building on the basic topology, a Meter Reference Point device type which has a separate rate for EV charging would add a second endpoint, tagged as EV, Import, AC, and Current.

Optionally, this endpoint may have a child endpoint representing an upcoming EV tariff, if available, tagged as EV, Import, AC, and Upcoming.

![](_page_193_Figure_3.jpeg)

*Figure 26. Example of a Meter Reference Point with a separate EV tariff*

#### **14.6.7.3. Export Rate**

Similarly, a Meter Reference Point device type which has a separate rate for exported electrical energy would add a second endpoint, tagged as Grid, Export, AC, and Current.

Optionally, this endpoint may have a child endpoint representing an upcoming export tariff, if available, tagged as Grid, Export, AC, and Upcoming.

![](_page_194_Figure_2.jpeg)

*Figure 27. Example of a Meter Reference Point with an export tariff*

#### **14.6.7.4. Combination of EV and Export**

The above topologies can be composed to represent various combinations of tariffs. In this example, a tariff has separate rates for an EV and for exporting energy to the grid.

![](_page_195_Figure_2.jpeg)

*Figure 28. Example of a Meter Reference Point with both an export and an EV tariff*

#### **14.6.7.5. Inclusion of Metering Data**

Instead of Electrical Energy Tariff endpoints, a Meter Reference Point may use endpoints with the Electrical Meter device type to represent tariffs with associated metering data.

![](_page_195_Figure_6.jpeg)

*Figure 29. Example of a Meter Reference Point that supports metering*

# <span id="page-196-0"></span>**14.7. Electrical Energy Tariff Device Type**

A Electrical Energy Tariff is a device that defines a tariff for the consumption or production of electrical energy.

#### <span id="page-196-1"></span>**14.7.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-196-2"></span>**14.7.2. Classification**

| Device Type ID | Device Type<br>Name         | Superset Of | Class  | Scope    |
|----------------|-----------------------------|-------------|--------|----------|
| 0x0513         | Electrical Energy<br>Tariff |             | Simple | Endpoint |

#### <span id="page-196-3"></span>**14.7.3. Conditions**

See the Base Device Type definition for conformance tags.

| Condition    | Description                                       |
|--------------|---------------------------------------------------|
| ActiveTariff | The tariff represents the currently active tariff |

### <span id="page-196-4"></span>**14.7.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                  | Client/Server | Quality | Conformance       |
|------------|-------------------------------|---------------|---------|-------------------|
| 0x0095     | Commodity Price               | Server        |         | [ActiveTariff].a+ |
| 0x00A0     | Electrical Grid<br>Conditions | Server        |         | O                 |
| 0x0700     | Commodity Tariff              | Server        |         | O.a+              |

## <span id="page-196-5"></span>**14.7.5. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank entry means no change.

| Cluster ID | Cluster<br>Name | Element | Name    | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------|------------|--------|-----------------|
| 0x001D     | Descriptor      | Feature | TagList |            |        | M               |

#### <span id="page-197-0"></span>**14.7.6. Semantic Tag Requirements**

The table below lists conformance requirements for semantic tags for this device type.

| Namespace ID | Namespace                      | Tag ID | Tag              | Conformance  |
|--------------|--------------------------------|--------|------------------|--------------|
| 0x0B         | Commodity Tariff<br>Chronology | 0x00   | Current          | ActiveTariff |
| 0x0D         | Commodity Tariff<br>Commodity  | 0x00   | ElectricalEnergy | M            |

# <span id="page-197-1"></span>**14.8. Electrical Meter Device Type**

An Electrical Meter device meters the electrical energy being imported and/or exported for billing purposes.

#### <span id="page-197-2"></span>**14.8.1. Revision History**

| Revision | Description      |
|----------|------------------|
| 1        | Initial revision |

#### <span id="page-197-3"></span>**14.8.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of                 | Class  | Scope    |
|----------------|---------------------|-----------------------------|--------|----------|
| 0x0514         | Electrical Meter    | Electrical Energy<br>Tariff | Simple | Endpoint |

### <span id="page-197-4"></span>**14.8.3. Device Type Requirements**

An Electrical Meter SHALL be composed of at least one endpoint with device types as defined by the conformance below.

| Device Type ID | Device Type Name  | Constraint | Conformance |
|----------------|-------------------|------------|-------------|
| 0x0510         | Electrical Sensor | min 1      | M           |

## <span id="page-197-5"></span>**14.8.4. Cluster Requirements**

| Cluster ID | Cluster Name           | Client/Server | Quality | Conformance |
|------------|------------------------|---------------|---------|-------------|
| 0x0B07     | Commodity Meter<br>ing | Server        |         | P, M        |

| Cluster ID | Cluster Name                     | Client/Server | Quality | Conformance |
|------------|----------------------------------|---------------|---------|-------------|
| 0x0090     | Electrical Power<br>Measurement  | Server        |         | M           |
| 0x0091     | Electrical Energy<br>Measurement | Server        |         | M           |

# <span id="page-198-0"></span>**14.9. Electrical Utility Meter Device Type**

An Electrical Utility Meter device provides utility account information, as well as optional details about tariffs and metering.

#### <span id="page-198-1"></span>**14.9.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

#### <span id="page-198-2"></span>**14.9.2. Classification**

| Device Type ID | Device Type<br>Name         | Superset Of              | Class  | Scope    |
|----------------|-----------------------------|--------------------------|--------|----------|
| 0x0511         | Electrical Utility<br>Meter | Meter Reference<br>Point | Simple | Endpoint |

#### <span id="page-198-3"></span>**14.9.3. Conditions**

Please see the Base Device Type definition for conformance tags.

### <span id="page-198-4"></span>**14.9.4. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition    | Conformance |
|----------|----------------|---------------------|--------------|-------------|
| Root     | 0x0016         | Root Node           | TimeSyncCond | M           |

## <span id="page-198-5"></span>**14.9.5. Cluster Requirements**

Each endpoint supporting the Electrical Utility Meter device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name             | Client/Server | Quality | Conformance |
|------------|--------------------------|---------------|---------|-------------|
| 0x0B06     | Meter Identifica<br>tion | Server        |         | M           |

#### <span id="page-199-0"></span>**14.9.6. Electrical Utility Meter Topology**

#### **14.9.6.1. Basic Utility Meter**

A basic Electrical Utility Meter device type has a simple import tariff endpoint for grid power, tagged as Grid, Import, AC, and Current.

Optionally, this endpoint may have a child endpoint representing an upcoming tariff, if available, tagged as Grid, Import, AC, and Upcoming.

![](_page_199_Figure_6.jpeg)

*Figure 30. Example of a basic Electrical Utility Meter*

Optionally, this endpoint may have child endpoints representing measurements of individual phases of a polyphase power supply.

![](_page_199_Figure_9.jpeg)

*Figure 31. Example of a phased Electrical Utility Meter*

#### **14.9.6.2. Separate EV Rate**

Building on the basic topology, an Electrical Utility Meter device type which has a separate rate for EV charging would add a second endpoint, tagged as EV, Import, AC, and Current.

Optionally, this endpoint may have a child endpoint representing an upcoming EV tariff, if available, tagged as EV, Import, AC, and Upcoming.

![](_page_200_Figure_5.jpeg)

*Figure 32. Example of an Electrical Utility Meter with a separate EV tariff*

#### **14.9.6.3. Export Rate**

Similarly, an Electrical Utility Meter device type which has a separate rate for exported electrical energy would add a second endpoint, tagged as Grid, Export, AC, and Current.

Optionally, this endpoint may have a child endpoint representing an upcoming export tariff, if available, tagged as Grid, Export, AC, and Upcoming.

![](_page_201_Figure_2.jpeg)

*Figure 33. Example of an Electrical Utility Meter with a separate export tariff*

#### **14.9.6.4. Combination of EV and Export**

The above topologies can be composed to represent various combinations of tariffs. In this example, a tariff has separate rates for an EV and for exporting energy to the grid.

![](_page_202_Figure_2.jpeg)

*Figure 34. Example of an Electrical Utility Meter with separate export and EV tariffs*

# <span id="page-204-0"></span>**Chapter 15. Network Infrastructure Device Types**

# <span id="page-204-1"></span>**15.1. Introduction**

Matter aims to build a universal IPv6-based communication protocol for smart home devices, and in principle almost any IPv6-bearing Wi-Fi, Thread, or Ethernet network is suitable for Matter deployment (see *Network Topology* in [\[MatterCore\]](#page-23-5)).

The Network Infrastructure device types defined in this chapter are designed to provide a reliable, secure, and performant connectivity experience for Matter devices and their users. To achieve this, these device types expose Matter application clusters for the purposes of network management, diagnostics, and configuration. They also include requirements on lower layers (including the network and physical layers) that contribute to the desired connectivity experience.

Note that Matter devices and applications cannot rely on the presence of Matter-certified Network Infrastructure Devices, or the presence of network features mandated by these device types, for their correct operation.

# <span id="page-204-2"></span>**15.2. Common Requirements**

#### <span id="page-204-3"></span>**15.2.1. Minimum Number of Devices to Support**

The count of IoT devices within a smart home can quickly grow to a substantial number when factoring in the quantity of light points, light switches, and an array of sensor devices that all require connectivity. Consequently, the network infrastructure must be capable of accommodating a substantial number of devices to avoid hitting constraints when users wish to add "one more" product. The requirements in this chapter were designed to result in an IP network (which MAY be a combination of Ethernet LAN, Wi-Fi WLAN, and Thread PAN networks) with a minimum of 300 Matter devices.

• Requirements related to Wi-Fi Access Points and Thread Border Routers are detailed in the sections for the [Network Infrastructure Manager](#page-204-4) and [Thread Border Router](#page-208-0) device types below.

# <span id="page-204-4"></span>**15.3. Network Infrastructure Manager Device Type**

A Network Infrastructure Manager provides interfaces that allow for the management of the Wi-Fi, Thread, and Ethernet networks underlying a Matter deployment, realizing the *Star Network Topology* described in [\[MatterCore\].](#page-23-5)

Examples of physical devices that implement the Matter Network Infrastructure Manager device type include Wi-Fi gateway routers.

Relevant hardware and software requirements for Network Infrastructure Manager devices are defined in [Section 15.3.6, "Other Requirements"](#page-206-0) and within the clusters mandated by this device type.

A Network Infrastructure Manager device MAY be managed by a service associated with the device vendor, for example, an Internet Service Provider. Sometimes this managing service will have policies that require the use of the Managed Device feature of the Access Control Cluster (see [Section](#page-206-1) [15.3.5.1, "ManagedAclAllowed Condition"\)](#page-206-1). Consequently, Commissioners of this device type should be aware of this feature and its use.

#### <span id="page-205-0"></span>**15.3.1. Revision History**

| Revision | Description                                                                        |
|----------|------------------------------------------------------------------------------------|
| 1        | Initial release                                                                    |
| 2        | Add Thread Network Diagnostics requirement;<br>extend "Other Requirements" section |

#### <span id="page-205-1"></span>**15.3.2. Classification**

| Device Type ID | Device Type<br>Name                | Superset Of | Class  | Scope    |
|----------------|------------------------------------|-------------|--------|----------|
| 0x0090         | Network Infra<br>structure Manager |             | Simple | Endpoint |

#### <span id="page-205-2"></span>**15.3.3. Conditions**

See the Base Device Type definition for conformance tags.

# <span id="page-205-3"></span>**15.3.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                           | Client/Server | Quality | Conformance |
|------------|----------------------------------------|---------------|---------|-------------|
| 0x0035     | Thread Network<br>Diagnostics          | Server        |         | M           |
| 0x0451     | Wi-Fi Network<br>Management            | Server        |         | M           |
| 0x0452     | Thread Border<br>Router Manage<br>ment | Server        |         | M           |
| 0x0453     | Thread Network<br>Directory            | Server        |         | M           |

## <span id="page-205-4"></span>**15.3.5. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition             | Conformance |
|----------|----------------|---------------------|-----------------------|-------------|
| Root     | 0x0016         | Root Node           | ManagedAclAl<br>lowed | O           |

#### <span id="page-206-1"></span>**15.3.5.1. ManagedAclAllowed Condition**

A Network Infrastructure Manager device MAY utilize the ManagedAclAllowed condition to allow the Managed Device (MNGD) feature flag of the Access Control Cluster on the device's Root Node endpoint (i.e. Endpoint 0).

Please refer to the "Managed Device Feature Usage Restrictions" section in the Access Control Cluster chapter of the Matter Core Specification for the complete set of limitations on use of this feature on endpoints with the Network Infrastructure Manager device type.

**NOTE**

The conformance of this element crosses endpoints. It is expressed against the Root Node endpoint and there SHALL NOT be a separate AccessControl cluster on the endpoint having the Network Infrastructure Manager device type.

#### <span id="page-206-0"></span>**15.3.6. Other Requirements**

The Network Infrastructure Manager SHALL implement a bridged Wi-Fi / Ethernet hub network, enabling IPv6 connectivity between Matter Nodes across transports.

The Network Infrastructure Manager SHALL support IP communication with at least 300 Matter devices on this network. If the Network Infrastructure Manager operates a DHCPv4 server, then it SHOULD be configured by default with a subnet mask and DHCP pool size that allow for at least 300 devices.

**NOTE**

This recommendation is meant to avoid IPv4 address exhaustion if a large number of devices request IPv4 addresses e.g. for non-Matter traffic.

#### **15.3.6.1. Ethernet Requirements**

The device SHALL provide an Ethernet LAN interface that is part of the bridged hub network.

The Root Node endpoint of the device MAY include a Network Commissioning cluster associated with this Ethernet interface.

#### **15.3.6.2. Wi-Fi Requirements**

The device SHALL support the operation of an IEEE 802.11 Wi-Fi network (ESS) and provide access to the SSID and credentials of this network via the Wi-Fi Network Management cluster. The mechanisms by which this network is configured are outside the scope of this specification. The device SHALL support concurrently operating BSSs for this ESS in the 2.4 GHz and 5 GHz frequency bands; it MAY support operating additional BSSs for this ESS in other frequency bands such as 6 GHz or sub-1 GHz. All BSSs in this ESS SHALL be part of the bridged hub network, i.e. bridged to each other and to the Ethernet interface.

The device MAY support operating additional Wi-Fi networks (e.g. a "guest network"); the requirements above do not apply to any such additional networks.

The device SHOULD NOT include any Network Commissioning cluster instances associated with the Wi-Fi Access Point interface.

The device SHALL be certified by the Wi-Fi Alliance in the Access Point role for Wi-Fi 6 or above. It SHALL additionally be certified in the Access Point role for Wi-Fi 6E if it supports operating in the 6 GHz band, and for Wi-Fi HaLow if it supports operating in the sub-1 GHz band.

To support the efficient operation of the network generally, and for low-power stations in particular, the Network Infrastructure Manager SHALL support, and upon (or before) Matter commissioning SHALL enable, the following Wi-Fi features:

- Extended Sleep Time with a sleep time support up to at least 60 minutes, which includes the following IEEE 802.11 features:
  - Basic Service Set (BSS) Max Idle Period
  - dot11BSSMaxIdlePeriodIndicationByNonAPSTA
- IPv6 Proxy Neighbor Discovery Protocol (NDP) including IPv6 duplicate address detection
- IPv4 Proxy Address Resolution Protocol (ARP)

The device SHALL support at least 100 simultaneous Wi-Fi associations - irrespective of the distribution of the Matter Wi-Fi devices over the supported bands; all Matter Wi-Fi devices could be on the same band. This includes associations of low-power Matter Wi-Fi devices that are asleep for a long time.

**NOTE**

For the case of in-field upgrades of pre-Matter Wi-Fi access points, an exemption (simultaneous association requirement reduced to 64) can be requested when applying for Matter certification, e.g. in case of Wi-Fi chipset limitations (see the [Alliance Certification Policy\)](#page-23-6).

#### **15.3.6.3. Thread Requirements**

The Network Infrastructure Manager device SHALL be certified by the Thread Group as *Built on Thread: Border Router* based on Thread 1.4.0 or above.

The device SHALL implement a Thread Border Router as described by the Thread specification, and provide connectivity between the Thread network and the Wi-Fi / Ethernet hub network. The Thread Interface associated with the Border Router SHALL be exposed via the Thread Border Router Management cluster.

The Thread Network Diagnostics cluster included on the endpoint SHALL be the instance corresponding to the Thread Interface associated with the Border Router functionality.

The device SHOULD NOT include any Network Commissioning cluster instances associated with the Thread Border Router.

The Network Infrastructure Manager device SHALL support working as a Thread Parent for a mini-

mum of 64 Thread Children simultaneously in any combination of Children End Device types. The Network Infrastructure Manager device SHALL support operating as a Thread Border Router in any Thread Network with up to 150 Thread nodes.

#### **15.3.6.4. Discovery and Commissioning**

A Network Infrastructure Manager device SHOULD implement Extended Discovery in order to be discoverable by entities on the local IP network, even when not in Commissioning Mode, and SHOULD populate the optional *device type* subtype (e.g., \_T144) to allow for filtering of discovery results to find only Nodes that match the Network Infrastructure Manager device type (see Commissioning Subtypes).

A Network Infrastructure Manager SHOULD populate the following DNS-SD TXT record key/value pairs in the Commissionable Node Discovery response: Commissioning Pairing Hint, and Commissioning Pairing Instruction so that the Commissioner can guide the user through the steps needed to put the Commissionee into Commissioning Mode. If the Network Infrastructure Manager provides its own app or website which includes a UX for putting the device into Commissioning Mode, then the device SHOULD populate the Commissioning VID/PID key/value pair and SHOULD set bit 1 of the Pairing Hint (Device Manufacturer URL), so that the Commissioner can utilize the URL specified in the CommissioningCustomFlowUrl of the DeviceModel schema entry indexed by the Vendor ID and Product ID in the Distributed Compliance Ledger and utilize flows described in Custom Commissioning Flow to redirect the user to a custom app or website specified by the device vendor, and receive the user back following the callback flow which contains the onboarding payload. This flow is described in detail in the Initiating Commissioning section of the Matter Core specification, under the User Journey titled User-Initiated Beacon Detection, Already Commissioned Device.

# <span id="page-208-0"></span>**15.4. Thread Border Router Device Type**

A Thread Border Router device type provides interfaces for querying and configuring the associated Thread network.

Instances of physical devices categorized as Thread Border Routers encompass standalone Thread Border Routers, conventional application devices like smart speakers, media streamers, and lighting fixtures equipped with a Thread Border Router, as well as Wi-Fi Routers incorporating Thread Border Router functionality.

The necessary hardware and software prerequisites are detailed within the clusters that are mandated by this device type.

### <span id="page-208-1"></span>**15.4.1. Revision History**

| Revision | Description                         |
|----------|-------------------------------------|
| 1        | Initial revision                    |
| 2        | Extend "Other Requirements" section |

#### <span id="page-209-0"></span>**15.4.2. Classification**

| Device Type ID | Device Type<br>Name     | Superset Of | Class  | Scope    |
|----------------|-------------------------|-------------|--------|----------|
| 0x0091         | Thread Border<br>Router |             | Simple | Endpoint |

#### <span id="page-209-1"></span>**15.4.3. Conditions**

See the Base Device Type definition for additional conformance tags.

#### <span id="page-209-2"></span>**15.4.4. Device Type Requirements**

The following table lists other device types to be implemented along with this device type based on conformance.

| ID     | Name                           | Constraint | Conformance |
|--------|--------------------------------|------------|-------------|
| 0x0019 | Secondary Network<br>Interface |            | O           |

If a Thread Border Router endpoint supports the Secondary Network Interface device type, then

- The Thread Border Router Management cluster and the Network Commissioning Cluster SHALL reflect the same underlying network configuration, i.e. changes made via either cluster SHALL also be reflected in the other.
- The MaxNetworks attribute in the Network Commissioning Cluster SHALL have a value of 1.

#### <span id="page-209-3"></span>**15.4.5. Cluster Requirements**

Each endpoint supporting the Thread Border Router device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                           | Client/Server | Quality | Conformance |
|------------|----------------------------------------|---------------|---------|-------------|
| 0x0035     | Thread Network<br>Diagnostics          | Server        |         | M           |
| 0x0452     | Thread Border<br>Router Manage<br>ment | Server        |         | M           |
| 0x0453     | Thread Network<br>Directory            | Server        |         | O           |

#### <span id="page-209-4"></span>**15.4.6. Other Requirements**

The device SHALL implement a Thread Border Router as described by the Thread specification, and provide connectivity between the Thread network and a hub network when connected via a functioning adjacent infrastructure link.

The Thread Interface associated with the Border Router SHALL be exposed via the Thread Border Router Management cluster.

The device MAY include a Network Commissioning cluster instance associated with the Wi-Fi or Ethernet adjacent infrastructure link interface on its Root Node. It SHOULD NOT include a Network Commissioning cluster instance associated with the Thread interface of the Border Router on its Root Node.

#### **15.4.6.1. Thread Requirements**

A device exposing the Thread Border Router device type SHALL be certified by the Thread Group as *Built on Thread: Border Router* based on Thread 1.4.0 or above.

The device SHALL implement a Thread Border Router as described by the Thread specification, and provide connectivity between the Thread network and the Wi-Fi / Ethernet hub network. The Thread Interface associated with the Border Router SHALL be exposed via the Thread Border Router Management cluster.

The Thread Border Router device SHALL support working as a Thread Parent for a minimum of 64 Thread Children simultaneously in any combination of Children End Device types. The Thread Border Router device SHALL support operating as a Thread Border Router in any Thread Network with up to 150 Thread nodes.

#### <span id="page-210-0"></span>**15.4.7. Cluster Usage**

This section describes how to control and monitor the operation of a Thread Border Router.

The Thread Border Router Device Type provides the Thread Border Router Management Cluster with the goal of ensuring a seamless user experience when adding a new Border Router to form a new Thread network or join an existing one. This section presents informative configuration sequences that a Fabric Admin can set up to improve coverage and Internet access redundancy for Thread networks using the Thread Border Router device type. Four use cases are covered:

- Initial configuration of a Thread Border Router when no PAN exists
- Joining an existing PAN
- Sharing an existing PAN
- Moving to a new PAN

#### **15.4.7.1. Initial configuration of Thread Border Router**

In this use case, there is initially no PAN at the user's home. The user installs a Matter certified Thread Border Router to use Thread connectivity for their Matter devices.

![](_page_211_Figure_2.jpeg)

After installation, the PAN configured by Admin A on the Thread Border Router is used to install the Thread Matter device on Fabric A.

#### **15.4.7.2. Joining an existing PAN**

In this use case, there is already a PAN in the user's home that is managed by a Fabric A with TBR1 (e.g. as a result of the above sequence diagram applied previously between Admin 1 and TBR1). The user installs a Matter-certified Thread Border Router (TBR2) to extend the Thread coverage and Internet access redundancy of Thread networks for their Matter devices.

![](_page_211_Figure_6.jpeg)

After installation, a single Thread PAN is shared by all Border Routers.

#### **15.4.7.3. Share an existing PAN**

In this use case, there is already a PAN in the user's home that is managed by Fabric A with TBR1

(e.g. as a result of the above sequence diagram applied previously between Admin 1 and TBR1). The user wants to use the Thread connectivity provided by the Matter-certified Thread Border Router managed by Fabric A with Fabric B to share its connectivity.

![](_page_212_Figure_3.jpeg)

After the installation, the Thread PAN is shared by Fabric A and B.

**NOTE** The user must use the Multiple Fabrics feature process between Fabrics A and B to commission the Thread Border Router from Fabric A to Fabric B.

#### **15.4.7.4. Merging to a new PAN**

This use case is a specific configuration where the user already has 2 PANs. One is managed by a Fabric A through a Matter Thread Border Router (TBR1) and the other is managed by a Fabric B through another Matter Thread Border Router (TBR2).

The user wishes to merge the existing Thread connectivity provided by the two Matter certified Thread Border Routers to share their connectivity to extend the Thread coverage and Internet access redundancy of the Thread networks for their Matter devices.

![](_page_213_Figure_2.jpeg)

After installation, the Thread PAN is shared between Fabrics A and B.

Note 1 : Activation of the pending dataset is Thread stack dependent and propagation of the new dataset to all Matter devices may fail, for example if devices are disconnected during the process.

Note 2 : This configuration should remain very rare if the previous installations followed the previous use cases.

# <span id="page-214-0"></span>**Chapter 16. Camera Device Types**

# <span id="page-214-1"></span>**16.1. Camera Device Type**

A Camera device is a camera that provides interfaces for controlling and transporting captured media, such as Audio, Video or Snapshots.

#### <span id="page-214-2"></span>**16.1.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

### <span id="page-214-3"></span>**16.1.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0142         | Camera              |             | Simple | Endpoint |

#### <span id="page-214-4"></span>**16.1.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-214-5"></span>**16.1.4. Device Type Requirements**

A Camera MAY expose elements of its functionality through one or more additional device types on different endpoints. All devices used in compositions SHALL adhere to the disambiguation requirements of the System Model. Other device types, not explicitly listed in the table, MAY also be included in device compositions but are not considered part of the core functionality of the device.

Cameras which implement occupancy detection based on the signals from the optical sensor, MAY expose this functionality using an Occupancy Sensing cluster on the primary camera endpoint along with the other [camera functionality](#page-215-0). The device type Occupancy Sensor SHALL NOT be added to the DeviceTypeList of this endpoint.

Cameras MAY have an Occupancy Sensor of a different type for occupancy detection independent of the optical sensor. If this sensor is exposed, it SHALL be placed on a child endpoint of the primary camera endpoint, with the corresponding device type Occupancy Sensor, as indicated in the following table:

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0107         | Occupancy Sensor |            | O           |

# <span id="page-214-6"></span>**16.1.5. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition                  | Conformance |
|----------|----------------|---------------------|----------------------------|-------------|
| Root     | 0x0016         | Root Node           | TLSCertifi<br>catesCond    | M           |
| Root     | 0x0016         | Root Node           | PowerSourceCond            | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWithNT<br>PCCond   | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWith<br>ClientCond | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWithTZ<br>Cond     | M           |
| Root     | 0x0016         | Root Node           | TLSClientCond              | M           |

#### <span id="page-215-0"></span>**16.1.6. Cluster Requirements**

| Cluster ID | Cluster Name                                    | Client/Server | Quality | Conformance |
|------------|-------------------------------------------------|---------------|---------|-------------|
| 0x0551     | Camera AV Stream<br>Management                  | Server        |         | M           |
| 0x0553     | WebRTC Transport<br>Provider                    | Server        |         | M           |
| 0x0554     | WebRTC Transport<br>Requestor                   | Client        |         | M           |
| 0x0553     | WebRTC Transport<br>Provider                    | Client        |         | O           |
| 0x0554     | WebRTC Transport<br>Requestor                   | Server        |         | O           |
| 0x0555     | Push AV Stream<br>Transport                     | Server        |         | O           |
| 0x0552     | Camera AV Set<br>tings User Level<br>Management | Server        |         | O           |
| 0x0550     | Zone Management                                 | Server        |         | O           |
| 0x0406     | Occupancy Sens<br>ing                           | Server        |         | O           |
| 0x0003     | Identify                                        | Server        |         | O           |

#### <span id="page-216-0"></span>**16.1.7. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                    | Element | Name                                | Constraint | Access | Confor<br>mance |
|------------|------------------------------------|---------|-------------------------------------|------------|--------|-----------------|
| 0x0550     | Zone Man<br>agement                | Feature | TwoDimen<br>sionalCarte<br>sianZone |            |        | M               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Video                               |            |        | M               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Audio                               |            |        | M               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Snapshot                            |            |        | M               |

# <span id="page-216-1"></span>**16.2. Floodlight Camera Device Type**

A Floodlight Camera device is a composite device which combines a camera and a light, primarily used in security use cases.

### <span id="page-216-2"></span>**16.2.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

#### <span id="page-216-3"></span>**16.2.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0144         | Floodlight Camera   |             | Simple | Endpoint |

#### <span id="page-216-4"></span>**16.2.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-216-5"></span>**16.2.4. Device Type Requirements**

A Floodlight Camera is composed of other device types listed in this table subject to the conformance column of the table. All devices used in compositions SHALL adhere to the disambiguation and superset requirements of the System Model. Specifically, please note that the On/Off Light, as listed, is a Superset Device Type as defined by the System Model (see *Superset Device Types* in [\[Mat](#page-23-5)[terCore\]\)](#page-23-5), and so the rules defined in that section apply to the use of On/Off Light as a superset when composed in this device type. Additional device types not listed in this table MAY also be included in device compositions.

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0100+        | On/Off Light+    | min 1      | M           |
| 0x0142         | Camera           | 1          | M           |

# <span id="page-217-0"></span>**16.3. Video Doorbell Device Type**

A Video Doorbell device is a composite device which combines a camera and a switch to provide a doorbell with Video and Audio streaming.

#### <span id="page-217-1"></span>**16.3.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

### <span id="page-217-2"></span>**16.3.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0143         | Video Doorbell      |             | Simple | Endpoint |

### <span id="page-217-3"></span>**16.3.3. Device Type Requirements**

This device type is composed of other device types listed in this table subject to the conformance column of the table. All devices used in compositions SHALL adhere to the disambiguation and superset requirements of the System Model. Additional device types not listed in this table MAY also be included in device compositions.

| Device Type ID | Device Type Name<br>Constraint |       | Conformance |
|----------------|--------------------------------|-------|-------------|
| 0x0142         | Camera                         | 1     | M           |
| 0x0148         | Doorbell                       | min 1 | M           |

# <span id="page-217-4"></span>**16.4. Intercom Device Type**

An Intercom is a device which provides two-way on demand communication facilities between devices.

Examples include but are not limited to:

• Room to room systems in a house

• Entry door to individual units in a multi-tenant building

#### <span id="page-218-0"></span>**16.4.1. Revision History**

| Revision | Description                |  |
|----------|----------------------------|--|
| 1        | Initial release            |  |
| 2        | Addition of Generic Switch |  |

#### <span id="page-218-1"></span>**16.4.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0140         | Intercom            |             | Simple | Endpoint |

### <span id="page-218-2"></span>**16.4.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-218-3"></span>**16.4.4. Device Type Requirements**

An Intercom SHALL be composed of at least one endpoint with the Generic Switch device type as defined by the conformance below. There MAY be more endpoints with other device types existing in the Intercom. The Generic Switch SHALL model the mechanism used by the Intercom to trigger an alert of the desired connected party.

All devices used in compositions SHALL adhere to the disambiguation and superset requirements of the System Model.

| ID     | Name           | Constraint | Conformance |
|--------|----------------|------------|-------------|
| 0x000F | Generic Switch | min 1      | M           |

### <span id="page-218-4"></span>**16.4.5. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition                  | Conformance |
|----------|----------------|---------------------|----------------------------|-------------|
| Root     | 0x0016         | Root Node           | TLSCertifi<br>catesCond    | M           |
| Root     | 0x0016         | Root Node           | PowerSourceCond            | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWithNT<br>PCCond   | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWith<br>ClientCond | M           |

| Location | Device Type ID | Device Type<br>Name | Condition              | Conformance |
|----------|----------------|---------------------|------------------------|-------------|
| Root     | 0x0016         | Root Node           | TimeSyncWithTZ<br>Cond | M           |

### <span id="page-219-0"></span>**16.4.6. Cluster Requirements**

Each endpoint supporting the Intercom device type SHALL include these clusters based on the conformance defined below.

An Audio connection MAY be established with an instance of an Intercom in one of two ways:

- via WebRTC, with the Intercom acting as a WebRTC Transport Requestor Client.
- via WebRTC, with a Controller acting as the WebRTC Transport Requestor and the Intercom, in this instance, acting as a WebRTC Transport Provider Server. In this case, the Controller may trigger the establishment of Audio through knowledge that there is user intent via subscriptions to the attributes of the Generic Switch, or other means.

| Cluster ID | Cluster Name                                    | Client/Server | Quality | Conformance |
|------------|-------------------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                                        | Server        |         | O           |
| 0x0551     | Camera AV Stream<br>Management                  | Server        |         | M           |
| 0x0552     | Camera AV Set<br>tings User Level<br>Management | Server        |         | O           |
| 0x0553     | WebRTC Transport<br>Provider                    | Server        |         | M           |
| 0x0553     | WebRTC Transport<br>Provider                    | Client        |         | M           |
| 0x0554     | WebRTC Transport<br>Requestor                   | Server        |         | M           |
| 0x0554     | WebRTC Transport<br>Requestor                   | Client        |         | M           |
| 0x0556     | Chime                                           | Client        |         | O           |

### <span id="page-219-1"></span>**16.4.7. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                    | Element | Name     | Constraint | Access | Confor<br>mance |
|------------|------------------------------------|---------|----------|------------|--------|-----------------|
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Audio    |            |        | M               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Video    |            |        | O               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Snapshot |            |        | X               |

#### <span id="page-220-0"></span>**16.4.8. Element Requirements on Component Device Types**

The table below lists qualities and conformance that override the cluster specification requirements for the clusters of the component device types. A blank table cell means there is no change to that item, and the value from the cluster specification applies.

| Device<br>ID   | Device            | Cluster<br>ID | Cluster | Element | Name                    | Con<br>straint | Access | Confor<br>mance |
|----------------|-------------------|---------------|---------|---------|-------------------------|----------------|--------|-----------------|
| Generic Switch |                   |               |         |         |                         |                |        |                 |
| 0x000F         | Generic<br>Switch | 0x003B        | Switch  | Feature | Momen<br>tarySwitc<br>h |                |        | M               |

# <span id="page-220-1"></span>**16.5. Audio Doorbell Device Type**

An Audio Doorbell device is composed in all cases with a generic switch to provide a doorbell with Audio only streaming.

### <span id="page-220-2"></span>**16.5.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |
| 2        | Remove superset |

#### <span id="page-220-3"></span>**16.5.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0141         | Audio Doorbell      |             | Simple | Endpoint |

#### <span id="page-221-0"></span>**16.5.3. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition                | Conformance |
|----------|----------------|---------------------|--------------------------|-------------|
| Root     | 0x0016         | Root Node           | TLSCertifi<br>catesCond  | M           |
| Root     | 0x0016         | Root Node           | PowerSourceCond          | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWithNT<br>PCCond | O           |
| Root     | 0x0016         | Root Node           | TLSClientCond            | O           |

#### <span id="page-221-1"></span>**16.5.4. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                   | Client/Server | Quality | Conformance |
|------------|--------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                       | Server        |         | M           |
| 0x003B     | Switch                         | Server        |         | M           |
| 0x0551     | Camera AV Stream<br>Management | Server        |         | M           |
| 0x0553     | WebRTC Transport<br>Provider   | Server        |         | M           |
| 0x0553     | WebRTC Transport<br>Provider   | Client        |         | O           |
| 0x0554     | WebRTC Transport<br>Requestor  | Server        |         | O           |
| 0x0554     | WebRTC Transport<br>Requestor  | Client        |         | M           |
| 0x0555     | Push AV Stream<br>Transport    | Server        |         | O           |
| 0x0556     | Chime                          | Client        |         | M           |

## <span id="page-221-2"></span>**16.5.5. Element Requirements**

The table below lists qualities and conformance values that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name                    | Element | Name     | Constraint | Access | Confor<br>mance |
|------------|------------------------------------|---------|----------|------------|--------|-----------------|
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Audio    |            |        | M               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Snapshot |            |        | X               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Video    |            |        | X               |

# <span id="page-222-0"></span>**16.6. Snapshot Camera Device Type**

A Snapshot Camera device is a camera which can only support retrieving still images on-demand via the Capture Snapshot command in the Camera AV Stream Management cluster.

#### <span id="page-222-1"></span>**16.6.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

#### <span id="page-222-2"></span>**16.6.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0145         | Snapshot Camera     |             | Simple | Endpoint |

#### <span id="page-222-3"></span>**16.6.3. Conditions**

See the Base Device Type definition for conformance tags.

#### <span id="page-222-4"></span>**16.6.4. Device Type Requirements**

A Snapshot Camera MAY expose elements of its functionality through one or more additional device types on different endpoints. All devices used in compositions SHALL adhere to the disambiguation requirements of the System Model. Other device types, not explicitly listed in the table, MAY also be included in device compositions but are not considered part of the core functionality of the device.

Snapshot Cameras which implement occupancy detection based on the signals from the optical sensor, MAY expose this functionality using an Occupancy Sensing cluster on the primary camera endpoint along with the other [camera functionality.](#page-215-0) The device type Occupancy Sensor SHALL NOT be added to the DeviceTypeList of this endpoint.

Snapshot Cameras MAY have an Occupancy Sensor of a different type for occupancy detection inde-

pendent of the optical sensor. If this sensor is exposed, it SHALL be placed on a child endpoint of the primary camera endpoint, with the corresponding device type Occupancy Sensor, as indicated in the following table:

| Device Type ID | Device Type Name | Constraint | Conformance |
|----------------|------------------|------------|-------------|
| 0x0107         | Occupancy Sensor |            | O           |

#### <span id="page-223-0"></span>**16.6.5. Condition Requirements**

The table below lists conditions and conformance values that override the device type definition.

| Location | Device Type ID | Device Type<br>Name | Condition              | Conformance |
|----------|----------------|---------------------|------------------------|-------------|
| Root     | 0x0016         | Root Node           | PowerSourceCond        | M           |
| Root     | 0x0016         | Root Node           | TimeSyncWithTZ<br>Cond | M           |

#### <span id="page-223-1"></span>**16.6.6. Cluster Requirements**

Each endpoint supporting the Snapshot Camera device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name                                    | Client/Server | Quality | Conformance |
|------------|-------------------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                                        | Server        |         | O           |
| 0x0406     | Occupancy Sens<br>ing                           | Server        |         | O           |
| 0x0550     | Zone Management                                 | Server        |         | O           |
| 0x0551     | Camera AV Stream<br>Management                  | Server        |         | M           |
| 0x0552     | Camera AV Set<br>tings User Level<br>Management | Server        |         | O           |

### <span id="page-223-2"></span>**16.6.7. Element Requirements**

This lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name     | Element | Name                                | Constraint | Access | Confor<br>mance |
|------------|---------------------|---------|-------------------------------------|------------|--------|-----------------|
| 0x0550     | Zone Man<br>agement | Feature | TwoDimen<br>sionalCarte<br>sianZone |            |        | M               |

| Cluster ID | Cluster<br>Name                    | Element | Name     | Constraint | Access | Confor<br>mance |
|------------|------------------------------------|---------|----------|------------|--------|-----------------|
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Snapshot |            |        | M               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Video    |            |        | X               |
| 0x0551     | Camera AV<br>Stream Man<br>agement | Feature | Audio    |            |        | X               |

# <span id="page-224-0"></span>**16.7. Chime Device Type**

A Chime device is a device which can play from a range of pre installed sounds and is typically used with a [Doorbell](#page-226-0), [Audio Doorbell](#page-220-1), or [Video Doorbell.](#page-217-0)

#### <span id="page-224-1"></span>**16.7.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

#### <span id="page-224-2"></span>**16.7.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0146         | Chime               |             | Simple | Endpoint |

#### <span id="page-224-3"></span>**16.7.3. Conditions**

See the Base Device Type definition for conformance tags.

### <span id="page-224-4"></span>**16.7.4. Cluster Requirements**

Each endpoint supporting the Chime device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Quality | Conformance |
|------------|--------------|---------------|---------|-------------|
| 0x0556     | Chime        | Server        |         | M           |
| 0x0003     | Identify     | Server        |         | O           |

# <span id="page-224-5"></span>**16.7.5. Element Requirements**

There are no cluster element overrides.

# <span id="page-225-0"></span>**16.8. Camera Controller Device Type**

A Camera controller device is a device that provides interfaces for controlling and managing camera devices.

#### <span id="page-225-1"></span>**16.8.1. Revision History**

| Revision | Description     |
|----------|-----------------|
| 1        | Initial release |

#### <span id="page-225-2"></span>**16.8.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0147         | Camera Controller   |             | Simple | Endpoint |

### <span id="page-225-3"></span>**16.8.3. Cluster Requirements**

Each endpoint supporting the Camera Controller device type SHALL include these clusters based on the conformance defined below. A node SHALL only ever have, at most, one instance of the Camera Controller's required clusters.

| Cluster ID | Cluster Name                                    | Client/Server | Quality | Conformance |
|------------|-------------------------------------------------|---------------|---------|-------------|
| 0x0003     | Identify                                        | Client        |         | O           |
| 0x002F     | Power Source                                    | Client        |         | O           |
| 0x0406     | Occupancy Sens<br>ing                           | Client        |         | O           |
| 0x0550     | Zone Management                                 | Client        |         | O           |
| 0x0551     | Camera AV Stream<br>Management                  | Client        |         | O           |
| 0x0552     | Camera AV Set<br>tings User Level<br>Management | Client        |         | O           |
| 0x0553     | WebRTC Transport<br>Provider                    | Client        |         | M           |
| 0x0554     | WebRTC Transport<br>Requestor                   | Server        |         | M           |
| 0x0555     | Push AV Stream<br>Transport                     | Client        |         | O           |
| 0x0801     | TLS Certificate<br>Management                   | Client        |         | O           |

| Cluster ID | Cluster Name              | Client/Server | Quality | Conformance |
|------------|---------------------------|---------------|---------|-------------|
| 0x0802     | TLS Client Man<br>agement | Client        |         | O           |

# <span id="page-226-0"></span>**16.9. Doorbell Device Type**

A Doorbell device is a switch which when pressed usually causes a [Chime](#page-224-0) to activate.

#### <span id="page-226-1"></span>**16.9.1. Revision History**

| Revision | Description     |  |
|----------|-----------------|--|
| 1        | Initial release |  |
| 2        | Remove superset |  |

#### <span id="page-226-2"></span>**16.9.2. Classification**

| Device Type ID | Device Type<br>Name | Superset Of | Class  | Scope    |
|----------------|---------------------|-------------|--------|----------|
| 0x0148         | Doorbell            |             | Simple | Endpoint |

#### **16.9.2.1. Cluster Requirements**

Each endpoint supporting this device type SHALL include these clusters based on the conformance defined below.

| Cluster ID | Cluster Name | Client/Server | Conformance |
|------------|--------------|---------------|-------------|
| 0x0003     | Identify     | Server        | M           |
| 0x003B     | Switch       | Server        | M           |
| 0x0556     | Chime        | Client        | M           |

#### **16.9.2.2. Element Requirements**

The table below lists qualities and conformance that override the cluster specification requirements. A blank table cell means there is no change to that item and the value from the cluster specification applies.

| Cluster ID | Cluster<br>Name | Element | Name                | Constraint | Access | Confor<br>mance |
|------------|-----------------|---------|---------------------|------------|--------|-----------------|
| 0x003B     | Switch          | Feature | Momen<br>tarySwitch |            |        | M               |