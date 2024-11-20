def replaceCity(city):
    return {
        "北京": "北京市",
        "上海": "上海市",
        "广州": "广州市",
        "深圳": "深圳市",
    }.get(city, city)

print(replaceCity("北京aa"))

dict = {
        "北京": "北京市",
        "上海": "上海市",
        "广州": "广州市",
        "深圳": "深圳市",
    }
print(list(reversed(dict)))