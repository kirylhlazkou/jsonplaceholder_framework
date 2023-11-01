def test_delete_post(create_post_one, post_deleter):
    data = create_post_one
    post_deleter.delete_post(data)
    post_deleter.check_response_status_is_200()
