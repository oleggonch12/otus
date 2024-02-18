import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", help="url"
    )

    parser.addoption(
        "--status_code", default=200, type=int, help="status_code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


def status_code(request):
    return request.config.getoption("--status_code")
