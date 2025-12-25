import pytest
import requests
from pytest_mock import MockerFixture
from app.other_funcs import get_random_number, get_data, get_status_code_from_response


def test_get_random_number_with_mock(mocker: MockerFixture):
    mocker.patch('app.other_funcs.random.randint', return_value=1)
    assert get_random_number() == 1


def test_get_data(mocker: MockerFixture):
    mocker.patch('app.other_funcs.requests.get', side_effect=requests.exceptions.ConnectionError)
    with pytest.raises(requests.exceptions.ConnectionError):
        get_data()


def test_logger(mocker: MockerFixture):
    mock_send = mocker.patch('app.other_funcs.log_message')
    mock_send('test')
    mock_send.assert_called_once_with('test')


def test_status_code_from_response(mocker: MockerFixture):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    assert get_status_code_from_response(mock_response) == 200
