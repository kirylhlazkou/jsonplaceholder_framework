import requests


class GetPost:
    status = None
    title = None
    body = None
    userid = None
    postid = None

    def get_post(self, data):
        postid_from_fixture = data['postid_from_fixture']
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{postid_from_fixture}')
        self.status = response.status_code
        self.userid = response.json()['userId']
        self.postid = response.json()['id']
        self.title = response.json()['title']
        self.body = response.json()['body']
        return response.json()

    def check_response_status_is_200(self):
        assert self.status == 200

    def check_userid_from_fixture_equal_response_userid(self, userid_from_fixture):
        # userid_from_fixture = create_post_one
        assert userid_from_fixture == self.userid

    def check_postid_from_fixture_equal_response_postid(self, postid_from_fixture):
        assert postid_from_fixture == self.postid

    def check_title_from_fixture_equal_response_title(self, title_from_fixture):
        assert title_from_fixture == self.title

    def check_body_from_fixture_equal_response_body(self, body_from_fixture):
        assert body_from_fixture == self.body
