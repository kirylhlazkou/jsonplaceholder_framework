def test_new_post_id(post_creator, random_string, random_integer):
    title = random_string
    body = random_string
    userid = random_integer
    post_creator.create_post(title, body, userid)
    post_creator.check_response_status_201()
    post_creator.check_sent_title_equal_response_title()
    post_creator.check_sent_body_equal_response_body()
    post_creator.check_sent_userid_equal_response_userid()
    post_creator.check_postid_is_a_positive_integer()
