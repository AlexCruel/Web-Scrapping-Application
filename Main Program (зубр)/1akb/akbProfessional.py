from main import Site

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr_190/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C37')