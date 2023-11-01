def test_get_post_id(create_post_one, post_getter):
    data = create_post_one
    post_getter.get_post(data)
    post_getter.check_response_status_is_200()
    post_getter.check_postid_from_fixture_equal_response_postid(data['postid_from_fixture'])
    post_getter.check_userid_from_fixture_equal_response_userid(data['userid_from_fixture'])
    post_getter.check_title_from_fixture_equal_response_title(data['title_from_fixture'])
    post_getter.check_body_from_fixture_equal_response_body(data['body_from_fixture'])
   