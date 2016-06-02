## Unit Tests for a Fibonacci Service

**Overview**

This repo contains unit tests for a Fibonacci web service located at http://52.196.171.190/.
Pytest was chosen as the unit testing framework.  

The tests attempt to verify the following:

   * The correct fibonacci number is returned for valid integer values by the REST API, in a JSON formatted response.
   * An appropriate error response and status is returned by the REST API for invalid input values (negative numbers, non-integers, etc).
   * Only GET requests are allowed by the REST API.
   * The front end web page displays expected text and UI elements.
   * The correct fibonacci number is displayed on the front-end web page after submission of a valid input value.
   * A meaningful error message is displayed on the front-end web page after submission of an invalid input value.

The structure of the repo is as follows:

* tests/
    * conftest.py: Configuration/utility methods for tests
    * test_dg_fib_be.py: Back-end unit tests
    * test_dg_fib_fe.py: Front-end unit tests

* reports/
    * test_results.xml: Test results in JUnit XML format
    * test_results.html: Test results in HTML format.
    * bug_report.md: Summary of bug(s) found.

* requirements.txt: Prerequisite modules/libraries

* runtests.sh: Sample bash script to run tests and generate reports.


**Usage**

The simplest way to run these tests is with the provided bash script:

```
bash ./runtests.sh
```

There is an option to specify a different base URL than the default:

```
python -m pytest --url=<your_url> tests
```

**Assumptions**

These unit tests are based on the following assumptions:

   * The backend and frontend docker containers running the service are on the same EC2 instance
   * Only GET requests should be allowed by the backend server (not POST, PUT, or DELETE).
   * Valid inputs include numbers with leading zero's ('010', '005') but not equations ('2*3') or scientific notation ('1e2')
   * The frontend web page should display an error if invalid input is entered.


**Installation**

Assuming you have pip installed:

```
pip install -r requirements.txt
```

