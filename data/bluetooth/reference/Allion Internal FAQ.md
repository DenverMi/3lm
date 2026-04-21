# Bluetooth Qualification – Frequently Asked Questions (FAQ)

This document consolidates the most common and important client questions around Bluetooth® qualification. It is intended for internal project use, client education, and consistent explanations.

---

## Core Concept Questions

### 1. What is a QDID, and what does it represent?
A QDID (Qualified Design ID) identifies a Bluetooth design that has already been tested and approved by the Bluetooth SIG.

A QDID may represent:
- A Bluetooth module or chip (controller hardware)
- A Bluetooth software stack (host software)
- A profile or subsystem

Reusing an existing QDID allows a product to reuse prior test results, reducing cost and schedule.

---

### 2. How can one product use multiple QDIDs?
Bluetooth products are modular by design.

For example:
- One QDID can represent the Bluetooth hardware (module or chip)
- Another QDID can represent the Bluetooth software stack

These are combined during qualification into a single Bluetooth system. This is a normal and supported process.

---

### 3. What is the difference between a Bluetooth Controller, Host Stack, and Profile?

- **Controller**: Hardware handling radio, PHY, and low-level Bluetooth functions
- **Host Stack**: Software managing connections, protocols, and data channels
- **Profiles**: Application-level features such as HFP, A2DP, HID

A product combines these layers into one Bluetooth system.

---

### 4. If we reuse a qualified Bluetooth module, why is testing still required?
Because the module qualification covers only hardware and low-level functionality.

If your product adds or changes:
- Profiles
- Firmware behavior
- Host software

Only those new or changed layers must be tested. Previously qualified layers are not retested.

---

### 5. Why does the Test Plan include profile tests but no RF or PHY tests?
This usually means:
- A fully qualified controller is reused
- No RF-impacting changes were made
- Only profile functionality is new

In this case, RF and PHY testing are not required. This is normal.

---

### 6. What does “Option 2a” mean in practice?
Option 2a means creating a new Bluetooth design by combining existing qualified designs without modification.

Under Option 2a:
- Existing designs are reused as-is
- Only newly added layers are tested
- Cost and schedule are minimized

This is one of the most common qualification paths.

---

### 7. How does the Bluetooth SIG decide what must be tested?
Testing requirements are determined by:
- ICS (Implementation Conformance Statement)
- Consistency Check results
- TCRL (Test Case Reference List)
- The automatically generated Test Plan

Only items appearing in the Test Plan are required.

---

### 8. Why do some protocols appear in explanations but not in the Test Plan?
Some protocols exist in the Bluetooth architecture but are not required unless explicitly selected in the ICS.

If a protocol:
- Does not appear in the ICS
- Does not appear in the Test Plan

Then it is not required.

---

### 9. If our product does not support Bluetooth LE, why is LE mentioned?
Some layers are shared internally between BR/EDR and LE.

However:
- LE is only considered supported if LE-specific layers are selected
- If the Test Plan shows no LE tests, no LE qualification is required

---

### 10. Which document should we trust if explanations conflict?
Trust the following, in this order:
1. ICS Consistency Check result
2. SIG-generated Test Plan
3. QPRD (Qualification Program Reference Document)

These override architecture diagrams, legacy assumptions, and informal explanations.

---

## Qualification Necessity & Scope

### 11. Do we need to qualify if we do not use the Bluetooth logo?
Yes. Qualification is required whenever Bluetooth technology is implemented, regardless of logo usage.

---

### 12. If we use a pre-qualified module, do we still need SIG registration?
Yes. Your product must still be Declared and Listed unless already covered by an existing End Product listing.

---

### 13. Does using a commercial Bluetooth dongle require qualification?
It depends.
- External accessory only: may not require qualification
- Integrated or system-controlled Bluetooth: qualification required

---

### 14. What triggers testing requirements?
Testing is required when functionality differs from referenced designs, such as:
- Firmware changes
- Profile additions
- RF or antenna changes

---

### 15. Can we fully reuse an existing QDID?
Only if hardware, firmware, stack, and supported features are unchanged.

---

## Cost & Schedule

### 16. How much does Bluetooth qualification typically cost?
Costs depend on testing scope, supported profiles, and consulting needs. Estimates are provided after design review.

---

### 17. What parts of the cost are testing vs consulting?
- **Testing**: RF-PHY and profile conformance (BQTF work)
- **Consulting**: design review, ICS/IXIT preparation, Declaration support

---

### 18. How long does the qualification process take?
- Declaration-only: ~1–2 weeks
- With testing: typically 2–4 weeks after readiness

---

### 19. Are Bluetooth SIG fees included?
No. SIG fees are paid directly to the Bluetooth SIG and are separate from testing or consulting fees.

---

### 20. Can derivative models be added later?
Yes. Derivative products using the same Bluetooth design can be added without additional cost.

---

## Technical & Testing

### 21. Which profiles require mandatory testing?
Profiles such as HFP, A2DP, AVRCP, HID, and DIS typically require testing unless fully covered by referenced QDIDs.

---

### 22. Is RF-PHY testing always required?
No. RF-PHY testing is not required if a qualified Controller Subsystem is reused without RF-impacting changes.

---

### 23. What is the difference between DTM and LE Reset testing?
- **DTM**: direct RF control mode
- **LE Reset**: host-controlled RF testing

The required method depends on chipset and TCRL rules.

---

### 24. What test evidence is required?
Evidence requirements depend on:
- TCRL version
- ICS selections
- Design type (Controller, Host, Profile, End Product)

---

## Documentation & Process

### 25. What is ICS?
ICS declares which Bluetooth features a product supports and determines required testing.

---

### 26. What is IXIT?
IXIT provides test-specific parameters needed to execute tests.

---

### 27. Can regulatory RF reports be reused for qualification?
No. FCC/CE reports cannot replace Bluetooth qualification evidence.

---

### 28. What is a Compliance Folder?
A mandatory archive containing qualification evidence that must be retained after product shipment ends.

---

## SIG System & Administration

### 29. Who must log into the SIG system?
The Listing Owner’s SIG account holder must log in to pay fees, submit Declarations, and manage listings.

---

### 30. What if our SIG account email is no longer accessible?
A new SIG account must be created or ownership transferred before proceeding.

---

## Key Takeaway
Bluetooth qualification is **tool-driven, not guess-driven**. If the SIG-generated Test Plan requires it, it must be done. If it does not, it will not be required later.

