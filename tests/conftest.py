import pytest

from src.ApiClient import ApiClient
from src.KafkaClient import KafkaClient
from src.ConfigParser import ConfigParser
from src.CommonFunctions import CommonFunctions
from src.DbConnector import DbConnector


def pytest_addoption(parser):
    parser.addoption("--conf_file", action="store", default="config.cfg", help="Provide Config File Name")
    parser.addoption("--op_path", action="store", default="", help="Provide Output Dir Path")


@pytest.fixture
def conf_file(request):
    return request.config.getoption("--conf_file")


@pytest.fixture
def op_path(request):
    return request.config.getoption("--op_path")


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    # pref=""
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture
def api_client(conf_file):
    return ApiClient(conf_file)


@pytest.fixture
def kafka_client(conf_file):
    return KafkaClient(conf_file)


@pytest.fixture
def kafka_topics(conf_file):
    return ConfigParser(conf_file).get_all_options('KAFKA.TOPIC')


@pytest.fixture
def dbo(conf_file):
    return DbConnector(conf_file)


@pytest.fixture
def common_functions(conf_file, dbo):
    return CommonFunctions(dbo, conf_file)
