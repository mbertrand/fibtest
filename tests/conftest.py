import pytest

def pytest_addoption(parser):
    """
    Add commandline option to specify the URL to test
    """
    parser.addoption("--url",
        action="store",
        default="http://52.196.171.190",
        help="REST URL to test")

@pytest.fixture
def url(request):
    """
    Get the commandline option value for url
    """
    return request.config.getoption("--url")
