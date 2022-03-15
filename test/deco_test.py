from src.deco import retry_exception
from unittest.mock import Mock


def test_retry_exception_retries_designated_number_of_times():
    mock_function = Mock()
    mock_function.side_effect = Exception('BlahBlahBlah')

    @retry_exception(max_retries=3)
    def some_function():
        mock_function()

    some_function()
    assert mock_function.call_count == 4