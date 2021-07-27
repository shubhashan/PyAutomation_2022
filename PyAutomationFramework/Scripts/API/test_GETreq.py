import pytest
import requests

def test_getReq():
    #GET req pass case wherein you get 200 OK as response
    Url="https://reqres.in/api/users?page=2"
    res=requests.get(Url)
    print(res)
    print(res.cookies)
    assert (res.status_code == 200), "Status code is not 200"

def test_getReq1():
    # GET req fail  case
    Url = "http://216.10.245.166/Library/GetBook.php?ID=3389 "
    res = requests.get(Url)
    print(res)
    assert (res.status_code == 404), "ID is present"


def test_getReq2():
    # GET req pass  case
    Url = "http://216.10.245.166/Library/GetBook.php?ID=bcd1227q "
    res = requests.get(Url)
    print(res)
    assert (res.status_code == 200), "Status code is not 200"





