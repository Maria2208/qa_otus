import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://ya.ru/",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        action="store",
        default='200',
        choices=['200', '201', '404', '301'],
        help="This is status_code"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
