from pytest_mock import MockerFixture

from app.file_checker import check_if_file_exists


def test_file_exists(mocker: MockerFixture):
    mocker.patch('os.path.exists', return_value=True)
    result = check_if_file_exists('/fake/path')
    assert result == 'Файл /fake/path существует'


def test_file_not_exists(mocker: MockerFixture):
    mocker.patch('os.path.exists', return_value=False)
    result = check_if_file_exists('/fake/path')
    assert result == 'Файл /fake/path не найден'
