![](_page_0_Picture_0.jpeg)

# **Matter Standard Namespaces Version 1.5.1**

Document: 23-31936-007\_Matter-1.5.1-Standard-Namespaces.pdf

March 16,2026

Sponsored by: Connectivity Standards Alliance

Accepted by: This document has been accepted for release by the Connectivity

Standards Alliance Board of Directors on **March 16,2026**

Abstract: The Matter specification defines fundamental requirements to

enable an interoperable application layer solution for smart home

devices over the Internet Protocol.

Keywords: Referenced in Chapter 1.

Copyright © 2022-2026 Connectivity Standards Alliance, Inc. 508 Second Street, Suite 109B Davis, CA 95616 - USA www.csa-iot.org All rights reserved.

Permission is granted to members of the Connectivity Standards Alliance to reproduce this document for their own use or the use of other Connectivity Standards Alliance members only, provided this notice is included. All other rights reserved. Duplication for sale, or for commercial or for-profit use is strictly prohibited without the prior written consent of the Connectivity Standards Alliance.

![](_page_2_Picture_0.jpeg)

# Matter Semantic Tag Namespaces

Version 1.5.1, 2026-03-10 23:04:42 -0700: Approved

#### **Table of Contents**

| Notice of Use and Disclosure 1                             |  |
|------------------------------------------------------------|--|
| Revision History 3                                         |  |
| 1. Introduction 5                                          |  |
| 1.1. Connectivity Standards Alliance Reference Documents 7 |  |
| 2. Common Closure Semantic Tag Namespace 9                 |  |
| 3. Common Compass Direction Semantic Tag Namespace 11      |  |
| 4. Common Compass Location Semantic Tag Namespace 13       |  |
| 5. Common Direction Semantic Tag Namespace 15              |  |
| 6. Common Level Semantic Tag Namespace 17                  |  |
| 7. Common Location Semantic Tag Namespace 19               |  |
| 8. Common Number Semantic Tag Namespace 21                 |  |
| 9. Common Position Semantic Tag Namespace 23               |  |
| 9.1. Examples 23                                           |  |
| 10. Electrical Measurement Semantic Tag Namespace 25       |  |
| 11. Commodity Tariff Chronology Semantic Tag Namespace 27  |  |
| 12. Commodity Tariff Commodity Semantic Tag Namespace 29   |  |
| 13. Laundry Semantic Tag Namespace 31                      |  |
| 14. Power Source Semantic Tag Namespace 33                 |  |
| 14.1. Grid Tag 33                                          |  |
| 14.2. Solar Tag 33                                         |  |
| 14.3. Battery Tag 33                                       |  |
| 14.4. EV Tag 34                                            |  |
| 15. Common Area Semantic Tag Namespace 35                  |  |
| 16. Common Landmark Semantic Tag Namespace 39              |  |
| 17. Common Relative Position Semantic Tag Namespace 41     |  |
| 18. Commodity Tariff Flow Semantic Tag Namespace 43        |  |
| 19. Refrigerator Semantic Tag Namespace 45                 |  |
| 20. Room Air Conditioner Semantic Tag Namespace 47         |  |
| 21. Switches Semantic Tag Namespace 49                     |  |
| 21.1. Custom Tag 49                                        |  |
| 22. Closure Semantic Tag Namespace 51                      |  |
| 23. Closure Panel Semantic Tag Namespace 53                |  |
| 24. Closure Covering Semantic Tag Namespace 55             |  |
| 25. Closure Window Semantic Tag Namespace 57               |  |
| 26. Closure Cabinet Semantic Tag Namespace 59              |  |

#### <span id="page-6-0"></span>**Notice of Use and Disclosure**

Copyright © Connectivity Standards Alliance (2023-2025). All rights reserved. The information within this document is the property of the Connectivity Standards Alliance and its use and disclosure are restricted, except as expressly set forth herein.

Connectivity Standards Alliance hereby grants you a fully-paid, non-exclusive, nontransferable, worldwide, limited and revocable license (without the right to sublicense), under Connectivity Standards Alliance's applicable copyright rights, to view, download, save, reproduce and use the document solely for your own internal purposes and in accordance with the terms of the license set forth herein. This license does not authorize you to, and you expressly warrant that you shall not: (a) permit others (outside your organization) to use this document; (b) post or publish this document; (c) modify, adapt, translate, or otherwise change this document in any manner or create any derivative work based on this document; (d) remove or modify any notice or label on this document, including this Copyright Notice, License and Disclaimer. The Connectivity Standards Alliance does not grant you any license hereunder other than as expressly stated herein.

Elements of this document may be subject to third party intellectual property rights, including without limitation, patent, copyright or trademark rights, and any such third party may or may not be a member of the Connectivity Standards Alliance. Connectivity Standards Alliance members grant other Connectivity Standards Alliance members certain intellectual property rights as set forth in the Connectivity Standards Alliance IPR Policy. Connectivity Standards Alliance members do not grant you any rights under this license. The Connectivity Standards Alliance is not responsible for, and shall not be held responsible in any manner for, identifying or failing to identify any or all such third party intellectual property rights. Please visit www.csa-iot.org for more information on how to become a member of the Connectivity Standards Alliance.

This document and the information contained herein are provided on an "AS IS" basis and the Connectivity Standards Alliance DISCLAIMS ALL WARRANTIES EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO (A) ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OF THIRD PARTIES (INCLUDING WITHOUT LIMITATION ANY INTELLEC-TUAL PROPERTY RIGHTS INCLUDING PATENT, COPYRIGHT OR TRADEMARK RIGHTS); OR (B) ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NONINFRINGEMENT. IN NO EVENT WILL THE CONNECTIVITY STANDARDS ALLIANCE BE LIABLE FOR ANY LOSS OF PROFITS, LOSS OF BUSINESS, LOSS OF USE OF DATA, INTERRUPTION OF BUSI-NESS, OR FOR ANY OTHER DIRECT, INDIRECT, SPECIAL OR EXEMPLARY, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL DAMAGES OF ANY KIND, IN CONTRACT OR IN TORT, IN CONNECTION WITH THIS DOCUMENT OR THE INFORMATION CONTAINED HEREIN, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE.

All company, brand and product names in this document may be trademarks that are the sole property of their respective owners.

This notice and disclaimer must be included on all copies of this document.

Connectivity Standards Alliance 508 Second Street, Suite 206 Davis, CA 95616, USA

#### <span id="page-8-0"></span>**Revision History**

| Revision | Date              | Details       | Editor          |
|----------|-------------------|---------------|-----------------|
| 1        | October 18, 2023  | Version 1.2   | Robert Szewczyk |
| 2        | April 17, 2024    | Version 1.3   | Robert Szewczyk |
| 3        | November 4, 2024  | Version 1.4   | Robert Szewczyk |
| 4        | March 17, 2025    | Version 1.4.1 | Robert Szewczyk |
| 5        | July 16, 2025     | Version 1.4.2 | Robert Szewczyk |
| 6        | November 10, 2025 | Version 1.5   | Robert Szewczyk |
| 7        | March 16, 2026    | Version 1.5.1 | Robert Szewczyk |

#### <span id="page-10-0"></span>**Chapter 1. Introduction**

This document contains namespaces as part of the semantic tag feature.

The standard namespaces are defined in this appendix. They consist of the common namespaces and device-specific namespaces.

The Common namespaces start with Namespace ID 0x01 and contains semantic tags that can apply to any domain. Examples include direction words like 'left', 'right', 'up' and 'down' or location words like 'inside' and 'outside'.

Device-specific namespaces begin with Namespace ID 0x41. The semantic tags defined in the device-specific namespaces SHALL be restricted for use within each device type or set of device types.

**NOTE**

Some namespaces specific to certain group of device types (related to Energy and Laundry) have been assigned an ID from the common range, even though they are only applicable to a certain set of device types only.

When indicating a specific namespace and tag in the spec, one of the following two methods SHALL be used:

| Method                          | Example         | Note             |
|---------------------------------|-----------------|------------------|
| Double colon separator          | Namespace::Tag  | Preferred method |
| Backticks with period separator | `Namespace.Tag` | Also acceptable  |

**NOTE**

Previously, the notation with a period separator (example: Namespace.Tag) was also used. Instances using that notation will be updated.

A [TagList](#page-12-1) MAY combine several of these tags, as appropriate for the device, provided that for any given device type the tags come from the namespace for that device type as well as any of the common namespaces, and/or from a manufacturer-specific namespace.

Tags MAY appear in bold or have any other decoration as needed to achieve the desired effect in the rendered output, such as shown in the example below. The decoration of tags is entirely optional.

**Example:** An outdoor luminaire with two light units, one shining upwards and one shining downwards. One light unit would be represented by an endpoint with a TagList which has TagStructs with Tags **Location::Outdoor** and **Position::Top** and **Direction::Upward**, while the other light unit would be represented by an endpoint with a TagList which has TagStructs with Tags **Location::Outdoor** and **Position::Bottom** and **Direction::Downward**.

| ID                | Namespace | Summary |
|-------------------|-----------|---------|
| Common namespaces |           |         |

| ID   | Namespace                                | Summary                                                                                       |
|------|------------------------------------------|-----------------------------------------------------------------------------------------------|
| 0x01 | Common Closure Namespace                 | Deprecated<br>Tags which are useful in<br>describing things related to<br>closing and opening |
| 0x02 | Common Compass Direction<br>Namespace    | Tags which are useful in<br>describing things related to<br>compass direction                 |
| 0x03 | Common Compass Location<br>Namespace     | Tags which are useful in<br>describing things related to<br>compass location                  |
| 0x04 | Common Direction Namespace               | Tags which are useful in<br>describing things related to<br>direction                         |
| 0x05 | Common Level Namespace                   | Tags which are useful in<br>describing things related to<br>level                             |
| 0x06 | Common Location Namespace                | Tags which are useful in<br>describing things related to<br>location                          |
| 0x07 | Common Number Namespace                  | Tags which are useful in<br>describing things related to<br>numbering                         |
| 0x08 | Common Position Namespace                | Tags which are useful in<br>describing things related to<br>position                          |
| 0x0A | Electrical Measurement Name<br>space     | Tags which are useful in<br>describing electrical loads                                       |
| 0x0B | Commodity Tariff Chronology<br>Namespace | Tags which are useful in<br>describing the chronological<br>order of Commodity Tariffs        |
| 0x0D | Commodity Tariff Commodity<br>Namespace  | Tags which are useful in<br>describing Commodity Tariff<br>commodities                        |
| 0x0E | Laundry Namespace                        | Tags which are useful with<br>laundry device types                                            |
| 0x0F | Power Source Namespace                   | Tags which are useful with<br>power source device types                                       |
| 0x10 | Common Area Namespace                    | Tags which are useful in<br>describing things related to<br>home areas                        |

| ID                         | Namespace                                          | Summary                                                                                                                |
|----------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 0x11                       | Common Landmark Namespace Tags which are useful in | describing things related to<br>home landmarks                                                                         |
| 0x12                       | Common Relative Position<br>Namespace              | Tags which are useful in<br>describing things related to<br>position relative to a reference<br>external to the device |
| 0x13                       | Commodity Tariff Flow Name<br>space                | Tags which are useful in<br>describing Commodity Tariff<br>flow                                                        |
| Device-specific namespaces |                                                    |                                                                                                                        |
| 0x41                       | Refrigerator Namespace                             | Tags which are useful with<br>refrigeration device types                                                               |
| 0x42                       | Room Air Conditioner Name<br>space                 | Tags which are useful with<br>Room Air Conditioner device<br>types                                                     |
| 0x43                       | Switches Namespace                                 | Tags which are useful with<br>switch device types                                                                      |
| 0x44                       | Closure Namespace                                  | Tags which are useful with clo<br>sure device types                                                                    |
| 0x45                       | Closure Panel Namespace                            | Tags which are useful with clo<br>sure panel device types                                                              |
| 0x46                       | Closure Covering Namespace                         | Tags which are useful with clo<br>sure (Covering) device types                                                         |
| 0x47                       | Closure Window Namespace                           | Tags which are useful with clo<br>sure (Window) device types                                                           |
| 0x48                       | Closure Cabinet Namespace                          | Tags which are useful with clo<br>sure (Cabinet) device types                                                          |

#### <span id="page-12-0"></span>**1.1. Connectivity Standards Alliance Reference Documents**

<span id="page-12-1"></span>

| Reference             | Reference Location/URL                                       | Description                                  |
|-----------------------|--------------------------------------------------------------|----------------------------------------------|
| [MatterCore]          | https://groups.csa-iot.org/wg/<br>members-all/document/27349 | Matter Core Specification                    |
| [MatterAppClusters]   | https://groups.csa-iot.org/wg/<br>members-all/document/27350 | Matter Application Cluster Spec<br>ification |
| [MatterDeviceLibrary] | https://groups.csa-iot.org/wg/<br>members-all/document/27351 | Matter Device Library                        |

### <span id="page-14-0"></span>**Chapter 2. Common Closure Semantic Tag Namespace**

This section contains the Common Closure semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a feature of a Closure, e.g. the button to activate opening a garage door.

This namespace has been deprecated as of Matter 1.4.2.

**NOTE**

Clients SHOULD still have support for these tags, since the tags could be used by a server certified on a previous revision of Matter.

| ID   | Namespace      |
|------|----------------|
| 0x01 | Common Closure |

| ID   | Name    | Summary                     |
|------|---------|-----------------------------|
| 0x00 | Opening | Move toward open position   |
| 0x01 | Closing | Move toward closed position |
| 0x02 | Stop    | Stop any movement           |

#### <span id="page-16-0"></span>**Chapter 3. Common Compass Direction Semantic Tag Namespace**

This section contains the Common Compass Direction semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a movement into a certain compass direction. Note the difference with [Chapter 4,](#page-18-0) *[Com](#page-18-0)[mon Compass Location Semantic Tag Namespace](#page-18-0)*.

| ID   | Namespace                |
|------|--------------------------|
| 0x02 | Common Compass Direction |

| ID   | Name          | Summary |
|------|---------------|---------|
| 0x00 | Northward     |         |
| 0x01 | NorthEastward |         |
| 0x02 | Eastward      |         |
| 0x03 | SouthEastward |         |
| 0x04 | Southward     |         |
| 0x05 | SouthWestward |         |
| 0x06 | Westward      |         |
| 0x07 | NorthWestward |         |

### <span id="page-18-0"></span>**Chapter 4. Common Compass Location Semantic Tag Namespace**

This section contains the Common Compass Location semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a position in a certain compass direction (e.g. an outdoor sensor in the North garden). Note the difference with [Chapter 3,](#page-16-0) *[Common Compass Direction Semantic Tag Namespace](#page-16-0)*.

| ID   | Namespace               |
|------|-------------------------|
| 0x03 | Common Compass Location |

| ID   | Name      | Summary |
|------|-----------|---------|
| 0x00 | North     |         |
| 0x01 | NorthEast |         |
| 0x02 | East      |         |
| 0x03 | SouthEast |         |
| 0x04 | South     |         |
| 0x05 | SouthWest |         |
| 0x06 | West      |         |
| 0x07 | NorthWest |         |

# <span id="page-20-0"></span>**Chapter 5. Common Direction Semantic Tag Namespace**

This section contains the Common Direction semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a movement in a certain direction relative to the device. Note the difference with [Chapter](#page-28-0) [9,](#page-28-0) *[Common Position Semantic Tag Namespace](#page-28-0)*.

| ID   | Namespace        |
|------|------------------|
| 0x04 | Common Direction |

| ID   | Name      | Summary |
|------|-----------|---------|
| 0x00 | Upward    |         |
| 0x01 | Downward  |         |
| 0x02 | Leftward  |         |
| 0x03 | Rightward |         |
| 0x04 | Forward   |         |
| 0x05 | Backward  |         |

### <span id="page-22-0"></span>**Chapter 6. Common Level Semantic Tag Namespace**

This section contains the Common Level semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a certain level for a feature of a device (e.g. a button to set the speed of a fan).

| ID   | Namespace    |
|------|--------------|
| 0x05 | Common Level |

| ID   | Name   | Summary |
|------|--------|---------|
| 0x00 | Low    |         |
| 0x01 | Medium |         |
| 0x02 | High   |         |

### <span id="page-24-0"></span>**Chapter 7. Common Location Semantic Tag Namespace**

This section contains the Common Location semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a location of a device (e.g. an outdoor temperature sensor).

| ID   | Namespace       |
|------|-----------------|
| 0x06 | Common Location |

| ID   | Name    | Summary                                                                                                     |
|------|---------|-------------------------------------------------------------------------------------------------------------|
| 0x00 | Indoor  | Element is indoors or related to<br>indoor equipment/conditions<br>(e.g. the "indoor" temperature).         |
| 0x01 | Outdoor | Element is outdoors or related<br>to outdoor equipment/condi<br>tions (e.g. the "outdoor" temper<br>ature). |
| 0x02 | Inside  | Element is located inside the<br>equipment (e.g. a sensor<br>"inside" a cabinet).                           |
| 0x03 | Outside | Element is located outside the<br>equipment (e.g. a sensor "out<br>side" a cabinet).                        |
| 0x04 | Zone    | Element is a part of a location<br>divided into zones (e.g. a yard<br>irrigation zone).                     |

### <span id="page-26-0"></span>**Chapter 8. Common Number Semantic Tag Namespace**

This section contains the Common Number semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a certain numeric feature of a device (e.g. a numeric input button).

| ID   | Namespace     |
|------|---------------|
| 0x07 | Common Number |

| ID   | Name      | Summary |
|------|-----------|---------|
| 0x00 | Zero      |         |
| 0x01 | One       |         |
| 0x02 | Two       |         |
| 0x03 | Three     |         |
| 0x04 | Four      |         |
| 0x05 | Five      |         |
| 0x06 | Six       |         |
| 0x07 | Seven     |         |
| 0x08 | Eight     |         |
| 0x09 | Nine      |         |
| 0x0A | Ten       |         |
| 0x0B | Eleven    |         |
| 0x0C | Twelve    |         |
| 0x0D | Thirteen  |         |
| 0x0E | Fourteen  |         |
| 0x0F | Fifteen   |         |
| 0x10 | Sixteen   |         |
| 0x11 | Seventeen |         |
| 0x12 | Eighteen  |         |
| 0x13 | Nineteen  |         |
| 0x14 | Twenty    |         |
| 0x15 | TwentyOne |         |

| ID   | Name        | Summary |
|------|-------------|---------|
| 0x16 | TwentyTwo   |         |
| 0x17 | TwentyThree |         |
| 0x18 | TwentyFour  |         |
| 0x19 | TwentyFive  |         |
| 0x1A | TwentySix   |         |
| 0x1B | TwentySeven |         |
| 0x1C | TwentyEight |         |
| 0x1D | TwentyNine  |         |
| 0x1E | Thirty      |         |

### <span id="page-28-0"></span>**Chapter 9. Common Position Semantic Tag Namespace**

This section contains the Common Position semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a position relative to the device (e.g. the temperature sensor in the top drawer of a refrigerator, or location of the buttons on a multi-button switch device). Note the difference with [Chapter](#page-20-0) [5,](#page-20-0) *[Common Direction Semantic Tag Namespace](#page-20-0)*.

| ID   | Namespace       |
|------|-----------------|
| 0x08 | Common Position |

The following tags are defined in this namespace.

| ID   | Name   | Summary                                  |
|------|--------|------------------------------------------|
| 0x00 | Left   |                                          |
| 0x01 | Right  |                                          |
| 0x02 | Top    |                                          |
| 0x03 | Bottom |                                          |
| 0x04 | Middle |                                          |
| 0x05 | Row    | Numeric value provided in<br>Label field |
| 0x06 | Column | Numeric value provided in<br>Label field |

When multiple endpoints are used for device types, and the associated consumer-facing locations of those endpoints are organized in a straight line, grid or matrix, these endpoints SHOULD be allocated in top-to-bottom, left-to-right order.

For grids or arrays larger than 3 elements in any direction, the Row and Column tags SHOULD be used.

If the Row or Column tags are used, the Label field in the same Semantic Tag structure SHALL be filled with a number comprised of Arabic numerals encoded as a string to indicate the row/column of the item. Number words (e.g. "one", "two", etc.) SHALL NOT be used to describe the position of the item. The first row/column SHALL use Label "1".

#### <span id="page-28-1"></span>**9.1. Examples**

The following example illustrates a compound device comprised of 9 endpoints arranged in a 3x3 grid. This example uses position tags to indicate position.

| compound device arranged in a 3x3 grid |      |        |        |        |       |
|----------------------------------------|------|--------|--------|--------|-------|
| Top                                    | Left | Top    | Middle | Top    | Right |
| Middle                                 | Left | Middle |        | Middle | Right |
| Bottom                                 | Left | Bottom | Middle | Bottom | Right |

The endpoints would be populated in this order (showing the TagList in their Descriptor cluster):

- EP 21: Top Left
- EP 22: Top Middle
- EP 23: Top Right
- EP 24: Middle Left
- EP 25: Middle
- EP 26: Middle Right
- EP 27: Bottom Left
- EP 28: Bottom Middle
- EP 29: Bottom Right

The following example illustrates a compound device comprised of 8 endpoints arranged in a 2x4 grid. This example uses the Row and Column tags along with Arabic numeral Labels to indicate position.

| Row "1" Column "1" | Row "1" Column "2" | Row "1" Column "3" | Row "1" Column "4" |
|--------------------|--------------------|--------------------|--------------------|
| Row "2" Column "1" | Row "2" Column "2" | Row "2" Column "3" | Row "2" Column "4" |

The endpoints would be populated in this order (showing the TagList in their Descriptor cluster):

- EP 31: {Row, "1"}, {Column, "1"}
- EP 32: {Row, "1"}, {Column, "2"}
- EP 33: {Row, "1"}, {Column, "3"}
- EP 34: {Row, "1"}, {Column, "4"}
- EP 35: {Row, "2"}, {Column, "1"}
- EP 36: {Row, "2"}, {Column, "2"}
- EP 37: {Row, "2"}, {Column, "3"}
- EP 38: {Row, "2"}, {Column, "4"}

### <span id="page-30-0"></span>**Chapter 10. Electrical Measurement Semantic Tag Namespace**

This section contains the standard semantic tag namespace for electrical measurement as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the electrical measurement domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace              |
|------|------------------------|
| 0x0A | Electrical Measurement |

| ID   | Name     | Summary                                                                                                                                      |
|------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00 | DC       | Indicates values measured for a<br>DC load                                                                                                   |
| 0x01 | AC       | Indicates values measured for a<br>single-phase AC load, or values<br>measured for the collective load<br>on a polyphase AC power sup<br>ply |
| 0x02 | ACPhase1 | Indicates values measured for<br>an AC load on phase 1 of a<br>polyphase power supply                                                        |
| 0x03 | ACPhase2 | Indicates values measured for<br>an AC load on phase 2 of a<br>polyphase power supply                                                        |
| 0x04 | ACPhase3 | Indicates values measured for<br>an AC load on phase 3 of a<br>polyphase power supply                                                        |

### <span id="page-32-0"></span>**Chapter 11. Commodity Tariff Chronology Semantic Tag Namespace**

This section contains the standard semantic tag namespace for the chronological order of Commodity Tariffs as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the energy calendar domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace                   |
|------|-----------------------------|
| 0x0B | Commodity Tariff Chronology |

| ID   | Name     | Summary                                      |
|------|----------|----------------------------------------------|
| 0x00 | Current  | Represents the current Com<br>modity Tariff  |
| 0x01 | Previous | Represents the previous Com<br>modity Tariff |
| 0x02 | Upcoming | Represents the upcoming Com<br>modity Tariff |

### <span id="page-34-0"></span>**Chapter 12. Commodity Tariff Commodity Semantic Tag Namespace**

This section contains the standard semantic tag namespace for Commodity Tariff commodities as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the Commodity Tariff commodity domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace                  |
|------|----------------------------|
| 0x0D | Commodity Tariff Commodity |

| ID   | Name             | Summary |
|------|------------------|---------|
| 0x00 | ElectricalEnergy |         |

### <span id="page-36-0"></span>**Chapter 13. Laundry Semantic Tag Namespace**

This section contains the standard semantic tag namespace for laundry as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the laundry domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace |
|------|-----------|
| 0x0E | Laundry   |

| ID   | Name     | Summary |
|------|----------|---------|
| 0x00 | Normal   |         |
| 0x01 | LightDry |         |
| 0x02 | ExtraDry |         |
| 0x03 | NoDry    |         |

# <span id="page-38-0"></span>**Chapter 14. Power Source Semantic Tag Namespace**

This section contains the standard semantic tag namespace for power sources as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the power source domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace    |
|------|--------------|
| 0x0F | Power Source |

The following tags are defined in this namespace.

| ID   | Name    | Summary                                                                              |
|------|---------|--------------------------------------------------------------------------------------|
| 0x00 | Unknown | The Power Source cluster is<br>related to power provided from<br>an unknown source   |
| 0x01 | Grid    | The Power Source cluster is<br>related to power provided from<br>the electrical grid |
| 0x02 | Solar   | The Power Source cluster is<br>related to power provided from<br>a solar panel array |
| 0x03 | Battery | The Power Source cluster is<br>related to power provided from<br>a battery           |
| 0x04 | EV      | The Power Source cluster is<br>related to power provided from<br>an electric vehicle |

#### <span id="page-38-1"></span>**14.1. Grid Tag**

Power Source clusters with this tag SHALL implement the WIRED feature.

#### <span id="page-38-2"></span>**14.2. Solar Tag**

Power Source clusters with this tag SHALL implement the WIRED feature.

#### <span id="page-38-3"></span>**14.3. Battery Tag**

Power Source clusters with this tag SHALL implement the BAT feature.

#### <span id="page-39-0"></span>**14.4. EV Tag**

Power Source clusters with this tag SHALL implement the BAT feature.

### <span id="page-40-0"></span>**Chapter 15. Common Area Semantic Tag Namespace**

This section contains the Common Area semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with an indoor or outdoor area of a home.

| ID   | Namespace             |
|------|-----------------------|
| 0x10 | Common Area Namespace |

| ID   | Name          | Summary                                                         |
|------|---------------|-----------------------------------------------------------------|
| 0x00 | Aisle         |                                                                 |
| 0x01 | Attic         |                                                                 |
| 0x02 | BackDoor      |                                                                 |
| 0x03 | BackYard      |                                                                 |
| 0x04 | Balcony       |                                                                 |
| 0x05 | Ballroom      |                                                                 |
| 0x06 | Bathroom      | Also known as Restroom                                          |
| 0x07 | Bedroom       |                                                                 |
| 0x08 | Border        |                                                                 |
| 0x09 | Boxroom       | A small room typically used for<br>storage                      |
| 0x0A | BreakfastRoom |                                                                 |
| 0x0B | Carport       |                                                                 |
| 0x0C | Cellar        |                                                                 |
| 0x0D | Cloakroom     |                                                                 |
| 0x0E | Closet        | A small room for storing cloth<br>ing, linens, and other items. |
| 0x0F | Conservatory  |                                                                 |
| 0x10 | Corridor      |                                                                 |
| 0x11 | CraftRoom     |                                                                 |
| 0x12 | Cupboard      |                                                                 |
| 0x13 | Deck          |                                                                 |

| ID   | Name          | Summary                                                                           |
|------|---------------|-----------------------------------------------------------------------------------|
| 0x14 | Den           | A small, comfortable room for<br>individual activities such as<br>work or hobbies |
| 0x15 | Dining        |                                                                                   |
| 0x16 | DrawingRoom   |                                                                                   |
| 0x17 | DressingRoom  |                                                                                   |
| 0x18 | Driveway      |                                                                                   |
| 0x19 | Elevator      |                                                                                   |
| 0x1A | Ensuite       | A bathroom directly accessible<br>from a bedroom                                  |
| 0x1B | Entrance      |                                                                                   |
| 0x1C | Entryway      |                                                                                   |
| 0x1D | FamilyRoom    |                                                                                   |
| 0x1E | Foyer         |                                                                                   |
| 0x1F | FrontDoor     |                                                                                   |
| 0x20 | FrontYard     |                                                                                   |
| 0x21 | GameRoom      |                                                                                   |
| 0x22 | Garage        |                                                                                   |
| 0x23 | GarageDoor    |                                                                                   |
| 0x24 | Garden        |                                                                                   |
| 0x25 | GardenDoor    |                                                                                   |
| 0x26 | GuestBathroom | Also known as Guest Restroom                                                      |
| 0x27 | GuestBedroom  |                                                                                   |
| 0x28 | Reserved28    | Deprecated: was Guest<br>Restroom; use 0x26 Guest Bath<br>room                    |
| 0x29 | GuestRoom     | Also known as Guest Bedroom                                                       |
| 0x2A | Gym           |                                                                                   |
| 0x2B | Hallway       |                                                                                   |
| 0x2C | HearthRoom    | A cozy room containing a fire<br>place or other point heat source                 |
| 0x2D | KidsRoom      |                                                                                   |
| 0x2E | KidsBedroom   |                                                                                   |
| 0x2F | Kitchen       |                                                                                   |

| ID   | Name            | Summary                                                                            |
|------|-----------------|------------------------------------------------------------------------------------|
| 0x30 | Reserved30      | Deprecated: was Larder; use<br>0x3D Pantry                                         |
| 0x31 | LaundryRoom     |                                                                                    |
| 0x32 | Lawn            |                                                                                    |
| 0x33 | Library         |                                                                                    |
| 0x34 | LivingRoom      |                                                                                    |
| 0x35 | Lounge          |                                                                                    |
| 0x36 | MediaTvRoom     |                                                                                    |
| 0x37 | MudRoom         | A space used to remove soiled<br>garments prior to entering the<br>domicile proper |
| 0x38 | MusicRoom       |                                                                                    |
| 0x39 | Nursery         |                                                                                    |
| 0x3A | Office          |                                                                                    |
| 0x3B | OutdoorKitchen  |                                                                                    |
| 0x3C | Outside         |                                                                                    |
| 0x3D | Pantry          | AKA a larder, a place where<br>food is stored                                      |
| 0x3E | ParkingLot      |                                                                                    |
| 0x3F | Parlor          |                                                                                    |
| 0x40 | Patio           |                                                                                    |
| 0x41 | PlayRoom        |                                                                                    |
| 0x42 | PoolRoom        | A room centered around a<br>pool/billiards table                                   |
| 0x43 | Porch           |                                                                                    |
| 0x44 | PrimaryBathroom |                                                                                    |
| 0x45 | PrimaryBedroom  |                                                                                    |
| 0x46 | Ramp            |                                                                                    |
| 0x47 | ReceptionRoom   |                                                                                    |
| 0x48 | RecreationRoom  |                                                                                    |
| 0x49 | Reserved49      | Deprecated: was Restroom; use<br>0x06 Bathroom                                     |
| 0x4A | Roof            |                                                                                    |
| 0x4B | Sauna           |                                                                                    |

| ID   | Name         | Summary                                                                                            |
|------|--------------|----------------------------------------------------------------------------------------------------|
| 0x4C | Scullery     | A utility space for cleaning<br>dishes and laundry                                                 |
| 0x4D | SewingRoom   |                                                                                                    |
| 0x4E | Shed         |                                                                                                    |
| 0x4F | SideDoor     |                                                                                                    |
| 0x50 | SideYard     |                                                                                                    |
| 0x51 | SittingRoom  |                                                                                                    |
| 0x52 | Snug         | An informal space meant to be<br>'cozy', 'snug', relaxed, meant to<br>share with family or friends |
| 0x53 | Spa          |                                                                                                    |
| 0x54 | Staircase    |                                                                                                    |
| 0x55 | SteamRoom    |                                                                                                    |
| 0x56 | StorageRoom  |                                                                                                    |
| 0x57 | Studio       |                                                                                                    |
| 0x58 | Study        |                                                                                                    |
| 0x59 | SunRoom      |                                                                                                    |
| 0x5A | SwimmingPool |                                                                                                    |
| 0x5B | Terrace      |                                                                                                    |
| 0x5C | UtilityRoom  |                                                                                                    |
| 0x5D | Ward         | The innermost area of a large<br>home                                                              |
| 0x5E | Workshop     |                                                                                                    |
| 0x5F | Toilet       | A room dedicated to a toilet; a<br>water closet / WC                                               |

### <span id="page-44-0"></span>**Chapter 16. Common Landmark Semantic Tag Namespace**

This section contains the Common Landmark semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a home landmark.

| ID   | Namespace                 |
|------|---------------------------|
| 0x11 | Common Landmark Namespace |

| ID   | Name           | Summary |
|------|----------------|---------|
| 0x00 | AirConditioner |         |
| 0x01 | AirPurifier    |         |
| 0x02 | BackDoor       |         |
| 0x03 | BarStool       |         |
| 0x04 | BathMat        |         |
| 0x05 | Bathtub        |         |
| 0x06 | Bed            |         |
| 0x07 | Bookshelf      |         |
| 0x08 | Chair          |         |
| 0x09 | ChristmasTree  |         |
| 0x0A | CoatRack       |         |
| 0x0B | CoffeeTable    |         |
| 0x0C | CookingRange   |         |
| 0x0D | Couch          |         |
| 0x0E | Countertop     |         |
| 0x0F | Cradle         |         |
| 0x10 | Crib           |         |
| 0x11 | Desk           |         |
| 0x12 | DiningTable    |         |
| 0x13 | Dishwasher     |         |
| 0x14 | Door           |         |
| 0x15 | Dresser        |         |

| ID   | Name           | Summary                                                                                                                 |
|------|----------------|-------------------------------------------------------------------------------------------------------------------------|
| 0x16 | LaundryDryer   |                                                                                                                         |
| 0x17 | Fan            |                                                                                                                         |
| 0x18 | Fireplace      |                                                                                                                         |
| 0x19 | Freezer        |                                                                                                                         |
| 0x1A | FrontDoor      |                                                                                                                         |
| 0x1B | HighChair      |                                                                                                                         |
| 0x1C | KitchenIsland  |                                                                                                                         |
| 0x1D | Lamp           |                                                                                                                         |
| 0x1E | LitterBox      |                                                                                                                         |
| 0x1F | Mirror         |                                                                                                                         |
| 0x20 | Nightstand     |                                                                                                                         |
| 0x21 | Oven           |                                                                                                                         |
| 0x22 | PetBed         |                                                                                                                         |
| 0x23 | PetBowl        |                                                                                                                         |
| 0x24 | PetCrate       | An indoor furnishing for pets to<br>rest or sleep inside                                                                |
| 0x25 | Refrigerator   |                                                                                                                         |
| 0x26 | ScratchingPost |                                                                                                                         |
| 0x27 | ShoeRack       |                                                                                                                         |
| 0x28 | Shower         | An area where a showerhead<br>dispenses water for people to<br>shower                                                   |
| 0x29 | SideDoor       |                                                                                                                         |
| 0x2A | Sink           |                                                                                                                         |
| 0x2B | Sofa           |                                                                                                                         |
| 0x2C | Stove          |                                                                                                                         |
| 0x2D | Table          |                                                                                                                         |
| 0x2E | Toilet         |                                                                                                                         |
| 0x2F | TrashCan       |                                                                                                                         |
| 0x30 | LaundryWasher  |                                                                                                                         |
| 0x31 | Window         |                                                                                                                         |
| 0x32 | WineCooler     | A type of refrigerator that is<br>shelved to hold wine bottles<br>and (typically) display them<br>through a glass front |

### <span id="page-46-0"></span>**Chapter 17. Common Relative Position Semantic Tag Namespace**

This section contains the Common Relative Position semantic tag namespace as part of the semantic tag feature.

The tags contained in this namespace MAY be used in any domain or context, to indicate an association with a position relative to some reference, which must be specified by the user of these tags. For example, the position may be relative to a household item, such as a dining table, and the user of these tags must indicate that. Note the difference with [Chapter 9,](#page-28-0) *[Common Position Semantic Tag](#page-28-0) [Namespace](#page-28-0)*, which contains tags indicating the position relative to the device.

| ID   | Namespace                |
|------|--------------------------|
| 0x12 | Common Relative Position |

| ID   | Name    | Summary                                         |
|------|---------|-------------------------------------------------|
| 0x00 | Under   |                                                 |
| 0x01 | NextTo  | Area in proximity to the point<br>of reference  |
| 0x02 | Around  | The area surrounding the point<br>the reference |
| 0x03 | On      |                                                 |
| 0x04 | Above   |                                                 |
| 0x05 | FrontOf |                                                 |
| 0x06 | Behind  |                                                 |

# <span id="page-48-0"></span>**Chapter 18. Commodity Tariff Flow Semantic Tag Namespace**

This section contains the standard semantic tag namespace for Commodity Tariff flow as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the Commodity Tariff flow domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace             |
|------|-----------------------|
| 0x13 | Commodity Tariff Flow |

| ID   | Name   | Summary |
|------|--------|---------|
| 0x00 | Import |         |
| 0x01 | Export |         |

# <span id="page-50-0"></span>**Chapter 19. Refrigerator Semantic Tag Namespace**

This section contains the standard semantic tag namespace for refrigerators as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the refrigerator domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace    |
|------|--------------|
| 0x41 | Refrigerator |

| ID   | Name         | Summary |
|------|--------------|---------|
| 0x00 | Refrigerator |         |
| 0x01 | Freezer      |         |

# <span id="page-52-0"></span>**Chapter 20. Room Air Conditioner Semantic Tag Namespace**

This section contains the standard semantic tag namespace for room air conditioners as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the room air conditioner domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace            |
|------|----------------------|
| 0x42 | Room Air Conditioner |

| ID   | Name       | Summary |
|------|------------|---------|
| 0x00 | Evaporator |         |
| 0x01 | Condenser  |         |

### <span id="page-54-0"></span>**Chapter 21. Switches Semantic Tag Namespace**

This section contains the standard semantic tag namespace for switches as part of the [semantic tag](#page-12-1) feature.

The tags contained in this namespace are restricted for use in the switches domain and SHALL NOT be used in any other domain or context. They are intended to indicate the function of a button on a switch device to allow a client to make an optimized user interface which matches the actual device without requiring a-priori knowledge of the layout of each specific switch device.

See the rules for applying these and other tags for switch devices, e.g. from the Common Position Namespace and the Common Number Namespace in the Generic Switch device type section in the Device Library.

| ID   | Namespace |
|------|-----------|
| 0x43 | Switches  |

The following tags are defined in this namespace.

| ID                                             | Name          | Summary                                        |  |  |
|------------------------------------------------|---------------|------------------------------------------------|--|--|
| tags to identify intended function of a button |               |                                                |  |  |
| 0x00                                           | On            |                                                |  |  |
| 0x01                                           | Off           |                                                |  |  |
| 0x02                                           | Toggle        |                                                |  |  |
| 0x03                                           | Up            | e.g. dim up (light)                            |  |  |
| 0x04                                           | Down          | e.g. dim down (light)                          |  |  |
| 0x05                                           | Next          | e.g. select next scene                         |  |  |
| 0x06                                           | Previous      | e.g. select previous scene                     |  |  |
| 0x07                                           | EnterOkSelect | Enter/OK/Select function                       |  |  |
| 0x08                                           | Custom        | Textual description provided in<br>Label field |  |  |
| 0x09                                           | Open          | e.g. open window covering                      |  |  |
| 0x0A                                           | Close         | e.g. close window covering                     |  |  |
| 0x0B                                           | Stop          | e.g. stop moving window cover<br>ing           |  |  |

#### <span id="page-54-1"></span>**21.1. Custom Tag**

When this value is used, the Label field in the same Semantic Tag structure SHALL be filled with a textual description of the function indicated on the button, such as a label or icon printed on the

| Matter Standard Namespaces | Connectivity Standards Alliance Document 23-31936 March 16, 2026 |
|----------------------------|------------------------------------------------------------------|
|----------------------------|------------------------------------------------------------------|

button, e.g. "dining".

### <span id="page-56-0"></span>**Chapter 22. Closure Semantic Tag Namespace**

This section contains the standard semantic tag namespace for closures as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the closure domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace |
|------|-----------|
| 0x44 | Closure   |

| ID   | Name       | Summary                                                                                                                                                                    |
|------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00 | Covering   | Any material or treatment used<br>to cover a window for privacy,<br>light control, insulation, or dec<br>oration.                                                          |
| 0x01 | Window     | An opening in a wall, door, or<br>roof fitted with glass or another<br>transparent material to allow<br>light, air, and views while pro<br>viding insulation and security. |
| 0x02 | Barrier    | A physical or conceptual<br>obstruction that prevents move<br>ment, access, or progress that<br>serve purposes such as security,<br>safety, privacy, control, etc.         |
| 0x03 | Cabinet    | A storage unit with shelves,<br>drawers, or doors, used for<br>organizing and protecting<br>items.                                                                         |
| 0x04 | Gate       | A movable barrier that controls<br>entry or exit through an open<br>ing in a fence, wall, or enclo<br>sure.                                                                |
| 0x05 | GarageDoor | A large, movable barrier that<br>provides access to a garage.                                                                                                              |
| 0x06 | Door       | A movable barrier that allows<br>entry and exit between spaces<br>while providing security, pri<br>vacy, and insulation.                                                   |

# <span id="page-58-0"></span>**Chapter 23. Closure Panel Semantic Tag Namespace**

This section contains the standard semantic tag namespace for closure panels as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the closure panel domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace     |
|------|---------------|
| 0x45 | Closure Panel |

| ID   | Name    | Summary                                                                                                                             |
|------|---------|-------------------------------------------------------------------------------------------------------------------------------------|
| 0x00 | Lift    | Refers to the upward or down<br>ward motion of an object, typi<br>cally along a vertical axis.                                      |
| 0x01 | Tilt    | Refers to the action of rotating<br>or tilting an object or surface<br>along a horizontal or vertical<br>axis.                      |
| 0x02 | Sliding | Refers to the smooth, horizontal<br>motion of an object along an<br>axis, where the object moves<br>back and forth or side to side. |
| 0x03 | Rotate  | Refers to the circular motion of<br>an object around a fixed point<br>or axis, typically in a circular<br>motion.                   |

# <span id="page-60-0"></span>**Chapter 24. Closure Covering Semantic Tag Namespace**

This section contains the standard semantic tag namespace for closure coverings as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the closure domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace        |
|------|------------------|
| 0x46 | Closure Covering |

| ID   | Name     | Summary                                                                                                                                                       |
|------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00 | Blind    | A covering made of horizontal<br>or vertical slats that can be<br>adjusted to control light, pri<br>vacy, and airflow.                                        |
| 0x01 | Awning   | A protective covering, typically<br>made of fabric or metal, that<br>extends from a building's exte<br>rior to provide shade or shelter<br>from the elements. |
| 0x02 | Shutter  | A hinged or sliding covering<br>typically made of wood, metal,<br>or vinyl, used to provide pri<br>vacy, security, and light control.                         |
| 0x03 | Venetian | A type of covering consisting of<br>horizontal slats that can be<br>adjusted to control light, pri<br>vacy, and airflow.                                      |
| 0x04 | Curtain  | A piece of fabric hung over a<br>window to provide privacy,<br>block light, or enhance the<br>room's embellishment.                                           |

### <span id="page-62-0"></span>**Chapter 25. Closure Window Semantic Tag Namespace**

This section contains the standard semantic tag namespace for closure windows as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the closure domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace      |
|------|----------------|
| 0x47 | Closure Window |

| ID   | Name   | Summary                                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------------------|
| 0x00 | Roof   | A window installed in a roof to<br>provide natural light, ventila<br>tion, and sometimes access to<br>the roof.            |
| 0x01 | Facade | A window installed in the verti<br>cal exterior wall of a building. It<br>allows natural light, ventilation,<br>and views. |

# <span id="page-64-0"></span>**Chapter 26. Closure Cabinet Semantic Tag Namespace**

This section contains the standard semantic tag namespace for closure cabinets as part of the semantic tag feature.

The tags contained in this namespace are restricted for use in the closure domain and SHALL NOT be used in any other domain or context.

| ID   | Namespace       |
|------|-----------------|
| 0x48 | Closure Cabinet |

| ID   | Name        | Summary                                                                                                        |
|------|-------------|----------------------------------------------------------------------------------------------------------------|
| 0x00 | CabinetDoor | A hinged or sliding panel used<br>to cover the opening of a cabi<br>net, providing access to its inte<br>rior. |
| 0x01 | Drawer      | A sliding storage compartment,<br>typically built into furniture<br>like cabinets, desks, or dressers.         |
| 0x02 | Flap        | A hinged front or flexible cover<br>that can be lifted or moved, pro<br>viding access to its interior.         |