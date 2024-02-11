from base_request import BaseRequest
import pytest


class PetStoreApiUser(BaseRequest):
    @pytest.mark.parametrize('https://dog.ceo/dog-api',
                             'https://www.openbrewerydb.org/', 'https://jsonplaceholder.typicode.com/')
    def __init__(self, base_url):
        super().__init__(base_url)

    def create_data(self, expected_error=False):
        return self.post('data', '', '', is_json=True, expected_error=expected_error)

    def get_data(self):
        return self.get('data', '')

    def update_page(self, expected_error=False):
        return self.put('data', '', '', is_json=True, expected_error=expected_error)

    def update_data(self, expected_error=False):
        return self.patch('data', '', '', is_json=True, expected_error=expected_error)

    def delete_data(self, expected_error=False):
        return self.delete('data', '')
