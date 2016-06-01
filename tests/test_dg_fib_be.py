import requests

"""
Back-end tests for the Fibonacci web app
"""

base_api_url = "{}:5000/api/fibonacci/{}"


def test_valid_numbers(url):
    """
    Make sure expected values are returned for certain numbers
    """
    fibs = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        10: 55,
        55: 139583862445
    }
    for num in fibs:
        r = requests.get(base_api_url.format(url, num), timeout=30)
        output = r.json()
        assert 'fibonacci' in output
        assert output['fibonacci'] == fibs[num]


def test_leading_zeros(url):
    """
    Make sure expected values are returned for numbers with leading zeros
    """
    fibs = {
        '04': 3,
        '0010': 55
    }
    for num in fibs:
        r = requests.get(base_api_url.format(url, num), timeout=30)
        output = r.json()
        assert 'fibonacci' in output
        assert output['fibonacci'] == fibs[num]


def test_float(url):
    """
    An invalid float input value should be handled gracefully by the API
    """
    r = requests.get(base_api_url.format(url, 4.4), timeout=30)
    assert r.status_code == 404
    output = r.json()
    assert 'error' in output, "REST API did not respond with an error message"
    assert output['error'] == 'resource not found'


def test_negative_number(url):
    """
    An invalid negative number should be handled gracefully by the API
    """
    r = requests.get(base_api_url.format(url, -1), timeout=30)
    assert r.status_code == 404
    output = r.json()
    assert 'error' in r.json(), "REST API did not respond with an error message"
    assert output['error'] == 'resource not found'


def test_nonnumeric(url):
    """
    An nonnumeric input should be handled gracefully by the API
    """
    r = requests.get(base_api_url.format(url, 'Hello world'), timeout=30)
    assert r.status_code == 404
    output = r.json()
    assert 'error' in output, "REST API did not respond with an error message"
    assert output['error'] == 'resource not found'


def test_alphanumeric(url):
    """
    An invalid input of mixed numbers & letters should be handled gracefully by the API
    """
    bad_inputs = ('1e2', '5 * 3', '123abd')
    for input in bad_inputs:
        r = requests.get(base_api_url.format(url, input), timeout=30)
        assert r.status_code == 404
        output = r.json()
        assert 'error' in output, "REST API did not respond with an error message"
        assert output['error'] == 'resource not found'


def test_invalid_methods(url):
    """
    Only GET requests should be allowed.
    """
    bad_methods = {
        'POST': requests.post,
        'PUT': requests.put,
        'DELETE': requests.delete
    }
    for method in bad_methods:
        r = bad_methods[method](url)
        assert r.status_code == 405, "Invalid request method {} was allowed".format(method)

