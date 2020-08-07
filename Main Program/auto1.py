from main import Site

auto1_12 = Site('https://auto1.by/', 'https://auto1.by/Details?id=2282016')
find_str = "find('td', title='Минимальная цена').get_text(strip=True)"
auto1_12.parser('div', 'details', find_str, 'E12')

auto1_14 = Site('https://auto1.by/', 'https://auto1.by/Details?id=2282017')
find_str = "find('td', style='white-space: nowrap; background: rgba(145, 253, 142, 0.44)').get_text(strip=True)"
auto1_14.parser('div', 'details', find_str, 'E14')