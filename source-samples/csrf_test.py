def test_csrf():
    ...
    # zapnutí ochrany proti CSRF
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['WTF_CSRF_CHECK_DEFAULT'] = True

    # zaslání požadavku na přihlášení bez platného tokenu
    response = app.test_client().post('/login', data={
        # na zaslaném hesle nezáleží
        # žádost bude odmítnuta na základě neplatného tokenu
        'password' : 'test password',
        'csrf_token' : 'some fake token'
        })

    assert response.status == '400 BAD REQUEST'
    # odpověď by měla zmiňovat CSRF
    assert 'CSRF' in response.data.decode('utf-8')