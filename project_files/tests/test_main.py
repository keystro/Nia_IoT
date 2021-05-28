import json

def test_main(app, client):
    res = client.get('/main')
    assert res.status_code == 200
    expected = {'Hello': 'World'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = "Hello, Welcome to Solaris Off The Grid Systems!"
    assert expected == res.get_data(as_text = True)

def test_home(app, client):
    res = client.get('/home')
    assert res.status_code == 200
    expected = "IoT Data Page"
    assert expected == res.get_data(as_text=True)


def test_appget(app, client):
    res = client.get('/appget')
    assert res.status_code == 200
    expected = "HTTP Respose Code 200: Data None"
    assert expected == res.get_data(as_text=True)
