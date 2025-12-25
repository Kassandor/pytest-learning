import pytest
import requests
from pytest_mock import MockerFixture

from app.user_processor import get_user_full_name


def test_get_user_full_name_success(mocker: MockerFixture):
    mock_response = mocker.Mock()
    # Затираем метод raise_for_status
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        'data': {
            'id': 2,
            'email': 'janet.weaver@reqres.in',
            'first_name': 'Janet',
            'last_name': 'Weaver',
        }
    }
    mocker.patch('app.user_processor.requests.get', return_value=mock_response)
    full_name = get_user_full_name(2)
    assert full_name == 'Janet Weaver'


def test_get_user_full_name_api_error(mocker: MockerFixture):
    mocker.patch('app.user_processor.requests.get', side_effect=requests.exceptions.RequestException)
    with pytest.raises(requests.exceptions.RequestException):
        get_user_full_name(221)


def test_get_user_name_integration_style(mocker: MockerFixture):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        'data': {
            'id': 2,
            'first_name': 'Guido',
            'last_name': 'van Rossum',
        }
    }
    mocker.patch('app.user_processor.requests.get', return_value=mock_response)
    assert get_user_full_name(2) == 'Guido van Rossum'
