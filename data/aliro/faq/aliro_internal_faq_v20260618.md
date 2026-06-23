# Aliro Internal FAQ

source_type: internal_faq
program: Aliro
doc_type: reference
audience: internal

## Q1. Is there an official "Golden Unit" for Aliro certification testing?

**Answer:** No. At present, the Aliro Certification Program does not define an official Aliro Golden Unit.

For development and evaluation purposes, the Alliance provides the Aliro Actuator project through GitHub. However, it is not considered an official certification reference device or Golden Unit.

**Key point:** The Aliro Actuator project may be useful for development or evaluation, but it is not an official certification Golden Unit.

**Search aliases:** Aliro Golden Unit; Aliro reference device; Aliro Actuator; official Golden Unit; certification reference device

## Q2. Where can I obtain information about connecting with Apple Wallet or Google Wallet APIs?

**Answer:** Contact Apple or Google directly.

Aliro defines interoperability between Readers and User Devices. Platform-specific topics are outside the scope of the Aliro Certification Program and are managed by the respective platform providers.

Out-of-scope platform topics include:

* Wallet APIs
* Secure Element access
* Background operation
* OS integration
* Partner onboarding requirements

The Alliance does not maintain contact persons for the platform providers.

**Key point:** Aliro certification does not cover Apple Wallet or Google Wallet API access or platform onboarding.

**Search aliases:** Apple Wallet API; Google Wallet API; Secure Element access; OS integration; partner onboarding; platform provider contact

## Q3. Does Aliro certification include NFC, Bluetooth, or UWB certification?

**Answer:** No. Aliro certification does not include NFC, Bluetooth, or UWB certification.

Aliro relies on external Dependent Certification Programs for connectivity technologies such as:

* NFC
* Bluetooth
* UWB

Aliro certification testing validates compliance with the Aliro specification, including Aliro protocol and functionality. The underlying NFC, Bluetooth, and UWB technologies are certified through their respective Dependent Certification Programs.

**Key point:** Aliro certification covers Aliro protocol and functionality, but connectivity technologies require their own dependent certifications.

**Search aliases:** NFC certification; Bluetooth certification; UWB certification; Dependent Certification Program; DCP; Aliro connectivity certification

## Q4. What are the requirements for inheriting certification from a previously certified connectivity component?

**Answer:** The certified connectivity capabilities must remain unchanged.

Aliro certification relies on Dependent Certification Programs for NFC, Bluetooth, and UWB. The applicant must provide the applicable Attestation of Network Transport Protocol Certification for each supported network transport protocol, such as NFC, BLE, or UWB.

If the final product changes certified connectivity capabilities, such as RF characteristics, antenna design, or certified wireless functionality, the existing attestation may no longer be applicable. Additional confirmation or certification through the relevant dependent certification program may be required.

Attestations are provided and signed by the member. The Alliance presumes the attestation is valid on a trust basis under the Certification Policy. If there are inconsistencies in the Certification Application, the Alliance may exercise rights such as revoking certifications.

**Key point:** Certification inheritance depends on unchanged certified connectivity capabilities and valid member-provided attestations.

**Search aliases:** certification inheritance; certified component; connectivity component; Attestation of Network Transport Protocol Certification; NFC attestation; BLE attestation; UWB attestation; RF change; antenna change

## Q5. If we use a certified NFC, Bluetooth, UWB module, or Aliro Software Component, is Aliro certification no longer required?

**Answer:** No. Aliro certification is still required.

Using certified components may allow portions of the certification process to be inherited or simplified, but it does not exempt the final product from Aliro certification.

**Key point:** Certified components may reduce or simplify testing, but the final product still needs Aliro certification.

**Search aliases:** certified module; certified component; Aliro Software Component; final product certification; certification still required; inherited certification

## Q6. Is certification still required when using a certified Aliro Software Component?

**Answer:** Yes. Certification is still required.

Applications that use an unmodified certified Aliro Software Component may qualify under the **"Aliro-capable UIC making use of Certified Component"** category.

Although this may reduce the amount of testing required, documentation submission, Alliance certification application, and Alliance approval are still required.

**Key point:** A certified Aliro Software Component can reduce testing scope, but it does not eliminate certification, documentation, application, or approval requirements.

**Search aliases:** certified Aliro Software Component; Aliro-capable UIC; Certified Component; reduced testing; documentation submission; Alliance approval

## Q7. What is the difference between Testing and Certification?

**Answer:** The Alliance Certified program maintains a strict distinction between testing and certification.

Testing is the process of verifying conformance to Alliance Standards.

Certification is the official recognition that a product conforms to an Alliance Standard and that the product manufacturer conforms to the relevant policies of the Alliance Certified program.

**Key point:** Testing verifies conformance, while certification grants official recognition under the Alliance Certified program.

**Search aliases:** testing versus certification; conformance testing; Alliance certification; official recognition; Alliance Certified program
