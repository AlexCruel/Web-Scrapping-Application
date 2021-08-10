from main import Site

auto = Site('', '')
find_str = "find('span', 'h1').get_text(strip=True)"
auto.parser('span', 'h1', find_str, 'E3')