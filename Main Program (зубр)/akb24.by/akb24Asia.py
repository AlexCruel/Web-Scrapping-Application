from main import Site

auto = Site('http://akb24.by/', 'http://akb24.by/topla/topla-e100')
find_str = "find('div', 'prod_price').get_text(strip=True)"
auto.parser('div', 'prod_price', find_str, 'E3')