## Matter Certification Sunset 

## Schedule 

## **Overview** 

After a period of time, Alliance certification programs may "sunset," meaning they will close and become unavailable to new product certifications. Sunset dates are proposed by the relevant Alliance working group and approved by the Alliance Board of Directors before going into effect. 

At the discretion of the Alliance, sunset programs may be kept open to 

recertifications of existing products. This includes Certification by Similarity, as long as the Similarity application is used to update an existing product and not certify a new, similar product. In other words, for Certification by Similarity, whether an application is considered a recertification depends on whether an existing product is being recertified (for example, a bug fix or update) or if a new product is being certified, with Certification by Similarity being leveraged to bypass the need for additional testing. The first case would be available post-sunset, but not the latter. 

Programs such as Certification Transfer, which rely on a previously existing certified product, may not reference a previously certified product certified to a sunset program. 

## **Matter Sunset Schedule** 

The following table contains a list of known Matter certification sunset dates by program version: 

|**Matter Version**|**Sunset Date**|**Open to Recertifications?**|
|---|---|---|
|Matter 1.0|December 31, 2024|Yes|
|Matter 1.1|June 30, 2025|Yes|
|Matter 1.2|December 31, 2025|Yes|
|Matter 1.3|June 30, 2026|Yes|



## **Grace Period** 

Typically, after an Alliance certification program has sunset, the Alliance will accept and continue to process new applications for certification to the sunset version _**if testing began before the sunset date**_ (for applications that require testing), or _**if the application was submitted before the sunset date**_ . 

Applications which fall into one of the two above cases are termed to be in the "grace period." Note if testing began before the sunset date, _**the Authorized Test Provider (ATL) must inform the Alliance of this fact before the sunset date for the application to qualify**_ . 

Example: Matter 1.2 will sunset on December 31, 2025. If formal Matter 1.2 testing (at an ATL) for a particular product begins before this date, Alliance Certification will accept the corresponding application for certification to Matter 1.2, even if the application is submitted after December 31, 2025, _**provided that the ATL informed Alliance Certification prior to December 31, 2025**_ . 

## Matter Platform 

## **Overview** 

Matter Platform certification is intended to be used as a foundation for a Derived Matter Product that implements and certifies additional clusters and functionality on top of the certified clusters and functionality provided by the Matter Platform to yield a compliant Matter implementation. The policy and requirements surrounding Matter Platform certification are outlined in the **Alliance Certification Policy** . 

The program consists of two components: 

1. Matter Certified Platform: Certification type that allows a member to certify a base platform for other members to use for Derived Matter Products. 

2. Derived Matter Product: Must be built on a Matter Certified Platform and enables reduced certification testing (functionality previously tested in the Matter Compliant Platform does not need to be retested). 

## **Requirements** 

## Matter Certified Platform 

A Matter Certified Platform must do the following when providing a platform for other members to build a Derived Matter Product: 

Implement an interface to one or more of the transports supported by Matter (Wi-Fi, Thread, or Ethernet) 

- Support Matter commissioning 

- On-network commissioning is required 

- Commissioning via other mechanisms is optional (BLE, Wi-Fi PAF, Proprietary) 

- Provide a Matter Platform Configuration indicating the parameters of the platform that are to be certified 

- Implement a Root Node device type and the associated mandatory clusters 

- Implements optional clusters according to those identified in the Platform PICS 

A Matter Certified Platform must do the following when testing and certifying the Platform: 

- Provide one or more test applications that implement a complete Matter Product and use the platform to be certified in the configuration to be certified. 

- This can reuse one of the standard Matter Sample Applications (if applicable). 

- Must indicate at least one SOE in the Declaration of Conformity for which this platform is being certified 

- Pass all test cases applicable for Platforms related to the Platform Certification’s configuration 

A member certifying a Matter Platform may make use of any certification programs available for Matter Products, such as Rapid Re-certification, FastTrack Re-certification, Certification by Similarity, Family Certification and Portfolio Certification. However, it is not permitted to use Certification Transfer to transfer only the platform to another member. 

All Matter Platforms must be certified to version 1.4.2 of the Matter specification or later. 

Currently, Matter Certified Platforms cannot be listed on the DCL. A Matter Platform does not need to provide a Matter Security Attestation. Derived Matter Product 

A Derived Matter Product makes use of a Matter Certified Platform and includes other clusters and functionality required to implement and certify a 

product. Those items that are added to the platform are generally tested during the product certification testing while functionality previously tested by the certified platform is skipped. The full set of results of the Derived Matter Product with the results of the previously Matter Certified Platform is reviewed by the Alliance to verify all tests appropriate for the product have been run. 

In general, a certified Derived Matter Product is considered to have the same rights, requirements, and status as a Matter Product that was certified without use of a Platform. A Derived Matter Product is required to abide by all the same rules as a Matter Product, for example usage of the logo and requirements to be registered in the DCL. An application for a Derived Matter Product must include a completed Matter Security Attestation covering both the Matter Platform and Product portions. 

An application for a Derived Matter Product must indicate the Certification ID of the Matter Certified Platform that was used. The manufacturer of a Derived Matter Product must have access to all applicable test results of the Matter Certified Platform. 

A Derived Matter Product must use the same version of the Matter specification as the version used by the Matter Certified Platform. Testing 

Please refer to the **PICS Tool User Guide** for technical instructions on selecting the applicable Derived Matter Product test cases for a given Certified Platform PICS. 

## Certification Process 

The certification process for Matter Certified Platforms and Derived Matter Products follows the certification steps outlined on the **Certification page** . For more information about testing requirements, contact your selected authorized test provider. For Derived Matter Products, the Certification ID # 

of the Matter Certified Platform is required for the application and can be obtained by contacting the Platform manufacturer. 

**==> picture [472 x 45] intentionally omitted <==**

## Rapid Recert with Matter 

## **Overview** 

The optional Rapid Recert program allows Alliance members to perform a limited form of self-testing for recertification of previously certified products (initial certification of the product must have already been obtained before Rapid Recert may be used). Participation in Rapid Recert does not change or otherwise affect recertification requirements – it is simply an optional way for members to perform self-testing (with ATL validation) in limited cases. The requirements are outlined in Chapter 12 of the **Alliance Certification Policy** . 

## **Requirements** 

Your company must first be qualified by the Alliance to submit Rapid Recert applications (first by having at least one individual attend an Alliance-approved training session, and second by submitting a Rapid Recert qualification application in the Certification Tool). Training sessions are often held at Alliance-sponsored events such as Member Meetings. Note that participating in a Specification Validation Event (SVE) also satisfies this requirement. Other qualification requirements are as follows (see the Alliance Certification Policy, Sec. 12.2, for the full list): 

- Be a registered Member of the **Working Group** which developed the specifications pertaining to the certified product or platform 

- Commit a Point of Contact (PoC) that will responding to any and all Alliance/ATL inquiries in a timely manner. A PoC email and phone 

number will be provided with test results and this will be used by the ATL and the Alliance for such inquiries. 

- PoC training is valid for a period of one (1) year from the month of the last training program attended. At least one valid PoC must be maintained at all times for your company to retain its overall qualification for Rapid Recert (see PoC retraining requirements below). 

- Shall have already obtained initial certification for the Matter products for which they you are requesting self-testing authorization (i.e. Rapid Recert qualification) 

- Maintain and make available to the Alliance certification team, on request, a list of all Member self-test individuals 

- Agree to provide test results in a test report and results format conforming to the Alliance Certification Policy requirements (Section 3.6, "Reporting of Test Results") 

After the qualification application is approved, you will be able to access the Rapid Recert product certification application form. 

Please note that Rapid Recert is only available where the scope of features being retested is substantially the same as the features originally certified and consistent with the Device Type(s) as originally tested and certified. If any new clusters are being added, or new functionality that the Alliance or working group has designated as requiring reassessment, then the associated tests shall be formally run by an Authorized Test Service provider (as an extension of the Rapid Recert testing performed by the member). 

Also note that recertification (whether by Rapid Recert, if available, or any other route) is required when the certified configuration of a product (the combination of HW/FW/enclosure – essentially anything affecting the product itself) changes or is updated. If the changes do not affect the Matter implementation (Matter HW/FW/network transports) of the product, then no 

additional testing would be required, only paperwork (Certification by Similarity). 

If testing is required, Rapid Recert may be available in limited cases (where the scope of the features being retested complies with Rapid Recert policy). Otherwise, full testing at an authorized test provider is required for 

recertification. Please see the Alliance Certification Policy for further detail. Point-of-Contact (PoC) status is on a per-individual basis and is valid for a 

period of one year from the month of the last completed training session. PoC status therefore requires annual (re-)training by attending an Alliance Approved training session. 

## **What does this mean?** 

You need to retrain in time to meet the requirements of the Alliance Certification Policy, Section 12.2.2 “Annual Re-training by the self-test individuals of the member company”. 

Examples of such past training programs are 

- Matter SVE 

- Matter SVE 2 

- Matter SVE 1.1 

- Amsterdam Member Meeting Training Session 

If your Rapid Recert training expires and there are no other PoCs registered for your company, company’s qualification will be affected. 

## **What action do I need to take?** 

To apply or re-apply for the Rapid Recertification Program as individual PoC, attend an Alliance Approved Training sessions as per Sec. 12.2.1.7 of the Certification Policy: “Attendance at an interactive, Alliance-approved training session (either at an Alliance-sponsored event or via some other Allianceapproved scheme – e.g., an ATL-run training program, which is equivalent to SVE participation). A Member participating in an SVE already satisfies this requirement.” 

If another PoC in your company exists with a valid training, and you no longer wish to maintain Point-of-Contact status, then no action is needed to maintain Rapid Recert qualification. 

Please note that, per Sec. 12.2.2, “[i]t is required that all registered Member PoCs be responsive to inquiries from ATLs and/or Alliance Director of Certification.” 

For more information, see the **Alliance Certification Policy** . 

