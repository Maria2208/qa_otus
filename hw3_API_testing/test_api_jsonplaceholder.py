import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    url = "https://jsonplaceholder.typicode.com"
    return url


@pytest.mark.parametrize('post_id', [1, 2, 3])
@pytest.mark.parametrize('user_id', [100, 1, 10])
def test_api_put_request(base_url, user_id, post_id):
    """Проверка, что изменения происходят по соответствующему пользователю и записи"""
    res = requests.put(f'{base_url}/posts/{post_id}',
                       data={'title': 'input_title', 'body': 'bar', 'userId': user_id})
    res_json = res.json()
    assert res.status_code == 200
    assert 'id' in res_json
    assert 'userId' in res_json
    assert res_json['id'] == post_id
    assert res_json['userId'] == str(user_id)


@pytest.mark.parametrize('post_id', [1, 2, 3])
def test_api_delete_post(base_url, post_id):
    """Проверка, что при удалении записи возвращается статус 200 и пустой словарь"""
    res = requests.delete(f'{base_url}/posts/{post_id}')
    res_json = res.json()
    assert res_json == {}
    assert res.status_code == 200


@pytest.mark.parametrize('post_id', [1, 2, 3])
def test_api_get_comments(base_url, post_id):
    """Проверка, что возвращаютс комментарии по соответствующему id"""
    res = requests.get(f'{base_url}/posts/{post_id}/comments')
    res_json = res.json()
    assert res.status_code == 200
    for val in range(len(res_json)):
        assert 'postId' in res_json[val]
        assert post_id == res_json[val]["postId"]


@pytest.mark.parametrize('post_id, title', [(1, 'title'), (2, ''), (3, 'dsdf')])
def test_api_patch_request(base_url, title, post_id):
    """Проверка, что изменяется заглавие по соответствующему id"""
    res = requests.patch(f'{base_url}/posts/{post_id}',
                         data={'title': title})
    res_json = res.json()
    assert res.status_code == 200
    assert 'id' in res_json
    assert 'title' in res_json
    assert res_json['id'] == post_id
    assert res_json['title'] == title


@pytest.mark.parametrize('post_id', [100000, 'kjsdhfkjsdhfk', '&^%^&!@'])
def test_api_response_404(base_url, post_id):
    """Проверка, что возвращается статус 404, если запись не найдена"""
    res = requests.get(f'{base_url}/posts/{post_id}')
    res_json = res.json()
    assert res.status_code == 404
    assert res_json == {}
