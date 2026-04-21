# Aliro Certification Tool Quick Start Guide

#### **Connectivity Standards Alliance – Copyright Notice, License and Disclaimer**

Copyright © Connectivity Standards Alliance (2026). All Rights Reserved. The information within this document is the property of the Connectivity Standards Alliance and its use and disclosure are restricted, except as expressly set forth herein.

Connectivity Standards Alliance hereby grants you a fully-paid, non-exclusive, non-transferable, worldwide, limited and revocable license (without the right to sublicense), under Connectivity Standards Alliance's applicable copyright rights, to view, download, save, reproduce and use the document solely for your own internal purposes and in accordance with the terms of the license set forth herein. This license does not authorize you to, and you expressly warrant that you shall not: (a) permit others (outside your organization) to use this document; (b) post or publish this document; (c) modify, adapt, translate, or otherwise change this document in any manner or create any derivative work based on this document; (d) remove or modify any notice or label on this document, including this Copyright Notice, License and Disclaimer. The Connectivity Standards Alliance does not grant you any license hereunder other than as expressly stated herein.

Elements of this document may be subject to third party intellectual property rights, including without limitation, patent, copyright or trademark rights, and any such third party may or may not be a member of the Connectivity Standards Alliance. Connectivity Standards Alliance members grant other Connectivity Standards Alliance members certain intellectual property rights as set forth in the Connectivity Standards Alliance IPR Policy. Connectivity Standards Alliance members do not grant you any rights under this license. The Connectivity Standards Alliance is not responsible for, and shall not be held responsible in any manner for, identifying or failing to identify any or all such third party intellectual property rights. Please visit www.csa-iot.org for more information on how to become a member of the Connectivity Standards Alliance.

This document and the information contained herein are provided on an "AS IS" basis and the Connectivity Standards Alliance DISCLAIMS ALL WARRANTIES EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO (A) ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OF THIRD PARTIES (INCLUDING WITHOUT LIMITATION ANY INTELLECTUAL PROPERTY RIGHTS INCLUDING PATENT, COPYRIGHT OR TRADEMARK RIGHTS); OR (B) ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NONINFRINGEMENT. IN NO EVENT WILL THE CONNECTIVITY STANDARDS ALLIANCE BE LIABLE FOR ANY LOSS OF PROFITS, LOSS OF BUSINESS, LOSS OF USE OF DATA, INTERRUPTION OF BUSINESS, OR FOR ANY OTHER DIRECT, INDIRECT, SPECIAL OR EXEMPLARY, INCIDENTIAL, PUNITIVE OR CONSEQUENTIAL DAMAGES OF ANY KIND, IN CONTRACT OR IN TORT, IN CONNECTION WITH THIS DOCUMENT OR THE INFORMATION CONTAINED HEREIN, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE.

All company, brand and product names in this document may be trademarks that are the sole property of their respective owners.

This Copyright Notice, License and Disclaimer must be included on all copies of this document.

# Purpose

This Quick Start Guide explains how to:

- Install and start the Aliro Certification Tool on a Raspberry Pi.
- Open the web GUI.
- Configure basic test parameters.
- Run your first Aliro test cases.

For detailed information, refer to the full User Manual.

# Revision

| Rev | Date       | Description      |
|-----|------------|------------------|
| 1   | 02/09/2026 | Initial revision |
|     |            |                  |

## Table of contents

| 1. Prerequisites                        | 5 |
|-----------------------------------------|---|
| 2. Install Ubuntu on the Raspberry Pi   |   |
| 3. Flash Murata UWB Board               | 6 |
| 4. Assemble and Boot                    | 6 |
| 5. SSH into the Raspberry Pi            | 6 |
| 6. Install the Aliro Certification Tool | 7 |
| 7. Initial Setup                        | 7 |
| 8. Open the Web GUI                     | 7 |
| 9. Create Your First Project            | 8 |
| 10. Run a Test Suite                    | 8 |
| 11. Basic Operations                    | 9 |

## 1. Prerequisites

#### **Hardware**

- Raspberry Pi 4 (8 GB recommended, 4 GB minimum).
- Micro SD card (16 GB or more).
- Power supply.
- NFC evaluation kit:
  - o OM27160A1EVK (I2C) or OM27160B1EVK (SPI).
- Murata LBUA0VG2BP-EVK-P (BLE/UWB) + micro-USB cable.
- Ethernet cable or Wi-Fi network with internet access.
- Optional: monitor, keyboard, HDMI cable.

#### **Software / Accounts**

- Raspberry Pi Imager (on your PC).
- Aliro TestHarness\_CertificationTool\_v1.0 SW package

## 2. Install Ubuntu on the Raspberry Pi

- 1. Run Raspberry Pi Imager on your PC.
- 2. Device: **Raspberry Pi 4**.
- 3. OS: **Ubuntu Server 22.04.3/22.04.4/22.04.5 LTS (64-bit)**.
- 4. Storage: Select your micro-SD card.
- 5. Apply OS customization:
  - o Set hostname, e.g. aliro-th-pi1.
  - o Set username and password.
  - o Enable **SSH** with password authentication.

- o Optionally configure Wi-Fi.
- 6. Write the OS to the SD card and wait for completion.
- 7. Insert the SD card into the Raspberry Pi.

## 3. Flash Murata UWB Board

Before use with the Test Harness, the Murata board firmware needs to be updated. The firmware file is named "uwb\_ble\_device\_fw-v05.00.03.bin" (or a later version) and can be found at https://github.com/NXP/aliro-th-additions. The board can be updated with the DK6Programmer tool (Windows only), or with MCUxpresso and a debugger.

For more details, see https://github.com/csa-access-control/aliroactuator/blob/main/third\_party/readme.md

## 4. Assemble and Boot

- 1. Connect the PN7160 evaluation kit to the Raspberry Pi.
- 2. Connect the Murata LBUA0VG2BP-EVK-P via micro-USB.
- 3. Connect Ethernet (or ensure Wi-Fi configured).
- 4. Connect power and boot the Raspberry Pi.
- 5. Wait for the system to start (1–2 minutes).

## 5. SSH into the Raspberry Pi

From your PC terminal:

If hostname does not work, use the Pi IP address instead:

Enter your password when prompted.

## 6. Install the Aliro Certification Tool

On the Raspberry Pi:

```
sh 
cd ~/aliro-certification-tool 
# Optional: checkout a specific release
# git checkout <release> 
./scripts/pi-setup/auto-install.sh
```

When prompted at the end of the script, type 1 to reboot the Pi.

Installation can take more than an hour. The first reboot afterwards may take several minutes.

## 7. Initial Setup

After the reboot, SSH again into the Raspberry Pi and run:

The harness is now running and will also start automatically at boot.

## 8. Open the Web GUI

1. From the Raspberry Pi, get the IP address:

2. On your PC, open a browser and navigate to:

http://<raspberry-pi-ip-address>

Example: http://192.168.2.9

3. Wait a few minutes after starting the harness before connecting.

You should see the Aliro Test Harness home page.

## 9. Create Your First Project

- 1. In the GUI, click **Create Project**.
- 2. Enter a **Project name**, e.g. "Reader DUT Trial".
- 3. Click **Edit** to open the JSON configuration.
- 4. Find the "test\_parameters" entry. Replace null with minimum required parameters for your scenario.

#### Example (Reader DUT):

- 5. Click **Update** to save.
- 6. Click **Create** to create the project.

You can adjust parameters later (Edit icon in project row).

## 10. Run a Test Suite

- 1. In the project list, click the triangular **Go To Test-Run** icon.
- 2. Click **Create new Test Run**.
- 3. In the top right, set an **Operator Name** (create if needed).
- 4. Select an Aliro test suite (e.g. a Reader or User Device suite).

5. Click **Start** to run the tests.

Watch progress and verdicts in the GUI. Failed tests can be re-run after adjusting test parameters or DUT configuration.

## 11. Basic Operations

• **Stop harness manually**:

• **Start harness manually**:

• **View logs**:

• **Update tool to new release**: