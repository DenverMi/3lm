# Qualification Program Reference Document

Abstract

This Qualification Program Reference Document (QPRD, as referred to in the Bylaws), contains the Compliance Requirements (as referred to in the Bluetooth Patent/Copyright License Agreement (PCLA)), the Bluetooth Qualification Process (as referred to in the Bluetooth Patent/Copyright License and Bluetooth Trademark License), and
policies and procedures for Qualified Product database management. This document supersedes the Compliance Requirements in Volume 0, Part B, Section 3 of the Bluetooth*®* Core Specification Version 5.4 and each earlier version of the Bluetooth Core Specification, the Qualification Program
Reference Document Version 2.3, and the Declaration Process Document Version 1.0.

* 1. Introduction
+ 1.1. Definitions
* 2. Compliance Requirements
* 3. The Bluetooth Qualification Process
+ 3.1. Provide Product details
+ 3.2. Specify the Design
- 3.2.1. Option 1: Use a single existing Design
- 3.2.2. Option 2: Create a new Design
* 3.2.2.1. Option 2a: Create a new Design that combines multiple existing Designs
* 3.2.2.2. Option 2b: Create any other new Design
* 3.2.2.3. Complete the consistency check
* 3.2.2.4. Generate test plan
* 3.2.2.5. Complete testing, test declaration, and test report(s)
+ 3.3. Pay an administrative fee
+ 3.4. Submission
- 3.4.1. Compliance Folder
+ 3.5. Verification
* 4. Qualified Product database
* 5. Acronyms and abbreviations
* 6. References
* A. Test requirements
+ A.1. Test case category
+ A.2. Test declaration
+ A.3. Test report
* B. TCW policy
+ B.1. Handling TCWs when errors in a validated Test System are encountered
- B.1.1. Multiple validated Test Systems referenced in the test plan
- B.1.2. Only one validated Test System referenced in the test plan

* Version: v5
* Version Date: 2026-04-21
* Feedback Email: bqrb-feedback@bluetooth.org

## *Version History*

| Version Number | Date (yyyy-mm-dd) | Comments |
| v1.0 | 2002-02-07 | The initial Qualification Program Reference Document |
| v2.1 | 2008-03-18 | Approved by the Bluetooth SIG Board of Directors. |
| v2.3 | 2014-05-01 | Approved by the Bluetooth SIG Board of Directors. |
| v3 | 2024-06-11 | Approved by the Bluetooth SIG Board of Directors. |
| v4 | 2025-07-21 | Approved by the Bluetooth SIG Board of Directors. |
| v5 | 2026-04-21 | Approved by the Bluetooth SIG Board of Directors. |

## *Acknowledgements*

| Name | Company |
| Alicia Courtney | Broadcom Corporation |
| Chris Church | Qualcomm Technologies, Inc. |
| Clive Feather | Samsung Cambridge Solution Centre |
| Magnus Sommansson | Qualcomm Technologies, Inc. |
| Miles Smith | Nordic Semiconductor ASA |
| Shirin Ebrahimi-Taghizadeh | Microsoft Corporation |
| Theodora Dimitropoulou | Renesas Electronics Corporation |
| Toby Nixon | Microsoft Corporation |
| Zhiwei Zhang | China Academy of Information and Communications Technology |
| Mark Powell | Bluetooth SIG |
| Denise Montoya | Bluetooth SIG |
| Lewis Chan | Bluetooth SIG |
| Joshua Graham | Bluetooth SIG |

**This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other
related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.**

**THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE
CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.**

**TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR
FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.**

**This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its
members.**

**This document is subject to change without notice.**

**Copyright © 2024–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.**

## 1. Introduction

This document contains the Compliance Requirements and specifies the Bluetooth Qualification Process, including the policies and procedures for Qualified Product database management.

Table 1.1 defines the terms used in this document. Unless another document expressly references this document and incorporates a term defined in this section,
these definitions do not apply and should not be used to interpret any other document published by the Bluetooth SIG.

### 1.1. Definitions

| Term | Definition |
| Bluetooth Qualification Test Facility (BQTF) | An accredited test facility that can perform testing and produce test results for any Member, and Bluetooth SIG will accept the results for the purposes of the Bluetooth Qualification Process. For more information about BQTFs, see the BQTF and BRTF Program Overview [4]. |
| Bluetooth Recognized Test Facility (BRTF) | An accredited test facility that can perform testing and produce test results for itself, and Bluetooth SIG will accept the results for purposes of the Bluetooth Qualification Process. For more information about BRTFs, see the BQTF and BRTF Program Overview [4]. |
| Bluetooth SIG | As defined in the Bylaws of Bluetooth SIG Inc., Section 1.1 [3] |
| Bluetooth Specifications | All specifications and updates to specifications adopted in accordance with the Bylaws of Bluetooth SIG [3] |
| Complete Layer | An implementation contains a complete layer if the implementation includes, for that layer, all mandatory features, all the mandatory elements of any optional feature that is included, and any features that are conditionally required. See Volume 0, Part D, Section 1 of the Bluetooth Core Specification for more information. |
| Compliance Folder | Documentation maintained by the Member to demonstrate that a Product meets all requirements of the Bluetooth Qualification Process, as further described in Section 3.4.1 |
| Core Configuration | As defined in Volume 0, Part D, Section 2 of the Bluetooth Core Specification, where also the following terms, used in this document, are specified: Core-Complete Configuration, Core-Controller Configuration, and Core-Host Configuration |
| Core Layer | Any layer as defined in Volume 0, Part D, Section 2 of the Bluetooth Core Specification |
| Design | An implementation of one or more Bluetooth Specifications |
| Design Number (DN) | A reference number issued for each unique Design that is issued the first time a Product using that Design completes the Bluetooth Qualification Process. |
| Implementation Conformance Statement (ICS) | The document produced by the Bluetooth SIG for each Bluetooth Specification that identifies the features of that Bluetooth Specification. |
| ICS Form | The form completed by a Member for each Design to identify all features of the Bluetooth Specifications in that Design. |
| Implementation eXtra Information for Testing (IXIT) | The form completed by a Member that provides additional configuration details to facilitate testing beyond supported features defined in the ICS, as defined in the Test Strategy and Terminology Overview (TSTO) [7]. |
| Layer | Core Layers and X2Core Layers are all layers. |
| Member | An entity who has executed the Bluetooth SIG’s membership agreements and has not withdrawn their membership or otherwise had their membership terminated. |
| Product | Includes only one Design, is sold as a single item, and is marketed under a name or trademark that uniquely identifies the Member who is the source of the product |
| Inter-Layer Dependency (ILD) | A Bluetooth Specification requirement in one Layer that is dependent on one or more features or elements of a feature implemented in another Layer. For more information, see the TSTO [7]. |
| Interoperability Testing (IOPT) | A collection of test cases, based on the ICS Form for the Design intended to verify interoperability for X2Core Layers |
| Product Publication Date | The date requested by the Member, when the Qualified Product details are visible to the public and other Members in the Qualified Product database, which may not be later than 180 days after submission. |
| Product Qualification Date | The date that the Bluetooth SIG notifies the Member that the Product has successfully completed the Bluetooth Qualification Process. |
| Qualified Product | A Product that has successfully completed the Bluetooth Qualification Process. |
| Receipt Number | A unique reference number issued as proof of payment of an administrative fee paid by a Member to complete the Bluetooth Qualification Process. |
| TCRL Package | The collection of files maintained by Bluetooth SIG that contains all the TCRLs for all active Bluetooth Specifications. |
| Test Case Reference List (TCRL) | For each Bluetooth Specification, the sheet within the TCRL Package that identifies the applicable versions of the TS and ICS to be used in the Bluetooth Qualification Process for Designs that implement that Bluetooth Specification. For more information, see the TSTO [7]. |
| Test Coverage Waiver (TCW) | A waiver of one or more Bluetooth Qualification Process requirements granted by Bluetooth SIG. See Appendix B for more information. |
| Test Set Erratum (TSE) | A report that tracks an error in the Bluetooth Qualification Process requirements (including a published test document) and any relevant fixes implemented to resolve the error. For more information on the issue process, see the Issue Process Document (IPD) [8]. |
| Test Suite (TS) | For each Bluetooth Specification, the document that contains the test cases for each Bluetooth Specification. For more information, see the TSTO [7]. |
| Test System | A system to be used by a Member to perform the specific tests as outlined in the test plan. |
| X2Core Layer | A single Bluetooth Specification that is not a Bluetooth Core Specification |

Table 1.1. Definitions

## 2. Compliance Requirements

This section defines the Compliance Requirements referred to in Section 1(i) of the Bluetooth Patent/Copyright License Agreement (PCLA) [1].

Each Member must demonstrate that each Product complies with the Bluetooth® Specification(s), as follows:

* Identify the Product, the Design included in the Product, the Bluetooth Specifications that the Design implements, and each of the features of each Bluetooth Specification that the Design implements.
* Complete the Bluetooth Qualification Process (see Section 3).

For a Product to complete the Bluetooth Qualification Process, the Member must submit the required documentation for the Product under a Bluetooth SIG user account belonging to the same Member completing the Bluetooth Qualification Process.

Each Member is responsible for ensuring that the information they submit is complete and accurate and their Products comply with the Bluetooth Specifications.

A supplier or other Member cannot complete the Bluetooth Qualification Process for any other company’s Product.

## 3. The Bluetooth Qualification Process

The Bluetooth Qualification Process promotes Product interoperability and reinforces the strength of the Bluetooth® brand and ecosystem to the benefit of all Members.

To complete the Bluetooth Qualification Process, a Product must include a Design that implements at least one Complete Layer.

The Bluetooth Qualification Process consists of the phases shown in Figure 3.1.

| |
| --- |
| |

Figure 3.1. Bluetooth Qualification Process

### 3.1. Provide Product details

For each Product, a Member must provide the following information:

* Product name
* Product description
* Model number
* Product Publication Date
* If the Product will be visible for other users with a user account issued under the same Member to view before the Product Publication Date

A Member may include additional details, such as the Product website.

The Product name and model number provided by the Member during the Bluetooth Qualification Process must match the Product name and model number used by the Member when marketing, advertising, distributing, and selling the Product.

### 3.2. Specify the Design

A Member has several options for specifying the Design.

Members may not specify an existing Design that has a Qualified Design ID (QDID) with the Bluetooth Product type (defined in Volume 0, Part B of the Bluetooth Core Specification Version 5.4 or earlier) Development Tool, Test Equipment, or Component (non-tested).

#### 3.2.1. Option 1: Use a single existing Design

This option applies to a Member qualifying a Product that includes an existing Design that has a DN, QDID, or Declaration ID (DID) and that Design has not been modified (e.g., rebranding a Qualified Product from another Member). The Design identified by the DN, QDID, or DID may only implement Bluetooth Specifications that are
active or deprecated at the time of Submission. No modifications may be made to the Design, including changes to the ICS Form.

Changes to the Product outside the Design are allowed, such as:

* Enabling technologies
* Changes to the industrial design
* Changes to the communication technology other than Bluetooth
* Changes to the features that are unrelated to Bluetooth, branding, packaging, color, shape, Product name, or Model number

Members are responsible for assessing that modifications to the Product outside of the Design do not affect compliance with Bluetooth Specifications or result in a change to the ICS Form.

#### 3.2.2. Option 2: Create a new Design

For each new Design, a Member must provide the following information:

* Design name (Optional, the Bluetooth SIG online tools will default to the Product name if the Member does not specify a Design name)
* If other Members are allowed to include the new Design in their Product (after it has been published in the Qualified Product database)
* If other users with accounts issued under the same Member are allowed to include the new Design in their Product (after it has been published in the Qualified Product database)
* If other Members are allowed to remove optional features from the Design when creating their new Design (This option is only available if the Design does not include a DN or QDID from other Members)

##### 3.2.2.1. Option 2a: Create a new Design that combines multiple existing Designs

For a Product that includes a new Design created by combining two or more unmodified Designs that have DNs or QDIDs into one of the permitted combinations in Table 3.1, a
Member must also provide the following information:

* DNs or QDIDs for Designs included in the new Design
* The desired Core Configuration of the new Design (if applicable, see Table 3.1 below)
* The active TCRL Package version used for checking the applicable Core Configuration (including transport compatibility) and evaluating test requirements

Any included Design must not implement any Layers using withdrawn specification(s).

When creating a new Design using Option 2a, the ILDs between Layers included in the Design will be checked based on the latest TCRL Package version used among the included Designs.

| Permitted Combinations | | | Creating | Requirements | | |
| Design 1 has | Design 2 has | Designs 3+ have (optional, additional Designs) | New Design has | ILD Check | Core Config. Check | IOPT Required for Layers added by |
| Core-Complete­ Configuration | X2Core Layers only | X2Core Layers only | Core-Complete­ Configuration | Requir­ed | Requir­ed | Design 2  and  Design 3+ |
| Core-Controller­ Configuration | Core-Host­ Configuration | - | Core-Complete­ Configuration | Requir­ed | Requir­ed | None |
| Core-Controller­ Configuration | Core-Host­ Configuration | X2Core Layers only | Core-Complete­ Configuration | Requir­ed | Requir­ed | Design 3+ |
| Core-Host­ Configuration­ | X2Core Layers only | X2Core Layers only | Core-Host Configuration | Requir­ed | Not required | Design 2  and  Design 3+ |
| Core-Controller­ Configuration | X2Core Layers implem­enting LC3 spec­ifi­cation only | - | Core-Controller­ Configuration | Requir­ed | Not required | None |
| X2Core Layers only | X2Core Layers only | X2Core Layers only | X2Core Layers only | Requir­ed | Not required | None |

Table 3.1. Permitted Combinations

##### 3.2.2.2. Option 2b: Create any other new Design

A Member must provide the following information:

* DN(s) or QDID(s) for any Design(s) included in the new Design
* An active TCRL Package version
* An ICS Form

An ICS Form is filled out for each new Layer implemented in the new Design and for each modified Layer based on an included Design. The active TCRL Package version must be used for all new and modified Layers. However, if a Layer is modified only by removing optional features and the Design permits such modifications, then the
Member may retain the TCRL Package version used in the included Design (see Section 3.2.2).

A new Design or any included Design must not implement any Layers using withdrawn specification(s). Implemented Layers in a new Design or any included Design using withdrawn specification(s) must be either completely removed or modified to implement an active specification and assessed against the active TCRL Package
version.

For each unmodified Layer from an included Design which does not use withdrawn specification(s), the Member may use the TCRL Package version selected when the included Design completed the Bluetooth Qualification Process or use the active TCRL Package version.

A Member may remove Layer(s) from included Design(s) that are not implemented in the new Design.

A Member must specify the new Design and complete the consistency check before submission.

###### 3.2.2.2.1. Create a subset of a Member’s Design

A Member can use Option 2b to identify that they want to create a subset of their existing Design that has a DN or QDID, provided that the existing Design does not include a DN or QDID from other Members. The subset Design is created by removing one or more Layers or optional features. The subset Design must still meet the
requirements of the same Core Configuration (if applicable). A subset Design cannot add Layers or features, and the TCRL Package versions cannot be changed. All other requirements from Section 3.2.2.2 also apply.

###### 3.2.2.2.2. Reassess Member’s Design

A Member can use Option 2b to identify that they want to reassess their existing Design that has a DN or QDID against an active TCRL Package version. The Member can modify the ICS Form only if any ICS selection changes are caused by the TCRL Package version update. Otherwise, the Member cannot modify the ICS Form or any
other Design details. The reassessed Design must still meet the requirements of the same Core Configuration (if applicable). All other requirements from Section 3.2.2.2 also apply.

##### 3.2.2.3. Complete the consistency check

When a Member creates a new Design, the ICS Form for the new Design must pass the consistency check performed by the tools provided by the Bluetooth SIG.

The consistency check determines whether the ICS Form is consistent with the requirements of the corresponding Bluetooth Specification(s) and any applicable deprecation and withdrawal policies and whether the ICS Form correctly shows support for:

* One or more Complete Layers
* The ILDs between Layers included in the Design, based on the latest TCRL Package version used among the included Designs; for unmodified Layers, only ILDs pointing to ICS that exist in the TCRL Package version from the included Design that completed the Bluetooth Qualification Process are reported
* Applicable Core Configuration (including transport compatibility)

If the Bluetooth SIG tool identifies any inconsistencies, then the Member must address the inconsistencies by correcting the ICS Form so that it passes the consistency check or by providing a TCW that indicates the requirement has been waived before submission (see Section 3.4). If the new Design follows Option 2a, then correction of inconsistencies must be by removal of ICS selections. The Bluetooth SIG tool may assist the Member in resolving the inconsistencies.

##### 3.2.2.4. Generate test plan

If testing is required based on the ICS Form, then the Bluetooth SIG tool will generate a test plan, which includes all test cases for the new and modified Layers and any applicable IOPT test cases. IOPT tests are generated only when one or more of the following conditions are met:

* A new X2Core Layer is added.
* An X2Core Layer from an included Design is either modified or that included Design doesn’t have a Core Configuration.
* Any Core Layer from an included Design is modified.

The generated test plan will be based on the ICS Form and test case mapping table of the TCRL Package version specified by the Member for each Layer.

If a Layer is modified only by removing optional features from a Design provided by a Member who has permitted such removals (see Section 3.2.2), then the test plan will
not include test cases for that Layer. However, any applicable IOPT testing will still be generated.

If no test plan is generated, then the Member will skip testing, test declaration, and test reports (see Section 3.2.2.5")).

##### 3.2.2.5. Complete testing, test declaration, and test report(s)

When a test plan is generated, the Member must:

* Follow the test requirements defined in Appendix A.
* For a Design with one or more new Layers, execute each mandatory test case according to the test case category requirements specified in the test plan.
* Test ILDs between Layers not included in the Product by using the test setup specified in the test plan that supports the Layers not included in the Product (to demonstrate application interoperability as defined in Volume 1, Part A, Section 6 of the Bluetooth Core Specification).
* For a Design that has a DN or QDID with one or more Layers that have been modified and the modification requires a change to the ICS Form, execute each mandatory test case according to the test case category requirements specified in the test plan.
* For a Design that has a DN or QDID with one or more Layers that have been modified, but the modification does not require a change to the ICS Form, use good engineering practices to determine which mandatory test cases are impacted by the modifications and execute those test cases. The Member may use previous test
evidence for non-impacted mandatory test cases. When a Member uses previous test evidence, the Member is still responsible for ensuring that the Design complies with the Bluetooth Specifications.
* Receive a pass verdict for each test case executed, except for test cases where an inconclusive verdict is permitted as defined in the TS.

The active date specified in the test plan is the date the test case takes effect.

In any case where a pass verdict cannot be obtained, then the Member must either:

* Update the Product and successfully complete retesting.
* Provide a TCW for that test case.

If a Member finds an error with the test plan, the test case, or the Test System that is used, then the Member must submit a TSE via the Bluetooth SIG issue system. In this case, it may be possible to waive test requirements by using an approved TCW.

### 3.3. Pay an administrative fee

Members are required to pay an administrative fee to complete the Bluetooth Qualification Process. For administrative fee rules, see the dues and fees [5].

If an administrative fee is required, then the Bluetooth SIG issues a Receipt Number upon payment by the Member. The Member will provide the Receipt Number as proof of payment with their submission. After all necessary documentation is prepared and the administrative fee is paid, then the Member may proceed to submission (see
Section 3.4).

Members who require the Bluetooth SIG to issue an invoice for an administrative fee will need to take into account the additional time it takes to issue an invoice.

### 3.4. Submission

Members use the Bluetooth SIG online tool to upload and submit the required documentation and to sign required declarations and attestations. The declarations and attestations include those regarding accuracy and completeness of information, authority to bind the Member, and agreement to and compliance with policies of and
agreements with the Bluetooth SIG.

| Documentation Submission Requirements | Use a single existing Design (Section 3.2.1) | Create a new Design (Section 3.2.2) |
| Product details | Required (provided in Section 3.1) | Required (provided in Section 3.1) |
| Design details | Required (the DN, QDID or DID is provided in Section 3.2.1) | Required (the DN(s) or QDID(s) are provided in Section 3.2.2.1 or Section 3.2.2.2) |
| ICS Form | N/A | Required (specified in Section 3.2.2.2) |
| Test declaration | N/A | Required (specified in Section 3.2.2.5")) if test plan is generated |
| Test report(s) | N/A | Required (specified in Section 3.2.2.5")) if test plan is generated |
| Receipt Number | See dues and fees [5] | See dues and fees [5] |
| TCW | N/A | Required if TCW is used |
| Declarations and Attestations | Required | Required |

Table 3.2. Documentation submission requirements

#### 3.4.1. Compliance Folder

For all Qualified Products, Members must maintain documentation listed in Table 3.3 in a single location (commonly referred to as the “Compliance Folder”).
Documentation must be stored at the time the Member submits the Product to the Bluetooth Qualification Process and be retained for no less than one year after the Member stops offering the Product for sale or distribution. The Member must make documentation available to the Bluetooth SIG for inspection if requested.

| Compliance Folder Requirements | Use a single existing Design (Section 3.2.1) | Create a new Design (Section 3.2.2) |
| Product details | Required | Required |
| Design details | Required | Required |
| Test declaration | N/A | Required if test plan is generated |
| Test report(s) | N/A | Required if test plan is generated |
| Test logs | N/A | Required if test plan is generated |
| TCW | N/A | As required |

Table 3.3. Compliance Folder requirements

### 3.5. Verification

The Bluetooth SIG will review the submitted materials. Most reviews are approved within one business day. The Bluetooth SIG intends to complete the review of more complex submissions within five business days.

During the verification, the Bluetooth SIG will typically evaluate the following criteria:

* Check that a valid and approved TCW has been provided to address any inconsistencies identified during the consistency check.
* Check that valid test reports are provided by the Member.
* Verify that the Product matches the Core Configuration specified by the Member.

If the submission is approved by the Bluetooth SIG, then the Product has successfully completed the Bluetooth Qualification Process and is a Qualified Product. The Qualified Product will be listed in the Qualified Product database (see Section 4), and the Member will be notified at the user account that made the submission. The Qualified Product will become visible to the public and other Members in the Qualified Product database on the specified Product
Publication Date. The notice will include the Product name and model number from the Member’s submission. If the Product includes a new Design (including subset Design and reassessed Design), then a unique DN will also be assigned to the new Design.

If the submission is rejected by the Bluetooth SIG, then the Product has not successfully completed the Bluetooth Qualification Process, and the Member will be notified at the user account that made the submission and is provided an explanation for rejection. The Member must resolve the reason for rejection before submitting the
materials again.

The following is a non-exhaustive list of examples of why submissions may be rejected by the Bluetooth SIG:

* A Product submission via the “creating a new Design” option may be rejected if:

+ The consistency check indicates that there are inconsistencies and the TCW provided by the Member does not waive the requirement. The Member must correct the ICS Form either by changing the specified Design so that it passes the consistency check or by providing a TCW that waives the corresponding requirement.
+ The test reports are incorrect. The Member must resubmit the Product with corrected test reports.

* A Product submission via the “using a single existing Design” option may be rejected if:

+ The Core Configuration is determined to be incorrect (e.g., a speaker that does not contain a Core-Complete Configuration). The Member may need to contact their supplier to inquire about the correct DN, QDID or DID for the Design or provide an explanation that establishes that their Product has the correct Core
Configuration.

If the Member is not satisfied with the explanation for the rejection, then the Member may appeal the rejection to the Bluetooth SIG by submitting an appeal in writing to qualification.services@bluetooth.com within 30 days of receiving the rejection. The Bluetooth SIG will review the appeal and consult BQRB if it indicates an
error in the Bluetooth Qualification Process. BQRB will help the Bluetooth SIG determine if the appeal should lead to a change to the Bluetooth Qualification Process and any other needed action.

## 4. Qualified Product database

Each Qualified Product will be added to the Qualified Product database. The visibility of the Product details fields is shown in Table 4.1.
The database is accessible via the Bluetooth SIG website.

| Product Detail Fields | Available Information View | | |
| Public `(From Product Publication Date)` | Other Members `(From Product Publication Date)` | All Users Accounts of Member Qualifying the Product `(From Product Qualification Date or Product Publication Date, depending on the selection)` |
| DN of new Design created as part of Product Submission | No | Yes | Yes |
| Member Name | Yes | Yes | Yes |
| Submitted By User Account | No | No | Yes |
| Product Contact | No | No | Yes |
| Product Name | Yes | Yes | Yes |
| Product Website | Yes | Yes | Yes |
| Product Qualification Date | No | Yes | Yes |
| Product Publication Date | No | No | Yes |
| Model Number | Yes | Yes | Yes |
| Product Description | Yes | Yes | Yes |
| Included DN(s) or QDID(s) (if applicable) | No | Yes | Yes |
| Design Name | No | Yes | Yes |
| Design Contact | No | No | Yes |
| Design available for other Members to use | No | Yes | Yes |
| Design available for other users within the same Member to use | No | No | Yes |
| Design available for other Members­ to remove optional features­ | No | Yes | Yes |
| ICS Form and the TCRL Package Version | No | Yes | Yes |

Table 4.1. Qualified Product database fields

Updates to Product details may be possible and the details are in Table 4.2.

| Product Detail or Submission Requirement | Update Method |
| Product Contact | Self-Serve |
| Included DN(s) or QDID(s) (if applicable) | SIG-Assisted\* |
| Design Name | SIG-Assisted |
| Design Contact | SIG-Assisted |
| Design available for other Members to use | SIG-Assisted |
| Design available for other users within the same Member to use | SIG-Assisted |
| Design available for other Members to remove optional features | SIG-Assisted |
| ICS Form and the TCRL Package Version | SIG-Assisted\* |
| Test Declaration | SIG-Assisted\* |
| Test Report | SIG-Assisted\* |

Table 4.2. Qualified Product correction

\*
: If a Member wants to correct these fields, then the Member must request to correct the original submission and submit all necessary materials to complete the Bluetooth Qualification Process for this Product. If the submission is approved, the SIG may notify other users who have included the corrected Design in their
Product.

A Member who identifies an error in the Product Details (i.e., Product name, model number, Product description, Product website, Product Qualification Date, or Product Publication Date) must first qualify a new Product as described in Section 3.2.1 with the corrected information, and then the Member may request that the Bluetooth SIG withdraw the original (incorrect) Product from the Qualified Product database; provided that the original Product has never been sold or distributed.

A Member may request withdrawal of a Product submission if the Product has never been sold or distributed. The request must be in writing to the Bluetooth SIG and contains Product name(s) and model number(s). The Bluetooth SIG will review the request and verify whether it is valid. If the request is not approved, the Bluetooth SIG
will notify the Member. If the withdrawal request is approved by the Bluetooth SIG, the Product will be removed from the Qualified Product database. If the Product is the only Product that uses the Design that was included in the submission, then the Bluetooth SIG will delete the associated DN or QDID for that Design. Other Members
will not be able to include the DN or QDID for their Product. No administrative fee will be refunded.

If a Member transfers ownership of a Qualified Product to another Member as part of a merger or acquisition, then the Member who submitted the Product to the Bluetooth Qualification Process must complete and submit the assignment agreement form [6] to
the Bluetooth SIG.

## 5. Acronyms and abbreviations

| Acronym/Abbreviation | Meaning |
| BQTF | Bluetooth Qualified Test Facility |
| BRTF | Bluetooth Recognized Test Facility |
| BTLA | Bluetooth Trademark License Agreement |
| DID | Declaration ID |
| DN | Design Number |
| HCI | Host Controller Interface (Volume 4, Part E in the Bluetooth Core Specification) |
| ICS | Implementation Conformance Statement |
| IOPT | Interoperability Testing |
| IXIT | Implementation eXtra Information for Testing |
| PCLA | Bluetooth Patent/Copyright License Agreement |
| QDID | Qualified Design ID |
| QPRD | Qualification Program Reference Document |
| TCRL | Test Case Reference List |
| TCW | Test Coverage Waiver |
| TS | Test Suite |
| TSE | Test Set Erratum |
| TSTO | Test Strategy and Terminology Overview |

Table 5.1. Acronyms and abbreviations

## 6. References

[4] Qualification test facilities program overview <https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-test-facilities/qualification-test-facilities-program-overview/>

[5] Dues and fees <https://www.bluetooth.com/fee-schedule/>

[6] Assignment Agreement Form <https://support.bluetooth.com/hc/en-us/article_attachments/27147896287629>

## Appendix A. Test requirements

### A.1. Test case category

| Test Case Category | Test System Requirements | | Performed by | Test Declaration Appendix [A.2] | Test Report Appendix [A.3] |
| Validated[1](#ftn.id3984) | Non-validated or Member-Defined |
| Category A: Mandatory (Test cases in the RF, RFPHY, BB, LL, ISOAL, LMP, and the Lower HCI role Layers) | Allowed | Not allowed | BQTF or BRTF | Required | Required |
| Category A: Mandatory (Test Cases in other Layers) | Allowed | Not allowed | Member or BQTF/BRTF or third party | Required | Required |
| Category B: Mandatory | Allowed | Allowed | Member or BQTF/BRTF or third party | Required | Required |
| Category C: Optional  (Recommended) | Allowed | Allowed | Member or BQTF/BRTF or third party | Required | Not Required­ |
| Category D: Optional  (Informational) | Allowed | Allowed | Member or BQTF/BRTF or third party | If performed, then required | Not Required­ |
| Category X: Optional  (Recommended) These are supplementary interoperability tests aimed at scenarios that do not have a direct specification reference. The tests are recommended by the Bluetooth SIG to be run for improved interoperability, but they are not required to be executed as part of the Bluetooth Qualification Program. | Allowed | Allowed | Member or BQTF/BRTF or third party | If performed, then required | Not Required­ |
| [1](#id3984) Test Systems are validated through the process described in the Test System Validation Process Document [9] | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

Table A.1. Test case category

### A.2. Test declaration

A Member must provide a test declaration by filling out the test plan to include the following:

* Test Case Verdict (pass, inconclusive, waived, or not required)
* Test Execution Date
* Test System details
* Test Report Reference (file name)
* TCW (when applicable)

### A.3. Test report

A Member must provide a test report for all Category A or B test cases in the test plan. A test report must contain:

* Identification of the test facility that conducted the tests
* Identification of the Member providing the Product for testing
* Identification of the Product including hardware and software version numbers
* A reference to the TS version
* A reference to the utilized Test System including the version
* IXIT values required by test cases executed
* For all test cases performed using a Member-defined test setup, information regarding test set up, execution, and results
* A summary list of all performed test cases with the test case identifier, date of test, and the verdict (pass, fail, or inconclusive)

## Appendix B. TCW policy

A Member may request a TCW using the process in the IPD [8].

When a TCW is granted, the TCW is available to all Members where the error is applicable.

A TCW remains valid until it is terminated. A TCW is terminated when the associated TSE indicates that the errors in the test documents or Test Systems have been fixed and the TSE has been incorporated in an active TCRL Package, if required. The details of the termination process are defined in the IPD [8].

The reasons a TCW may be granted include:

* An error in the test case mapping table
* An error in ICS conditionals
* An error in a test case initial condition, procedure, or pass verdict
* An error in test case category in the TCRL Package
* An error in a Test System (see also Appendix B.1)
* An error in the Bluetooth SIG online tool’s interface or generated test plan
* No commercially available Test System can perform the test case, and it is not feasible to implement the test case in-house
* A request to use a newly validated Test System (i.e., when the validation is not yet referenced in a TCRL)
* A request to apply the corrections from a TSE (e.g., modify a part of the test case) before the TSE is published in the applicable test document and referenced in a TCRL Package

### B.1. Handling TCWs when errors in a validated Test System are encountered

If a validated Test System referenced in an applicable test plan for a Category A test case encounters an error that prevents completion of an affected test case(s), the Member may request a TCW.

#### B.1.1. Multiple validated Test Systems referenced in the test plan

When the applicable test plan references more than one validated Test System for the affected Category A test case(s), a TCW may be granted that waives the requirement to conduct the affected test case(s) at a BQTF and allows the Member to complete testing using an alternate validated Test System referenced in the test plan, in
an alternate laboratory. All other qualification requirements remain unchanged.

#### B.1.2. Only one validated Test System referenced in the test plan

When the applicable test plan references only one validated Test System for the affected Category A test case(s), a TCW that specifies the path to complete the affected test case(s) may be granted.
