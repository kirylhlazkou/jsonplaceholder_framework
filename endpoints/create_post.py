import requests


class CreatePost:
    status = None
    sent_title = None
    title = None
    sent_body = None
    body = None
    sent_userid = None
    userid = None
    postid = None

    def create_post(self, title, body, userid):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
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

    def check_response_status_201(self):
        assert self.status == 201

    def check_sent_title_equal_response_title(self):
        assert self.sent_title == self.title

    def check_sent_body_equal_response_body(self):
        assert self.sent_body == self.body

    def check_sent_userid_equal_response_userid(self):
        assert self.sent_userid == self.userid

    def check_postid_is_a_positive_integer(self):
        assert isinstance(self.postid, int) and self.postid > 0
