import pytest
import requests
import cerberus


@pytest.fixture(scope="session")
def base_url():
    url = "https://dog.ceo/api"
    return url


def test_api_json_schema(base_url):
    """Проверка структуры ответа за запрос /breeds/image/random"""
    res = requests.get(base_url + "/breeds/image/random")

    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"},
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


@pytest.mark.parametrize('url_data', ['hound', 'akita', 'basenji'])
def test_api_random_image_200(base_url, url_data):
    """Проверка ответа в методе GET /images"""
    url = f'{base_url}/breed/{url_data}/images'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200
    assert 'message' in res_json
    assert 'status' in res_json


@pytest.mark.parametrize('url_data', ['123', 'akitaaaa'])
def test_api_random_image_404(base_url, url_data):
    """Проверка, что в ответе возвращается статус 404, если в запросе переданы не существующие породы"""
    url = f'{base_url}/breed/{url_data}/images'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 404
    assert 'error' in res_json['status']
    assert 'Breed not found (master breed does not exist)' in res_json['message']


@pytest.mark.parametrize('url_data',
                         ['hound', 'australian', 'buhund'])
def test_api_success_status(base_url, url_data):
    """Проверка респонса в методе GET /list"""
    url = f'{base_url}/breed/{url_data}/list'
    res = (requests.get(url=url))
    res_json = res.json()
    assert res.status_code == 200
    assert 'message' in res_json
    assert 'status' in res_json
    assert len(res_json['message']) >= 1


@pytest.mark.parametrize('url_data', ['hound', 'akita', 'basenji'])
def test_api_image_in_response(base_url, url_data):
    """Проверка, что в ответе возвращаются файлы формата .jpg/.jpeg"""
    url = f'{base_url}/breed/{url_data}/images'
    res = (requests.get(url=url)).json()
    for val in res['message']:
        assert ".jpg" or ".jpeg" in val
