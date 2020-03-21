import time
import pytest
from threadex import Thread


def func():
    return 'thread_test'


def func_err():
    return 1/0


@pytest.fixture
def thread():
    t = Thread(target=func)
    yield t


@pytest.fixture
def thread_err():
    t = Thread(target=func_err)
    yield t
