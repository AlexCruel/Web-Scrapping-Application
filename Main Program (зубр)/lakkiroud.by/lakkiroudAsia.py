from main import Site

auto = Site('http://lakkiroud.by/', 'http://lakkiroud.by/katalog-akkumulatorov/legkovye/black-horse-66-ah/')
find_str = "find('div', 'price red').get_text(strip=True)"
auto.parser('div', 'price red', find_str, 'E3')