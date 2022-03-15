from unittest.mock import patch
import pytest

@patch.dict('os.environ', {'MAX_RETRIES': '4','BACKOFF': '0'})
@patch('requests.post', autospec=True, spec_set=True)
def test_retries_specified_number_of_times(post_mock):
    post_mock.side_effect = Exception('Bad things man')

    from src.retry_example import run_it
    with pytest.raises(Exception):
        run_it()

    assert post_mock.call_count == 5