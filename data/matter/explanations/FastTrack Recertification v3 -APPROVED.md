# FastTrack Recertification Program

- Addendum to Alliance Certification Policy
- October 15, 2025
- Alliance Document Number: Published as: 24-76056-03

### Table of Contents

| 10 | Scope |
| 11 | References |
| 12 | Abbreviations and Terminology |
| 13 | Overview |
| 14 | Checks and Balances |
| 15 | Scope of Allowed Changes |
| 16 | Exclusions |
| 17 | Qualifications |
| 18 | Member Qualification |
| 19 | Maintaining Member Qualification |
| 20 | Product Qualification |
| 21 | Processes & Procedures |
| 22 | Term of Program |
| 23 | Appendix A |
| 24 | Submission during certification: |
| 25 | Unique devices |
| 26 | Large Devices, or device that require systems to function |
| 27 | Privacy and security policies |
| 28 | Results reporting |
| 29 | Exception requests |
| 30 | Requirements for submission to the interop lab |
| 31 | |

# <span id="page-2-0"></span>Scope

- This document details an update to the Alliance Certification Policy [R1] that streamlines the
- issuance of software updates to previously certified products and platforms by making the
- process of recertification more efficient and less costly to members of the Alliance Working
- Groups (WG).
- At this time the program is available for recertification of Matter and Zigbee products and
- platforms. Other working groups may recommend the adoption of this program for their
- standards by discussing it with the Test and Certification Oversight Committee.
- This document also details an additional, simplified and streamlined means of Alliance product
- and platform testing that may be performed by qualified Alliance Members in lieu of testing
- performed by an Alliance-qualified Authorized Test Laboratory (ATL). This document details the
- product, platform and Member qualification requirements for participating in this program as well
- as the procedures to be followed for testing and recertification request submission.
- The FastTrack Recertification Program (FRP) may be used in conjunction with other certification
- programs detailed in [R1] such as Product Family Certification, Portfolio Certification, Matter
- Software Component Solution and Zigbee Direct Component Solution.
- This document is an addendum to the Alliance Certification Policy [R1] as the FastTrack Recert
- program is designed to run for a trial period of one year from inception. During this period,
- modifications to this addendum might be released. At the expiration of the trial period, this
- addendum (with possible modifications) could be:
- a) integrated into the Alliance Certification Policy, or
- b) invalidated depending on the results, or
- c) extended for another one year period.
- The overview and description of the FastTrack Recert Program is for recertification only. There is
- no proposed change or modification to the existing certification process for new devices and
- platforms.

### <span id="page-3-0"></span><sup>60</sup> References

- 61 [R1] CSA Document 15-0288: Connectivity Standards Alliance Certification Policy
- <span id="page-3-1"></span>62 [R2] CSA Document: Interop Lab Rules of Engagement

### <sup>63</sup> Abbreviations and Terminology

| Alliance | Connectivity Standards Alliance |
| ATL | Authorized Test Laboratory |
| BoD | Board of Directors |
| Alliance | Connectivity Standards Alliance |
| CSG | Certification Subgroup |
| DCL | Distributed Compliance Ledger |
| FRP | FastTrack Recertification Program |
| Member | An Alliance member company |
| PoC | Point of Contact |
| Program | FastTrack Recertification Program |
| SC | Steering Committee |
| SVE | Specification Validation Event |
| TCOC | Test and Certification Oversight Committee |
| Vendor | An Alliance member company that<br>produces/sells certified products |
| WG | Working Group |

### <span id="page-4-0"></span>Overview

- The Alliance Working Groups are committed to releasing new versions of the Specification, Test
- Plan and in case of Matter, SDK, regularly. As Matter is an evolving standard, these new SDK
- versions not only include new features and support for more device types, but also a significant
- number of bug fixes and other improvements. Therefore, the Matter SC decided that it is
- important to ensure issues and bugs seen in the market and identified by the WG are addressed
- and fixes available to members in a timely fashion.
- Further, the Matter Working Group has received feedback that many members are not regularly
- updating their products, with a high number still using Matter 1.0. There were several reasons
- cited for this, but the majority of the feedback received was due to the recertification process
- being both very costly and cumbersome. Products running older SDK versions are considered to
- be a major contributor to Matter quality concerns.
- For mature standards like Zigbee the standard continues to evolve with the challenges from new
- competing standards and updates to security. The Zigbee CSG and SC decided that it is important
- to ensure change requests, interoperability issues, security patches and bugs seen in the market
- and identified by the Zigbee Working Group are addressed and fixes are available to deploy in a
- timely and cost effective manner. The cost of recertification, the time at test labs and certification
- approvals tends to hinder regular updates for many members.
- The FastTrack Recert Program is designed to address the above challenges for Alliance Working
- groups by defining an additional recertification process to enable accelerated software updates to
- previously certified devices.
- Note that the existing recertification flows in the Certification Policy remain available to
- Members.
- The Program is grounded in these fundamental principles:
- **Self-Test and Attest**: In addition to the ability to self-test, as in the Rapid Recert program (see section 12 of [R1]), members will also be able to self-attest the validity of the test results. This means that with this Program, members will not be required to employ ATLs for the validation of test results.
- **Rapid In-field Upgrades:** Members are allowed to issue updates to in-field devices and platforms after receiving an acknowledgement from the Alliance Director of Certifications of the receipt of the certification request.
- **Certificate Declaration Generation not required:** The previously required step of generation and issuance of a new Certification Declaration (CD) will no longer be required; for Matter products, only a DCL update is required for the product following approval of a recertification request. The DCL is considered the source of truth for certification status of software versions for Matter products.

### <span id="page-5-0"></span>Program Requirements

- Since the Program removes substantial process burdens and removes an independent validation step relative to the Rapid Recert program, it therefore institutes a few checks and balances to ensure that the Alliance is able to verify the self-test results if needed. To this end, members who qualify for and use the FRP will be required to meet the following conditions:
- 1. Store the output of the tests for all FRP-related testing for a period of at least five years from the date of the approved certification by the Alliance. Members shall share the results with the Alliance upon request.
- 2. Share representative samples of the product or platform or family of products or platforms with the Alliance for use in the Alliance Interoperability Lab pursuant to the rules of the Interop Lab (see Appendix A\). This sample must be provided within 3 months of a product first applying for FastTrack recertification. This will allow the Alliance to test the ensuing software updates and validate the member's test results should the need arise. Refer to Appendix A for details of the device submission process to the Interop Lab.

There is no requirement for the member to wait for the Interop Lab testing results in order to ship the updated product or platform to market or wait to push an over-the-air update to deployed devices.

#### <span id="page-5-1"></span>Scope of Allowed Changes

- The scope of changes to product or platform software permitted under the Program, subject to the listed Exclusions, include the following:
- Security fixes
- Critical bug fixes
- Fixes to improve interoperability
- Updates to a newer spec version
- A spec version which is certifiable at the time of applying for recertification using FRP
- The Alliance reserves the right to restrict use of FRP for certain specification updates
- SDK updates recommended by Matter SC and approved by the TCOC
- Device improvements and bug fixes

#### <span id="page-5-2"></span>Exclusions

- There are a few types of changes that are not permitted to be self-tested under the FastTrack
- Recertification program. Such changes shall rely on the policies and procedures defined in the
- existing Rapid Recertification program (step 2 in Section 12.3 of [R1]) or "full" ATL testing. These
- are:

- New device types or additions or changes to existing clusters
- Adding features not previously tested in a certification context
- Certain exclusions as determined by the Working Group SC and approved by the TCOC
- For every new version of the specification released, the SC may request the Director of Certifications to mandate certain tests and/or areas be validated at an ATL, or to exclude certain tests and/or exemption from validation at an ATL.
- For these types of changes, only the testing of the specific areas that do not qualify for the FRP
- will have to go through the policies and procedures defined in Rapid Recertification, i.e., the ATL
- will need to execute only the tests related to the exclusions listed in the above bullet points. For
- the remainder of the testing, the FRP applies, i.e. the ATL does not need to check the logs of those
- tests.

# <span id="page-6-0"></span>Qualifications

#### <span id="page-6-1"></span>Acquiring Member Qualification

- To participate in the Program, an Alliance Member SHALL meet the same requirements as those for Rapid Recert (sections 12.2.1 and 12.2.2 in [R1]):
- 1. Be a registered Member of the applicable Working Group
- 2. Commit to PoCs responding to Alliance inquiries in a timely manner. A PoC email and phone number will be provided with test results and this will be used by the Alliance for such inquiries.
- 3. Request and be granted FastTrack Program membership from the Director Of Certifications, having attested to meeting all of the applicable requirements.
- 4. Shall have already obtained initial certification for a product or platform for which they are anticipating performing self-testing on.
- 5. Maintain and make available to Alliance certification team on request, a list of all Member self-test individuals.
- 6. When requested by the Alliance to submit results, agree to provide test results in a test report and results format conforming to the Alliance Certification Policy requirements (see section 3.6 of [R1])
- 7. Attendance at an interactive, Alliance-approved training session (either at an Alliance- sponsored event or via some other Alliance-approved scheme – *e.g.*, an ATL-run training program, which is equivalent to SVE participation). A Member having participated in an SVE may satisfy this requirement, but must obtain confirmation from the Director of Certifications.

### <span id="page-6-2"></span>Maintaining Member Qualification

- In order for a member company to maintain their qualification, they must maintain the items listed in the Acquiring Member Qualification and they must do the following.
- 1. Participation in the relevant subgroups of the corresponding Working Group
- a. This will help ensure that the Member stays abreast of changes to testing methodology and proper operation of all test tooling.
- b. Matter requires participation in Matter CSG
- c. Zigbee requires participation in both Zigbee CSG and the relevant Zigbee TSG.
- 2. Self-test individuals must participate in annual training
- a. This requires that one or more of the named individuals from the member company attend an Alliance-approved training session or an SVE as described in step 7 of the Acquiring Member Qualification section, in order to extend the Member's Qualification for another 1-year term.
- Qualified Members utilizing this Program SHALL participate in conformance with policies and procedures in this document. It is required that all registered Member PoCs be responsive to inquiries from ATLs and/or Alliance Director of Certifications. Members should account for PoC leaves of absence, paid time off, etc., by registering additional PoCs for coverage, registering or maintaining an internal mailing list, or by other means.
- The Director of Certifications together with the Alliance certification team will monitor the self-
- test statistics of Members enrolled in the program. Should a Member drop below acceptable levels
- of quality of self-testing, or fail to maintain the requirements for inclusion within the Program, the
- Director of Certifications will discuss remedial measures with the Member's PoC with an
- associated timeline for execution. The Director of Certifications may choose to suspend or revoke
- the Member's right to participate in the Program should satisfactory improvements not be made.

#### Use with Certification Transfer Program (CTP)

The Certification Transfer Program (see section 7 of [R1]) allows a Promoter or Participant member to transfer their certification to another Alliance Member without undergoing testing. The transferring recipient may be an Adopter, Associate, Participant or Promoter member.

FastTrack recertification Program may be used by the transferring member according to the Program requirements described above.

The transfer recipient does not directly use the FastTrack recertification Program since they are not required to do testing. If the transfer recipient has previously registered this product and is just receiving a recertification then it will qualify for Expedited CTP Recertification.

- Expedited CTP recipients are able to issue the updates to in-field devices after receiving an
- acknowledgement from the Alliance Director of Certifications of the receipt of the recertification
- request.

#### <span id="page-8-0"></span>Product and Platform Qualification

- All currently certified products and platforms are eligible for the Program. This includes software
- components as well as hardware-based devices. To use the Program to update a product or
- platform, the product or platform shall already have successfully completed certification and been
- officially granted certified status by the Alliance Director of Certifications in line with Alliance and
- Working Group certification policy. This process typically includes successful completion of ATL-
- or SVE-based testing.

## <span id="page-8-1"></span>Processes & Procedures

- To qualify to participate in the FastTrack Recertification program, a product or platform vendor
- meeting all requirements outlined in this document shall apply via *certification@csa-iot.org* for
- approval by the Director of Certifications. Once approved, the vendor may then choose to retest
- (self-test) an already certified product or platform with the new software version, as required by
- the Alliance Certification Policies, using the following procedure. Note that retesting a certified
- product at an ATL remains an option for vendors even if they are approved to use the FastTrack
- Recertification process.
- The following procedure shall be followed:
- 1. All relevant testing is performed by the product vendor using the latest applicable approved test harness and test scripts, utilizing other devices/components as required by Working Group and Alliance Certification policies.
- 2. The scope of the features eligible for the FRP must be consistent with the device type(s) and platform as originally tested and certified for the product and must fall within the permitted list.
- 3. Testing is supervised by and/or test results are reviewed by one or more vendor PoCs for accuracy and to ensure compliance with test procedures and policies.
- 4. Any errors or anomalies encountered during testing are reviewed by the PoC. Legitimate test failures shall be remediated and relevant test cases re-run to ensure that all required tests pass cleanly on the prospective software version/instantiation.
- 5. Upon successful completion of all relevant tests, a registered PoC shall attest to the veracity and legitimacy of the results bundle in the Declaration of Conformity \(https://groups.csa-iot.org/wg/members-all/document/126\).

- a. The registered PoC must additionally ensure that the test results are stored in a manner that can be retrieved and shared with the Alliance upon request from the Alliance Director of Certifications during the retention period documented under Program Requirements.
- 6. The registered PoC must then send the completed Declaration of Conformity document along with other supporting documents (for example, PICS or attestations) to the Director of Certifications to make a decision on the issuance of certification.
- a. If the software update contains urgent fixes then, when the Director of Certifications acknowledges receipt of the request for issuance of certification, the member company may deploy the software to certified products without waiting for a formal issuance of certification. Note that certification of the updated product is still subsequently required.
- The Program builds upon existing Alliance and Working Group Certification Policy and procedures. All existing aspects of certification remain in force, including but not limited to:
- Certificate issuance
- Distributed Compliance Ledger (DCL) updates, if applicable.
- Term of certification
- Revocation of certification
- <span id="page-9-0"></span>● Alliance certification and ATL testing/processing fees

### Term of Program

- The FastTrack recertification Program will be run as a "pilot" program for a term of one year
- starting November 5, 2024.
- The Test and Certification Oversight Committee (TCOC), in collaboration with the Alliance
- Working Group Steering Committee (SC) shall conduct quarterly reviews of the efficacy and
- operational aspects of the Program, taking into account feedback from Members, ATLs, the
- Director of Certifications and Alliance staff. Improvements to the Program may be implemented
- and this policy revised at any time during the trial period as deemed appropriate. Any changes
- shall be approved by the TCOC and Alliance Board of Directors (BoD).
- At the end of first year, this addendum should be integrated into the Working Group and/or
- Alliance Certification Policy, extended, or discontinued depending on the overall success of the
- Program.

### <span id="page-10-0"></span>Appendix A - Interop Lab Policy and Procedures

- Interoperability testing has proven key to uncovering issues that affect customers. The Alliance is
- seeking to expand that testing to more devices to improve quality. Broad participation in
- interoperability testing encourages device manufacturers and ecosystem vendors to fix
- interoperability issues found in order to improve quality. Issues or failures discovered as a result
- of Alliance interoperability testing do not affect certification, however members are encouraged
- <span id="page-10-1"></span>to use the Program to fix any issues identified.

#### Submission

- For the purposes of FRP, two (2) samples of the certification device shall be submitted to the
- Interop Lab, if 2 samples are not already present at the Interop Lab. These devices will remain in
- the Alliance lab for interop testing indefinitely. Upon receipt of the samples an Alliance
- Interoperability Lab will respond to the submitter with an estimated time of interoperability
- testing completion, with the goal to have testing completed within 3 weeks of samples arriving at
- the lab. (See "Exception requests" below for how to request to opt out of the number of samples,
- or submission). The product submission process begins by following the instructions at
- <span id="page-10-2"></span>https://community.csa-iot.org/page/interoperability.

#### Unique devices

- The Interop Lab aims to have only unique devices (unique in the sense of device/technology
- behavior) in order to utilize the lab resources efficiently. Therefore, the Alliance reserves the right
- to exclude any additional Family certification, Portfolio certification and Certification by Similarity
- (CbS) devices. Only one sample of a Family, Portfolio or CbS group should be sent. This would
- typically be the most feature complete device of the set.
- Example: If you have a light bulb product SKU that is going through certification, and that product
- SKU has 10 additional variant SKUs being sold in different regions, you are not required to submit
- 11 product SKUs to the Interop Lab. One SKU per CbS group, Family, or Portfolio group is
- <span id="page-10-3"></span>sufficient.

#### Large devices, or devices that require systems to function

- There are several categories of devices for which it may be difficult to ship to and/or store in the
- Interop Lab. Washer/dryers, dishwashers, coolers, and AC units are all examples of this kind of
- device. These devices may be submitted with control boards only, or limited samples can be sent
- per request of the Vendor. Vendors of these devices may request exceptions due to the burden of
- shipment being too costly or the number of samples required to be sent is too difficult for the
- member company. These exceptions may be granted at the discretion of the Director of
- Certifications.

<span id="page-11-0"></span> Devices that require a system to function should be sent with that system, or the submitter shall reach out to the Interop lab to ensure a suitable environment in which to execute testing of the samples exists. Privacy, Security, and Results All products participating in Interop Lab, whether for FastTrack Recertification or other reasons, are subject to the rules defined in the Interop Lab Rules of Engagement [R2]. Exception requests Any Member can request an exception to submit the device to the Interop Lab at any time and for any reason. These exception requests may be granted at the sole discretion of the Alliance Director of Certifications. Exceptions granted will typically be one time only and are only valid for a specific time period. An exception for any other product requires a separate exception request. Exception request statistics will be tracked at the Alliance with anonymized reports provided to the Working Group SC or TCOC as requested. Example of possible exceptions: - A product that is not yet launched and requires confidentiality for launch - Similar/more thorough testing is performed as part of their own QA program - Another device from the same manufacturer with identical protocol behavior was already submitted - A device is unable to be hooked up due to required connected systems - A device is unable to be sent to the lab due to its large size or configuration Requirements for submission to the Interop Lab - Two (2) product samples as close to shipping configuration as possible - If only one product is available or able to be shipped due to size/connected systems

<span id="page-11-1"></span>required exceptions requests will need to be submitted.

- All documentation on how to use the device and update it to latest firmware

results may be shared -- preferably the same PoC(s) registered with the Program

- One or more points of contact in case of questions, and with whom Interop Lab testing
