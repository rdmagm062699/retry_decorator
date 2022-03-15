from ast import Call
from time import sleep
import pytest
from src.deco import retry_exception
from unittest.mock import Mock, patch, call


@patch('src.deco.sleep', autospec=True, spec_set=True)
def test_retry_exception_retries_designated_number_of_times(sleep_mock):
    mock_function = Mock()
    mock_function.side_effect = Exception('BlahBlahBlah')
    sleep_mock.side_effect = None

    @retry_exception(max_retries=3)
    def some_function():
        mock_function()

    with pytest.raises(Exception):
        some_function()
    assert mock_function.call_count == 4


@patch('src.deco.sleep', autospec=True, spec_set=True)
def test_retry_exception_implements_exponential_backoff(sleep_mock):
    mock_function = Mock()
    mock_function.side_effect = Exception('BlahBlahBlah')
    sleep_mock.side_effect = None

    @retry_exception(max_retries=5, backoff=2)
    def some_function():
        mock_function()

    with pytest.raises(Exception):
        some_function()

    expected_calls = [
        call(1), call(2), call(4), call(8), call(16)
    ]

    assert sleep_mock.call_count == 5
    sleep_mock.assert_has_calls(expected_calls)


@patch('src.deco.sleep', autospec=True, spec_set=True)
def test_retry_exception_never_sleeps_any_seconds_if_backoff_is_zero(sleep_mock):
    mock_function = Mock()
    mock_function.side_effect = Exception('BlahBlahBlah')
    sleep_mock.side_effect = None

    @retry_exception(max_retries=5, backoff=0)
    def some_function():
        mock_function()

    with pytest.raises(Exception):
        some_function()

    expected_calls = [
        call(0), call(0), call(0), call(0), call(0)
    ]

    assert sleep_mock.call_count == 5
    sleep_mock.assert_has_calls(expected_calls)
