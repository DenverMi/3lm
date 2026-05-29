# General Bluetooth FAQ

### 1. Do I Need to Qualify?

To brand (or re-brand) and sell a Bluetooth® product, your company must join the Bluetooth Special Interest Group (SIG) and complete the Qualification process. To learn more about joining the Bluetooth SIG, please visit https://www.bluetooth.com/developwith-bluetooth/join.

The Bluetooth Qualification Process exists to ensure global product interoperability, improve quality, and provide the best user experience.

#### ALL Bluetooth® Products Must Be Qualified

Your supplier or other member companies cannot qualify your products on your behalf, you must complete the Bluetooth Qualification Process for your product yourself You can only qualify your products under your member company's account and only by completing the Bluetooth Qualification Process.

Products must be qualified on or before the date that you begin to sell or distribute the product. The details you provide for each product must exactly match the product, its packaging markings, and marketing materials. Products that appear to have not completed the Bluetooth Qualification Process may be impounded by customs authorities and will be subject to Bluetooth SIG enforcement actions.

If you are a retailer or supplier selling or distributing another organization's qualified Bluetooth product, and you are not adding any logos, branding, or representing the product as your own, you do not need to complete the Qualification Process for the product. However, you should ensure that the product has been properly qualified. You can check if a product is properly qualified by referring to the Qualified Product database.

A member choosing not to use the Bluetooth trademarks must still be compliant with the Bluetooth Patent & Copyright License Agreement. Members are encouraged to review the conditions of the license agreements and consult their legal counsel with any questions regarding the applicable requirements. We are unable to provide any legal advice, including the ramifications resulting from a member's failure to adhere to the procedures set out in the Bluetooth SIG's operative, governing documents. For these reasons, we advise that each

member company completes the defined processes to ensure they demonstrate and declare compliance to both license agreements.

The Membership Agreements can be downloaded at https://www.bluetooth.com/aboutus/governing-documents.

If you do not qualify your product, you become subject to enforcement action, potentially leading to suspension or revocation of your Bluetooth SIG membership if no corrective actions are taken. Our Trademark License Enforcement Program protects all Bluetooth SIG members by ensuring Bluetooth products are properly qualified. You can read more about the program here.

If you suspect a product is in violation, you may report it to the Bluetooth SIG. Please note that the Bluetooth SIG does not track, analyze, or enforce patents, member-owned or otherwise. In these cases, you should consult your own legal counsel.

#### 2. Understanding Core Configurations

Bluetooth® technology is implemented through a combination of software and hardware. This is often referred to as the Bluetooth Host (software) and Controller (hardware). The two most prevalent implementations of the Bluetooth specification are Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR), adopted as version 2.0/2.1, and Bluetooth Low Energy (LE), adopted as version 4.0. Each implementation has different use cases, and each uses a different chipset to meet hardware requirements. Dual-mode chipsets are also available for devices to support both implementations.

Each implementation has a Core Configuration (defined in Volume 0, Part D of the Bluetooth Core Specification) that represents the minimum required layers for both the Host and Controller portions which together are considered a complete Bluetooth implementation. Below you will find diagrams of the most common Core Configurations and the layer requirements for each. For complete information on Core Configurations, requirements, and conditionals, please review [Volume 0, Part D of the Bluetooth Core](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/consolidated-table-of-contents,-acknowledgments,---core-configurations/core-configurations.html#UUID-92feba2a-4f1d-1744-e991-adfd41f1d3b8)  [Specification.](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/consolidated-table-of-contents,-acknowledgments,---core-configurations/core-configurations.html#UUID-92feba2a-4f1d-1744-e991-adfd41f1d3b8)

# Core-Controller Configurations

| Configuration |             |  |
|---------------|-------------|--|
| Layer         | Requirement |  |
| HCI           | Mandatory   |  |
| ISOAL         | Conditional |  |
| LESEC         | Conditional |  |
| LL            | Mandatory   |  |
| RFPHY         | Mandatory   |  |
| SEC           | Mandatory   |  |
| LMP           | Mandatory   |  |
| BB            | Mandatory   |  |
| RF            | Mandatory   |  |

| LE Core-Controller<br>Configuration |             |  |
|-------------------------------------|-------------|--|
| Layer                               | Requirement |  |
| HCI                                 | Mandatory   |  |
| ISOAL                               | Conditional |  |
| LESEC                               | Conditional |  |
| LL                                  | Mandatory   |  |
| RFPHY                               | Mandatory   |  |

# Core-Host Configurations

| BR/EDR Core-Host<br>Configuration |             |  |
|-----------------------------------|-------------|--|
| Layer                             | Requirement |  |
| GATT                              | Conditional |  |
| ATT                               | Optional    |  |
| GAP                               | Mandatory   |  |
| SDP                               | Mandatory   |  |
| L2CAP                             | Mandatory   |  |
| HCI                               | Mandatory   |  |

| Configuration |             |  |
|---------------|-------------|--|
| Layer         | Requirement |  |
| GATT          | Conditional |  |
| ATT           | Conditional |  |
| GAP           | Mandatory   |  |
| SDP           | Mandatory   |  |
| SM            | Conditional |  |
| L2CAP         | Mandatory   |  |
| HCI           | Mandatory   |  |

| Configuration |             |  |
|---------------|-------------|--|
| Layer         | Requirement |  |
| GATT          | Conditional |  |
| ATT           | Conditional |  |
| GAP           | Mandatory   |  |
| SM            | Conditional |  |
| L2CAP         | Conditional |  |
| HCI           | Mandatory   |  |

# Core-Complete Configurations

| Configuration |             |  |
|---------------|-------------|--|
| Layer         | Requirement |  |
| GATT          | Conditional |  |
| ATT           | Optional    |  |
| GAP           | Mandatory   |  |
| SDP           | Mandatory   |  |
| L2CAP         | Mandatory   |  |
| HCI           | Conditional |  |
| SEC           | Mandatory   |  |
| LMP           | Mandatory   |  |
| BB            | Mandatory   |  |
| RF            | Mandatory   |  |
|               |             |  |

| Bry EBry EE Core Complete |             |  |  |  |  |
|---------------------------|-------------|--|--|--|--|
| Configuration             |             |  |  |  |  |
| Layer                     | Requirement |  |  |  |  |
| GATT                      | Conditional |  |  |  |  |
| ATT                       | Conditional |  |  |  |  |
| GAP                       | Mandatory   |  |  |  |  |
| SDP                       | Mandatory   |  |  |  |  |
| SM                        | Conditional |  |  |  |  |
| L2CAP                     | Mandatory   |  |  |  |  |
| HCI                       | Conditional |  |  |  |  |
| ISOAL                     | Conditional |  |  |  |  |
| LESEC                     | Conditional |  |  |  |  |
| LMP                       | Mandatory   |  |  |  |  |
| Ш                         | Mandatory   |  |  |  |  |
| BB                        | Mandatory   |  |  |  |  |
| RFPHY                     | Mandatory   |  |  |  |  |
| RF                        | Mandatory   |  |  |  |  |
|                           |             |  |  |  |  |

| LE Core-Complete<br>Configuration |             |  |  |  |
|-----------------------------------|-------------|--|--|--|
| Layer                             | Requirement |  |  |  |
| GATT                              | Conditional |  |  |  |
| ATT                               | Conditional |  |  |  |
| GAP                               | Mandatory   |  |  |  |
| SM                                | Conditional |  |  |  |
| L2CAP                             | Conditional |  |  |  |
| HCI                               | Conditional |  |  |  |
| ISOAL                             | Conditional |  |  |  |
| LESEC                             | Conditional |  |  |  |
| LL                                | Mandatory   |  |  |  |
| RFPHY                             | Mandatory   |  |  |  |

#### 3. Updating Your Company's Qualification Contact

What is the Qualification Contact?

The Qualification Contact is your company's designated contact to receive communications regarding the Bluetooth Qualification Program as well as any potential issues regarding your company's qualifications.

Occasionally, other members using your qualified designs may encounter issues and contact the Bluetooth SIG for assistance. When appropriate, the Bluetooth SIG may communicate the issue to your company's Qualification Contact, or your company may consent to allow the Qualification Contact details to be shared with those members reporting the issue so the member may e-mail the Qualification Contact directly.

Only the Primary Contact for a member company may change the Qualification Contact. If you are not the primary contact and would like to change your company's Qualification Contact, please request your company's Primary Contact to make the change.

How to Update the Qualification Contact?

Step 1: In the [Member Account Resources and Contacts page,](https://apps.bluetooth.com/mycompany/membercontact) locate the Qualification Contactsection and click Edit Qualification Contact:

![](_page_3_Picture_7.jpeg)

Step 2: In the Qualification Contact page, use the search feature to locate the new Qualification Contact or enter the information manually in the section below the search. Please click the consent check-box if you consent to allow the Bluetooth SIG to share the contact details with other member companies experiencing issues qualifying using your previously qualified design. Once completed, click Save Changes to update the Qualification Contact:

| Search for existing users within                                     | n your company to populate the form below.                                                                                                                                                                                                                     |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                      | - Or -                                                                                                                                                                                                                                                         |
| Enter contact informati                                              | on manually                                                                                                                                                                                                                                                    |
| First Name:                                                          |                                                                                                                                                                                                                                                                |
| Last Name:                                                           |                                                                                                                                                                                                                                                                |
| Email address:                                                       |                                                                                                                                                                                                                                                                |
| This email address can be for a                                      | n individual or an alias.                                                                                                                                                                                                                                      |
| Qualification Contact<br>with other members<br>that utilize my compa | Bluetooth Special Interest Group to share the details of my company's Bluetooth SIG account for issues regarding the qualification of products any's previously qualified designs. Please see our reinformation on how the Bluetooth SIG protects information. |

### 4. Product Qualification Fees

A Product Qualification Fee is charged for the first product submission from a Member company that includes a specific design. Subsequent product submissions from the same Member company that include the same design will not be charged a Product Qualification Fee.

Product Qualification Fees are paid through our online purchasing system in Qualification Workspace. Payment can be made via credit card or invoice. Credit card payments will be processed instantly. Payment via invoice may take 1-2 weeks to process, depending on the time it takes to issue, receive, and process the invoice.

Once payment is processed by Bluetooth SIG, you will be issued a Receipt Number. A Receipt Number is a unique reference number issued as proof of payment of the Product Qualification Fee by a Member to complete the Bluetooth Qualification Process.

Product Qualification Fees are non-refundable. All Receipt Numbers not used will expire 12 months from the date of receipt of payment of the Product Qualification Fee. Receipt Numbers and their expiration dates can be found in the "Pay Product Qualification Fee" section of Qualification Workspace.

The current Bluetooth SIG Schedule of Dues and Fees can be found here:

#### <https://www.bluetooth.com/fee-schedule/>

If you have any questions regarding fees or payment, please submit a support request.

#### 5. Bluetooth Qualification Consultants

#### What is a Bluetooth Qualification Consultant?

Bluetooth® Qualification Consultants are independent consultants who have met specific requirements and are permitted to call themselves "Bluetooth Qualification Consultants." Bluetooth Qualification Consultants have passed a test that is facilitated by Bluetooth SIG. The test covers a wide range of topics related to Bluetooth and the Qualification process. Members may, but are not required to, engage Bluetooth Qualification Consultants to provide qualification-related services and guidance.

Please visit [this link](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-consultants/) for more information and a list of currently available Bluetooth Qualification Consultants.

#### How does a member use a Bluetooth Qualification Consultant?

If you wish to engage a Bluetooth Qualification Consultant to provide services related to or guidance on your specific qualification scenario, you will need to engage the consultant directly.

To prepare submissions for your company in Qualification Workspace, the consultant may need to create a user account under your company's account. The consultant can use that account to access Qualification Workspace and prepare submissions under your company's account.

Here's a step-by-step guide:

- 1. You engage Consultant John Doe (e.g., a Bluetooth Qualification Consultant) directly.
- 2. You provide an email address to John Doe that uses the same email address domain as your company's Bluetooth SIG membership registration (e.g., john.doe@example.com).
- 3. John Doe uses the john.doe@example.com email address to apply for a Bluetooth SIG user account on Bluetooth SIG's website. (Note that if your company does not provide John Doe with access to the email account associated with the john.doe@example.com email address, then John Doe may require further assistance from your company to complete the user account registration process because a validation email will be sent to that email address and confirmation that the email address is valid must occur to complete the user account registration.)

4. Once John Doe has obtained a user account with the john.doe@example.com email address, John Doe can log in to Qualification Workspace and qualify products on behalf of your company.

Bluetooth Qualification Consultants are not employed by or representatives of the Bluetooth SIG. Each member that engages a Bluetooth Qualification Consultant is responsible for establishing the terms of its relationship with the Bluetooth Qualification Consultant, including payment and scope of services.

#### How do you apply to become a Bluetooth Qualification Consultant?

To become a Bluetooth Qualification Consultant, you must satisfy all program requirements, including passing an exam to evaluate your proficiency with Bluetooth specifications (including test specifications) and the Bluetooth Qualification Program.

If you're interested in becoming a Bluetooth Qualification Consultant, you can find more information [here.](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-consultants/qualification-consultant-program-overview/)

#### 6. Deprecation & Withdrawal

#### Deprecation and Withdrawal Overview

Product interoperability is at the heart of the Bluetooth® brand and is one of the core benefits of Bluetooth technology. Deprecation and Withdrawal (D&W) is designed to promote global product interoperability and quality by encouraging Bluetooth members to use the latest versions of Bluetooth specifications. This includes several important updates to the Bluetooth Qualification Policy, as well as the deprecation and withdrawal of older Bluetooth specifications and the adoption of maintenance releases for a number of active Bluetooth specifications.

The BoD encourages SIG members to work diligently toward bringing their products into compliance with the latest versions of Bluetooth specifications to promote interoperability, improve quality, and provide the best user experiences. The BoD would also like to thank members for their important feedback on Deprecation and Withdrawal. To provide feedback, please submit a support request and select "BoD Feedback" from the Category drop-down.

When a specification reaches the end of its useful life, the Bluetooth Special Interest Group may choose to deprecate or withdraw the specification. Deprecated and withdrawn specifications are no longer maintained by the Bluetooth SIG and are not updated with any further error corrections, clarifications, or feature enhancements. For more information on specification deprecation and withdrawal, please see the [Specification Management Process](https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=40557)  [Document \(SMPD\),](https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=40557) Section 8.

#### Approved Specification Deprecation and Withdrawal Dates

To view the latest updates on deprecation and withdrawal dates, please visit the [Specifications and Documents](https://www.bluetooth.com/specifications/specs/) page on Bluetooth.com.

### Deprecation and Withdrawal Impacts on the Qualification Process

Deprecation and withdrawal of specifications impact the options available to members in the Qualification Process when using previously qualified designs. The table below details these impacts:

| Specify the Design   | Using Active   | Using Deprecated        | Using Withdrawn |  |
|----------------------|----------------|-------------------------|-----------------|--|
| Options              | Specifications | Specifications          | Specifications  |  |
| Option 1             |                |                         |                 |  |
| (Section 3.2.1)      | Allowed        | Allowed                 | Not Allowed     |  |
| Option 2a            |                |                         | Not Allowed     |  |
| (Section 3.2.2.1)    | Allowed        | Allowed                 |                 |  |
| Option 2b            |                | Allowed if unmodified   |                 |  |
| (Section 3.2.2.2)    | Allowed        | from an included Design | Not Allowed     |  |
| Reassess a Design    |                |                         | Not Allowed     |  |
| (Section 3.2.2.2.1)  | Allowed        | Not Allowed             |                 |  |
| Create a Subset of a |                |                         |                 |  |
| Design               | Allowed        | Allowed                 | Not Allowed     |  |
| (Section 3.2.2.2.2)  |                |                         |                 |  |

#### 7. Trademark Licenses & Qualification Requirements by Product Scenario

Bluetooth SIG, Inc. ("Bluetooth SIG") exclusively owns the Bluetooth® trademarks which include, the BLUETOOTH word mark, "B" Design figure mark, and BLUETOOTH & "B" Design combination mark (the "Bluetooth Trademarks"). To use the Bluetooth Trademarks in connection with products or services, a company must become a Bluetooth SIG member and have a license from Bluetooth SIG. One requirement of the Bluetooth SIG trademark licensing program is that members must qualify their products (see the [Bluetooth](https://www.bluetooth.com/about-us/governing-documents/)  [Trademark License Agreement](https://www.bluetooth.com/about-us/governing-documents/) for more details). The trademark license granted to a Bluetooth SIG member is not sub-licensable and is nontransferable. A company representing a product as its own must obtain its own license to use the Bluetooth Trademarks and properly qualify its own product. A supplier cannot qualify a product on behalf of a customer, and a supplier cannot transfer its license to use the Bluetooth Trademarks to a customer.

Product Scenario Who Must Qualify?

Building my own product - My company creates the product that will be offered under my company's brand. My company may create the product with components that were previously qualified by suppliers or may create the product entirely from my company's own

components. The product may be manufactured by my company or by a supplier.

My company must qualify the product

![](_page_8_Figure_5.jpeg)

Contract Manufacturing - My company contracts supplier(s) to create and manufacture and/or label the product that will be offered under my company's brand:

- Full Custom My company provides the supplier(s) with complete specifications for the product
- Partial Customization My company provides the supplier(s) with details of the customizations needed to an existing product
- Re-branding My company provides the supplier with details of the branding customizations needed to an existing product

My company must qualify the product. (The supplier may decide to qualify the product as well, but their qualification does not apply to my company)

![](_page_8_Figure_11.jpeg)

Re-selling - My company is selling another company's product that my company has not changed and does not use my company's brand

![](_page_8_Figure_13.jpeg)

The company that is representing the product as their own must qualify the product. My company should make sure that it is only selling qualified products.

### 8. Trademark License Enforcement Audit

The audit process consists of Bluetooth SIG reviewing product(s) that have been released to the market using the Bluetooth Trademarks. During the audit process, Bluetooth SIG will use the product name and model number found on the company website and marketplace, including third-party retailers, then compare this information with product data found in the Qualified Product Database.

Bluetooth SIG recommends each member ensure their products using Bluetooth trademarks have successfully completed the Qualification Process and can be found in the Qualified Product Database.

Below is an example of an audit:

STEP 1 ‒ Find product information

![](_page_9_Picture_4.jpeg)

STEP 2 ‒ Search the product name in the Qualified Product Database under the member's Qualifications

![](_page_9_Picture_6.jpeg)

STEP 3 ‒ Ensure the product has successfully completed the Bluetooth Qualification Process

![](_page_9_Picture_8.jpeg)

#### Links to helpful information:

[Bluetooth Qualification Process](https://www.bluetooth.com/develop-with-bluetooth/qualify/)

[Product Name and Model Number Requirements](https://qualification.support.bluetooth.com/hc/en-us/articles/26985778870285)

[Qualifying Additional Products that use an Existing Design](https://qualification.support.bluetooth.com/hc/en-us/articles/28366464522893)

[Qualified Product Database](https://qualification.bluetooth.com/Listings/Search)

[Brand Guide](https://www.bluetooth.com/develop-with-bluetooth/marketing-branding/)

[Trademark License Enforcement Program](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/trademark-license-enforcement/)

#### 9. How to Establish a Corrective Action Plan

When your member account is placed under enforcement, to resolve the enforcement issue, a corrective action plan (CAP) may be required to get your member account back into good standing. When submitting a CAP, you must include a detailed proposal of all actions you will take to remedy the non-compliance. The CAP must include a timeframe (no later than 90 days) for the corrective action to be completed. Bluetooth SIG staff will review the proposed CAP and provide feedback if more information is required. You can learn more about the Trademark License Enforcement Program [here.](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-enforcement-program/)

#### Corrective Action Plan Spreadsheet

A primary tool that should be used when creating a corrective action plan is the CAP spreadsheet template which can be downloaded [here.](https://www.bluetooth.com/wp-content/uploads/2021/02/CAP-Proposal.xlsx) The spreadsheet can also be provided, upon request, directly from Bluetooth SIG staff.

The steps below look at each section of the CAP spreadsheet and show you how to fill out all required fields correctly.

Product Name: All Product Names for the products that your company sells, brands, and represents as its own must be listed. Your company trademark must also be part of the product name. General names, such as Bluetooth speaker, are not acceptable.

Model Number: All product model numbers presented to consumers must be listed. If you have more than one model number for each product, you should include all model numbers in the declaration. Each model number is a different product and should be listed separately.

Design Number (DN) or Qualified Design ID (QDID): List the DN or QDID provided to you by the manufacturer. List multiple DNs/QDIDs if necessary.

Product Publication Date: Include today's date. If the product has not yet been released, include the future planned publication date.

Actions Planned: Include a list of the actions your company will take to make this product compliant.

Expected Resolution Date: List the date on which you plan to have this product compliant and resolve the enforcement issue.

Please be aware that all the above information must be included for your Corrective Action Plan (CAP) to be approved. If one or more fields do not seem applicable, please type N/A in the specific field.

If you do not complete all actions required in the CAP within the documented timeline, Bluetooth SIG staff may take additional actions, including, but without limitation to, reporting your member account to the Bluetooth SIG Board of Directors for a vote to suspend membership.

Note: The Enforcement Escalation Process may continue (and Cost Recovery Fees may be assessed) until Bluetooth SIG staff determine in its discretion that all issues have been resolved, regardless of the member's proposal of, or Bluetooth SIG's or its staff's approval of, any CAP.

## IOPT Testing

#### IOPT Testing Overview

Interoperability testing (IOPT) helps ensure product quality and the interoperability of Bluetooth products. With the adoption of Qualification Program Reference Document (QPRD) v3, new IOPT testing requirements were mandated for new designs and certain design combinations. Since the launch of QPRDv3, IOPT test cases have been optional as they have not yet reached their active date.

On January 8, 2025, IOPT test requirements became active, and Qualification Workspace will generate test plans with required IOPT test cases for design combinations as defined in QPRDv3. [QPRDv3 Table 3.1](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/QPRD/out/en/index-en.html?id=42423#UUID-c53ac674-5f92-d4b9-a8dc-4f3fcfe80067) (image below) details the combinations requiring IOPT testing. This requirement will apply to Options 2a and 2b of the Qualification Process. To ease the transition to IOPT testing, a couple of Test Coverage Waivers (TCWs) have been approved that will allow members to waive IOPT testing for submissions using TCRL 2024-2. Members choosing to waive IOPT testing with this TCW can enter "Waived" for test case verdicts in their test plan and enter the TCW in the Evidence Notes field. Submissions using TCRL 2025-1 will need to complete the testing. For more information, please see the [IOPT Test Case Waivers](https://qualification.support.bluetooth.com/hc/en-us/articles/31233488117005-IOPT-Testing#h_01JPK5QNWDFV1898RSGK9YBK1F) section below.

To test IOPT test cases, members will need to use [Profile Tuning Suite \(PTS\),](https://www.bluetooth.com/develop-with-bluetooth/qualify/qualification-test-tools/profile-tuning-suite/) Bluetooth SIG's testing software that automates compliance testing to the specified functional requirements of Bluetooth Host Parts and specifications that reside above the Host Controller Interface (HCI). For more information on how to perform IOPT testing in PTS, please see the following article: [How to execute IOPT test cases from Qualification](https://support.bluetooth.com/hc/en-us/articles/33573077030797-How-to-execute-IOPT-test-cases-from-Qualification-workspace-ICS-export-file)  [workspace ICS export file.](https://support.bluetooth.com/hc/en-us/articles/33573077030797-How-to-execute-IOPT-test-cases-from-Qualification-workspace-ICS-export-file)

PTS requires the use of PTS Dongles, which enable connection to the product under test. For more details about the available PTS Dongles and where they can be purchased, please see the following article: [What is the difference between the Profile Tuning Suite \(PTS\)](https://support.bluetooth.com/hc/en-us/articles/360049018492)  [Dongles?](https://support.bluetooth.com/hc/en-us/articles/360049018492)

Bluetooth SIG also partners with [Bluetooth Qualification Consultants](https://www.bluetooth.com/develop-with-bluetooth/qualify/qualification-consultants/)  [\(BQCs\)](https://www.bluetooth.com/develop-with-bluetooth/qualify/qualification-consultants/) and [Bluetooth Qualification Test Facilities \(BQTFs\)](https://www.bluetooth.com/develop-with-bluetooth/qualify/qualification-test-facilities/) that can offer guidance relating to, or completion of, IOPT testing.

#### QPRDv3 Table 3.1

| Permitted Combinations               |                                                               | Creating                                                | Requiremen                           | Requirements |                          |                                         |
|--------------------------------------|---------------------------------------------------------------|---------------------------------------------------------|--------------------------------------|--------------|--------------------------|-----------------------------------------|
| Design 1 has                         | Design 2 has                                                  | Designs 3+ have<br>(optional,<br>additional<br>Designs) | New Design has                       | ILD Check    | Core<br>Config.<br>Check | IOPT Required<br>for Layers<br>added by |
| Core-<br>Complete<br>Configuration   | X2Core<br>Layers only                                         | X2Core<br>Layers only                                   | Core-<br>Complete<br>Configuration   | Required     | Required                 | Design 2<br>and<br>Design 3+            |
| Core-<br>Controller<br>Configuration | Core-Host<br>Configuration                                    | -                                                       | Core-<br>Complete<br>Configuration   | Required     | Required                 | None                                    |
| Core-<br>Controller<br>Configuration | Core-Host<br>Configuration                                    | X2Core<br>Layers only                                   | Core-<br>Complete<br>Configuration   | Required     | Required                 | Design 3+                               |
| Core-Host<br>Configuration           | X2Core<br>Layers only                                         | X2Core<br>Layers only                                   | Core-Host<br>Configuration           | Required     | Not<br>required          | Design 2<br>and<br>Design 3+            |
| Core-<br>Controller<br>Configuration | X2Core Layers<br>implementing<br>LC3<br>specification<br>only | -                                                       | Core-<br>Controller<br>Configuration | Required     | Not<br>required          | None                                    |
| X2Core<br>Layers only                | X2Core<br>Layers only                                         | X2Core<br>Layers only                                   | X2Core<br>Layers only                | Required     | Not<br>required          | None                                    |

#### Export .ICS File for Option 2a Drafts

If you use an .ICS file to import into PTS and configure your testing, the .ICS file for a draft that uses Option 2a in Qualification Workspace can be obtained via the Draft Products page. Navigate to the [Draft Products](https://qualification.bluetooth.com/MyProjects/DraftProducts) page in Qualification Workspace, locate the draft and click on the Actions link next to the draft. You will see an option for Export ICS in the drop-down menu. Please note that this will export all the ICS for the design, not just the ICS related to the IOPT test cases.

#### IOPT Test Case Waivers

[ES-26784](https://bluetooth.atlassian.net/browse/ES-26874) - This waiver applies to IOPT tests generated in Option 2A for TCRL 2024-2. [ES-27227](https://bluetooth.atlassian.net/jira/software/c/projects/ES/issues/ES-27227?filter=10781) - This waiver applies only to individual SGSIT/SGGIT test cases generated under the IOPT heading generated by Qualification Workspace in Option 2B for TCRL 2024-2.

#### Additional Resources

[PTS Knowledge Base Articles](https://support.bluetooth.com/hc/en-us/sections/360010319732-Profile-Tuning-Suite-PTS) [IOPT Test Suite](https://www.bluetooth.com/specifications/specs/interoperable-product-testing/)

## [Qualification Program Reference Document \(QPRD\) v3](https://www.bluetooth.com/develop-with-bluetooth/qualify/qprd-3-html/) [Profile Tuning Suite Download](https://www.bluetooth.com/develop-with-bluetooth/qualify/qualification-test-tools/profile-tuning-suite/)

#### Testing Overview

The testing part of the qualification process demonstrates that a product complies with Bluetooth specifications and will be interoperable with other Bluetooth products. During the qualification process, the features you select in the Implementation Conformance Statement (ICS) Selection step in Qualification Workspace will determine the test cases that must be performed to demonstrate compliance and interoperability of the product. Additional information about the test cases can be found in the most recent Test Case Reference List (TCRL) and Test Suite documents. These documents can be found here: [Specifications and Documents.](https://www.bluetooth.com/specifications/specs/)

If you need help with the testing process, the Bluetooth Special Interest Group (SIG) maintains a list of [Bluetooth Qualified Test Facilities](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-test-facilities/) and [Bluetooth Qualification](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-consultants/)  [Consultants](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-consultants/) that can assist in performing required testing or providing guidance on qualification. You can also submit questions to Bluetooth SIG staff by submitting a support request.

### Test Documentation

#### Test Plan

The Test Plan indicates test requirements/test cases to be met based on the [Implementation](https://qualification.support.bluetooth.com/hc/en-us/articles/27694433301517)  [Conformance Statement \(ICS\)](https://qualification.support.bluetooth.com/hc/en-us/articles/27694433301517) selections for your product. Members are responsible for completing the tests and indicating test verdicts and dates of testing within the test plan. The completed test plan (also referred to as "Test Declaration") is submitted in Qualification Workspace.

The test cases generated also depend upon the Test Case Reference List (TCRL) version. Please see the following article for more information on the TCRL: [Test Case Reference List](https://qualification.support.bluetooth.com/hc/en-us/articles/26704631555085)  [\(TCRL\).](https://qualification.support.bluetooth.com/hc/en-us/articles/26704631555085)

Information about test cases, test suites, and ICS can be found on the [Specifications and](https://www.bluetooth.com/specifications/specs/)  [Documents](https://www.bluetooth.com/specifications/specs/) page of our website.

For more information on how to complete the Test Declaration, please see the [Test](https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=228307)  [Declaration Best Practices](https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=228307) document.

#### Test Plan Column Definitions

Test Case ID - Formatted as follows: Layer/Role/Capabilities/Behavior Valid or Invalid (BV or BI)/#/Conformation or Interoperability (-C or -I). Example: HCI/AEN/BI-01-C

Legacy Test Case ID - Test Case ID was previously identified as

Test Case Description - Name found in Test Suite

Test Case Category - Test execution and evidence requirements defined in the TCRL

Active Date - The date the latest requirements of the test case becomes mandatory for Qualification. Until this date, it is optional to use the requirements in the previous TCRL for the test case.

Test Platform - Test system that shall be used if Test Category A, otherwise members can choose their own test system or set up in accordance with the TCRL.

TCMT (Test Case Mapping Table) - ICS items selected to require the test case for Qualification

TSE- TSEs included in the active TCRL

TCRL Release Notes - Released TSEs or other technical notes included in the active TCRL TCRL Version with Last TSE - Last TCRL where the test case was materially affected Test Case Verdict (Pass, Fail, Waived, Not Required) -

- Pass: Test executed by Member and achieved Pass verdict
- Waived: The test case has an approved Test Coverage Waiver (if waived, the TCW shall be referenced in the Evidence Notes column)
- Not Required: For optional test cases for which members opt not to perform testing

Test Execution (Date) - Date the test was executed according to the Test Report

Test Equipment Platform - The make, model, serial number, and SW version of the system used during test execution

Test Report Reference - The name of the Test Report document found in the Compliance Folder

IUT Configuration - Indicate if a special setup was used for the IUT to run the test case, including the hardware and software versions

Evidence Notes - Any TCWs used or other information applicable to the execution of the test case

#### Test Reports

Any test reports indicated in the Test Report Reference column of the completed test plan should be submitted in Qualification Workspace.

As indicated in the [QPRD Appendix A.3,](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/QPRD/out/en/index-en.html#UUID-528b851d-c1b5-9b75-1597-74cab717cd17) test reports shall contain at a minimum:

- Identification of the test facility that conducted the tests.
- Identification of the Member providing the Product for testing.
- Identification of the Product including hardware and software version numbers.
- A reference to the TS version.

- A reference to the utilized Test System including the version.
- IXIT values required by test cases executed.
- For all test cases performed using a Member-defined test setup, information regarding test setup, execution, and results.
- A summary list of all performed test cases with the test case identifier, date of test, and the verdict (pass, fail, or inconclusive)

Test reports are required for [Category A and B test cases.](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/QPRD/out/en/index-en.html#UUID-3a0d618a-c663-3666-3209-cb664fc54bc8)

### Test Case Reference List (TCRL)

The Test Case Reference List (TCRL) package is a qualification reference for all Bluetooth Special Interest Group (SIG) members. It is a living document that introduces new test cases, removes test cases, and categorizes test cases. Members may only use these document references to qualify their Bluetooth® enabled products.

All TCRL packages will have an Available Date and an Active Date. The Available Date represents when the Bluetooth SIG first publishes the TCRL package. The Active Date means the date that the TCRL package is mandatory for qualification. A previous TCRL package release becomes inactive after the newer TCRL package release reaches its Active Date.

Depending upon the features supported by a Bluetooth design, test cases from the TCRL package will be added to the design's test plan in Qualification Workspace. Members will then need to perform these tests and provide test evidence to attest that their design complies with the specification and is interoperable with other Bluetooth-enabled products. See the most recent [TCRL packages.](https://www.bluetooth.com/specifications/tcrl/)

