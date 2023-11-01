import requests


class PatchPost:
    status = None
    sent_title = None
    title = None
    sent_body = None
    body = None
    sent_userid = None
    userid = None
    postid = None

    def patch_post(self, data, title, body, userid):
        postid_from_fixture = data['postid_from_fixture']
        response = requests.post(
            f'https://jsonplaceholder.typicode.com/posts/{postid_from_fixture}',
            json = {"title": title, "body": body, "userId": userid},
            headers = {'Content-Type': 'application/json'}
        )
        self.sent_title = title
        self.sent_body = body
        self.sent_userid = userid
        self.status = response.status_code
        self.title = response.json()['title']
        self.body = response.json()['body']
        self.userid = response.json()['userId']
        self.postid = response.json()['id']
        return response

    def check_response_status_is_200(self):
        assert self.status == 200

    def check_sent_title_equal_response_title(self):
        assert self.sent_title == self.title

    def check_sent_body_equal_response_body(self):
        assert self.sent_body == self.body

    def check_sent_userid_equal_response_userid(self):
        assert self.sent_userid == self.userid

    def check_postid_from_fixture_not_equal_response_postid(self, postid_from_fixture):
        assert postid_from_fixture != self.postid