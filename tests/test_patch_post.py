def test_patch_post(create_post_one, post_patcher):
    data = create_post_one
    post_patcher.put_post(data)
    post_patcher.check_response_status_is_200()
    post_patcher.check_postid_from_fixture_equal_response_postid(data['postid_from_fixture'])
    post_patcher.check_sent_title_equal_response_title()
    post_patcher.check_sent_body_equal_response_body()
    post_patcher.check_sent_userid_not_equal_response_userid()
