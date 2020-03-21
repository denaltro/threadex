import time
import pytest
from threadex import ThreadStateEnum, Thread


def test_thread__state_default(thread):
    assert thread.state is ThreadStateEnum.NULL


def test_thread_state_online(thread):
    thread.start()
    assert thread.state is ThreadStateEnum.ONLINE


def test_thread_state_stop(thread):
    thread.start()
    thread.stop()
    assert thread.state is ThreadStateEnum.STOPPED


def test_thread_state_error(thread_err):
    thread_err.start()
    assert thread_err.state is ThreadStateEnum.ERROR


def test_thread_state_exit(thread):
    thread.start()
    assert thread.state is ThreadStateEnum.EXIT


def test_thread_result_result(thread):
    thread.start()
    result, _ = thread.result
    assert result is 'thread_test'


def test_thread_uptime_not_started(thread):
    assert thread.uptime is None


def test_thread_uptime_started(thread):
    thread.start()
    assert thread.uptime > 0


def test_thread_uptime_stopped(thread):
    thread.start()
    thread.stop()
    assert thread.uptime > 0


def test_thread_uptime_error(thread_err):
    thread_err.start()
    assert thread_err.uptime >= 0


def test_thread_uptime_exit(thread):
    thread.start()
    assert thread.uptime > 0
