def test_get_posts(get_posts):
    get_posts.get_all_posts()
    get_posts.check_response_status_200()
    get_posts.check_number_of_posts()
