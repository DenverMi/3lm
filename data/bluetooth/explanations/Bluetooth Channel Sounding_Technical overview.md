[Table of
Contents][]

- 1. Introduction
- 2. Background
- [2.1 Device Positioning and Bluetooth
LE](#21-device-positioning-and-bluetooth-le)
- [2.1.1 Bluetooth® Find
Me](#211-bluetooth-find-me)
- [2.1.2 Beacons and First-Generation Distance
Estimation](#212-beacons-and-firstgeneration-distance-estimation)
- [2.1.3 Bluetooth® Direction Finding With AoA and
AoD](#213-bluetooth-direction-finding-with-aoa-and-aod)
- [2.1.4 Bluetooth® Channel
Sounding](#214-bluetooth-channel-sounding)
- [2.2 An Introduction to Bluetooth® Channel
Sounding](#22-an-introduction-to-bluetooth-channel-sounding)
- [2.2.1 The Fundamental Properties of Radio
Waves](#221-the-fundamental-properties-of-radio-waves)
- [2.2.1.1 Amplitude and Wave
Cycles](#2211-amplitude-and-wave-cycles)
- [2.2.1.2
Wavelength](#2212-wavelength)
- 2.2.1.3 Frequency
- 2.2.1.4 Phase
- [2.2.1.5 The Mathematical Relationship Between Frequency and
Wavelength](#2215-the-mathematical-relationship-between-frequency-and-wavelength)
- [2.2.2 Distance Measurement
Methods](#222-distance-measurement-methods)
- [2.2.2.1 Phase-Based Ranging
(PBR)](#2221-phasebased-ranging-pbr)
- 2.2.2.1.1 Theory
- [2.2.2.1.2 Worked
Example](#22212-worked-example)
- [2.2.2.2 Round-Trip Timing
(RTT)](#2222-roundtrip-timing-rtt)
- 2.2.2.2.1 Theory
- [2.2.2.3 Real-World
Challenges](#2223-realworld-challenges)
- [3. Bluetooth® Channel
Sounding](#3-bluetooth-channel-sounding)
- 3.1 Overview
- 3.2 Architecture
- [3.2.1 Device
Roles](#321-device-roles)
- 3.2.2 Topology
- [3.2.3 Antenna
Arrays](#323-antenna-arrays)
- [3.2.4
Applications](#324-applications)
- [3.2.5 Data Transport
Architecture](#325-data-transport-architecture)
- [3.2.6 Channel Sounding in the Bluetooth LE
Stack](#326-channel-sounding-in-the-bluetooth-le-stack)
- [3.3 Bluetooth® Channel Sounding Control
Procedures](#33-bluetooth-channel-sounding-control-procedures)
- [3.3.1 Bluetooth® Channel Sounding Security
Start](#331-bluetooth-channel-sounding-security-start)
- [3.3.2 Bluetooth® Channel Sounding Capabilities
Exchange](#332-bluetooth-channel-sounding-capabilities-exchange)
- [3.3.3 Bluetooth® Channel Sounding
Configuration](#333-bluetooth-channel-sounding-configuration)
- [3.3.4 Mode-0 FAE Table
Request](#334-mode0-fae-table-request)
- [3.3.5 Bluetooth® Channel Sounding
Start](#335-bluetooth-channel-sounding-start)
- [3.3.6 Bluetooth® Channel
Sounding](#336-bluetooth-channel-sounding)
- [3.4 Events, Subevents, and
Steps](#34-events-subevents-and-steps)
- [3.4.1 LE-ACL Connections and Time
Division](#341-leacl-connections-and-time-division)
- [3.4.2 Time
Division](#342-time-division)
- 3.4.2.1 Structure
- 3.4.2.2 Timing
- [3.5 Bluetooth® Channel Sounding
Steps](#35-bluetooth-channel-sounding-steps)
- [3.5.1 About
Steps](#351-about-steps)
- [3.5.2 Packets and
Tones](#352-packets-and-tones)
- 3.5.3 Step Modes
- 3.5.3.1 Mode-0
- 3.5.3.2 Mode-1
- 3.5.3.3 Mode-2
- 3.5.3.4 Mode-3
- [3.6 Establishing Phase
Differences](#36-establishing-phase-differences)
- [3.7 Antenna
Switching](#37-antenna-switching)
- [3.8 Mode
Sequencing](#38-mode-sequencing)
- [3.8.1 Mode Sequencing
Overview](#381-mode-sequencing-overview)
- [3.8.2 Mode
Combinations](#382-mode-combinations)
- [3.8.3 Mode Sequence Configuration and Sub_Mode
Insertion](#383-mode-sequence-configuration-and-submode-insertion)
- [3.8.4 Main Mode
Repetition](#384-main-mode-repetition)
- [3.8.5 Applications and Mode Sequencing
Considerations](#385-applications-and-mode-sequencing-considerations)
- [3.9 RF Channels and Channel
Selection](#39-rf-channels-and-channel-selection)
- [3.9.1 The Bluetooth® Channel Sounding Channel
Map](#391-the-bluetooth-channel-sounding-channel-map)
- [3.9.2 Channel
Filtering](#392-channel-filtering)
- [3.9.3 Frequency
Hopping](#393-frequency-hopping)
- [3.9.4 Channel
Selection](#394-channel-selection)
- 3.9.4.1 Overview
- [3.9.4.2 Channel Index
Shuffling](#3942-channel-index-shuffling)
- 3.9.4.3 CSA #3a
- 3.9.4.4 CSA #3b
- 3.9.4.5 CSA #3c
- [3.10 RTT Options and
Accuracy](#310-rtt-options-and-accuracy)
- [3.10.1 Timing Based on an Access
Address](#3101-timing-based-on-an-access-address)
- [3.10.2 Fractional Timing
Estimates](#3102-fractional-timing-estimates)
- [3.10.3 A Comparison of RTT
Methods](#3103-a-comparison-of-rtt-methods)
- [3.11 The LE 2M 2BT
PHY](#311-the-le-2m-2bt-phy)
- [3.11.1 Modulation
Schemes](#3111-modulation-schemes)
- [3.11.2 Bandwidth-Bit Period
Product](#3112-bandwidthbit-period-product)
- 3.11.3 LE 2M 2BT
- [3.12 SNR Control for Bluetooth® Channel Sounding
Steps](#312-snr-control-for-bluetooth-channel-sounding-steps)
- 3.13 Security
- 3.13.1 Overview
- [3.13.2 PBR and RTT Cross
Checking](#3132-pbr-and-rtt-cross-checking)
- [3.13.3 Initializing Bluetooth® Channel Sounding
Security](#3133-initializing-bluetooth-channel-sounding-security)
- [3.13.4 Deterministic Random Bit Generator
(DRBG)](#3134-deterministic-random-bit-generator-drbg)
- [3.13.4.1 Secure Access
Addresses](#31341-secure-access-addresses)
- [3.13.4.2 Random Sequence for RTT Fractional
Timing](#31342-random-sequence-for-rtt-fractional-timing)
- [3.13.4.3 Sounding Sequence Marker
Signals](#31343-sounding-sequence-marker-signals)
- [3.13.4.4 Tone Extension Slot Random
Transmissions](#31344-tone-extension-slot-random-transmissions)
- [3.13.4.5 Random Selection of Antenna
Paths](#31345-random-selection-of-antenna-paths)
- [3.13.5 Sounding
Sequences](#3135-sounding-sequences)
- [3.13.6 Attack Detection and
Reporting](#3136-attack-detection-and-reporting)
- 3.13.7 LE 2M 2BT
- [3.13.8 SNR Control and RTT
Security](#3138-snr-control-and-rtt-security)
- [3.13.9 CS Security
Levels](#3139-cs-security-levels)
- [3.13.10 Vendor-Specific Implementations and Additional
Security](#31310-vendorspecific-implementations-and-additional-security)
- [3.13.11 Channel Sounding Amplitude-based Attack
Resilience](#31311-channel-sounding-amplitudebased-attack-resilience)
- [3.14 Host
Applications](#314-host-applications)
- [3.14.1 The Distance Measurement
Algorithm](#3141-the-distance-measurement-algorithm)
- [3.14.2 Controller to Host Communication of Bluetooth® Channel
Sounding
Data](#3142-controller-to-host-communication-of-bluetooth-channel-sounding-data)
- [3.14.2.1 HCI Event
Types](#31421-hci-event-types)
- [3.14.2.2 HCI Event
Timing](#31422-hci-event-timing)
- [3.14.2.3 HCI Event
Content](#31423-hci-event-content)
- [3.14.3 Mode Combinations and Mode
Sequencing](#3143-mode-combinations-and-mode-sequencing)
- [3.14.4 Application Layer
Security](#3144-application-layer-security)
- [3.15 Bluetooth Channel Sounding
enhancements](#315-bluetooth-channel-sounding-enhancements)
- [3.15.1 Resilience Against
Amplitude‑Based Attacks  ](#3151-resilience-against-amplitudebasedattacks)
- [3.15.2 Inline PCT
Transfer Support ](#3152inline-pct-transfersupport)
- [3.15.3 PHY‑Specific RTT
Accuracy Support ](#3153-physpecific-rtt-accuracysupport)
- [4. A Summary of Bluetooth Core Specification
Changes](#4-a-summary-of-bluetooth-core-specification-changes)
- 4.1 Architecture
- 4.2 Host
- [4.2.1 Generic Access
Profile](#421-generic-access-profile)
- [4.2.2 Host Controller
Interface](#422-host-controller-interface)
- 4.3 Controller
- [4.3.1 Physical
Layer](#431-physical-layer)
- 4.3.2 Link Layer
- [4.3.3 Bluetooth® Channel
Sounding](#433-bluetooth-channel-sounding)
- 5. Conclusion
- 6. References

**Version:** 1.0
**Revision Date:** 9 July 2024
**Author:** Martin Woolley, Bluetooth SIG

Bluetooth® Low Energy (LE) is well-known the world over for providing
users with wireless data transfer and audio capabilities. The technology
is in our pockets thanks to its incorporation within our ever-smarter
phones. It's on our wrists, in smart watches, and in fitness trackers.
It's in our cars, allowing hands-free control and communication. And
it's in our ears, enabling the streaming of high-quality audio from
personal music devices and from broadcast sources via the new Bluetooth
LE Audio capability, [Auracast™ broadcast

But for many years, Bluetooth LE has also been establishing itself as a
pervasive and
applications. Bluetooth LE can be used to detect and report the presence
of another device in the immediate environment, to estimate the distance
between devices, and to calculate the direction in which another device
can be found. These device positioning capabilities have been used to
enable a wide range of applications, including digital key, asset
tracking, *Find My*, and indoor navigation.

Bluetooth technology has continuously improved over its 25-year history.
It has taken a positive evolutionary path that has yielded a series of
remarkable new features and improvements to the results that products
can achieve with it.

The update to the Bluetooth Core Specification adds a new feature called
Bluetooth® Channel Sounding which enables secure fine ranging between
two Bluetooth devices and is the topic of this paper. This paper is not
intended to replace or be a substitute for the Bluetooth Core
Specification.

Bluetooth LE was first specified in 2010. From that point on, a number
of key events in the evolution of Bluetooth LE as a technology for
location services can be identified.

The same year that Bluetooth LE was first included in the Bluetooth Core
Specification, the first formal location-related Bluetooth LE profile
specification was released. This was the Find Me Profile.

The Find Me Profile defines a standard approach to personal item
finding, also known as *Find My*. One device assumes the role of Find Me
Locator. This is usually a smart phone. Other devices, which the user
perhaps has a history of misplacing (keys with a Bluetooth key fob are a
favorite), are paired with the Find Me Locator device and each assume
the role of Find Me Target.

The Target device implements a GATT^1^ service called
the Immediate Alert Service.

When the user needs to be assisted in finding a misplaced device, they
run an application on their smartphone. The application executes a
device discovery procedure by scanning for advertising packets being
broadcast by the missing device. Having discovered the Target device,
the Locator connects to it. The application's user interface (UI)
indicates that this has been done. The user typically then presses a
button on the UI. This causes the application to write to the Alert
Level characteristic which belongs to the Immediate Alert service. The
Target device responds to the change of Alert Level value in some
suitable way, perhaps emitting a loud beeping sound, flashing LEDs on
and off or both. At this point, the user realizes their keys were in
their jacket pocket all along, have fallen down the back of the sofa, or
they are somewhere less predictable. Either way, Bluetooth technology
saves the day and the user, and their lost item is reunited.

Bluetooth® Find Me is an example of a presence application. Bluetooth LE
is used to determine that the lost device is nearby but does not provide
an indication of its direction or distance from the Locator.

Bluetooth beacons leverage the advertising capability of Bluetooth LE.
Advertising involves broadcasting small packets of data which any device
in range can receive by scanning.

In 2013, Apple released the specification for the iBeacon format. This
became a popular format for the content of the payloads that a beacon
device would broadcast. The data in an iBeacon message includes a field
called TX Power which contains a value representing the signal strength
that can be expected if measured at a distance of one meter from the
beacon. It was the presence of the TX Power field in iBeacon messages as
well as in other comparable beacon data formats such as Google's
Eddystone, which heralded the arrival of the first generation of
Bluetooth LE distance estimation.

This early version of Bluetooth distance estimation involved the use of
two data values and some simple physics and works like this:

- The TX Power field in beacon messages provides a reference power level
at a known distance such as one meter.
- The Received Signal Strength Indicator (RSSI) associated with each
received beacon message quantifies the signal strength at the
receiving device.
- Physics defines a theoretical relationship between the rate at which
the signal strength diminishes the further away from the transmitter
that it is measured. Specifically, the signal strength at a receiver
is inversely proportional to the square of its distance from the
transmitter.
- The reduction of measured signal strength as we move further away from
the transmitter is called Path Loss or Attenuation. In the case of
iBeacon transmissions, path loss = TX Power -- RSSI.
- Thus, knowing a reference power level at a fixed distance, the
measured RSSI of a received beacon transmission and the inverse square
relationship between distance and path loss, attenuation can be used
to estimate the distance between the beacon and the receiver.

[![Figure
1](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1.png "Figure 1 - Path loss and distance"){.aligncenter
.wp-image-234481 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1.png 758w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-600x331.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-300x165.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-450x248.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-660x364.png 660w"
sizes="auto, (max-width: 758px) 100vw, 758px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1.png)

*Figure 1 -- Path loss and distance*

Being able to estimate distance like this was quite a breakthrough, and
beacons have become popular in all sorts of applications, such as
retail, travel, and museums.

While beacons were an excellent fit for some requirements, distance
measurements based on RSSI and path loss are not sufficiently accurate
for other applications. Lacking an indication of the direction of the
transmitter is also a limitation when location data was needed rather
than just proximity. Furthermore, the various proprietary beacon types
such as iBeacon do not incorporate any explicit security safeguards.

In 2019, version 5.1 of the Bluetooth Core Specification included a
major new feature, Bluetooth Direction Finding.

The Bluetooth Direction Finding feature enables applications to
accurately calculate the direction of a received signal using phase
measurements made by the Bluetooth LE controller. Two methods are
defined.

In the Angle of Arrival (AoA) method, the receiving device has an
antenna array and measurements of the received signal taken at different
antennas exhibit phase differences due to the slightly different
distances of each of its antennas to the single antenna in the
transmitting device.

In the Angle of Departure (AoD) method, the transmitting device has an
antenna array. The receiving device has a single antenna but possesses
details of the antenna array in the remote, transmitting device. This
enables it to make similar calculations from phase measurements made at
its single antenna.

[![Figure
2](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2.png "Figure 2 - Direction Finding using AoA and AoD"){.aligncenter
.wp-image-234482 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2.png 1440w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-600x300.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-300x150.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-768x384.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-450x225.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-660x330.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-800x400.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-1000x500.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-1200x600.png 1200w"
sizes="auto, (max-width: 1440px) 100vw, 1440px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2.png)

*Figure 2 -- Direction Finding using AoA and AoD*

Phase measurements in the form of In-Phase and Quadrature (IQ) samples
are passed from the Bluetooth controller to the application. IQ samples
consist of pairs of phase and amplitude values which the application is
able to use to calculate the direction in which the transmitter can be
found.

[![Figure
3](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3.png "Figure 3 - IQ Sample"){.aligncenter
.wp-image-234483 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3.png 2320w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-600x600.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-2000x2000.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-300x300.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-768x768.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1536x1536.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-2048x2048.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-200x200.png 200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-450x450.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-660x660.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-800x800.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1000x1000.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1200x1200.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1600x1600.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-50x50.png 50w"
sizes="auto, (max-width: 2320px) 100vw, 2320px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3.png)

*Figure 3 -- IQ Sample*

The new Bluetooth® Channel Sounding feature makes it possible to create
products that have the ability to calculate the distance between two
Bluetooth devices with significantly better accuracy than could ever be
produced using the RSSI and path loss first generation method. It works
in an entirely different way and includes a variety of security
safeguards that mitigate various types of risk.

It is expected that Bluetooth® Channel Sounding will benefit Find My
solutions, digital key products, and many more Bluetooth connected
devices.

Before discussing Bluetooth® Channel Sounding in Bluetooth LE, this
section will first present some of the basic theory behind the feature.
Readers already familiar with the topic should skip to section 3,
Bluetooth® Channel Sounding.

Radio is a form of electromagnetic radiation and physicists often
describe it in terms of waves. Radio waves have various basic
properties, an understanding of which is important.

The amplitude of a radio wave corresponds to the energy that it carries,
or, in more common terms, the signal strength. It oscillates above and
below a central reference value. This above and below oscillation
repeats regularly and periodically. A single transition up to the peak
amplitude, down to the trough, and back up to the starting reference
value is called a wave cycle. Figure 4 depicts two complete wave cycles,
with amplitude on the vertical scale. The extent of the first wave cycle
is highlighted.

[![Figure
4](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1200x417.png "Figure 4 - Wave Cycle with amplitude on the vertical scale"){.aligncenter
.wp-image-234484 .size-1200w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1600x556.png 1600w"
sizes="auto, (max-width: 1200px) 100vw, 1200px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4.png)

*Figure 4 -- Wave Cycle with amplitude on the vertical scale*

A single wave cycle has a physical length. The wavelength is related to
the frequency, and, in the case of Bluetooth technology, falls somewhere
between about 12.0 cm and about 12.5 cm.

[![Figure
5](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1200x417.png "Figure 5 - Wavelength"){.aligncenter
.wp-image-234485 .size-1200w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1600x556.png 1600w"
sizes="auto, (max-width: 1200px) 100vw, 1200px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5.png)

*Figure 5 -- Wavelength*

Radio travels at the speed of light in a vacuum^2^.
The number of complete wave cycles that pass over a fixed point in space
in one second is called the frequency. Frequency is measured in hertz
(Hz) where 1 Hz represents one wave cycle per second. A Bluetooth signal
works at considerably higher frequencies measured in gigahertz (GHz).

[![Figure
6](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1000x348.png "Figure 6 - Frequency"){.aligncenter
.wp-image-234438 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1600x556.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6.png)

*Figure 6 -- Frequency*

Points that sit somewhere within a single wave cycle are expressed by an
angular measurement known as the phase. Phase values have a range of 0
-- 360 degrees or 0 -- 2π radians. Figure 7 illustrates the concept of
phase with a number of phase values (expressed in radians) marked at
appropriate points on the wave cycle.

[![Figure
7](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1000x348.png "Figure 7 - Phase"){.aligncenter
.wp-image-234439 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1600x556.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7.png)

*Figure 7 -- Phase*

Frequency (f) and wavelength (λ) are inversely related to each other.
The shorter the wavelength, the higher the frequency and vice versa.
Furthermore, the relationship between these two variables and the speed
of light (c) are defined by a set of simple formulae, allowing any one
of the three quantities to be calculated from known values for the other
two. The speed of light is a constant with a value of 299792458 m/s.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Formula</th>
<th class="has-text-align-left" data-align="left">Use</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left"><img
src="https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_1.svg"
height="100" alt="2405 Channel Sounding Formulas 1" /></td>
<td class="has-text-align-left" data-align="left">Calculate an unknown
wavelength from a known frequency and the constant speed of light.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left"><img
src="https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_2.svg"
height="100" alt="2405 Channel Sounding Formulas 2" /></td>
<td class="has-text-align-left" data-align="left">Calculate an unknown
frequency from a known wavelength and the constant speed of light.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left"><img
src="https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_3.svg"
height="216" alt="2405 Channel Sounding Formulas 3" /></td>
<td class="has-text-align-left" data-align="left">Calculate the speed of
light using a frequency value and the corresponding wavelength.</td>
</tr>
</tbody>
</table>

*Table 1 -- Frequency and Wavelength Formulae*

The two most commonly used methods in wireless distance measurement
technologies are Phase-Based Ranging (PBR) and Round-Trip Timing (RTT).
The theory behind both methods will be outlined in this section.

It's easy to visualize distance as a function of the wavelength of a
signal in terms of the number of wave cycles that are needed for the
signal to stretch from a transmitter to a receiver.

[![Figure
8](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1000x348.png "Channel Sounding Figure 8"){.aligncenter
.wp-image-234440 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1600x556.png 1600w"

*Figure 8 -- Distance from wavelength and wave cycles*

In Figure 8, the signal transmitted on the left of the illustration is
clearly ten and a half wavelengths away from the receiver. If we know
the frequency of the signal then we know the wavelength. And if we know
the wavelength, then knowing the number of wave cycles, we can use
multiplication to find the distance between the two devices.

If the transmission frequency is 2402 MHz for example, then the
wavelength is 12.48095162 cm. This figure was arrived at by dividing the
speed of light by the frequency.

The transmitting device has no way of knowing the number of wave cycles
between its antenna and that of the receiver, however. So, the PBR
method involves a technique which allows the deduction of the distance
between transmitter and receiver based on other data. Here's how it
works.

We'll refer to the device that wishes to calculate a distance
measurement as Device A. The other device will be Device B.

1. Device A transmits a signal at a known frequency, f1. The initial
phase of this signal is known to Device A, and, for the purpose of
illustration, let's assume that this signal is transmitted with a
phase of zero radians.
2. Device B receives the f1 signal at its antenna and notes its phase,
which we will refer to as the receive phase.
3. Device B then echoes the received signal back to Device A by
transmitting on the same frequency, f1 and, critically, ensuring
that the initial phase of this transmission is exactly the same as
the receive phase of the signal received from Device A. This results
in the return signal being a continuation of the signal from Device
A in terms of phase and frequency.
4. Device A measures the receive phase of the signal arriving from
Device B. We'll call this value Pf1.

[![Figure
9](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1000x157.png "2405 Channel Sounding Figure 9"){.aligncenter
.wp-image-234441 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9.png)

*Figure 9 -- Two-way ranging with frequency f1*

Device A now chooses a new frequency, f2, and the four steps are
repeated. The result of this second execution of the four steps is a new
phase measurement made by Device A of the signal received back from
Device B which we'll call Pf2.

[![Figure
10](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1000x157.png "2405 Channel Sounding Figure 10"){.aligncenter
.wp-image-234442 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10.png)

*Figure 10 -- Two-way ranging with frequency f2*

Device A now calculates the difference between the phase values measured
for each of f1 and f2, i.e., it calculates Pf2 -- Pf1. Armed with the
phase difference and the difference between the frequencies f1 and f2,
it is now possible to calculate the distance using the following
formula:

![2405 Channel Sounding Formulas
4](https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_4.svg){.aligncenter
.size-full .wp-image-208116 loading="lazy" decoding="async" width="937"

Where c is the speed of light, (Pf2 -- Pf1) is the phase difference and
(f2 -- f1) is the frequency separation, and *r* is the two-way ranging
distance between the two devices.

This approach, where the second device transmits a signal back to the
originating device so that it can take phase measurements, is called
two-way ranging.

The real-world can present challenges not reflected in this explanation
of some basic theory. We'll encounter some of those challenges later in
this section.

Let's try a simple worked example to see this in action. We'll use a
rather artificial case where we already know the distance between the
two devices so that we can see how the formula correctly arrives at the
same result.

Figure 11 shows two devices, Device A and Device B, which are exactly
1.248095162 meters apart. Device A has transmitted a signal with a
frequency of 2.402 MHz and a wavelength of 12.48095162 cm. By a truly
remarkable coincidence, the two devices are therefore at a distance from
each other of exactly ten times this wavelength.

[![Figure
9](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1000x157.png "Figure 11"){.aligncenter
.wp-image-234441 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9.png)

*Figure 11 -- Devices exactly ten f1 wave cycles apart*

Given Device A transmits this signal with an initial phase of zero, and,
since Device B is an exact multiple of the wavelength away, the receive
phase at Device B is also zero. As shown, Device B transmits a signal
back to device A, setting the initial phase to the same value of the
receive phase as the signal it originally received so that we
effectively have a continuation.

Figure 12 shows the second signal transmitted by Device A at frequency
f2. This time the chosen frequency is a higher frequency than f1 with a
value of f2 = 2.432 MHz. The initial phase at Device A is once again
zero.

[![Figure
10](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1000x157.png "Figure 12"){.aligncenter
.wp-image-234442 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10.png)

*Figure 12 -- Devices a little over ten f2 wave cycles apart*

The wavelength of f2 is shorter than the wavelength of f1 because f2 has
a higher frequency. This results in the receive phase at Device B being
non-zero. In fact, it's 0.784744210 radians. By the time the signal has
been retransmitted by Device B, with the same initial phase and received
by Device A, its phase will be 1.56948842 radians.

Device A now has all that it needs to calculate the distance to Device
B. The frequency difference is 30 MHz, and the phase difference is
1.56948842. Substituting these values in the formula for r, the
calculated distance is 2.49 meters to two decimal places. But this is
for the round trip from Device A to Device B and back again, so the
actual distance between the two devices is half of that figure, i.e.,
1.24 meters. This is the expected result and demonstrates how the
formula for r, based on the speed of light and known phase and frequency
separations of the two transmitted signals, can be used to accurately
calculate the distance between the two devices.

There's a complication however and this is hinted at in the formula for
phase and the modular division of (2 \* π). Phase values change as the
distance increases, but they are periodic meaning that when a phase
value reaches (2 \* π) radians it resets to zero and the same values
start to be repeated. This can give rise to ambiguity in determining the
distance between two devices since more than one distance could be
implied by the same phase difference value. This is known as distance
ambiguity.

Exactly when distance ambiguity is encountered depends on the frequency
separation. In general, distance ambiguity occurs earlier with larger
frequency differences. Luckily, the issue can be addressed by using PBR
in conjunction with the second distance measurement method, Round-Trip
Timing.

The theory behind using round-trip timings to calculate the distance
between two devices is very simple. Radio (RF) transmissions travel at
the speed of light, a known constant. So if we can calculate the time it
takes for a transmission to travel between two devices, we can calculate
the distance. All we have to do is multiply the round-trip time by the
speed of light.

For example, if an RF signal takes 20 nanoseconds to travel from Device
A to Device B and back to Device A, simply multiplying the speed of
light by 20 nanoseconds will give us a total bidirectional distance of
just under six meters and thus the distance between the two devices is
just under three meters.

*Bidirectional Distance 2r = c \* 0.00000002*

where c is the speed of light (299792458 m/s) and 0.00000002 is the
bidirectional time of flight (ToF) in seconds. This gives us the
following result:

*2r = 299792458 \* 0.00000002\
= 5.99584916*

and therefore the distance between Device A and Device B is

*2.99792458 meters*

But whilst this basic formula is correct, using it in the context of
Bluetooth devices is a bit more complicated, and the theory as presented
so far is incomplete.

The act of formulating and transmitting an RF signal takes time as does
the act of receiving, processing, and transmitting the round-trip
response. It might take a device something in the order of magnitude of
200 microseconds to formulate and transmit a packet, and, bearing in
mind that radio waves can travel just under 300 meters in a single
microsecond, these seemingly short time periods can be highly
significant in the context of distance measurements.

[![2405 Channel Sounding Figure
13](https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13.png "Figure 13"){.aligncenter
.wp-image-218307 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-600x176.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-300x88.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-768x225.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1536x451.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-450x132.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-660x194.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-800x235.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1000x294.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1200x352.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1600x470.png 1600w"
sizes="auto, (max-width: 2000px) 100vw, 2000px"}](https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13.png)

*Figure 13 -- RTT breakdown (Not to scale -- signal content not
representative)*

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Instant in Time</th>
<th class="has-text-align-left" data-align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left"
data-align="left"><strong>ToD<sub>A</sub></strong></td>
<td class="has-text-align-left" data-align="left">Time of Departure from
Device A. This is the time at which the signal is transmitted over the
air by Device A.</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left"><strong>ToA<sub>B</sub></strong></td>
<td class="has-text-align-left" data-align="left">Time of Arrival at
Device B. This is the time at which the signal arrives at the antenna of
Device B.</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left"><strong>ToD<sub>B</sub></strong></td>
<td class="has-text-align-left" data-align="left">Time of Departure from
Device B. This is the time at Device B transmits over the air.</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left"><strong>ToA<sub>A</sub></strong></td>
<td class="has-text-align-left" data-align="left">Time of Arrival at
Device A. This is the time at which the signal from Device B is received
at Device A’s antenna.</td>
</tr>
</tbody>
</table>

The green dotted lines represent elapsed time during which neither of
the two signals are *in the air*.

The round-trip time (RTT) can be expressed in terms of the timing
instants depicted in Figure 13 as follows:

*RTT = 2 \* ToF = (ToA~A~ -- ToD~A~) -- (ToD~B~ -- ToA~B~)*

For Device A to calculate RTT, it needs to know the turnaround time at
Device B (i.e., ToD~B~ --- ToA~B~). In theory, there are a number of
ways in which this could work. In practice, the simplest solution is for
a fixed turnaround period to be agreed by Device A and Device B in
advance. Device B must then guarantee to complete its processing and,
exactly as that turnaround period expires, transmit its response. Device
A then uses that pre-agreed value for (ToD~B~ --- ToA~B~).

The theory presented for both the PBR and RTT methods of distance
measurement is sufficient for gaining an initial insight into the topic
and, in a purely theoretical context, it is complete. However, in the
real world, accurate distance measurement is more complicated. There are
several challenges which must be addressed if satisfactory results are
to be produced by real devices used in real-world situations.

Examples of the types of challenges that a wireless distance measurement
technology should address are:

- The complications arising from multi-path propagation of radio signals
- The accuracy and stability of the frequency of generated signals
- The stability of internal clocks and the accuracy and resolution of
timestamps
- Distance ambiguity in phase-based ranging
- Security

In the remainder of this paper, we'll learn about high-accuracy distance
measurement in Bluetooth technology and gain an appreciation of how the
technology has been designed to work effectively in the face of
real-world issues such as these.

Bluetooth® Channel Sounding offers the potential for products to achieve
much higher accuracy distance measurements than has previously been
possible. How accurate measurements are depends on environmental
conditions and how the Bluetooth® Channel Sounding feature is harnessed
by the application layer. It also depends on implementation choices,
details of which fall outside of the Bluetooth Core Specification but
which can improve the quality of the raw data used in calculations.

Bluetooth® Channel Sounding provides applications with a flexible
toolkit for distance measurement with a number of quite different
configurations possible. Both the Phase-based Ranging (PBR) and
Round-Trip Timing (RTT) distance measurement methods are supported in
the specification. In most cases, it is expected that PBR will be used
as the primary and most accurate method of distance measurement with RTT
used alongside it to provide extra security.

PBR, as used by Bluetooth® Channel Sounding, can measure distances up to
about 150 meters before distance ambiguity arises. By using RTT in
addition to PBR, applications can identify and eliminate distance
ambiguity and therefore measure longer distances.

Applications may place different levels of priority over issues like
accuracy, security, latency, and power consumption. The configurability
of the Bluetooth® Channel Sounding feature provides applications with
control or influence over many of the system's key capabilities and
behaviors so that its operation is focused on the right priorities for
the application using it.

In this section we will proceed to examine the Bluetooth® Channel
Sounding feature and the core Bluetooth stack capabilities upon which it
depends.

The Bluetooth® Channel Sounding feature defines two device roles. The
first is the Initiator, and the second is the Reflector.

The Initiator is the device that wishes to calculate the distance from
itself to another device. The other device is the Reflector.

Either the Initiator or the Reflector can kick off the Bluetooth®
Channel Sounding procedure, details of which will be covered later in
this paper.

[![Figure
14](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14.png "Figure 14 - Roles"){.aligncenter
.wp-image-234444 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14.png 7566w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-600x115.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-2000x383.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-300x57.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-768x147.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1536x294.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-2048x392.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-450x86.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-660x126.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-800x153.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1000x192.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1200x230.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1600x307.png 1600w"
sizes="auto, (max-width: 7566px) 100vw, 7566px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14.png)

*Figure 14 -- Roles*

Bluetooth® Channel Sounding takes place in a one-to-one topology with
communication taking place between one device in the Initiator role and
one device in the Reflector role.

It should be noted that the Bluetooth® Channel Sounding Initiator role
may be assumed by either the device acting in the Link Layer LE Central
role or as the LE Peripheral. The same applies to the Bluetooth® Channel
Sounding Reflector role which may be assumed by either the LE Central
device or the LE Peripheral device.

Devices that use Bluetooth® Channel Sounding may include an antenna
array. This provides a series of alternate paths for the exchange of the
Bluetooth® Channel Sounding transmissions that are used for phase-based
ranging and can improve the accuracy of distance measurements by
lessening the impact of multi-path propagation.

Bluetooth® Channel Sounding requires that distances are calculated by
the application layer using data provided by the Bluetooth controller.
That data is acquired by the controller during the execution of the
Bluetooth® Channel Sounding procedure and is a result of signal
exchanges and low-level measurements made at each device. Data is passed
to the application layer in HCI events.

The application layer is also responsible for providing the Bluetooth
controller with configuration choices and preferences which are used in
establishing a Bluetooth® Channel Sounding configuration that is
supported by and suitable for the applications on the two devices.

For two devices to be able to participate in a system with one device in
the Initiator role and the other in the Reflector role, both must have a
Bluetooth LE controller which supports the Bluetooth® Channel Sounding
feature.

[![Figure
15](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1000x648.png "Figure 15 – Bluetooth® Channel Sounding applications and the Bluetooth stack"){.aligncenter
.wp-image-234445 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1000x648.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-600x389.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-2000x1295.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-300x194.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-768x497.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1536x995.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-2048x1326.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-450x291.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-660x427.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-800x518.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1200x777.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1600x1036.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New.png)

*Figure 15 -- Bluetooth® Channel Sounding applications and the Bluetooth
stack*

The Bluetooth Core Specification defines the architecture of Bluetooth
technology from a number of perspectives. In the first perspective, a
generalized data transport architecture is defined.

With reference to definitions in the Bluetooth Core Specification, the
terms in Figure 16 are described as follows:

- **L2CAP** is the Logical Link Control and Adaptation Protocol. An
L2CAP Channel is a logical connection at the L2CAP level between two
devices that serves a single application or higher layer protocol.
- A **Logical Link** is "The lowest architectural level used to offer
independent data transport services to clients of the Bluetooth
system".
- A **Logical Transport** deals with issues such as transmit and receive
routines, flow control mechanisms, acknowledgment protocols, and link
identification. A Logical Transport can be synchronous, asynchronous,
or isochronous.
- A **Physical Link** is a connection between devices established at the
level of the Link Layer. The Link Layer is one of the layers of the
Bluetooth protocol stack.
- **Physical Channels** define patterns of occupancy of RF carriers by
one or more communicating devices.
- **Physical Transports** define generally applicable issues, such as
over-the-air packet structures and modulation schemes which are used
to encode digital data for transmission using radio signals as the
carrier.

The generic data transport architecture applies to both Bluetooth LE and
Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR).

Figure 17 shows a subset of the Data Transport Architecture. Highlighted
in blue are a new Physical Channel type and a new Physical Link type
that have been defined for Channel Sounding.

[![Figure
17](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17.png "Figure 17 - CS and the Data Transport Architecture"){.aligncenter
.wp-image-234447 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17.png 1341w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-600x271.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-300x136.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-768x347.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-450x203.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-660x298.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-800x362.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-1000x452.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-1200x542.png 1200w"
sizes="auto, (max-width: 1341px) 100vw, 1341px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17.png)

*Figure 17 -- CS and the Data Transport Architecture*

No Logical Transport type or Logical Link type is associated with the LE
Channel Sounding physical link.

The more comprehensive way of defining Bluetooth LE is in terms of the
full protocol stack and its layers. Much of the Bluetooth Core
Specification is dedicated to defining each layer. Figure 18 depicts the
Bluetooth LE stack.

[![Figure
18](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18.png "Figure 18 - The Bluetooth LE stack"){.aligncenter
.wp-image-234449 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18.png 654w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18-509x600.png 509w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18-254x300.png 254w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18-450x531.png 450w"
sizes="auto, (max-width: 654px) 100vw, 654px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18.png)

*Figure 18 -- The Bluetooth LE stack*

A summary of the responsibilities of each layer of the Bluetooth LE
stack is contained within Table 2.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Layer</th>
<th class="has-text-align-left" data-align="left">Key
Responsibilities</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Generic Access Profile
(GAP)</td>
<td class="has-text-align-left" data-align="left">Defines operational
modes and procedures that may be used in a non-connected state, such as
how to use advertising for connectionless communication and device
discovery. Defines security levels and some user interface
standards.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Generic Attribute
Profile (GATT)</td>
<td class="has-text-align-left" data-align="left">Defines high-level
data types known as services, characteristics, and descriptors in terms
of underlying attributes in the attribute table.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Attribute Protocol
(ATT)</td>
<td class="has-text-align-left" data-align="left">A protocol used for
the discovery and use of data held by the server in a logical data
structure known as the attribute table.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Security Manager
Protocol (SMP)</td>
<td class="has-text-align-left" data-align="left">A protocol used during
the execution of security procedures such as pairing.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Logical Link Control
and Adaptation Protocol (L2CAP)</td>
<td class="has-text-align-left" data-align="left">Provides data channel
multiplexing services over RF connections, segmentation and reassembly
of large SDUs, and enhanced error detection and retransmission
facilities.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Host Controller
Interface (HCI)</td>
<td class="has-text-align-left" data-align="left">Provides an interface
for bi-directional communication of commands and data between the host
component and the controller.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Isochronous Adaptation
Layer (ISOAL)</td>
<td class="has-text-align-left" data-align="left">Allows different frame
durations to be used by devices using isochronous channels.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Link Layer</td>
<td class="has-text-align-left" data-align="left">Defines air interface
packet formats, bit stream processing procedures such as error checking,
a state machine and protocols for over-the-air communication, and link
control. Defines several distinct ways of using the underlying radio for
connectionless, connection-oriented, and isochronous communication known
as logical transports.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Physical Layer</td>
<td class="has-text-align-left" data-align="left">Defines all aspects of
Bluetooth technology that are related to the use of radio (RF),
including modulation schemes, frequency bands, channel use, transmitter,
and receiver characteristics. Three combinations of Physical Layer
parameters are defined and are referred to as the LE 1M, LE 2M, and LE
2M 2BT PHYs. LE 2M 2BT was defined for the first time in the version 6.0
of the Bluetooth Core Specification and may only be used with Bluetooth®
Channel Sounding. A further PHY, LE Coded, is defined. Despite the name,
LE Coded uses the same Physical Layer parameters as LE 1M but applies
forward error-correction coding and pattern mapping in the Link
Layer.</td>
</tr>
</tbody>
</table>

*Table 2 -- Summary of the key responsibilities and features of each
layer of the Bluetooth LE stack*

The Physical Layer, Link Layer, Host Controller Interface, and Generic
Access Profile sections of the Bluetooth Core Specification have all
been impacted by the introduction of Bluetooth® Channel Sounding.
Section 4 explains this further.

Before Bluetooth® Channel Sounding can be started, the device in the
link layer LE Central role must connect to the device in the link layer
LE Peripheral role. Security is then started on the LE-ACL connection
that is established so that it can provide a secure transport for the
exchange of various link layer Protocol Data Units (PDUs) during several
procedures that are concerned with preparing for and then initiating
Bluetooth® Channel Sounding.

The main procedures which prepare for and then initiate Bluetooth®
Channel Sounding are:

1. Security Start
2. Capabilities Exchange
3. Configuration
4. Start

Not all of these procedures are mandatory, depending on issues such as
whether or not the two devices have previously exchanged information
which may have been cached. A possible sequence of procedures and
associated PDUs is shown in Figure 19.

[![Figure
19](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19.png "Figure 19 - A possible CS initiation procedure sequence"){.aligncenter
.wp-image-234450 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19.png 462w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19-319x600.png 319w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19-159x300.png 159w"
sizes="auto, (max-width: 924px) 100vw, 924px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19.png)

*Figure 19 -- A possible CS initiation procedure sequence*

Bluetooth® Channel Sounding has its own security capabilities that are
distinct from those associated with the LE-ACL connection over which the
initialization procedures are executed. The Bluetooth® Channel Sounding
Start Procedure allows the two devices to securely exchange parameters
that are later used in Bluetooth® Channel Sounding security functions.

The Bluetooth® Channel Sounding Security Start procedure starts with the
LE Central device generating three random numbers and sending them to
the LE Peripheral device in a LL_CS_SEC_REQ PDU. The LE Peripheral
device generates three random numbers of its own, governed by the same
rules as the Central's random numbers and sends them back to the Central
in a LL_CS_SEC_RSP PDU.

The random numbers generated by each device are named and described in
Table 3.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Name</th>
<th class="has-text-align-left" data-align="left">Description</th>
<th class="has-text-align-left" data-align="left">Length (bits)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">CS_IV_C</td>
<td class="has-text-align-left" data-align="left">Initialization Vector
generated by the Central.</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_IN_C</td>
<td class="has-text-align-left" data-align="left">Instantiation Nonce
generated by the Central.</td>
<td class="has-text-align-left" data-align="left">32</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_PV_C</td>
<td class="has-text-align-left" data-align="left">Personalization Vector
generated by the Central.</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_IV_P</td>
<td class="has-text-align-left" data-align="left">Initialization Vector
generated by the Peripheral.</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_IN_P</td>
<td class="has-text-align-left" data-align="left">Instantiation Nonce
generated by the Peripheral.</td>
<td class="has-text-align-left" data-align="left">32</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_PV_P</td>
<td class="has-text-align-left" data-align="left">Personalization Vector
generated by the Peripheral.</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
</tbody>
</table>

*Table 3 -- CS Security Parameters*

When both devices are in possession of both sets of Bluetooth® Channel
Sounding security parameters, the values of each Central/Peripheral pair
are concatenated by the respective link layers. This results in both
devices possessing the same values for the three Bluetooth® Channel
Sounding security parameters CS_IV, CS_IN and CS_PV.

The Bluetooth® Channel Sounding capabilities of two devices may vary
significantly and in order that a mutually supported configuration can
be arrived at before starting, the two devices must each be in
possession of information about the capabilities of the other device.

The exchange of capabilities is achieved by one device sending its
details in a LL_CS_CAPABILITIES_REQ PDU and the other responding with
its details in a LL_CS_CAPABILITIES_RSP PDU. A device may cache
capabilities data previously received by a device and therefore elect to
not exchange capabilities with the other device. Either device may
initiate this procedure, however.

Examples of ways in which capabilities may vary include PHY support, RTT
accuracy, Bluetooth® Channel Sounding modes^3^
supported, attack detection support, and the maximum number of antenna
paths supported.

This procedure involves the exchange of LL_CS_CONFIG_REQ and
LL_CS_CONFIG_RSP PDUs. In essence, using the capabilities previously
exchanged, this procedure then allows devices to select the specific
configuration that will be used.

Multiple configuration parameter sets may be maintained. Each such
configuration is assigned an identifier by the Host. This identifier
must be unique amongst the identifiers used by this pair of devices and
may be used to reference a given parameter set during link layer
procedures.

The application on the device which transmits the LL_CS_CONFIG_REQ PDU
is able to select which of the Initiator or Reflector roles it wants to
assume. The other device responds with LL_CS_CONFIG_RSP and must assume
the other role.

Fractional Frequency Offset Actuation Error (FAE) is a measure of the
difference between a generated frequency and the expected or requested
frequency, expressed in Parts Per Million (ppm). All devices have some
degree of inaccuracy in this respect, and, typically, its magnitude will
vary according to the RF channel in use.

For the purposes of achieving distance measurement results that are as
accurate as possible, a device which supports Bluetooth® Channel
Sounding may have a table of data called the Mode-0 FAE Table. The table
contains FAE values for each channel and is set up during the
manufacturing process.

The Mode-0 FAE Table Request procedure allows an Initiator to request a
Reflector's mode-0 FAE table. This involves the Initiator transmitting a
LL_CS_FAE_REQ PDU to which the Reflector replies with a LL_CS_FAE_RSP
PDU containing its FAE table.

Once acquired, the FAE table may be stored for future use with the same
Reflector so that this procedure need only be executed once for a given
device pair.

When Bluetooth® Channel Sounding security has been started, devices are
in possession of information about each others' capabilities, the
Initiator has the Reflector's mode-0 FAE table (if it has one) and the
devices have agreed on a suitable configuration, then the Channel
Sounding Start procedure may be initiated. This is accomplished via
LL_CS_REQ, LL_CS_RSP and LL_CS_IND PDUs.

The LL_CS_REQ and LL_CS_RSP PDUs include proposed timing and structural
parameters from each device. These parameters govern the way that time
is divided and how it is made use of during Bluetooth® Channel Sounding.
A LL_CS_IND PDU is sent by the device in the Central role after
receiving a LL_CS_REQ or LL_CS_RSP PDU from the Peripheral. The
LL_CS_IND indicates that Bluetooth® Channel Sounding should now start
and contains parameter values that are acceptable to both devices based
on the proposals contained within the previous exchanges of PDUs.

The Bluetooth® Channel Sounding procedure starts after the Bluetooth®
Channel Sounding Start procedure has completed. This is the mechanism by
which the two devices exchange RF signals for the purpose of taking
measurements that can be used by an application for distance
calculations.

In an ACL connection, packets can be transmitted during a connection
event. The timing of connection events is based on the value of the
connection interval parameter for that ACL connection. During a
connection event, the Central and the Peripheral devices each take turns
to transmit a packet with the Central transmitting first and the
Peripheral responding. Depending on other connection parameters, the
Peripheral may be permitted to only respond to a subset of packets and
the Central may be permitted to only transmit during a subset of events.

An LE-ACL connection is used during the initiation procedures of
Bluetooth® Channel Sounding as described in 3.3 Bluetooth® Channel
Sounding Control Procedures.

[![Figure
20](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20.png "Figure 20 - Connection Events and Intervals in an LE-ACL Connection"){.aligncenter
.wp-image-234451 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20.png 1369w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-600x208.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-768x266.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-800x277.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-1000x346.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-1200x415.png 1200w"
sizes="auto, (max-width: 1369px) 100vw, 1369px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20.png)

*Figure 20 -- Connection Events and Intervals in an LE-ACL Connection*

Bluetooth® Channel Sounding takes place in a series of procedures. Each
procedure consists of a number of CS Events, and each CS Event is
further partitioned into CS Subevents. The final subdivision of time
within this hierarchical scheme is the CS Step. It is within steps that
packets or tones are transmitted and received. Figure 21 depicts this
structural scheme for the partitioning of time by way of an example.

[![Figure
21](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21.png "Figure 21 - Structure of Bluetooth® Channel Sounding procedures"){.aligncenter
.wp-image-234452 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21.png 1824w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-600x302.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-300x151.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-768x386.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1536x772.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-450x226.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-660x332.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-800x402.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1000x503.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1200x603.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1600x804.png 1600w"
sizes="auto, (max-width: 1824px) 100vw, 1824px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21.png)

*Figure 21 -- Structure of Bluetooth® Channel Sounding procedures in an
example configuration*

There are a number of parameters that allow the structural aspects of
Bluetooth® Channel Sounding procedures to be controlled. Some of the key
configurable variables are shown in Table 4.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Configurable
Variable</th>
<th class="has-text-align-left" data-align="left">Range/Value</th>
<th class="has-text-align-left" data-align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Number of CS procedure
repetitions</td>
<td class="has-text-align-left" data-align="left">0 to 65535</td>
<td class="has-text-align-left" data-align="left">The number of CS
procedure repetitions to execute before Bluetooth® Channel Sounding is
terminated. A value of 0 indicates that CS procedures should run until
terminated via the Bluetooth® Channel Sounding Procedure Repeat
Termination procedure.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Number of subevents
per event</td>
<td class="has-text-align-left" data-align="left">1 to 16</td>
<td class="has-text-align-left" data-align="left">The number of
subevents anchored off the same ACL event.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Subevent Interval</td>
<td class="has-text-align-left" data-align="left">0 or in the range 625
us to 40959.375 ms.</td>
<td class="has-text-align-left" data-align="left">Time interval between
the beginning of a CS subevent and the beginning of the next CS subevent
within the same CS event. 0 means no division into subevents.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Duration of each
subevent</td>
<td class="has-text-align-left" data-align="left">Variable</td>
<td class="has-text-align-left" data-align="left">The duration of each
subevent.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Number of steps per
subevent</td>
<td class="has-text-align-left" data-align="left">2 to 160</td>
<td class="has-text-align-left" data-align="left">Randomly selected from
a configured range. There are a maximum of 256 steps per procedure.</td>
</tr>
</tbody>
</table>

*Table 4 -- Example Bluetooth® Channel Sounding configuration
parameters*

The timing, duration, and scheduling of procedures, events, subevents,
and steps is controlled by a number of parameters which are configured
during the Bluetooth® Channel Sounding Configuration and Bluetooth®
Channel Sounding Start procedures.

All procedure, event, subevent, and step start times are directly or
indirectly anchored to a selected connection event in the underlying LE
ACL connection. In the first Bluetooth® Channel Sounding procedure
instance, its first event and subevent all start at the same time,
scheduled to occur at an offset from the selected connection event
anchor point. The first step occurs at an offset from the start of the
first subevent called T_FCS. T_FCS has a value in the range 15 μs to 150
μs, and the period it covers is used to change the frequency by hopping.

Both procedures and events occur at intervals whose value is expressed
in terms of a number of ACL connection intervals. Figure 22 shows an
example where the procedure interval has a value of 4 and the event
interval a value of 2.

[![Figure
22](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22.png "Figure 22 - Procedure and Event Scheduling"){.aligncenter
.wp-image-234453 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22.png 1713w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-600x243.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-300x121.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-768x311.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1536x621.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-450x182.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-660x267.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-800x324.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1000x405.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1200x485.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1600x647.png 1600w"
sizes="auto, (max-width: 1713px) 100vw, 1713px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22.png)

*Figure 22 -- Procedure and Event Scheduling with procedure interval = 4
and event interval = 2*

The first subevent in each event starts at the same time as the event,
offset from the relevant ACL connection event. The number of subevents
per event is a configuration parameter and subevents occur once per
subevent interval as shown in Figure 23.

[![Figure
23](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23.png "Figure 23 - Example of CS subevent within CS event scheduling"){.aligncenter
.wp-image-234454 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23.png 1713w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-600x243.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-300x121.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-768x311.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1536x621.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-450x182.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-660x267.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-800x324.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1000x405.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1200x485.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1600x647.png 1600w"
sizes="auto, (max-width: 1713px) 100vw, 1713px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23.png)

*Figure 23 -- Example of CS subevent within CS event scheduling*

Each subevent includes at least two steps. This can vary from subevent
to subevent, depending on how channel sounding is being used by the
application. Steps can vary in duration, again, depending on
configuration. The scheduling of steps and the RF transmission and
reception slots assigned to them is subject to meticulous timing rules,
further details of which can be found in the Bluetooth Core
Specification.

It is within steps that an exchange of RF signals between Initiator and
Receiver takes place. Depending on the channel sounding method or
methods that the application layer has opted to use (PBR and/or RTT),
details vary.

In general, steps are either concerned with calibration or with the
acquisition of low-level measurements that can be used by the
application layer in a distance measurement algorithm.

When RTT is in use, packets of a type called CS_Sync are exchanged by
Initiator and Reflector.

[![Figure
24](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24.png "Figure 24 - The CS_Sync Packet"){.aligncenter
.wp-image-234455 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24.png 1937w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-600x125.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-300x62.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-768x159.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1536x319.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-450x93.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-660x137.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-800x166.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1000x208.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1200x249.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1600x332.png 1600w"
sizes="auto, (max-width: 1937px) 100vw, 1937px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24.png)

*Figure 24 -- The CS_Sync Packet*

The inclusion of a Sounding Sequence or Random Sequence at the end of a
CS_Sync packet is optional. CS_Sync packets can be transmitted using
either the LE 1M, LE 2M or LE 2M 2BT PHY. The GFSK^4^
modulation scheme is used as with other Bluetooth LE packets.

When PBR is in use, signals known as CS Tones are exchanged by Initiator
and Reflector. These signals use Amplitude Shift Keying (ASK) to create
a symbol whose frequency is fixed for a specified period of time.

Steps have an associated mode which determines the goal of the step and
the type of activity that takes place within it. Four modes are defined
and are designated mode-0, mode-1, mode-2, and mode-3.

Mode-0 is concerned with calibration. All devices will exhibit some
degree of clock drift and inaccuracy in frequency generation. This is an
issue for both the RTT and PBR distance measurement methods.

The purpose of a mode-0 step is to allow the Initiator to measure the
amount by which the frequency of signals transmitted by the Reflector
differ from those generated by the Transmitter.

The Initiator transmits a CS_Sync packet on a selected channel and
frequency. The Reflector replies with a CS_Sync packet and a CS Tone.
Both are required to be transmitted on the same frequency as the signal
received from the Initiator.

On receiving the response signal from the Reflector, the Initiator
calculates a value called the Fractional Frequency Offset (FFO). The
calculation of FFO involves the frequency of the tone received from the
Reflector and the Reflector's mode-0 FAE table. FFO is later used in
calculations to compensate for the differences between the two devices
and improve the accuracy of the results.

Figure 25 shows the transmission of a CS_Sync packet by the Initiator
followed by the CS_Sync and CS Tone sent in response by the Reflector.
The duration of various time slots are indicated by symbolic names with
the following meanings:

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Symbol</th>
<th class="has-text-align-left" data-align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">T_SY</td>
<td class="has-text-align-left" data-align="left">Time for
synchronization sequence. Duration depends on CS_Sync packet length and
the PHY used.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_RD</td>
<td class="has-text-align-left" data-align="left">Time for transmission
ramp down. This is 5 μs and is used by the transmitter to remove energy
from the RF channel.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_IP1</td>
<td class="has-text-align-left" data-align="left">Time for interlude
period between the end of the Initiator’s transmission and the start of
the transmission by the Reflector. Durations vary between 10 μs and 145
μs and are determined in the capabilities exchange procedure.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_GD</td>
<td class="has-text-align-left" data-align="left">Guard time. Always 10
μs in duration.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_FM</td>
<td class="has-text-align-left" data-align="left">Time for frequency
measurement. Always 80 μs in duration for step mode-0.</td>
</tr>
</tbody>
</table>

*Table 5 -- Time slot parameters*

[![Figure
25](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25.png "Figure 25 - Mode-0 transmissions and time slots"){.aligncenter
.wp-image-234456 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25.png 1713w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-600x163.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-300x82.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-768x209.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1536x418.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-450x122.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-660x180.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-800x218.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1000x272.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1200x326.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1600x435.png 1600w"
sizes="auto, (max-width: 1713px) 100vw, 1713px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25.png)

*Figure 25 -- Mode-0 transmissions and time slots*

Support for mode-0 steps is mandatory.

In a mode-1 step, the round-trip timing (RTT) of a CS_Sync packet sent
from an Initiator to a Reflector and back again is calculated.

A timestamp is recorded by the Initiator when transmitting the initial
CS_Sync packet and is known as the Time of Departure (ToD). The
Initiator records a second timestamp on receiving the CS_Sync packet
sent back by the Reflector. This is known as the Time of Arrival (ToA).

[![Figure
26](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1000x248.png "Figure 26 - Mode-1 transmissions and time slots"){.aligncenter
.wp-image-234457 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1000x248.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-600x149.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-300x74.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-768x191.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1536x381.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-450x112.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-660x164.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-800x199.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1200x298.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1600x397.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26.png 1878w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26.png)

*Figure 26 -- Mode-1 transmissions and time slots*

The interlude period, T_IP1 is of a known fixed length that is
sufficient in duration for the Reflector to prepare and then transmit
its packet. The use of a pre-agreed, fixed period in this part of the
exchange means that the Initiator knows the turnaround time at the
Receiver and can use this in its RTT calculation.

Support for mode-1 steps is mandatory.

The purpose of a mode-2 step is to support phase-based ranging (PBR).

A mode-2 step starts with the Initiator transmitting a CS Tone on a
selected channel and via each available antenna path. After a ramp down
time and interlude period, the Reflector replies with a CS Tone,
selecting the same frequency as the tone received from the Initiator and
over each of its antenna paths. Figure 27 illustrates the exchange. Time
slot duration involves the terms described in Table 5 and the additional
terms defined in Table 6.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Symbol</th>
<th class="has-text-align-left" data-align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">T_SW</td>
<td class="has-text-align-left" data-align="left">Time period reserved
for antenna switching.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_PM</td>
<td class="has-text-align-left" data-align="left">Time for the
transmission of a phase measurement tone.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_IP2</td>
<td class="has-text-align-left" data-align="left">Time for interlude
period between CS Tones.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">N_AP</td>
<td class="has-text-align-left" data-align="left">Number of antenna
paths.</td>
</tr>
</tbody>
</table>

*Table 6 -- Additional step mode-2 timing parameters*

[![Figure
27](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1000x268.png "Figure 27 - mode-2 transmissions and time slots"){.aligncenter
.wp-image-234458 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1000x268.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-600x161.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-300x81.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-768x206.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1536x412.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-450x121.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-660x177.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-800x215.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1200x322.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1600x429.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27.png 1878w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27.png)

*Figure 27 -- mode-2 transmissions and time slots*

The Initiator measures the phase of CS Tone received from the Reflector
during the period T_PM, once for each antenna path. Adjustments are made
using compensation values calculated in the mode-0 step. Phase
measurements are passed to the application layer in an HCI event in the
form of an array of IQ samples.

It should be noted that the expression for the total duration of the CS
Tone(s) transmission includes the term **N_AP + 1**. This is because an
extra time period known as a CS Tone extension slot follows the T_PM
duration time slots that are allocated for each antenna path. Use of
this time slot for transmission is randomized for security reasons, but,
when it is used, a CS Tone is transmitted using the same antenna used in
the immediately prior T_PM time slot.

Support for mode-2 steps is mandatory.

A mode-3 step supports both RTT calculation and PBR using combined
exchanges of CS_Sync packets and CS Tones.

[![Figure
28](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1000x260.png "Figure 28 - mode-3 transmissions and time slots"){.aligncenter
.wp-image-234459 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1000x260.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-600x156.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-300x78.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-768x200.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1536x400.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-450x117.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-660x172.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-800x208.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1200x312.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1600x417.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B.png 1878w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B.png)

*Figure 28 -- mode-3 transmissions and time slots*

Support for mode-3 is not mandatory. Applications wishing to combine PBR
and RTT but finding through the capabilities exchange procedure that
mode-3 is not supported by both Initiator and Reflector may instead use
a mode sequence that combines both mode-2 and mode-1 steps.

Mode-3 steps include an extension slot as was described for mode-2
steps.

In the previous sections on mode-0, mode-1, mode-2, and mode-3 steps,
the focus was on the details of how time is divided and used in a single
step of each type. But distance calculations require multiple exchanges,
either to improve the accuracy of the calculated distance or because the
method used demands it. PBR by definition, needs at least two exchanges.

For phase differences to be available for measurement, there needs to be
more than one transmitted signal and more than one frequency must be
involved. A single step involves the exchange of a single CS Tone on a
single selected channel and frequency. As such, it is clear that the PBR
method requires the execution of an absolute minimum of two steps of a
mode that supports the PBR method. It should be noted that in general
terms, a larger number of CS Tone exchanges using a correspondingly
larger set of RF channels will provide the application with more data
and the opportunity to produce more accurate distance measurements. A
larger number of exchanges will require more time to execute, however.

As noted in 3.2.3 Antenna Arrays, devices may include multiple antennas
for use during phase-based ranging exchanges. The maximum number of
antennas that a device may have for use during PBR exchanges (i.e.,
mode-2 or mode-3 steps) is four. A given pair of antenna configurations,
one belonging to the Initiator and one to the Reflector, provides a
number of antenna paths between the two devices.

A total of eight antenna permutations are defined by the Bluetooth Core
Specification. Table 7 lists these configurations.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Antenna Configuration
Index (ACI)</th>
<th class="has-text-align-left" data-align="left">Device A number of
antennas</th>
<th class="has-text-align-left" data-align="left">Device B number of
antennas</th>
<th class="has-text-align-left" data-align="left">Number of antenna
paths (N_AP)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0</td>
<td class="has-text-align-left" data-align="left">1</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">3</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">3</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">3</td>
<td class="has-text-align-left" data-align="left">4</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">4</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">4</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">5</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">3</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">6</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">4</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">7</td>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">4</td>
</tr>
</tbody>
</table>

*Table 7 -- Antenna Configurations*

Antenna switching takes place during mode-2 steps (PBR) and during the
PBR-related part of each mode-3 step. Specifically, it is when
transmitting a CS Tone that antenna switching can be applied, depending
on the antenna configuration of the transmitting device. The calculation
of the duration of the CS Tone transmission time slots in mode-2 and
mode-3 steps accommodates antenna switching and multiple antenna paths:

*(T_SW+T_PM)\*(N_AP+1)*

- T_SW provides time for antenna switching to take place and has a value
of either 0, 2, 4, or 10 microseconds.
- T_PM is the time for the transmission of the CS Tone.
- N_AP is the number of antenna paths. The +1 term is to allow for the
extension slot.

A Bluetooth® Channel Sounding procedure always involves the execution of
a sequence of multiple steps and a mix of at least two modes. The
Bluetooth Core Specification defines mode combination and sequencing
rules, key aspects of which shall be explored in this section.

Bluetooth® Channel Sounding applications will produce better quality,
more accurate distance measurements when provided with data by the
Bluetooth controller that is derived from larger numbers of exchanges of
packets and tones.

Steps of at least two different mode types are always involved in a
Bluetooth® Channel Sounding procedure. The first is the mode-0 step for
frequency offset measurement and the second must be any one of the other
modes. The primary non-mode-0 mode is called the Main_Mode. The
secondary non-mode-0 mode, if there is one, is called the Sub_Mode.
Table 8 lists the six permitted non-mode-0 mode combinations.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Main_Mode</th>
<th class="has-text-align-left" data-align="left">Sub_Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Mode-1</td>
<td class="has-text-align-left" data-align="left">None</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Mode-2</td>
<td class="has-text-align-left" data-align="left">None</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Mode-3</td>
<td class="has-text-align-left" data-align="left">None</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Mode-2</td>
<td class="has-text-align-left" data-align="left">Mode-1</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Mode-2</td>
<td class="has-text-align-left" data-align="left">Mode-3</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Mode-3</td>
<td class="has-text-align-left" data-align="left">Mode-2</td>
</tr>
</tbody>
</table>

*Table 8 -- Permitted non-mode-0 mode combinations*

Applications are able to configure the step mode sequence using HCI
commands. Amongst the key parameters that may be requested and agreed
between devices are those shown in Table 9.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">HCI Parameter</th>
<th class="has-text-align-left" data-align="left">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Mode_0_Steps</td>
<td class="has-text-align-left" data-align="left">Defines the number of
consecutive mode-0 steps to be executed at the start of each CS
subevent. Permitted values are 1, 2, or 3.</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Main_Mode_Type</td>
<td class="has-text-align-left" data-align="left">Indicates the mode
which will be the main mode (1, 2, or 3).</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Sub_Mode_Type</td>
<td class="has-text-align-left" data-align="left">Indicates the mode
which will be the submode (1, 2, or 3).</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">Min_Main_Mode_Steps</td>
<td class="has-text-align-left" data-align="left">Determines the minimum
number of main mode steps that must always be executed before a submode
step.</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">Max_Main_Mode_Steps</td>
<td class="has-text-align-left" data-align="left">Determines the maximum
number of main mode steps that must always be executed before a submode
step.</td>
</tr>
</tbody>
</table>

*Table 9 -- Mode sequencing control parameters*

In general, step mode sequencing follows this pattern:

1. One or more mode-0 steps start the subevent
2. A sequence of n main mode steps then follows, where n is randomly
selected and falls in the range of Min_Main_Mode_Steps to
Max_Main_Mode_Steps inclusive
3. A single submode step follows the sequence of n main mode steps due
to a process that the Bluetooth Core Specification calls sub_mode
insertion

Step mode sequences are not tied to subevent boundaries other than by
the general rule that subevents must always start with one or more
mode-0 steps. Full sequences can span more than one subevent.

[![Figure
32](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1000x334.png "Figure 33 - A step mode sequence example"){.aligncenter
.wp-image-234464 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1000x334.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-600x200.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-2000x667.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-300x100.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-768x256.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1536x513.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-2048x683.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-450x150.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-660x220.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-800x267.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1200x400.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1600x534.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32.png)

*Figure 33 -- A step mode sequence example*

There is another mode sequencing parameter that can be used by
applications. Main_Mode_Repetition specifies a number of the most recent
main mode steps from the last subevent to be repeated in the current
subevent.

When main mode repetition applies, the steps repeated in the current
subevent use the same channel index as was used for the respective steps
in the previous subevent. This ensures that the repeated step
transmissions have the same intended frequency. Note that the purpose of
repeating main mode steps on the same frequency is to address possible
frequency drift as well as Doppler shift effects.

Main mode repetition affords applications the opportunity to correlate
some of the properties of the exchanges and may make it easier to track
the velocity of moving devices.

Steps that are incorporated into the mode sequence due to main mode
repetition are not counted in the submode insertion process.

The ability to configure mode combinations and control step mode
sequences using submode insertion and main mode repetition gives
applications a lot of control over the process of Bluetooth® Channel
Sounding. PBR is the most accurate of the two distance measurement
methods and using RTT at the same time adds considerable security to the
system. It also allows distance ambiguity which can arise using the PBR
method to be dealt with.

Step mode-3 provides support for both methods in a single mode type but
support for mode-3 is optional. Therefore devices that discover during
the capabilities exchange procedure that mode-3 is not available, must
mix mode-1 (RTT) and mode-2 (PBR) steps. This can be achieved by
selecting mode-2 as the main mode and mode-1 as the submode.

A further consideration for applications is latency. Each exchange of
signals takes time. Mode-1 RTT exchanges sometimes take longer than
Mode-2 PBR exchanges depending on the number of antenna paths.
Applications that need to keep latency below a certain threshold are
likely to opt to include a lower proportion of RTT exchanges in the
Bluetooth® Channel Sounding procedure.

[![Figure
34](https://www.bluetooth.com/wp-content/uploads/2025/01/Figure_34-1000x334.png "Figure 34 - A 3:1 PBR to RTT ratio using mode-2 and mode-1"){.aligncenter
.wp-image-234464 .size-1000w loading="lazy" decoding="async"
height="334"}](https://www.bluetooth.com/wp-content/uploads/2025/01/Figure_34.png)

*Figure 34 -- A 3:1 PBR to RTT ratio using mode-2 and mode-1*

[![Figure
35](https://www.bluetooth.com/wp-content/uploads/2025/01/Figure_35-1-1000x334.png "Figure 35 - A 3:1 PBR to RTT ratio using mode-2 and mode-3"){.aligncenter
.wp-image-234464 .size-1000w loading="lazy" decoding="async"
height="334"}](https://www.bluetooth.com/wp-content/uploads/2025/01/Figure_35-1.png)

*Figure 35 -- A 3:1 PBR to RTT ratio using mode-2 and mode-3*

Typically, Bluetooth LE divides the 2.4 GHz ISM band into 40 channels,
each 2 MHz wide. This is not the case when using Bluetooth® Channel
Sounding, however.

For the purposes of Bluetooth® Channel Sounding, 72 channels are
defined, each with a 1 MHz width and a unique channel index value. The
arrangement of these channels ensures that the LE primary advertising
channels are avoided.

A channel width of 1 MHz rather than the usual 2 MHz ensures that the
frequency separation between PBR signals that use adjacent channels is
such that distance ambiguity does not arise until around 150 meters.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">CS Channel Index</th>
<th class="has-text-align-left" data-align="left">RF Center
Frequency</th>
<th class="has-text-align-left" data-align="left">Allowed</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0</td>
<td class="has-text-align-left" data-align="left">2402 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2403 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">2404 MHz</td>
<td class="has-text-align-left" data-align="left">Yes</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">…</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">22</td>
<td class="has-text-align-left" data-align="left">2424 MHz</td>
<td class="has-text-align-left" data-align="left">Yes</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">23</td>
<td class="has-text-align-left" data-align="left">2425 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">24</td>
<td class="has-text-align-left" data-align="left">2426 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">25</td>
<td class="has-text-align-left" data-align="left">2427 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">26</td>
<td class="has-text-align-left" data-align="left">2428 MHz</td>
<td class="has-text-align-left" data-align="left">Yes</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">…</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">76</td>
<td class="has-text-align-left" data-align="left">2478 MHz</td>
<td class="has-text-align-left" data-align="left">Yes</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">77</td>
<td class="has-text-align-left" data-align="left">2479 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">78</td>
<td class="has-text-align-left" data-align="left">2480 MHz</td>
<td class="has-text-align-left" data-align="left">No</td>
</tr>
</tbody>
</table>

*Table 10 -- Bluetooth® Channel Sounding channel indices and RF physical
channels*

A channel index filter bit map is maintained. This is a list of the
channel indices defined for Bluetooth® Channel Sounding with each
channel marked as either included or excluded. The Bluetooth® Channel
Sounding channel index filter map is maintained by a link layer
procedure called Channel Sounding Channel Map Update procedure which
allows either the Initiator or Reflector to inform the other device
about which channels to use or avoid, based on its assessment of local
channel conditions. An excluded channel is never selected by any of the
channel selection algorithms.

Frequency hopping generally takes place immediately before the execution
of a step, as depicted in Figure 36.

[![Figure
35](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1000x81.png "Figure 36 - Frequency hopping ahead of step execution"){.aligncenter
.wp-image-234467 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1000x81.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-600x49.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-2000x162.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-300x24.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-768x62.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1536x124.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-2048x166.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-450x36.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-660x53.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-800x65.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1200x97.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1600x129.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35.png)

*Figure 36 -- Frequency hopping ahead of step execution*

An exception to this rule applies when mode repetition has been
configured with a non-zero value assigned to the Main_Mode_Repetition
parameter. Steps repeated due to mode repetition will use the same
channel index as the step in the previous subevent that they repeat.

A new set of three channel selection algorithms (CSA) has been defined
for use in Bluetooth® Channel Sounding. Collectively they are known as
CSA #3 and individually as CSA #3a, CSA #3b, and CSA #3c.

CSA #3a is used solely for selecting the channel to use in mode-0 steps.
CSA #3b and CSA #3c are both designed for use with non-mode-0 steps but
only one of the two may be used during a Bluetooth® Channel Sounding
procedure instance. Consequently, two different channel selection
algorithms are actively associated with Bluetooth® Channel Sounding at
any time.

Channel selection involves two distinct channel index lists. The first
is used by CSA #3a and the selection of channels for mode-0 steps. The
second is used for non-mode-0 steps with CSA #3b or CSA #3c.

Channel index lists are created by randomizing the order of those
channels marked as included in the channel map to create a shuffled
channel list. CSA #3a and CSA #3b do this in exactly the same way. CSA
#3c takes a different approach but relies on the same primitive
shuffling function, known as cr1 in the Bluetooth Core Specification.

The mode-0 channel selection algorithm CSA #3a uses a shuffled channel
list. The shuffled channel list used for mode-0 step frequency hopping
is distinct from the corresponding list of channels used for non-mode-0
channel hopping. Each entry in the shuffled channel list is unique and
used only once. When all entries in the shuffled channel list have been
used it is regenerated, creating a new randomized list of channels.

The non-mode-0 channel selection algorithm CSA #3b uses a shuffled
channel list that is distinct from the corresponding list of channels
used for mode-0 channel hopping. CSA #3b allows the channel index list
to be iterated more than once before it is regenerated, and this is
controlled by a parameter called CSNumRepetitions which applications may
set.

Algorithm CSA #3c is significantly different to CSA #3b. Subsets of the
included channels in the channel map are organized into groups and
channel patterns generated which form shapes. Two pattern types are
supported and named hat and X. CSA #3c may offer some advantages in
detecting reflected signal paths in some circumstances. Support for CSA
#3c is optional.

The RTT method involves the exchange of CS_Sync packets in steps of
mode-1 and/or mode-3. Several ways of establishing the Time of Arrival
(ToA) timestamps, that are needed for the calculation of round-trip
times, are defined. An application can indicate the method to be used
during the Bluetooth® Channel Sounding configuration procedure via HCI
commands using the RTT_Type parameter.

The options are to base timing measurements on the Access Address field,
to use a sounding sequence that is either 32 or 96 bits in length, or to
use a random sequence which may be 32, 64, 96, or 128 bits in length.
The accuracy of time estimates varies according to the method used and
the length of the field used for timing purposes. Both the use of a
sounding sequence and the use of a random sequence allow a more accurate
form of estimate known as a fractional timing estimate to be made.

CS_Sync packets contain a 32-bit Access Address field. The simplest
method which may be used to establish a ToA value involves the
controller using its clock to capture a timestamp at the time when the
Access Address field in a CS_Sync packet has been received.

An Access Address is a 32-bit binary value at the link layer but when
transmitted its value is represented by a series of analog symbols,
formed by applying GFSK modulation to those digital bits. A single
symbol consists of a radio transmission at a frequency that represents a
0- or 1-bit value and that depending on the symbol rate, has a duration
of either one microsecond or half a microsecond.

The transmitter's oscillator and the receiver's oscillator are unlikely
to be in phase with each other and this can be a source of inaccuracies
in this process. To improve results, it is suggested that measurements
are taken over a series of packets exchanged in a sequence of steps and
the distribution of values calculated. This distribution can then be
used to improve the accuracy of ToA timestamps.

Two optional methods which offer better ToA timestamp accuracy are
described in the Link Layer Specification, Part H, sections 3.3 and 3.4.
Both provide fractional timing estimates.

CS_Sync packets can accommodate extra, optional data at the end of the
packet. If this option is used, one of two fields may be appended to the
CS_Sync packet: either a Random Sequence or a Sounding Sequence.

The first of the fractional timing methods involves analyzing the
optional Random Sequence field in CS_Sync packets to determine
fractional timing errors. The fractional timing error calculated from
the Random Sequence is used to optimize the Access Address timestamp.

The second fractional timing method is based on an analysis of a
Sounding Sequence field appended to a CS_Sync packet. A sounding
sequence is an alternating pattern of 0s and 1s at the link layer which
when modulated using GFSK produces two distinct radio tones with
different frequencies and differing phases. An analysis of the phase
difference exhibited by the two tones allows a fractional timing error
to be calculated and used to optimize the ToA timestamp.

Bluetooth® Channel Sounding application developers can derive round-trip
times based on measurements produced by one of three different methods.
The choices are to use the ToA of an Access Address or to use one of two
fractional methods based on either a random sequence or a sounding
sequence in a CS_Sync packet.

The three RTT methods offer differing degrees of distance measurement
accuracy, security and latency for application developers. In general,
the fractional methods have the potential to deliver the most accurate
results and the best security.

A modulation scheme defines a means of encoding digital information in
signals using one or more of the signal's physical properties. Frequency
Shift Keying (FSK) is a simple example of a modulation scheme. It
involves producing a symbol that represents a binary value of 1 by
shifting the frequency of a carrier signal up by a certain amount (the
frequency deviation) or down by the same amount to represent a binary 0.

[![Figure
36](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1000x256.png "Figure 37 - Frequency Shift Keying (FSK) encoded bit stream"){.aligncenter
.wp-image-234468 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1000x256.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-600x154.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-2000x513.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-300x77.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-768x197.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1536x394.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-2048x525.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-450x115.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-660x169.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-800x205.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1200x308.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1600x410.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36.png)

*Figure 37 -- Frequency Shift Keying (FSK) encoded bit stream
01010101010*

The abrupt switching between frequencies that is a feature of basic FSK
results in the generation of noise that spreads over a wider range of
frequencies than is desirable. To counter this, Bluetooth technology
uses a special variant of FSK called Gaussian Frequency Shift Keying
(GFSK). GFSK differs from basic FSK in that it involves a filter that
causes the transition between frequencies to follow a curve. The shape
of the curve and the rate of frequency transitions is determined by
various parameters, including the Bandwidth-Bit Period Product or BT.

The Bandwidth-Bit Period Product (BT) is an attribute of a signal that
provides information about the relationship between its bandwidth and
the duration of symbols. BT affects the shape and span of the radio
pulses that constitute symbols. A higher BT value results in a narrower,
squarer pulse and a lower value results in a wider, more rounded pulse
shape.

The Bluetooth Core Specification introduces a new PHY called LE 2M 2BT.
LE 2M 2BT may currently only be used with Bluetooth® Channel Sounding. A
comparison of PHYs with key aspects of LE 2M 2BT highlighted appears in
Table 11.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left"></th>
<th class="has-text-align-left" data-align="left">LE 1M</th>
<th class="has-text-align-left" data-align="left">LE Coded</th>
<th class="has-text-align-left" data-align="left">LE 2M</th>
<th class="has-text-align-left" data-align="left">LE 2M 2BT</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Symbol Rate</td>
<td class="has-text-align-left" data-align="left">1 Msym/s</td>
<td class="has-text-align-left" data-align="left">2 Msym/s</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">BT</td>
<td class="has-text-align-left" data-align="left">0.5</td>
<td class="has-text-align-left" data-align="left">2.0</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Min. Frequency
Deviation</td>
<td class="has-text-align-left" data-align="left">185 kHz</td>
<td class="has-text-align-left" data-align="left">370 kHz</td>
<td class="has-text-align-left" data-align="left">420 kHz</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Error Detection</td>
<td class="has-text-align-left" data-align="left">CRC</td>
<td class="has-text-align-left" data-align="left">N/A</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Error Correction</td>
<td class="has-text-align-left" data-align="left">NONE</td>
<td class="has-text-align-left" data-align="left">FEC</td>
<td class="has-text-align-left" data-align="left">NONE</td>
<td class="has-text-align-left" data-align="left">N/A</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Requirement</td>
<td class="has-text-align-left" data-align="left">Mandatory</td>
<td class="has-text-align-left" data-align="left">Optional</td>
<td class="has-text-align-left" data-align="left">Optional. Only to be
used with Channel Sounding.</td>
</tr>
</tbody>
</table>

*Table 11 -- A comparison of Bluetooth LE PHYs*

[![Figure
37](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37.png "Figure 38 - Pulse Shapes"){.aligncenter
.wp-image-234469 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37.png 778w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-600x471.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-300x236.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-768x603.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-450x353.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-660x518.png 660w"
sizes="auto, (max-width: 778px) 100vw, 778px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37.png)

*Figure 38 -- Pulse Shapes*

Some radio transmitters have the ability to adjust their signal-to-noise
ratio (SNR) to lie within a specified range. This capability, if
supported by both the Initiator and Reflector devices, can be used to
improve the security of Bluetooth® Channel Sounding steps that relate to
the RTT distance measurement method i.e. mode-1 and mode-3 steps.

The Bluetooth Core Specification defines a number of SNR Output Index
(SOI) values that correspond to associated SNR output levels measured in
dB. Table 12 reproduces these definitions.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">SNR Output Index
(SOI)</th>
<th class="has-text-align-left" data-align="left">SNR Output Level
(dB)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0</td>
<td class="has-text-align-left" data-align="left">18</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">21</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">24</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">3</td>
<td class="has-text-align-left" data-align="left">27</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">4</td>
<td class="has-text-align-left" data-align="left">30</td>
</tr>
</tbody>
</table>

*Table 12 -- SNR Output Indices and Levels*

Security issues that are unique to distance measurement solutions
generally involve the threat of untrusted devices somehow tricking one
trusted device into concluding that another trusted device is
sufficiently close for some action to be granted or taken.

Bluetooth® Channel Sounding includes a collection of features which can
act as countermeasures to a number of distance measurement security
threats. These features can be regarded as falling into four categories:

1. Using PBR and RTT methods in combination
2. Randomization of the bit stream and transmission patterns
3. Defense against symbol manipulation
4. RF signal analysis techniques including attack detection

Bluetooth® Channel Sounding supports two distance measurement methods,
phase-based ranging (PBR) and round-trip timing (RTT). The two methods
work completely differently. An application may use both methods in
conjunction by selecting a suitable mode combination such as mode-2 as
the main mode for PBR and mode-1 as the submode for RTT.

The complexity of attacking both methods simultaneously so that both the
phase of the Bluetooth® Channel Sounding signals and calculated
round-trip times are manipulated to give misleading and consistent
results is regarded by security experts as very high.

Firstly, devices must have been paired with each other. This is
necessary for it to be possible for an encrypted LE-ACL link to be
created. CS Security Start then takes place over the encrypted LE-ACL
link which means that the exchange of Bluetooth® Channel Sounding
security key data is protected from eavesdroppers.

Finally, both the Central and Peripheral devices perform a secure
exchange of partial values of Bluetooth® Channel Sounding security data.
This provides both devices with the same data from which to construct a
complete and common value for each of the CS initialization vector
(CS_IV), CS instantiation nonce (CS_IN) and CS personalization vector
(CS_PV).

The Bluetooth Core Specification defines a random bit generator that is
consistent with the recommendations defined in NIST Special Publication
800-90Ar1. It is known as the Deterministic Random Bit Generator or
DRBG.

Instantiating DRBG requires the three Bluetooth® Channel Sounding
security parameters, CS_IV, CS_IN and CS_PV to be provided as inputs.
Having executed the Bluetooth® Channel Sounding Security Start
procedure, both the Initiator and Reflector device possess the same
values for these parameters. When initialized with the same parameters
values, two instances of DRBG will produce exactly the same bit
sequences over a series of invocations and it is this which makes the
algorithm deterministic.

In the case of Bluetooth® Channel Sounding, each device changes its
Access Address field in CS_Sync packets at every mode-0, mode-1 and
mode-3 CS step. New Access Address values are generated using selection
rules that involve the DRBG and both devices know the Access Address
that will be used by the other. Receiving devices check the Access
Address value and report any issues to the host.

The Access Address field is 32 bits in length and can have 4,294,967,296
different values. A malicious device wishing to spoof a CS_Sync packet
will therefore have a 1 in 4,294,967,296 chance of guessing the correct
Access Address value in each one of the multiple CS_Sync packets
exchanged.

CS_Sync packets can include an optional Random Sequence field. This
field supports one of the fractional RTT methods. The content of the
Random Sequence field is regenerated using the CS DRBG for every
transmitted CS_Sync packet. The Random Sequence field may be 32, 64, 96,
or 128 bits in length.

A Sounding Sequence consists of a predictable alternating pattern of 32
or 96-bits and is used for fractional RTT calculations. To mitigate the
risk of this known bit pattern being exploited, DRBG is used to select
positions within the sequence to insert one of two randomly selected
4-bit values known as marker signals. Marker signals selected by DRBG
have a value of either 0b1100 or 0b0011. The random insertion of random
bit patterns within a sounding sequence protects against sounding
sequence spoofing.

Mode-2 and mode-3 steps include a tone extension slot. The tone
extension slot is always reserved but whether or not a transmission
takes place in that time slot is randomized and governed by DRBG. The
receiving device knows when to expect and when not to expect a
transmission in the tone extension slot but an attacking device does
not.

During phase-based ranging, a tone is transmitted over every available
antenna path that exists between the two devices. The sequence of paths
used is randomized using DRBG at every Bluetooth® Channel Sounding step.

A sounding sequence consists of a sequence of alternating bit values of
0 and 1. The corresponding RF signal can be viewed as consisting of two
tones of different frequencies and with differing phases. PBR
calculations can therefore be made using the phase differences of the
two tones encoded in the Sounding Sequence field of a single CS_Sync
packet simultaneously while using the CS_Sync packet to calculate a
round-trip time. The simultaneous calculation of both RTT and PBR
measurements based on a single packet makes an attempt to attack the
exchange extremely complex.

The Bluetooth® Channel Sounding section of the Link Layer specification
includes a description of an attack detector system. Bluetooth® Channel
Sounding attack detection in the Bluetooth controller is based on the
evaluation of received signals against a reference signal definition and
the examination of the received signal for indicators of a possible
attack such as unexpected bit transitions or phase adjustments.

A standardized metric for reporting the probability of an attack being
underway is defined by the Bluetooth Core Specification and is called
the Normalized Attack Detector Metric or NADM. Table 13 contains the
NADM value definitions.

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">NADM Value</th>
<th class="has-text-align-left" data-align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0x00</td>
<td class="has-text-align-left" data-align="left">Attack is extremely
unlikely</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x01</td>
<td class="has-text-align-left" data-align="left">Attack is very
unlikely</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x02</td>
<td class="has-text-align-left" data-align="left">Attack is
unlikely</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x03</td>
<td class="has-text-align-left" data-align="left">Attack is
possible</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x04</td>
<td class="has-text-align-left" data-align="left">Attack is likely</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x05</td>
<td class="has-text-align-left" data-align="left">Attack is very
likely</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x06</td>
<td class="has-text-align-left" data-align="left">Attack is extremely
likely</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0xFF</td>
<td class="has-text-align-left" data-align="left">Unknown NADM. Default
value for RTT types that do not have a random sequence or sounding
sequence.</td>
</tr>
</tbody>
</table>

*Table 13 -- NADM values*

[![Figure
38](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1000x693.png "Figure 39 - Attack Detector System Outline"){.aligncenter
.wp-image-234470 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1000x693.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-600x416.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-2000x1386.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-300x208.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-768x532.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1536x1065.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-2048x1419.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-450x312.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-660x457.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-800x554.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1200x832.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1600x1109.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38.png)

*Figure 39 -- Attack Detector System Outline*

There exist a number of known physical layer attacks that involve a
man-in-the-middle (MITM) attacker anticipating the value of partially
received symbols from a legitimate transmitting device and relaying
full, generated versions of those symbols with the timing manipulated so
that the legitimate recipient miscalculates the round-trip time. The LE
2M 2BT PHY with its bandwidth bit-period product value of 2.0 involves
symbol pulses that have a duration that is shorter than the pulses
associated with the other PHYs and this lessens the risk of these types
of attack.

The SNR Control feature allows the Initiator and Receiver to mix a
pre-agreed amount of random noise into signals. This applies only to
CS_Sync packet transmissions made during mode-1 (RTT) and mode-3 (RTT
and PBR) steps. By injecting noise into the signal, it becomes harder
and slower for the attacker's analysis to complete and thus reduces the
likelihood of such attacks succeeding. On the other hand, the Initiator
and Reflector devices, having pre-agreed the SNR, are able to filter the
artificially added noise easily.

The Generic Access Profile (GAP) section of the Bluetooth Core
Specification defines security modes and security levels. A formal
definition of four security levels for Bluetooth® Channel Sounding is
included. It is likely that future Bluetooth profile specifications will
reference these definitions.

Controller implementers may opt to introduce further vendor-specific
security measures.

Amplitude-based attack resilience strengthens the security capabilities
of Bluetooth® Channel Sounding. By defining a precise attack model, a
robust DFT-based detection metric, and a thorough multi-stage testing
regimen, it ensures that certified devices can reliably detect
sophisticated attempts to manipulate distance measurements.

Coupled with necessary updates to the HCI and Link Layer protocols, the
Channel Sounding Amplitude-based Attack Resilience feature provides a
comprehensive framework for mitigating evolving threats. It reflects
Bluetooth's commitment to security, helping to ensure that its precision
ranging technology remains both accurate and trustworthy in the face of
new challenges.

Creating Bluetooth fine-ranging applications and products involves
harnessing the Bluetooth® Channel Sounding feature of the controller and
combining it with custom, application-layer code. Developers of the
application component of a solution must take care of various issues
which this section highlights.

The Bluetooth stack does not generate distance measurements directly.
Instead, during the execution of CS steps by the Bluetooth controller,
low-level measurements of phase and/or timing are made and it is from
this data that applications can calculate distance measurements.

The algorithm which applications use for calculating distances is not
specified by the Bluetooth Core Specification. Consequently, this is one
area in which vendors can differentiate. Superior algorithms will
produce superior results.

The Host Controller Interface Functional Specification defines two
events that are used by a controller to pass Bluetooth® Channel Sounding
data to the host. The two events are called LE CS Subevent Result and LE
CS Subevent Result Continue.

The controller aggregates the measurements generated during the steps
executed within a Bluetooth® Channel Sounding subevent. Complete or
partial sets of results are reported using a LE CS Subevent Result HCI
event. If an incomplete set is reported, the remainder of the results
are reported in one or more LE CS Subevent Result Continue events that
are sent later. The HCI event fields Subevent_Done_Status and
Procedure_Done_Status indicate to the application layer whether all data
for the subevent or procedure has been reported or whether there is more
to come.

[![Figure
39](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39.png "Figure 40 - Example Bluetooth® Channel Sounding HCI data reporting"){.aligncenter
.wp-image-234471 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39.png 924w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-600x394.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-300x197.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-768x504.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-450x295.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-660x433.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-800x525.png 800w"
sizes="auto, (max-width: 924px) 100vw, 924px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39.png)

*Figure 40 -- Example Bluetooth® Channel Sounding HCI data reporting*

The Bluetooth® Channel Sounding HCI events convey a range of types of
data from the controller to the host. A selection of key fields and data
structures are described here.

**Frequency_Compensation** --- The purpose of mode-0 steps is to
determine differences between wanted and actual frequencies generated by
the Initiator and Reflector. This is used to calculate a fractional
frequency offset (FFO) which can then be used to compensate for the
impact that such differences have both on frequency and timing values
and ultimately to improve the accuracy of distance measurements.

**Num_Steps_Reported** --- This field indicates how many steps are being
reported on in this HCI event. It also indicates the size of four step
related arrays of data: Step_Mode, Step_Channel, Step_Data_Length, and
Step_Data.

**Step_Mode \[ \]** --- This array contains the mode of each step,
ordered by step number and expressed as a value in the range 0 -- 3.

**Step_Channel \[ \]** --- This array contains the index of the RF
channel used in the execution of the corresponding step.

**Step_Data_Length \[ \]** --- The data reported for each step is
variable in terms of its content and structure. This array contains the
length of each element in the associated Step_Data array.

**Step_Data \[ \]** --- The data reported for each step depends on the
step mode, the device role (Initiator or Reflector) and whether or not a
sounding sequence is used. The structure containing the relevant data is
called the Mode_Role_Specific_Info object and eleven variants of this
structure are defined. Examples of data which may be found include
Packet_Quality, Tone_Quality, the received signal strength indicator
(RSSI), the measured frequency offset, a NADM value, the antenna
identifier, phase correction terms and elapsed time measurements between
packet transmission and arrival. Time values are expressed as a multiple
of units of half a nanosecond.

The application layer is responsible for deciding which step modes to
use and where both a primary mode and a submode are used, what the ratio
between the number of steps of each of the selected modes should be.
Application or product developers will need to consider distance
measurement accuracy requirements, security and latency in arriving at
conclusions as well as the features supported by the local controller.

The application layer can exercise some control over the security of the
overall solution in its selection of mode combinations and RTT
parameters. Developers should first seek to understand and evaluate the
security levels defined by the Generic Access Profile (GAP) as a
start-point for establishing what security options to adopt.

It is recommended that PBR and RTT are always used in combination so
that cross-checking of distance calculations based on the two methods
can be used. PBR is supported by Bluetooth® Channel Sounding to offer
the most accurate distance measurements whilst the primary reason for
also supporting RTT is as a security measure.

NADM values are created by the NADM algorithm in the Bluetooth
controller and a standardized adjective form of meanings is defined for
these values. But it is the application layer which must decide what
action to take (if any) for each of the possible NADM values.

Bluetooth® Channel Sounding is designed as an extensible framework that
continues to evolve through incremental feature enhancements across Core
Specification updates. While the core architecture and procedures
establish a common foundation, additional capabilities may be introduced
over time to address newly identified requirements, operational
considerations, or implementation refinements. This section summarizes
Bluetooth® Channel Sounding enhancements that extend specific aspects of
the version 1 features found in Core Specification v6.0. As Channel
Sounding continues to evolve, this section is intended to expand to
incorporate future enhancements.

Bluetooth Core Specification version 6.2 introduces enhanced resilience
against a class of ranging attacks that exploit amplitude manipulation
to influence distance measurements in Channel Sounding. These attacks
apply a periodic amplification pattern synchronized to the symbol timing
of Channel Sounding packets, causing predictable phase distortions in
the receiver through amplitude‑to‑phase conversion in the analog front
end. To detect such behavior, the specification extends the existing
Normalized Attack Detector Metric (NADM) framework with a Discrete
Fourier Transform (DFT)--based detection method. This approach analyzes
energy components at the symbol frequency and its harmonics, which are
characteristic of periodic amplitude manipulation, and incorporates the
resulting metric into existing NADM reporting. The enhancement
strengthens Channel Sounding's ability to detect advanced early‑commit
ranging attacks without prescribing specific receiver
implementations, maintaining flexibility while addressing newly
identified threat vectors.

Bluetooth Core Specification version 6.3 introduces support for an
inline Phase Correction Term (inline PCT) as an enhancement to the
Channel Sounding phase‑based ranging procedure. Inline PCT allows a
reflector device to apply a phase correction term within the radio
processing chain prior to retransmission, enabling phase‑aligned signal
forwarding without requiring all phase compensation to be performed
digitally at the initiator. By incorporating phase correction inline,
this mechanism can reduce control and reporting overhead associated with
phase error compensation while preserving the
fundamental two‑way Channel Sounding measurement model. Support for
inline PCT is optional and negotiated between
devices, maintaining interoperability with implementations that rely
on initiator‑side digital phase correction. To learn more, refer to
[section 3 of the Bluetooth® Core Specification v6.3 technical
rel="noreferrer noopener"}.

Bluetooth Core Specification version 6.3 enhances Channel Sounding
Round‑Trip Time (RTT) measurements by introducing PHY‑specific RTT
accuracy declarations. Prior to this enhancement, devices reported a
single RTT accuracy target that applied uniformly across all supported
PHYs, despite differing symbol rates and timing characteristics. The
updated mechanism allows devices to declare RTT accuracy requirements
independently for each PHY, including LE 1M and optional higher‑rate
PHYs such as LE 2M. This enables more accurate alignment between RTT
exchange counts and the achievable timing precision of each PHY,
improving efficiency and consistency in multi‑PHY environments. The
enhancement is supported through updated Link Layer capability exchanges
and versioned Host Controller Interface
commands, maintaining interoperability with legacy implementations. To
learn more, refer to [section 3 of the Bluetooth® Core Specification
v6.3 technical
rel="noreferrer noopener"}.

To introduce the Bluetooth® Channel Sounding feature, changes have been
made to several layers of the Bluetooth Core Specification. A summary of
key changes is presented in this section with the intention that this
provide a chapter-by-chapter high-level reference for orientation
purposes only. The Bluetooth Core Specification should be consulted for
full details.

Volume 1, Part A of the Bluetooth Core Specification describes the
architecture of the technology.

- Section 3, Transport Architecture introduces a new packet structure
and signaling format for Bluetooth® Channel Sounding. It also defines
the new LE Channel Sounding Physical Channel and LE Channel Sounding
Physical Link.
- Section 9, Bluetooth® Channel Sounding using Bluetooth Low Energy
provides a short summary of the Bluetooth® Channel Sounding feature.

Volume 3, Part C defines the Generic Access Profile.

- Section 9 introduces the GAP Bluetooth® Channel Sounding procedures
and the roles of Initiator and Reflector.
- Section 10 defines the four Bluetooth® Channel Sounding security
levels.

Volume 4, Part E contains the Host Controller Interface Functional
Specification.

- Section 7.7.6.5 LE Meta event has been updated to add a variety of new
event types relating to Bluetooth® Channel Sounding including the LE
CS Subevent Result event and the LE CS Subevent Result Continue event.
- Section 7.8 LE Controller Commands now includes additional commands
for use with Channel Sounding such as the LE CS Read Remote FAE Table
command, the LE CS Create Config command, the LE CS Security Enable
command and the LE CS Procedure Enable command.

Volume 6, Part A contains the Physical Layer Specification.

- Section 1 introduces the new LE 2M 2BT PHY.
- Section 2 introduces a new channel arrangement for Bluetooth® Channel
Sounding.
- Section 3 defines the new SNR Control feature.
- Section 3.4 adds a Stable Phase requirement for devices that support
Bluetooth® Channel Sounding.
- Section 3.5 describes requirements for frequency measurement and
generation in Bluetooth® Channel Sounding. This includes a
specification for fractional frequency offset (FFO) measurement
requirements.
- Section 5.3 is a new section which describes Antenna Switching for
Bluetooth® Channel Sounding.
- Section 6 covers phase measurement requirements and includes a
reference receiver definition, a description of phase measurement
accuracy requirements, frequency actuation error compensation
requirements, and phase measurement timing rules.
- Appendix B provides an example of a test equipment setup for
Bluetooth® Channel Sounding.

Volume 6, Part B contains the Link Layer Specification.

- Section 2.4.2 defines new link layer controller PDU types associated
with the Bluetooth® Channel Sounding feature together with their
opcodes.
- Section 4 contains updates to the link layer air interface protocol
for Bluetooth® Channel Sounding. This includes updated sleep clock
accuracy requirements in section 4.2 and a specification for
Bluetooth® Channel Sounding procedures, events, subevents, and steps
in section 4.5.18. Security requirements for an ACL link associated
with Bluetooth® Channel Sounding and the control PDUs it may transport
are provided in section 4.5.18.2.
- Section 5.1 covers the subject of link layer control. It has been
updated to include new control procedures relating to Bluetooth®
Channel Sounding, such as the Bluetooth® Channel Sounding Start
procedure, the Bluetooth® Channel Sounding Capabilities Exchange
procedure, the Bluetooth® Channel Sounding Configuration procedure,
and the Bluetooth® Channel Sounding Start procedure.

Volume 6, Part H is a new section dedicated to the new Bluetooth®
Channel Sounding feature. It covers the definition of physical RF
channels to be used with Bluetooth® Channel Sounding, the new CS_Sync
packet format, measuring RTT, and the various methods of obtaining time
of arrival or departure timestamps. The new channel selection algorithms
for Bluetooth® Channel Sounding are defined in this section along with
step modes, step combination and sequencing rules, phase measurement
rules, and random bit generation using the DRBG.

With Bluetooth® Channel Sounding, developers can create exciting
products and applications which leverage the feature's secure fine
ranging capability.

End users of Find My and digital key solutions, based on the world's
most ubiquitous low-power wireless technology, will enjoy performance
enhancements thanks to the quality of the results that can be achieved
by devices that use the Bluetooth® Channel Sounding feature. And knowing
that product developers have been provided with a comprehensive set of
security features with which to address pertinent issues will offer
peace of mind.

The technical flexibility of Bluetooth® Channel Sounding means that
developers can prioritize whichever aspect of ranging that matters the
most, be it security, accuracy, or latency. Not all applications are the
same and this has been recognized and catered for in the design of the
Bluetooth® Channel Sounding feature. Developers have been given the
freedom to decide what matters most to them and their users in the
implementation of their products.

More than five billion Bluetooth enabled devices ship each year. This
results in massive economies of scale which benefit product and
component manufacturers and, ultimately, their customers.

Bluetooth® Channel Sounding and the ability to perform secure fine
ranging presents the opportunity to enhance the convenience, safety, and
security of many Bluetooth connected devices. Presence detection,
direction finding, and now channel sounding can each be used separately
or in combination to create spatially aware products and applications
that end users and business enterprises can benefit from.

Bluetooth technology is absolutely pervasive and it's based on widely
adopted and meticulously specified technical standards. Adopting
Bluetooth® Channel Sounding is an easy, safe choice for developers
looking to add fine-ranging capabilities to their Bluetooth products.
Download the Bluetooth Core Specification for full details of this
exciting addition to the extensive set of Bluetooth technology features!

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">Item</th>
<th class="has-text-align-left" data-align="left">Location</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Bluetooth® Core
Specification v6.0</td>
<td class="has-text-align-left" data-align="left"><a
href="https://www.bluetooth.com/specifications/specs/core60-html/">https://www.bluetooth.com/specifications/specs/core60-html/</a></td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Find Me Profile</td>
<td class="has-text-align-left" data-align="left"><a
href="https://www.bluetooth.com/specifications/specs/find-me-profile-1-0/">https://www.bluetooth.com/specifications/specs/find-me-profile-1-0/</a></td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">Immediate Alert
Service</td>
<td class="has-text-align-left" data-align="left"><a
href="https://www.bluetooth.com/specifications/specs/immediate-alert-service-1-0/">https://www.bluetooth.com/specifications/specs/immediate-alert-service-1-0/</a></td>
</tr>
</tbody>
</table>

**FOOTNOTES**

*1. Generic Attribute Profile\
2. The speed varies depending on the material a signal
passes through. It is common to use the speed of light in the
theoretical calculations, however.\
3. CS modes are explained in section 3.5\
4. Gaussian Frequency Shift Keying*
