import logging

import requests

def visit(
        url,
        method='get',
        params=None,
        data=None,
        json=None,
        **kwargs
):
    """访问接口。

    返回字典 。 res.json()
    """
    res = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        **kwargs
    )
    return res.json()







