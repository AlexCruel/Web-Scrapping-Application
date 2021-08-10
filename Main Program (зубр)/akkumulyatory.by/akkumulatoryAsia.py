from main import Site

auto = Site('https://akkumulyatory.by/', 'https://akkumulyatory.by/catalog/legkovye/tudor/technika/tudor_technika_tb620_62_a_ch/')
find_str = "find('span', 'product-item-detail-price-current').get_text(strip=True)"
auto.parser('span', 'product-item-detail-price-current', find_str, 'E3')