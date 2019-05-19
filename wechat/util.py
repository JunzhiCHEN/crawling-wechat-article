

class Util(object):
    def __init__(self):
        pass

    def handle_cookie(self, cookie_str):
        kv_list = str(cookie_str).split("; ")
        cookie_dict_list = []
        for one in kv_list:
            k_and_v = one.split("=", maxsplit=1)
            kv = {"name":k_and_v[0], "value":k_and_v[1]}
            cookie_dict_list.append(kv)
        return cookie_dict_list
