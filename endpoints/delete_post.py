import requests


class DeletePost:
    status = None
    title = None
    body = None
    userid = None
    postid = None

    def delete_post(self, data):
        postid_from_fixture = data['postid_from_fixture']
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{postid_from_fixture}')
        self.status = response.status_code
        return response.json()

    def check_response_status_is_200(self):
        assert self.status == 200
