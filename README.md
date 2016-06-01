## Unit Tests for a Fibonacci Service

**Overview**

This repo contains unit tests for a Fibonacci web service located at http://52.196.171.190/.
Pytest was chosen as the unit testing framework.  The structure of the repo is as follows:

* tests/
    * conftest.py: Configuration/utility methods for tests
    * test_dg_fib_be.py: Back-end unit tests
    * test_dg_fib_fe.py: Back-end unit tests

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
   * The frontend web page should display an error if invalid input is entered.
   * Only GET requests should be allowed by the backend server (not POST, PUT, or DELETE).


**Installation**

Assuming you have pip installed:

```
pip install -r requirements.txt
```

