# diluted dtool_lookup_server tests/__init__.py
import random
import string
import os
import sys

import pytest

# Pytest does not add the working directory to the path so we do it here.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.join(_HERE, "..")
sys.path.insert(0, _ROOT)

JWT_PUBLIC_KEY = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8LrEp0Q6l1WPsY32uOPqEjaisQScnzO/XvlhQTzj5w+hFObjiNgIaHRceYh3hZZwsRsHIkCxOY0JgUPeFP9IVXso0VptIjCPRF5yrV/+dF1rtl4eyYj/XOBvSDzbQQwqdjhHffw0TXW0f/yjGGJCYM+tw/9dmj9VilAMNTx1H76uPKUo4M3vLBQLo2tj7z1jlh4Jlw5hKBRcWQWbpWP95p71Db6gSpqReDYbx57BW19APMVketUYsXfXTztM/HWz35J9HDya3ID0Dl+pE22Wo8SZo2+ULKu/4OYVcD8DjF15WwXrcuFDypX132j+LUWOVWxCs5hdMybSDwF3ZhVBH ec2-user@ip-172-31-41-191.eu-west-1.compute.internal"  # NOQA

snowwhite_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMTEwMDgzMywianRpIjoiNmE3Yjk5NDYtNzU5My00OGNmLTg2NmUtMWJjZGIzNjYxNTVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InNub3ctd2hpdGUiLCJuYmYiOjE2MjExMDA4MzN9.gXdQpGnHDdOHTMG5OKJwNe8JoJU7JSGYooU5d8AxA_Vs8StKBBRKZJ6C6zS8SovIgcDEYGP12V25ZOF_fa42GuQErKqfwJ_RTLB8nHvfEJule9dl_4z-8-5dZigm3ieiYPpX8MktHq4FQ5vdQ36igWyTO5sK4X4GSvZjG6BRphM52Rb9J2aclO1lxuD_HV_c_rtIXI-SLxH3O6LLts8RdjqLJZBNhAPD4qjAbg_IDi8B0rh_I0R42Ou6J_Sj2s5sL97FEY5Jile0MSvBH7OGmXjlcvYneFpPLnfLwhsYUrzqYB-fdhH9AZVBwzs3jT4HGeL0bO0aBJ9sJ8YRU7sjTg"  # NOQA
grumpy_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMTEwMTY0NywianRpIjoiYWFmMTc3NTQtNzc4Mi00ODAzLThlZDItODZhYmI0ZDVhYThlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImdydW1weSIsIm5iZiI6MTYyMTEwMTY0N30.tvYTnOflEGjPM1AmDMQxE-2CAa7Je3uhq5DEQutUUGyuMHyT7phsam8l0aHGQjlCZb2X98Gs9QeQ5rXwxP5y8oteQzk26QbunW3Jpg46E1PheESURqOScLgyyiKa6aHtztb5aa5VxK2LgFB13JrQZ03GJpuDPQj7q1Lbu2Cn0JjX3YXRuF14ZkZk8ZrybnKsJ3RLKup_SUDeDx20hJFYBbnyd8jZSd5xV9eQfSrMHFhDBAnV9c8gzMXKnNR5OtVLyFWVrOB4OsP3Woy2eyXmM9G3Qljft6j_jtYcra7-7BnvIZE8JSLcTT0cH563KISFNqMxmkrWqhZaHRCRRhwsPg"  # NOQA
dopey_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMTEwMTY5NCwianRpIjoiZjNlOTFmNjQtZTIzZi00MWRkLThhOTAtMWUzYzkzMDlmYTM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRvcGV5IiwibmJmIjoxNjIxMTAxNjk0fQ.KJHiQN3MNGsfRQ_pGU0AGNSP-7-PR3oWvxUxjqtY23FPcrH3dJ3MTSVvD1kWiiEOkE-3kbq9KOg8g4OhpifBM44DbA-R5Xjuk_99Grc6TnPQMaB7W5s1k8JCs20wTW4gAM4t1ANixVQT0IW6T0OF_WeotWp-RaOkzYlMAp3KNotCNvlbj-fS-d3NEDucNjbHG_p9DgbOVLxD1jM-7GykMpLNvVeI5KZkgjvtxXvQt2sU_Dnm-J15TmknUaO6pLF--OA8AM8rZDf4p-QISsOu6uQEbxo9XSU_OHe7pzNebge54v3hd0vj5nAVqLg73myUHqOximaaObQRXk7ZOqjE4g"  # NOQA
sleepy_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMTEwMTcxOCwianRpIjoiMDM2YmNmZTktODg5OC00Nzg0LWIwYWQtZTRkOTczN2JjZjgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InNsZWVweSIsIm5iZiI6MTYyMTEwMTcxOH0.OoHNM5l_p8n2OKz-IEondgHzUhHwXmPY0rWnXrto9WSkHEGOAL6Yqc37dancRUIzvvG2l_oK88O0eHJEFMPT0M0F-18wvCQ9wdQfiAUSiagFw4o_sUomHXu0xWjDFZ-gClUW-85qZiyKjx8gYvCYod1rehBy1B52kZ6DAd2tzQfwzI8ncgsjdsqGcOotkLisidGrqRA2jXqeJjPrwNQlHNl4OH7n7pxzzMb4_spyWEG12pjYZwa77oMDim_RjQpmo8RnNOEgenN9fGnBN3myluKY8AV7ZCat5vORzrKARWOj_-EQr6c6-9ZrxLWArEVkecB-WG6f5U8KmnUsrPq6Cg"  # NOQA
noone_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMTEwMTc1MywianRpIjoiZWVlODQ1MmMtZGJkYi00Njk1LWFmYWItNDhmZTQ2ZDNlYzE4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5vb25lIiwibmJmIjoxNjIxMTAxNzUzfQ.HFfZFesk55Wi6ucUyjs3XR80giJhIvuK-9mrwJ0X0pvKqRGaa6kfPssZgO9LwrMsjRNClQVLdaHr12YTuMmPWAXj7glLvQeaGP60tfGhDacHJxIEQT1PyVdynGz66y4o13Gq32MY5zMXM4cFCy6-n0x6T-Gzrw5lJyn_wXGFeUE2rms19RZt4UrDLUXeKZlGUPyeMd34j23Io5IegrL4U5LLHvmP8IM9xZROcruJ87FLSZxHIdjg36YZ8oyTt7L8W-26fR6Ts_asyEpm0nOo8N1lszNPkx87f7Ckwyqoyom33nUIJUapDPR0LqYNd8bH_rp37Ed31zlAIU0L-hAipA"  # NOQA

BASE_URI = "s3://snow-white"


def random_string(
    size=9,
    prefix="test_",
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
):
    return prefix + ''.join(random.choice(chars) for _ in range(size))


def compare_nested(A, B):
    """Compare nested dicts and lists."""
    if isinstance(A, list) and isinstance(B, list):
        for a, b in zip(A, B):
            if not compare_nested(a, b):
                return False
        return True
    if isinstance(A, dict) and isinstance(B, dict):
        if set(A.keys()) == set(B.keys()):
            for k in A.keys():
                if not compare_nested(A[k], B[k]):
                    return False
            return True
        else:
            return False
    return A == B