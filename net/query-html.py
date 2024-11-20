import requests

class net_exception(Exception):
    """ descriptor """
    def __init__(self, fn):
        self.fn = fn

    def __enter__(self, type, value):
        print('catch it')
        self.fn()

    def __exist__(self, error, msg):
        print('exist it')

@net_exception
def query_html():
    res = requests.get("https://www.baidu.com")
    # print(res.content)

query_html()