from main import Site

auto = Site('', '')
find_str = "find('div', 'price red').get_text(strip=True)"
auto.parser('div', 'price red', find_str, 'E3')