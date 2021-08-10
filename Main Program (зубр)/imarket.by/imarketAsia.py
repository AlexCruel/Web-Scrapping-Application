from main import Site

auto = Site('https://imarket.by/', 'https://imarket.by/product/zubr-mulyator-zubr-premium-new-r-plus-80-ach/')
find_str = "find('p', 'price').get_text(strip=True)"
auto.parser('p', 'price', find_str, 'E3')