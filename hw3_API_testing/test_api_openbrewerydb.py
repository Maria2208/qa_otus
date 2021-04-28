import pytest
import requests
import cerberus


@pytest.fixture(scope="session")
def base_url():
    url = "https://api.openbrewerydb.org"
    return url


@pytest.mark.parametrize('url_data', ['Dog', 'Barrel', 'Brewery'])
def test_api_autocomplete(base_url, url_data):
    """Проверка ответа в методе GET /autocomplete"""
    res = requests.get(
        base_url + "/breweries/autocomplete",
        params={'query': url_data}
    )
    res_json = res.json()
    assert res.status_code == 200
    for val in range(len(res_json)):
        assert 'id' in res_json[val]
        assert 'name' in res_json[val]
        assert url_data in res_json[val]["name"]


@pytest.mark.parametrize('url_data', ['Doggggg', '1231231123', 'dOOOOg'])
def test_api_empty_responce(base_url, url_data):
    """Проверка ответа в методе GET /autocomplete при передаче не существующего названия пивоварни"""
    res = requests.get(
        base_url + "/breweries/autocomplete",
        params={'query': url_data}
    )
    res_json = res.json()
    assert res.status_code == 200
    assert res_json == []


@pytest.mark.parametrize('url_data', ['Dog', 'Barrel', 'Brewery'])
def test_api_json_schema(base_url, url_data):
    """Проверка структуры ответа"""
    res = requests.get(base_url + "/breweries/search", params={'query': url_data}).json()

    schema = {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {"type": "string"},
        "address_3": {"type": "string"},
        "city": {"type": "string"},
        "county_province": {"type": "string"},
        "state": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }
    for val in range(len(res)):
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)


@pytest.mark.parametrize('url_data', ['Jackson', 'Austin', 'Dubuque'])
def test_api_get_breweries_by_state(base_url, url_data):
    """Проверка ответа в методе GET /breweries с параметром by_city"""
    res = requests.get(
        base_url + "/breweries",
        params={'by_city': url_data}
    )
    res_json = res.json()
    assert res.status_code == 200
    for val in range(len(res_json)):
        assert 'city' in res_json[val]
        assert url_data in res_json[val]["city"]


@pytest.mark.parametrize('breweries_id, id_in_response', [(8865, 8865), (8662, 8662), (9170, 9170)])
def test_api_filtering(base_url, breweries_id, id_in_response):
    """Проверка ответа в методе GET /breweries/{id}"""
    response = requests.get(f'{base_url}/breweries/{breweries_id}')
    res_json = response.json()
    assert response.status_code == 200
    assert 'id' in res_json
    assert res_json['id'] == id_in_response
