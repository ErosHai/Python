# hello函数
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello! {username.upper()}")
#
# greet_user('zhang san')
# greet_user('li si')
from urllib3 import proxy_from_url


# fullname函数
# def get_fullname(first_name, last_name):
#     fullname = f'{first_name} {last_name}'
#     return fullname.title()
#
# result = get_fullname('zhang', 'san')
# print(result)

# city函数
def get_city(city, country):
    result = f'{city} in {country}'
    return result.title()


city1 = get_city('beijing', 'china')
city2 = get_city('tokyo', 'japan')
city3 = get_city('seoul', 'korean')
print(city1)
print(city2)
print(city3)
