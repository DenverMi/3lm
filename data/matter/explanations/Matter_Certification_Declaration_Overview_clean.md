# **Matter Certification Declaration Overview**

# <span id="page-2-0"></span>**Certification Declaration**

A Certification Declaration (CD) is a cryptographic document provided by the Connectivity Standards Alliance upon successful completion of certification by a device type. The CD is included in the device firmware to allow a Matter device to assert its protocol compliance as of the date of manufacture of the device.

For more information about the Certification Declaration, refer to *Chapter 6.3. Certification Declaration* from the Matter Specification.

# <span id="page-2-1"></span>**Obtaining a Certification Declaration file**

A member is required to submit its product for Certification. The requirements to submit a Certification request are: Certification application to the CSA, completed Declaration of Conformity (DoC), completed PICS, final test report (for new products). Refer to CSA Certification Policy (Doc. # 07-4842), *Section 2.8 Requirements for Certification,* for more details.

After successful completion of the certification process, the Alliance provides the (signed) Certification Declaration file to the requesting member. This production CD will replace the Testing CD, and may be located in a separate region from the recently certified application firmware.

# <span id="page-2-2"></span>**Certification Declaration PKI**

The Alliance's Certification and Testing team controls a PKI with Certification Authorities for the only purpose of signing the Certification Declaration files. The Root CA (Certificate Authority) signs a controlled number of Intermediate CAs used as Signing Cert and Keys. The Signing Certs and Keys are managed by Alliance Authorized Individuals under the Certification and Testing team.

# <span id="page-2-3"></span>**Certification Declaration Signing Certs and Keys**

The 'Certification Declaration Signing Cert' is a certificate used to sign a Certification Declaration file. The private Key associated with the Signing Cert is stored in an HSM managed by Alliance Authorized Individuals.

### <span id="page-2-4"></span>**Development and Testing CD - Signing Cert and Key**

The Matter SDK contains a Signing Certificate with its Private Key used for testing and development. The manufacturers can use these cert/key to sign the Testing CD, so no Alliance involvement is needed. These files can be used during development to create a Testing CD with the product information, the certification\_type may be set to "provisional" during Validation

Events. After the certification is completed, the Testing CD is replaced with the Production CD provided by the Alliance.

### <span id="page-3-0"></span>**Production CD - Signing Cert**

The Production CD Signing Certs are available in the Distributed Compliance Ledger (DCL) (Main-Net).

- **●** Web User Interface: <https://webui.dcl.csa-iot.org/>
- **●** CSA ON host DCL endpoints:

| Endpoint | Host | Port | Usage |
| REST | https://on.dcl.csa-iot.org | 443 | REST API |
| gRPC | on.dcl.csa-iot.org | 8443 | gRPC API |
| Tendermint RPC | https://on.dcl.csa-iot.org | 26657 | CLI client |

Certification Declaration key records on Main-Net DCL

| Subject as Text | Subject | Subject Key Id | | | | |
| Matter Certification and Testing CA | MFIxDDAKBgNVBAoMA0NTQTEsMCoGA1UEAwwjTWF0 dGVyIENlcnRpZmljYXRpb24gYW5kIFRlc3RpbmcgQ0ExFD ASBgorBgEEAYKifAIBDARDNUEw | 97:E4:69:D0:C5:04:14:C2:6F:C7:01:F7: 7E:94:77:39:09:8D:F6:A5 | | | | |
| Certification Declaration Signing Key 001 | MFgxDDAKBgNVBAoMA0NTQTEyMDAGA1UEAwwpQ2Vy dGlmaWNhdGlvbiBEZWNsYXJhdGlvbiBTaWduaW5nIEtle SAwMDExFDASBgorBgEEAYKifAIBDARDNUEw | FE:34:3F:95:99:47:76:3B:61:EE:45:39: 13:13:38:49:4F:E6:7D:8E | | | | |
| Certification Declaration Signing Key 002 | MFgxDDAKBgNVBAoMA0NTQTEyMDAGA1UEAwwpQ2Vy dGlmaWNhdGlvbiBEZWNsYXJhdGlvbiBTaWduaW5nIEtle SAwMDIxFDASBgorBgEEAYKifAIBDARDNUEw | DD:04:DB:58:5B:21:4C:1C:58:15:87:E6 :56:8D:F4:87:B6:DD:C7:01 | | | | |
| Certification Declaration Signing Key 003 | MFgxDDAKBgNVBAoMA0NTQTEyMDAGA1UEAwwpQ2Vy dGlmaWNhdGlvbiBEZWNsYXJhdGlvbiBTaWduaW5nIEtle SAwMDMxFDASBgorBgEEAYKifAIBDARDNUEw | 47:10:35:E7:C0:4E:AA:A8:BE:7C:4D:4C :13:E3:E4:C2:09:95:A8:4B | | | | |
| Certification Declaration Signing Key 004 | MFgxDDAKBgNVBAoMA0NTQTEyMDAGA1UEAwwpQ2Vy dGlmaWNhdGlvbiBEZWNsYXJhdGlvbiBTaWduaW5nIEtle SAwMDMxFDASBgorBgEEAYKifAIBDARDNUEw | F6:86:03:A3:69:2E:98:10:72:41:9E:A1: E1:AB:38:54:BD:77:95:D3 | | | | |
| Certification Declaration Signing Key 005 | MFgxDDAKBgNVBAoMA0NTQTEyMDAGA1UEAwwpQ2Vy dGlmaWNhdGlvbiBEZWNsYXJhdGlvbiBTaWduaW5nIEtle SAwMDMxFDASBgorBgEEAYKifAIBDARDNUEw | 63:7F:26:34:AD:62:EA:FE:6A:F6:62:EF: B9:6F:6F:D2:FC:BF:FC:2F | | | | |

The generation of each of these keys were held under a Ceremony. The Ceremony recordings and related documentation are available here.

# <span id="page-3-1"></span>**Download 'Production CD - Signing Cert' from DCL**

### <span id="page-3-2"></span>**Web User Interface**

- 1. Open the DCL Web User Interface (ie. <https://webui.dcl.csa-iot.org/>)
- 2. Go to the 'PKI' section
- 3. On the search box, type "Matter Certification and Testing CA"

4. Click on the "Download" button from a Root CA or Intermediate CA to get the certificate PEM file.

### <span id="page-4-0"></span>**CLI Client**

- 1. Download the 'dcld' CLI client
- 2. Configure the ON endpoint. ie to use CSA's ON:

```
$ ./dcld config chain-id "main-net"
$ ./dcld config node "https://on.dcl.csa-iot.org:26657"
```

3. Query the a Certificate using CLI command:

```
$ ./dcld query pki x509-cert \
--subject <Certificate Subject> \
--subject-key-id <Certificate Subject Key ID>
```

#### *ie. Matter Certification and Testing CA:*

```
$ ./dcld query pki x509-cert \
--subject
MFIxDDAKBgNVBAoMA0NTQTEsMCoGA1UEAwwjTWF0dGVyIENlcnRpZmljYXRpb24gYW5kIFRlc3Rpbm
cgQ0ExFDASBgorBgEEAYKifAIBDARDNUEw \
--subject-key-id 97:E4:69:D0:C5:04:14:C2:6F:C7:01:F7:7E:94:77:39:09:8D:F6:A5
```

4. Query the all Intermediate Certificates by issuer (root cert's subjectKeyId) using CLI command:

```
$ ./dcld query pki all-child-x509-certs \
--subject <Root Certificate Subject> \
--subject-key-id <Root Certificate Subject Key ID>
```

*ie. Matter Certification and Testing CA's child certificates (Intermediate CAs):*

```
$ ./dcld query pki all-child-x509-certs \
--subject
MFIxDDAKBgNVBAoMA0NTQTEsMCoGA1UEAwwjTWF0dGVyIENlcnRpZmljYXRpb24gYW5kIFRlc3Rpbm
cgQ0ExFDASBgorBgEEAYKifAIBDARDNUEw \
--subject-key-id 97:E4:69:D0:C5:04:14:C2:6F:C7:01:F7:7E:94:77:39:09:8D:F6:A5
```

Information about CLI commands here.

### <span id="page-4-1"></span>**REST API**

- 1. Open a web browser
- 2. Query a Certificate using the subject and subjectKeyId: https://on.dcl.csa-iot.org/dcl/pki/certificates/{**subject**}/{**subjectKeyId**}
- *ie. Matter Certification and Testing CA* https://on.dcl.csa-iot.org/dcl/pki/certificates/MFIxDDAKBgNVBAoMA0NTQTEsMCoGA1 UEAwwjTWF0dGVyIENlcnRpZmljYXRpb24gYW5kIFRlc3RpbmcgQ0ExFDASBgorBgEEAYKif

AIBDARDNUEw/97%3AE4%3A69%3AD0%3AC5%3A04%3A14%3AC2%3A6F%3AC7%3A01 %3AF7%3A7E%3A94%3A77%3A39%3A09%3A8D%3AF6%3AA5

3. Query the Child Certificates by issuer (root cert's subject) and authorityKeyId (root cert's subjectKeyId)

https://on.dcl.csa-iot.org/dcl/pki/child-certificates/{**issuer**}/{**authorityKeyId**}

*ie. Matter Certification and Testing CA*

https://on.dcl.csa-iot.org/dcl/pki/child-certificates/MFIxDDAKBgNVBAoMA0NTQTEsMCo GA1UEAwwjTWF0dGVyIENlcnRpZmljYXRpb24gYW5kIFRlc3RpbmcgQ0ExFDASBgorBgEEA YKifAIBDARDNUEw/97%3AE4%3A69%3AD0%3AC5%3A04%3A14%3AC2%3A6F%3AC7%3 A01%3AF7%3A7E%3A94%3A77%3A39%3A09%3A8D%3AF6%3AA5

Information about REST API here.

# <span id="page-5-0"></span>**Certification Declaration Signing Procedure**

For testing through an SVE or through a certification program, a manufacturer MAY use a Certification Declaration (CD) with certification type set to provisional (certification\_type = 1) to indicate that this PID/VID/SoftwareVersion combo has not been certified yet.

Upon a successful certification, an Official Certification Declaration with the certification type set to certified (certification\_type = 2) SHALL be signed by the CSA Certification and Testing team and provided to the manufacturer for inclusion in the production version of the product. Lastly, the CSA Certification and Testing team will add an entry in the DCL to announce the certification of this PID/VID/SoftwareVersion.

**Note:** The Certification Declaration signing procedure follows the same structure as the certification\\_declaration\\_test\\_vector.py example from the connectedhomeip-spec repository with the difference that it uses an HSM instead of a PEM file for the private Key to sign the Certification Declaration blobs.

# <span id="page-5-1"></span>**Certification Declaration Verification Procedure (to be added to specification)**

To verify a Certification Declaration file, commissioners with access to the DCL information SHALL check the DCL information for this PID/VID/SoftwareVersion for the up-to-date status of the certification.

If the DCL does not contain any entries pertaining to the particular PID/VID/SoftwareVersion combo, the commissioners SHALL treat the product as uncertified.

### <span id="page-6-0"></span>**Appendix A. Alliance Certificate Authorities raw text**

#### <span id="page-6-1"></span>**Matter Certification and Testing CA**

----BEGIN CERTIFICATE----

MIICATCCAaegAwIBAgIHY3Nhcm9vdDAKBggqhkjOPQQDAjBSMQwwCgYDVQQKDAND U0ExLDAqBgNVBAMMI01hdHRlciBDZXJ0aWZpY2F0aW9uIGFuZCBUZXN0aW5nIENB MRQwEgYKKwYBBAGConwCAQwEQzVBMDAgFw0yMjA3MDcxOTI4MDRaGA8yMTIyMDYx MzE5MjgwNFowUjEMMAoGA1UECgwDQ1NBMSwwKgYDVQQDDCNNYXR0ZXIgQ2VydGlm aWNhdGlvbiBhbmQgVGVzdGluZyBDQTEUMBIGCisGAQQBgqJ8AgEMBEM1QTAwWTAT BgcqhkjOPQIBBggqhkjOPQMBBwNCAAQ4SjrDq12+y3IP5iEdPK1IYm/3EaCkkp+t 2GD44nf/wN4fPrYzejSEe1o6BW6ocQ6Td+7t7iUXA/3ZNQE1y45Io2YwZDASBgNV HRMBAf8ECDAGAQH/AgEBMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQU1+Rp0MUE FMJvxwH3fpR3OQmN9qUwHwYDVR0jBBgwFoAU1+Rp0MUEFMJvxwH3fpR3OQmN9qUwCgYIKoZIzj0EAwIDSAAwRQIgearlB0fCJ49UoJ6xwKPd1PEopCOL9jVCviODE1eI+mQCIQDvvDCKi7kvj4R4BoFS4BVZGCk4zJ84W4tfTTfu891RbQ==

----END CERTIFICATE----

#### <span id="page-6-2"></span>**Certification Declaration Signing Key 001**

----BEGIN CERTIFICATE----

MIICBzCCAa2gAwIBAgIHY3NhY2RrMTAKBggqhkjOPQQDAjBSMQwwCgYDVQQKDAND U0ExLDAqBgNVBAMMI01hdHRlciBDZXJ0aWZpY2F0aW9uIGFuZCBUZXN0aW5nIENB MRQwEgYKKwYBBAGConwCAQwEQzVBMDAgFw0yMjEwMDMxOTI4NTVaGA8yMDcyMDky MDE5Mjg1NVowWDEMMAOGA1UECgwDQ1NBMTIwMAYDVQQDDC1DZXJ0aWZpY2F0aW9uIER1Y2xhcmF0aW9uIFNpZ25pbmcgS2V5IDAwMTEUMBIGCisGAQQBgqJ8AgEMBEM1QTAwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATN7uk+RPi3K+PRqcB+IZaLmv/ztAPwXhZp17Hlyu5vx3FLQufiNpXpLNdjVHOigK5ojze7lInhFim5uU/3sJkpo2YwZDASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQU/jQ/1Z1Hdjth7kU5ExM4SU/mfY4wHwYDVR0jBBgwFoAU1+Rp0MUEFMJvxwH3fpR3OQmN9qUwCgYIKoZIzj0EAwIDSAAwRQIgEDWOcdKsVGtUh3evHbBd1lq4aS7yQtOp6GrOQ3/zXBsCIQDxorh2RXSaI8m2RCcoWaiWa0nLzQepNm3C2jrQVJmC2Q==----ENDCERTIFICATE----

### <span id="page-6-3"></span>**Certification Declaration Signing Key 002**

----BEGIN CERTIFICATE----

MIICCDCCAa2gAwIBAgIHY3NhY2RrMjAKBggqhkjOPQQDAjBSMQwwCgYDVQQKDAND
U0ExLDAqBgNVBAMMI01hdHRlciBDZXJ0aWZpY2F0aW9uIGFuZCBUZXN0aW5nIENB
MRQwEgYKKwYBBAGConwCAQwEQzVBMDAgFw0yMjEwMDMxOTM2NDZaGA8yMDcyMDky
MDE5MzY0NlowWDEMMAoGA1UECgwDQ1NBMTIwMAYDVQQDDC1DZXJ0aWZpY2F0aW9u
IER1Y2xhcmF0aW9uIFNpZ25pbmcgS2V5IDAwMjEUMBIGCisGAQQBgqJ8AgEMBEM1
QTAwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQDGTfo+UJRBF3ydFe7RiU+43V0
jBKuKFV9gCe51MNW2RtAjP8yJ1AXs1+Mi6IFFtXIOVK3JBKAE9/Mj5XSAKkLo2Yw
ZDASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQU
3QTbWFshTBxYFYfmVo30h7bdxwEwHwYDVR0jBBgwFoAU1+Rp0MUEFMJvxwH3fpR3
OQmN9qUwCgYIKoZIzj0EAwIDSQAwRgIhAJruzxZ806CP/LoQ07PN9xAbjLdwUalV
h0Qfx304Tb92AiEAk+jnf2qtyfKyTEHpT3Xf3bfekqUOA+8ikB1yjL5oTsI=
----END CERTIFICATE----

### <span id="page-7-0"></span>**Certification Declaration Signing Key 003**

----BEGIN CERTIFICATE----

MIICBjCCAa2gAwIBAgIHY3NhY2RrMzAKBggqhkjOPQQDAjBSMQwwCgYDVQQKDAND
U0ExLDAqBgNVBAMMI01hdHRlciBDZXJ0aWZpY2F0aW9uIGFuZCBUZXN0aW5nIENB
MRQwEgYKKwYBBAGConwCAQwEQzVBMDAgFw0yMjEwMDMxOTQxMDFaGA8yMDcyMDky
MDE5NDEwMVowWDEMMAoGA1UECgwDQ1NBMTIwMAYDVQQDDC1DZXJ0aWZpY2F0aW9u
IER1Y2xhcmF0aW9uIFNpZ25pbmcgS2V5IDAwMzEUMBIGCisGAQQBgqJ8AgEMBEM1
QTAwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASfV1zV/bdSHxCk3zHwc5ErYUco
8tN/W2uWvCy/fAsRlpBXfVVdIaCWYKiwgqM56lMPeoEthpO1b9dkGF+rzTL1o2Yw
ZDASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQU
RxA158BOqqi+fE1ME+PkwgmVqEswHwYDVR0jBBgwFoAU1+Rp0MUEFMJvxwH3fpR3
OQmN9qUwCgYIKoZIzj0EAwIDRwAwRAIgIFecbY+1mVVNqxH9+8IMB8+safdyIJU2
AqqtZ/w7AkQCIHiVlYTaCnJsnW5/cvj9GfIv7Eb0cjdmcAkrYGbnPQzX
----END CERTIFICATE----

### <span id="page-7-1"></span>**Certification Declaration Signing Key 004**

----BEGIN CERTIFICATE----

MIICBjCCAa2gAwIBAgIHY3NhY2RrNDAKBggqhkjOPQQDAjBSMQwwCgYDVQQKDAND U0ExLDAqBgNVBAMMI01hdHRlciBDZXJ0aWZpY2F0aW9uIGFuZCBUZXN0aW5nIENB MRQwEgYKKwYBBAGConwCAQwEQzVBMDAgFw0yMjEwMDMxOTQzMjFaGA8yMDcyMDky MDE5NDMyMVowWDEMMAoGA1UECgwDQ1NBMTIwMAYDVQQDDC1DZXJ0aWZpY2F0aW9u IER1Y2xhcmF0aW9uIFNpZ25pbmcgS2V5IDAwNDEUMBIGCisGAQQBgqJ8AgEMBEM1 QTAwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAR8/I2IEKic9PoZF3jyr+x4+FF6 16P1f8ITutiI42EedP+2hL3rqKaLJSNKXDWPNzurm20wThMG3XYgpSjRFhwLo2Yw ZDASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQU 9oYDo2kumBByQZ6h4as4VL13ldMwHwYDVR0jBBgwFoAUl+Rp0MUEFMJvxwH3fpR3 OQmN9qUwCgYIKoZIzj0EAwIDRwAwRAIgLqAfkbtLYYdmQsnbn0CWv3G1/lbE36nz HbLbW5t6PY4CIE8oyIHsVhNSTPcb3mwRp+Vxhs8tKhbAdwv5BGgDaAHj

### <span id="page-7-2"></span>**Certification Declaration Signing Key 005**

----BEGIN CERTIFICATE----

MIICBzCCAa2gAwIBAgIHY3NhY2RrNTAKBggqhkjOPQQDAjBSMQwwCgYDVQQKDAND
U0ExLDAqBgNVBAMMI01hdHRlciBDZXJ0aWZpY2F0aW9uIGFuZCBUZXN0aW5nIENB
MRQwEgYKKwYBBAGConwCAQwEQzVBMDAgFw0yMjEwMDMxOTQ3MTVaGA8yMDcyMDky
MDE5NDcxNVowWDEMMAoGA1UECgwDQ1NBMTIwMAYDVQQDDC1DZXJ0aWZpY2F0aW9u
IER1Y2xhcmF0aW9uIFNpZ25pbmcgS2V5IDAwNTEUMBIGCisGAQQBgqJ8AgEMBEM1
QTAwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARDilLGYqKm1yZH+V63UxNu5K4P
2zqpwWkxQms9CGf5EDrn16G4h+n4E6byb3a7zak1k3h8EneMqPKXXcRaIEL5o2Yw
ZDASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQU
Y38mNK1i6v5q9mLvuW9v0vy//C8wHwYDVR0jBBgwFoAU1+Rp0MUEFMJvxwH3fpR3
OQmN9qUwCgYIKoZIzj0EAwIDSAAwRQIhAM1HQpvkHKxLJByWaSYAPRZgh3Bis18W
AViq7c/mtzEAAiBZO01Ve6Qo9iQPIBWZaVx/S/YSNO9uKNa/pvFu3V+nIg==
----END CERTIFICATE----
