import requests


class GetAllPosts:
    len_response = None
    status = None

    def get_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.status = response.status_code
        self.len_response = len(response.json())
        return response

    def check_number_of_posts(self):
        assert self.len_response == 100

    def check_response_status_200(self):
        assert self.status == 200
