import json
from django.http import HttpResponse


# 统一返回json的格式
def render_json(data, code=0):
    result = {
        "data": data,
        "code": code,
    }

    # ensure_ascii=False：可以让序列化之后的中文能正常显示， 默认ascii码
    json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)

    return HttpResponse(json_str)

