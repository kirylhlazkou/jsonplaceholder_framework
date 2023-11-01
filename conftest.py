import pytest
import random
import string
from endpoints.create_post import CreatePost
from endpoints.get_post import GetPost
from endpoints.get_all_post import GetAllPosts
from endpoints.put_post import PutPost
from endpoints.patch_post import PatchPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def post_creator():
    return CreatePost()


@pytest.fixture()
def post_getter():
    return GetPost()


@pytest.fixture()
def random_string():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))


@pytest.fixture()
def random_integer():
    return random.randint(1, 100)


@pytest.fixture()
def create_post_one(post_creator, random_string, random_integer):
    title = random_string
    body = random_string
    userid = random_integer
    response = post_creator.create_post(title, body, userid)
    data = {
        'postid_from_fixture': response.json()['id'],
        'userid_from_fixture': response.json()['userId'],
        'title_from_fixture': response.json()['title'],
        'body_from_fixture': response.json()['body']
    }
    yield data


@pytest.fixture()
def get_posts():
    return GetAllPosts()


@pytest.fixture()
def post_putter():
    return PutPost()


@pytest.fixture()
def post_patcher():
    return PatchPost()


@pytest.fixture()
def post_deleter():
    return DeletePost()
