import requests
import json

url = 'https://mubu.com/login/password'

s = requests.session()


def mubu_login_api():
    url = 'https://mubu.com/api/login/submit'
    data = {
        'phone': '15999555574',
        'password': 'qq316118979',
    }
    result = s.post(url=url, data=data)
    return result


def mubu_create_list():
    url = 'https://mubu.com/api/list/create_doc'
    data = {
        'folderId': 0,
        'type': 0
    }
    rep = s.post(url=url, data=data)
    assert rep.json()['code'] == 0



if __name__ == '__main__':
    data = mubu_login_api()
    mubu_create_list()
    
