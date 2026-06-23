---
label: Development
order: 99
---

> [!NOTE]
> Some links on this page are only accessible to Alliance members.

The process of developing a Matter product is highly dependent on the device
being developed, the platform being used, and the policies of the company doing the development. There
is no single "best" way to integrate Matter into a product. This guide aims to
address the common considerations for Matter product development.

- Information on the Connectivity Standards Alliance (Alliance) open source SDK is available at the

- Integration of the SDK on specific platforms is covered by the
Platform guides.

## Matter-Specific Product Considerations

The documentation in this section aims to give a brief overview of some of the
common product and factory considerations and challenges that may differ from
non-Matter products.

Matter devices require some material to be provisioned at the factory, after
certification. Some of these materials need to be provisioned on a per-device
basis, some are per-product-line.

Most platforms provide a comprehensive factory data solution customized to
Matter materials. To learn more, see the documentation for your selected
Platform.

### Device Attestation Certificates and Certification Authorities

Device attestation certificates are used to attest devices (or commissionable apps,
in the case of Matter Casting) as being authentic
devices that are manufactured by the stated vendor and certified as a Matter
device. The full attestation procedure and certificate set is described in the
Handbook's
Device Attestation
section. The attestation certificate chain matches the Vendor and Product IDs
declared on the device and in the certification declaration.

The device attestation chain consists of the Device Attestation Certificate
(DAC), which is signed by the Product Attestation Intermediate (PAI), which is
signed by the Product Attestation Authority (PAA).

The DAC and PAI are provided by the product being commissioned (device, app, etc), and the PAA is distributed in the
DCL and does not appear on the product.

As a part of the attestation chain, each attesting product needs to be provisioned with:

- Device attestation private key
- Private, stored in the secure subsystem where possible
- See section 6.3.2 Firmware information of the Matter specification
- Covered by the
- Device Attestation Certificate (DAC)
- Public
- Signed by a PAI
- Product Attestation Intermediate (PAI)
- Public
- Signed by a PAA (whose certificate is found in the DCL)

Attesting products can either opt to purchase DAC provisioning packages from a Matter PKI provider or use their
own PAA by operating a Certification Authority (CA) that conforms to the Connectivity Standards Alliance PKI
requirements. Both of these options have an impact on the operational and/or BOM
costs of the product and should therefore be considered early in the process.
More information about this important product decision can be found in

Operation of a CA is covered by the PKI certificate policies and attested by the
CPS.

A list of PKI providers can be found on the Alliance site:

- Product Attestation Authorities

#### Development DACs

During the development phase, developers often opt to use test DACs using the test Vendor IDs.
The SDK has a number of example DACs that chain up to the SDK test PAAs and these are loaded
by default by the example apps. The development controllers load the test PAAs by default, which
simplifies development.

Development controllers can be switched to use production PAAs by using the `--paa-trust-store-path` parameter.

Test DACs are not permitted during certification testing, and devices must arrive with two instances
with individually provisioned DACs in order to show that the device can meet the requirements
around individual provisioning. Devices at certification are not required to use production DACs.

Device manufacturers may wish to consider joining the Alliance early in the process to understand
the details of the security procedures within the Alliance.

### Certification Declaration (CD)

The Certification Declaration (CD) is provided by the Connectivity Standards Alliance certification team after an attesting product is
certified. It is tied to the Vendor ID and Product ID (or IDs) of the certified
product, and is signed by the Alliance. The public key corresponding to the signing key is
well known and distributed through the DCL.

- CD Signing Certs Root CA

- CD Signing Cert SKIDs

The CD is NOT a standard X.509 certificate, but is
instead a CMS-encoded SignedData payload containing a TLV-encoded structure,
described in section 6.3.1 Certification Declaration of the Matter specification. Certification
Declarations can be viewed using the
Certificate Tool.

The Certification Declaration for the product line is provided after
certification testing, and therefore cannot be hard-coded in the firmware. New
Certification Declarations are issued for each certified firmware update.
Therefore, product development should include a strategy for initial
provisioning and updates of the Certification Declaration.

See
Preparing a Device for Certification
for discussion of CDs used for certification testing.

### Matter Onboarding Materials (QR Codes and Manual Codes)

In addition to DACs, each individual unit needs to be provisioned with its own
onboarding material for discovery and initial commissioning. This includes the
following per-unit items provisioned on the device:

- discriminator
- PAKE verifier (encodes the passcode and PAKE salt)
- PAKE salt

It also includes the following items encoded on the device exterior or
packaging, both of which encode the discriminator and passcode for the
corresponding unit:

- QR code
- manual code

Manual codes are required for all devices, QR codes are optional but
recommended. The rules for QR and manual code inclusions are covered in section
5.7.6 and section 13.6 of the specification.

Information about on-package badging and QR and manual codes are documented in the
Brand Guidelines.

### In-Field Updates to Matter

If a product that has already been released with non-Matter firmware wishes to update
to include Matter functionality, the Matter firmware and supporting materials can be
installed on the in-field devices using their already available, non-Matter update
mechanism. Devices can continue to use their original update mechanism for future
Matter updates, or may opt to use the Matter-specified Over-the-Air (Matter OTA)
update mechanism.

In-field update considerations are
discussed in section 5.8 of the specification. It is important to note that
in-field products are subject to the same per-unit requirements as Out-of-Box
Matter products. It is therefore important to consider not only how to distribute
the firmware but also either how to display the on-boarding material or perform a
background commissioning. It is also necessary to provision the per-unit materials
discussed earlier in this section in a secure manner, using the security materials
present on the device before the update.

## Certification Programs

Product developers should be aware of the various certification programs and how
they may impact the product development process across the entire line.

In particular:

- Products considering software component certification should understand
which types of products and operating environments qualify for this program.
- Products with various SKUs and variants should understand the portfolio
certification program and what constitutes a viable portfolio parent.
- Bridge devices should understand the bridge certification program and how
certification of the supported device types works.

Product manufacturers should be aware that the Alliance has a sunset policy in effect
for prior specification revisions. See the
information.

## Distribution of Over-the-Air Updates (OTA) and Re-Certification

As development continues on the Matter SDK, developers continue to find and fix
bugs, improve performance and maintainability. Ongoing specification development
works to improve interoperability and performance with new features. For these
reasons, its important to consider delivering software updates using either the
Matter OTA mechanism or a manufacturer-specific mechanism.

The mechanism for delivering OTAs is an important product consideration that
needs to be built into the shipping firmware. Update cadence affects the
certification planning for products since all updates need to be
re-certified.
