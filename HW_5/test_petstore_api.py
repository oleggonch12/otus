import pytest
from petstore_api import PetStoreApiUser


@pytest.fixture(scope='function')
def pet_store_api_user():
    return PetStoreApiUser()


def test_create(pet_store_api_user):
    user_id = pet_store_api_user.create_data('data')
    expected_body = {
             'id': user_id,
         }
    user_info = pet_store_api_user.get('user', 'username')
    for key, value in expected_body.items():
        print(user_info[key])
        print(value)
        assert user_info[key] == value, (
            f'[{key}] Actual value: {user_info[key]}, expected: {value}'
        )


def test_get(pet_store_api_user):
    pass


def test_put(pet_store_api_user):
    user_id = pet_store_api_user.update_page('data')
    expected_body = {
        'id': user_id,
    }
    user_info = pet_store_api_user.get('user', 'username')
    for key, value in expected_body.items():
        print(user_info[key])
        print(value)
        assert user_info[key] == value, (
            f'[{key}] Actual value: {user_info[key]}, expected: {value}'
        )


def test_patch(pet_store_api_user):
    user_id = pet_store_api_user.update_data('data')
    expected_body = {
        'id': user_id,
    }
    user_info = pet_store_api_user.get('user', 'username')
    for key, value in expected_body.items():
        print(user_info[key])
        print(value)
        assert user_info[key] == value, (
            f'[{key}] Actual value: {user_info[key]}, expected: {value}'
        )


def test_delete(pet_store_api_user):
    user_id = pet_store_api_user.delete_data('data')
    user_info = pet_store_api_user.get('user', 'username')
    assert user_info.status_code == '404'
