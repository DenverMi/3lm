## Aliro Certification Tool Quick Start Guide

## Purpose

This Quick Start Guide explains how to:

- Install and start the Aliro Certification Tool on a Raspberry Pi.
- Open the web GUI.
- Configure basic test parameters.
- Run your first Aliro test cases.

For detailed information, refer to the full User Manual.

## Revision

| Rev | Date | Description |
| 1 | 02/09/2026 | Initial revision |

## 1. Prerequisites

## Hardware

- Raspberry Pi 4 (8 GB recommended, 4 GB minimum).
- Micro SD card (16 GB or more).
- Power supply.
- NFC evaluation kit:
- o OM27160A1EVK (I2C) or OM27160B1EVK (SPI).
- Murata LBUA0VG2BP-EVK-P (BLE/UWB) + micro-USB cable.
- Ethernet cable or Wi-Fi network with internet access.
- Optional: monitor, keyboard, HDMI cable.

## Software / Accounts

- Raspberry Pi Imager (on your PC).
- Aliro TestHarness\_CertificationTool\_v1.0 SW package

## 2. Install Ubuntu on the Raspberry Pi

1. Run Raspberry Pi Imager on your PC.
2. Device: Raspberry Pi 4 .
3. OS: Ubuntu Server 22.04.3/22.04.4/22.04.5 LTS (64-bit) .
4. Storage: Select your micro-SD card.
5. Apply OS customization:
6. o Set hostname, e.g. aliro-th-pi1.
7. o Set username and password.
8. o Enable SSH with password authentication.
9. o Optionally configure Wi-Fi.
6. Write the OS to the SD card and wait for completion.
7. Insert the SD card into the Raspberry Pi.

## 3. Flash Murata UWB Board

Before use with the Test Harness, the Murata board firmware needs to be updated. The firmware file is named 'uwb\_ble\_device\_fw-v05.00.03.bin' (or a later version) and can be found at https://github.com/NXP/aliro-th-additions. The board can be updated with the DK6Programmer tool (Windows only), or with MCUxpresso and a debugger.

For more details, see https://github.com/csa-access-control/aliroactuator/blob/main/third\_party/readme.md

## 4. Assemble and Boot

1. Connect the PN7160 evaluation kit to the Raspberry Pi.
2. Connect the Murata LBUA0VG2BP-EVK-P via micro-USB.
3. Connect Ethernet (or ensure Wi-Fi configured).
4. Connect power and boot the Raspberry Pi.
5. Wait for the system to start (1-2 minutes).

## 5. SSH into the Raspberry Pi

From your PC terminal:

```
ssh <username>@<hostname>.local # Example: ssh ubuntu@aliro-th-pi1.local
```

If hostname does not work, use the Pi IP address instead:

ssh &lt;username&gt;@&lt;ip-address&gt;

Enter your password when prompted.

## 6. Install the Aliro Certification Tool

On the Raspberry Pi:

```
sh cd ~/aliro-certification-tool # Optional: checkout a specific release # git checkout <release> ./scripts/pi-setup/auto-install.sh
```

When prompted at the end of the script, type 1 to reboot the Pi.

Installation can take more than an hour. The first reboot afterwards may take several minutes.

## 7. Initial Setup

After the reboot, SSH again into the Raspberry Pi and run:

```
git submodule update --init --recursive # Default (SPI PN7160):
```

```
cd ~/aliro-certification-tool cd test_collections/aliro ./setup.sh # For I2C kits: # NXP_TRANSPORT=I2C ./setup.sh cd ~/aliro-certification-tool ./scripts/start.sh
```

The harness is now running and will also start automatically at boot.

## 8. Open the Web GUI

1. From the Raspberry Pi, get the IP address:
2. On your PC, open a browser and navigate to:

http://&lt;raspberry-pi-ip-address&gt;

```
Example: http://192.168.2.9
```

3. Wait a few minutes after starting the harness before connecting.

You should see the Aliro Test Harness home page.

## 9. Create Your First Project

1. In the GUI, click Create Project .
2. Enter a Project name , e.g. 'Reader DUT - Trial'.
3. Click Edit to open the JSON configuration.
4. Find the "test\_parameters" entry. Replace null with minimum required parameters for your scenario.

## Example (Reader DUT):

```
"test_parameters": { "dut_reader_public_key": "<READER_PUB_KEY_HEX_OR_PEM>", "dut_reader_group_identifier": "00113344667799AA00113344667799AA", "dut_reader_issuer_group_identifier": "00113344667799AA00113344667799AB", "dut_reader_group_sub_identifier": "113344667799AA00113344667799AA00", "dut_reader_group_resolving_key": "00000000000000000000000000000000" {
```

5. Click Update to save.
6. Click Create to create the project.

You can adjust parameters later (Edit icon in project row).

## 10. Run a Test Suite

1. In the project list, click the triangular Go To Test-Run icon.
2. Click Create new Test Run .
3. In the top right, set an Operator Name (create if needed).
4. Select an Aliro test suite (e.g. a Reader or User Device suite).

## 5. Click Start to run the tests.

Watch progress and verdicts in the GUI. Failed tests can be re-run after adjusting test parameters or DUT configuration.

## 11. Basic Operations

## · Stop harness manually :

```
cd ~/aliro-certification-tool ./scripts/stop.sh
```

## · Start harness manually :

```
./scripts/start.sh
```

## · View logs :

```
cd ~/aliro-certification-tool docker compose logs
```

## · Update tool to new release :

```
cd ~/aliro-certification-tool git fetch git checkout <new-release-tag> ./scripts/update.sh
```
