### Self Pre-Test

Before submitting a product for formal certification testing, doing a self pre-test is
important to identify and fix certification-blocking bugs.

During formal certification, tests are run through the test harness, which
provides logs and certification materials for submission to the certification
program. In the self pre-test phase, tests can either be run through the test
harness or locally on a desktop for faster test iteration.

## Test Selection and PICS

The set of tests required to certify a device is determined from the
Protocol Implementation Conformance Statement (PICS). This conformance statement
is filled out by the manufacturer using the PICS tool
and the set of templates for a specific release of the specification:

Detailed information about PICS, how to fill them out, and the tools available is
available in the PICS guide.

## Running Tests

When tests are run for certification, they are run through the test harness, which is
used to assist ATLs with test selection and the collection of logs required for submissions
to the certification program. The test harness runs on a Raspberry Pi, external to the
development computer. This is the official tool for test submission for certification.

When iterating on software development, it is often easier to run tests locally. It
is common for manufacturers to run tests locally until they are certain the tests are
passing, then move on to use the official tool.

The certification program uses a combination of different types of testing for
certification. Tests can be automated in YAML or Python.

Tests that are automated in YAML are located in the
YAML SDK folder.

Tests that are implemented in Python are located in the
Python SDK folder.

Some tests are not automated for various reasons, and consist of a set of manual
steps that the tester needs to perform and check. These tests are run from the
verification steps document, which can be found in the official
for each specification revision.

## Running Tests Locally

Information about running tests locally can be found in the SDK documentation:
- YAML
- Python

## Running Tests on the Test Harness

A full description of how to build the test harness and run tests is available in the
test harness user guide. Each specification release contains a version of the test harness
user guide specific to that release. The user guide for each release

## Fixing Bugs

Documentation around common problems when running tests can be found in the
`matter-test-scripts` repository.

The Matter test harness tiger team has a dedicated Slack channel for test harness questions at (#csg-matter-test-harness-help).

Questions about tests for specific clusters can also be directed to the supporting Tiger Team.

In the case where a test case bug is identified, the affected manufacturer should file a request with
the Change Control Board (CCB). Information about the CCB process can be found in the

CCB requests are filed in the CCB tool.
