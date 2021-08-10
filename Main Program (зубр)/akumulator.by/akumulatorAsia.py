from main import Site

auto = Site('https://akumulator.by/', 'https://akumulator.by/catalog/akkumulyatoryi-72-78-ach/akkumulyator-centra-futura-77-r')
find_str = "find('span', 'val oneClick_price').get_text(strip=True)"
auto.parser('span', 'val oneClick_price', find_str, 'E3')