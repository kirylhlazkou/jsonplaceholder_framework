def test_put_post(create_post_one, post_putter):
    data = create_post_one
    post_putter.put_post(data)
    post_putter.check_response_status_is_200()
    post_putter.check_postid_from_fixture_equal_response_postid(data['postid_from_fixture'])
    post_putter.check_sent_title_equal_response_title()
    post_putter.check_sent_body_equal_response_body()
    post_putter.check_sent_userid_equal_response_userid()
