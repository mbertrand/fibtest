## Fibonacci Web Service Bug Report

The Web Service overall performed as expected:

    * Correct Fibonacci numbers were returned by the backend for valid integer inputs, and displayed on the front end.
    * The backend returned 404 status codes and errors in JSON format for invalid inputs
    * The backend returned 405 status codes when requests were made with unsupported methods (POST, PUT, etc).

However, 1 front-end test failed:
    * test_submit_invalid_number

The cause of the failure was the lack of feedback on submission of an invalid input.  Although the backend responded
with an appropriate error message, no error message was displayed on the front end.

There was also one test which was deliberately omitted: calculating the Fibonacci number for a very large integer.
Manual testing indicated that submitting a value like 9999999999999999 would cause the backend to hang and stop
responding, even on an m3.medium EC2 instance.  There should probably be some validation in the app to prevent
large numbers above a certain value from being processed.