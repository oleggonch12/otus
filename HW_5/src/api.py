from .base_request import BaseRequest


class Api(BaseRequest):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_data(self, endpoint, endpoint_id):
        return self.get(endpoint, endpoint_id)