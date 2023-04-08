def test_user_model(user, database):
    test_username = "newstd"
    test_email = "newstd@abc.com"

    test_user = user(username=test_username, email=test_email)
    database.session.add(test_user)
    database.session.commit()

    assert test_user == user.get_by_email(test_email)