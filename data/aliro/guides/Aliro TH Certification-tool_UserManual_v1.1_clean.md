## Aliro Certification Tool User Manual

## 1. Introduction

The Aliro Certification Tool is a test harness and tooling environment designed to simplify development, testing, and certification of Aliro devices, as defined by the Connectivity Standards Alliance Access Control Working Group (ACWG).

## This tool provides:

- A browser-based user interface to configure test projects.
- Automated and semi-automated execution of test cases based on the Aliro specification and ACWG CSG Test Plan.
- Integration with Aliro-specific test scripts and the Aliro Actuator.

## This version of the Aliro Certification Tool uses:

- Aliro Specification Version 1.0
- Aliro Test Plan Version 1.0

## Intended audience

- Device vendors implementing Aliro Readers and User Devices.
- Internal development, QA, and pre-certification teams.
- Test and certification lab engineers.

## 2. References

1. Aliro Specification 1.0
2. Aliro Test Plan Version 1.0
3. 3.
4. Aliro Certification Tool Repository: Aliro TestHarness\_CertificationTool\_v1.0.zip/aliro-certificationtool
4. Aliro Actuator Repository and Murata Firmware Instructions:

Aliro TestHarness\_CertificationTool\_v1.0.zip/aliro-actuator

(See the third\_party folder for Murata firmware update information.)

5. Raspberry Pi Imager:

https://www.raspberrypi.com/software/

## 3. Aliro Test Harness Overview

## 3.1 Architecture and Layout

The Aliro Certification Tool runs on a Raspberry Pi 4 with Ubuntu Server 22.04.x LTS (64-bit) and consists of:

- Core Test Harness containers
- o Backend services (logic, scheduling, orchestration).
- o Web frontend (GUI).
- o Database (projects, test runs, configurations).
- Aliro test collections
- o Located in test\_collections/aliro .
- o The setup.sh script builds Aliro-specific components, including NFC drivers.
- Hardware interfaces
- o NFC: NXP PN7160 evaluation kits
-  OM27160A1EVK (I2C) or OM27160B1EVK (SPI).
- o BLE/UWB: Murata LBUA0VG2BP-EVK-P via micro-USB.

## · System service

- o A systemd service (e.g. aliro-th ) starts the Test Harness automatically at boot.

Here below is an illustration of the set-up:

## 3.2 Data Model

## Key data entities:

- Project
- o Represents a device or campaign under test.
- o Stores Aliro test parameters (keys, identifiers, certificates).
- Test Suite
- o Group of related test cases (e.g., Reader tests, User Device tests, step-up tests).
- Test Case
- o Individual test script, mapped to ACWG test plan cases.

## · Test Run

- o Execution of selected test cases under a specific project configuration.
- o Records operator, time, verdicts, and logs.
- Test Parameters
- o Aliro-specific cryptographic and identity data used by scripts.

## 3.3 Data Flow

## A typical flow:

1. User creates a Project and configures test parameters.
2. User creates a Test Run with selected test suites/cases.
3. The harness orchestrates scripts that use the Aliro Actuator as protocol peer.
4. Test results and logs are stored and accessible via the GUI or CLI.

## 4. Getting Started

## 4.1 System Requirements

## Hardware

- Raspberry Pi 4 Model B
- o 8 GB RAM recommended (4 GB may work).
- o Micro SD card: 16 GB or more.
- o Power supply.
- NFC interface:
- o OM27160A1EVK (I2C) or OM27160B1EVK (SPI).
- BLE/UWB interface:
- o Murata LBUA0VG2BP-EVK-P + micro-USB to USB-A cable.
- Network:
- o LAN/Wi-Fi network with Internet access.
- o Optional Ethernet cable.

## Optional:

- Micro-HDMI to HDMI cable.
- Monitor and USB keyboard.

## 4.2 Installing Ubuntu on SD-Card

1. Download and run Raspberry Pi Imager:
2. CHOOSE DEVICE: select 'Raspberry Pi 4'.
3. CHOOSE OS → Other general-purpose OS → Ubuntu → select one of:
4. o Ubuntu Server 22.04.3 LTS (64-bit)
5. o Ubuntu Server 22.04.4 LTS (64-bit)
6. o Ubuntu Server 22.04.5 LTS (64-bit)

```
https://www.raspberrypi.com/software/
```

Important : You must pick exactly one of the above versions.

4. CHOOSE STORAGE: select the micro SD card.
5. Click NEXT.
6. In OS Customization:
4. o Set hostname (e.g. aliro-th-pi1 ).
5. o Set username and password.
6. o Optionally configure Wi-Fi (only password-protected networks).
7. o Enable SSH with password authentication.
7. Save settings and write the OS to the SD card.
8. Wait for writing and verification to complete.

## 4.3 Flashing Murata UWB Board

Before use with the Test Harness, the Murata board firmware needs to be updated. The firmware file is named 'uwb\_ble\_device\_fw-v05.00.03.bin' (or a later version) and can be found at https://github.com/NXP/aliro-th-additions. The board can be updated with the DK6Programmer tool (Windows only), or with MCUxpresso and a debugger.

For more details, see https://github.com/csa-access-control/aliroactuator/blob/main/third\_party/readme.md

## 4.4 Assembling the Raspberry Pi

1. Ensure the Raspberry Pi is powered off.
2. Attach OM27160 evaluation kit to the Raspberry Pi as per its hardware guide.
3. Connect Murata LBUA0VG2BP-EVK-P via the micro-USB cable.
4. Insert the micro SD card.
5. Optionally connect Ethernet, monitor, and keyboard.
6. Power on the Raspberry Pi.

## 4.5 Connecting to the Raspberry Pi

## 4.5.1 SSH using Hostname

1. Wait for the Pi to boot.
2. On your PC:
3. Enter the password.

```
sh ssh <username>@<hostname>.local # Example: ssh ubuntu@aliro-th-pi1.local
```

If hostname resolution fails, use the IP address.

## 4.5.2 SSH using IP Address

1. Wait for the Pi to boot.
2. On your PC:
3. Enter the password.

```
sh ssh <username>@<ip-address> # Example: ssh ubuntu@192.168.2.9
```

To discover the IP:

- On Linux/macOS:
- On Windows:

```
sh arp -na | grep -i "b8:27:eb\|dc:a6:32\|e4:5f:01"
```

```
bat arp -a | findstr b8-27-eb dc-a6-32 e4-5f-01
```

## 4.5.3 Using Monitor and Keyboard

Log in locally with the configured username and password (default Ubuntu: ubuntu / ubuntu if unchanged).

## 4.6 Installing the Aliro Certification Tool

Run the auto-installer:

Enter your password when prompted. At the end, choose option 1 to reboot.

Notes:

- Installation can take over an hour, depending on network speed.
- First reboot after installation may take 5+ minutes.

## 4.7 Initial Setup and Start-up

1. Initialize submodules:
2. Set up Aliro test collection:
3. o SPI kit:
4. o I2C kit:
3. Start the harness:

| sh | |
| cd | ~/aliro-certification-tool |

The harness also starts automatically at boot.

## 5. Using the Web GUI

## 5.1 Opening the GUI

1. Ensure your PC and the Raspberry Pi are on the same network.
2. In a browser, navigate to:
3. Wait a couple minutes after boot before connecting.

```
http://<raspberry-pi-ip-address> Example: http://192.168.2.9
```

To find the Pi IP on the Pi:

```
sh hostname -I
```

## 5.2 Creating and Configuring a Test Project

1. Click 'Create Project'.
2. Enter a project name.
3. Click 'Edit' to open the JSON configuration.
4. Locate the "test\_parameters" field (default null ).
5. For Reader tests, set parameters such as:
6. Click 'Update' to save.
7. Click 'Create' to create the project.

```
json "test_parameters": { "dut_reader_public_key": "043928f3...c5d34ee", "dut_reader_group_identifier": "00113344667799AA00113344667799AA", "dut_reader_issuer_group_identifier": "00113344667799AA00113344667799AB", "dut_reader_group_sub_identifier": "113344667799AA00113344667799AA00", "dut_reader_group_resolving_key": "00000000000000000000000000000000" }
```

You can edit parameters later by clicking the pencil icon on the project row.

## 5.3 Creating and Running a Test Run

1. On the projects list, click the triangular 'Go To Test-Run' icon next to the project.
2. Click 'Create new Test Run'.
3. Choose or create an 'Operator Name' in the top right.
4. Select one or more test suites or individual test cases.
5. Click 'Start' to execute.

The GUI displays test status and logs in real time.

## 6. Test Parameters

The Aliro test scripts depend on cryptographic keys, group identifiers, and certificates configured in test\_parameters .

You can configure them at project creation or later by editing the project.

## 6.1 Test Parameters for Reader Tests

- dut\_reader\_public\_key
- dut\_reader\_group\_identifier
- dut\_reader\_issuer\_group\_identifier

Public key of the Reader DUT.

Format: DER-encoded HEX or PEM with \n .

Group Identifier of the Reader DUT.

Format: HEX string.

Group Identifier for Reader Issuer CA certificate.

Format: HEX string.

- dut\_reader\_group\_sub\_identifier
- dut\_reader\_group\_resolving\_key
- th\_access\_credential\_private\_key / th\_access\_credential\_public\_key

Sub-group Identifier for Reader DUT.

Format: HEX string.

Group resolving key used in BLE tests.

Format: HEX string.

Keys for the user access credential simulated by the tool.

Format: DER HEX or PEM with \n .

- dut\_reader\_issuer\_public\_key
- th\_credential\_issuer\_private\_key / th\_credential\_issuer\_public\_key
- th\_credential\_issuer\_ca\_private\_key / th\_credential\_issuer\_ca\_public\_k ey

Reader System Issuer CA certificate public key (for certificate verification). Format: DER HEX or PEM with \n .

Keys used to sign simulated Access Documents for the Reader.

Format: DER HEX (for private key: 138 or 32 bytes) or PEM with \n .

Keys used to sign simulated Access Document Certificates for the Reader.

Format: DER HEX (for private key: 138 or 32 bytes) or PEM with \n .

- dut\_access\_element\_id

Access Element ID requested by the Reader.

Format: string.

## 6.2 Test Parameters for User Device Tests

Private and public key fields must match: either configure both or none.

- th\_reader\_private\_key / th\_reader\_public\_key
- th\_reader\_group\_identifier
- th\_reader\_sub\_group\_identifier
- th\_reader\_certificate

Keys for the simulated Reader.

Format: DER HEX (for private key: 138 or 32 bytes) or PEM with \n .

Group Identifier for simulated Reader.

Format: HEX string.

Sub-group Identifier for simulated Reader.

Format: HEX string.

Reader certificate used for LOAD CERT and AUTH1 commands.

Format: HEX string.

- th\_reader\_group\_resolving\_key
- th\_reader\_spsm
- th\_access\_credential\_public\_key

Group resolving key used for BLE tests.

Format: HEX string.

SPSM value for BLE tests.

Format: HEX string.

Access credential public key for the key slot lookup.

Format: DER HEX or PEM with \n .

- th\_reader\_issuer\_public\_key

Reader System Issuer CA certificate public key for key generation.

Format: DER HEX or PEM with \n .

- dut\_credential\_issuer\_public\_key

Credential Issuer Public key loaded into the Reader DUT to validate Access Documents. Format: DER-encoded HEX or PEM with \n .

- dut\_credential\_issuer\_ca\_public\_key

Credential Issuer CA Public key loaded into the Reader DUT to validate Access Document Certificates.

Format: DER-encoded HEX or PEM with \n .

- th\_access\_element\_id

Access Element ID requested by simulated Reader.

Format: string.

## 7. Updating and Managing the Tool

## 7.1 Updating to a New Release

1. On the Pi:
2. Run the update script:

```
sh cd ~/aliro-certification-tool git fetch git checkout <target-release-tag> # Example: git checkout release/test_event1-2024
```

```
sh ./scripts/update.sh
```

## 7.2 Starting and Stopping the Test Harness

- Stop:
- Start:

```
sh cd ~/aliro-certification-tool ./scripts/stop.sh
```

```
sh ./scripts/start.sh
```

To disable autostart:

```
sh sudo systemctl disable aliro-th
```

## 7.3 Accessing Logs

From the aliro-certification-tool directory:

| sh |
| docker compose logs |

Use docker compose logs -f to follow logs live.

## 7.4 Optional Network Configurations

## 7.4.1 Wi-Fi Without Password

Edit /etc/netplan/50-cloud-init.yaml :

```
yaml network: ... wifis: wlan0: dhcp4: true optional: true access-points: "<network_name>": {}
```

Apply and reboot:

```
sh sudo netplan apply sudo reboot
```

## 7.4.2 Link-Local Address on Ethernet

Edit /etc/netplan/50-cloud-init.yaml :

```
yaml network: ... ethernets: eth0: dhcp4: true optional: true link-local: [ ipv4, ipv6 ]
```

Apply and reboot:

```
sh sudo netplan apply sudo reboot
```

## 8. Authoring and Maintaining Test Scripts

Aliro test scripts live under:

## text

test\_collections/aliro

They must follow the same structure as the sample collections (suites and test cases) so the harness can auto-discover them.

After modifying or adding test scripts:

1. Restart the backend container:
2. View backend logs with:

(adapt service name if different.)

## 9. Step-Up Provisioning

Step-up tests use three components:

- Access Document
- Device Response
- Device Request

Based on the Device Request, a Device Response is constructed using the Access Document. To validate step-up tests, the DUT must contain the correct Access Document.

A provisioning script is provided at:

| text |
| test_collections/aliro/support/access_doc/step-up/step_up_provision.py |

Use this script to prepare and load the correct Access Document in the DUT before running step-up certification tests.

## 10. Aliro Actuator

## 10.1 Overview

The Aliro Actuator is a Python implementation of the Aliro specification used as:

- Reference implementation of Reader and User Device roles.
- Tool for generating keys and certificates.
- Programmable peer for certification tests (controlled via scripts).

Project documentation (HTML/PDF) is under docs/build . Examples are under examples .

## 10.2 Hardware and Prerequisites

The actuator uses the NXP nci library for PN7160 NFC boards:

- OM27160A1EVK (I2C)
- OM27160B1EVK (SPI)

For BLE/UWB, the Murata LBUA0VG2BP-EVK-P must have the correct firmware (see third\_party/murata\_fw ).

## 10.3 NFC Support (NCI Library)

Default installation:

- SPI kit:
- I2C kit:

If needed, manual build via linux\_libnfc-nci (clone, edit libnfc-nxp.conf , apply patch, configure, make, install).

## 10.4 Python Environment (Poetry)

Install dependencies:

```
sh sudo apt install python3-pip pip install poetry PATH="$PATH:/home/<user-name>/.local/bin" sudo -E $(which poetry) install --no-root sudo -E $(which poetry) shell
```

## 10.5 Firmware and Flashing

Flash recommended firmware for Murata and other boards as described in third\_party/readme.md .

## 10.6 Examples

Inside the Poetry shell:

- NFC:

```
sh python3 -m examples.nfc.reader.standard python3 -m examples.nfc.reader.fast python3 -m examples.nfc.user_device
```

## · BLE:

```
sh python3 -m examples.ble.reader.standard python3 -m examples.ble.reader.fast python3 -m examples.ble.user_device
```

## · UWB:

```
sh python3 -m examples.ble.reader.ble_uwb python3 -m examples.ble.user_device_ble_uwb
```

- Cryptography:

```
sh python3 -m examples.cryptography.generate_certificate python3 -m examples.cryptography.generate_keypair
```

## 10.7 Using the Actuator API

- Reader class: aliro\_actuator.access\_protocol.reader.Reader
- User Device class: aliro\_actuator.access\_protocol.user\_device.UserDevice

## Common usage:

```
python reader = Reader(transport_protocol="NFC") # or BLE/UWB reader.transaction_initiation()
```

or:

```
python user = UserDevice(transport_protocol="BLE") user.transaction_initiation()
```

## Two patterns:

1. Handle functions (session-based)
2. o Call start\_new\_session() .
3. o Use methods prefixed with handle\_... .
4. o State is stored in a session object.
2. Command/response methods (low-level)
6. o Use command\_... and response\_... methods.
7. o Provide all fields explicitly and handle responses manually.

## 10.8 Packaging, Development, and Quality

- Build wheel:
- VS Code + Dev Container:
- o Open repo, reopen in Dev Container, press F5 to debug.

```
sh poetry build
```

## · Testing:

sh

scripts/test.sh

- Linting and formatting:

```
sh scripts/lint.sh scripts/format.sh
```

Quality tools: flake8 , black , isort , mypy , cspell .

## 11. Actuator Integration with the Test Harness

## 11.1 Typical Test Setups

## 1. Reader DUT

- o DUT implements Reader.
- o Actuator simulates User Device.
- o Test Harness coordinates scripts and uses 'Reader test parameters'.

## 2. User Device DUT

- o DUT implements User Device.
- o Actuator simulates Reader.
- o Test Harness coordinates scripts and uses 'User Device test parameters'.

## 11.2 Mapping Test Parameters to Actuator Configuration

## Reader DUT

Use parameters described in Section 6.1:

- dut\_reader\_* describe the Reader DUT.
- th\_access\_credential\_* describe the simulated User Device.
- dut\_reader\_issuer\_public\_key validates Reader certificates.

## User Device DUT

Use parameters described in Section 6.2:

- th\_reader\_* configure the simulated Reader (actuator).
- th\_access\_credential\_public\_key , th\_reader\_issuer\_public\_key configure access credentials and issuer CA.

## 11.3 Example Integration Flows

## Reader DUT, NFC Standard Access

- Hardware: Reader DUT + PN7160 with Pi.
- Actuator: examples.nfc.user\_device (User Device role).
- Test Harness: fill dut\_reader\_* and th\_access\_* parameters, run Reader test suite.

## User Device DUT, BLE Fast Transaction

- Hardware: User Device DUT + Murata board on Pi.
- Actuator: examples.ble.reader.fast (Reader role).
- Test Harness: fill th\_reader\_* , th\_access\_* parameters, run User Device test suite.

## 11.4 Using Actuator Helpers to Fill Test Parameters

Generate keys and certificates:

<!-- formula-not-decoded -->

Paste generated values into test\_parameters fields.

## 11.5 Summary Mapping

| DUT Role | Actuator Role | Example Scripts | Main Test Parameters |
| User Device | NFC/ BLE user_device examples | `dut_reader_*`, `th_access_*` | Reader DUT |
| Reader | NFC/ BLE reader.* examples | `th_reader_*`, `th_access_*` | User Device |
| Reader / UD | `reader/stepup.py` | Above + Access Document via step-up script | Step-up DUT |
