from main import Site

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-ultra-asia-45-a-h-360a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C29')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-ultra-asia-60-a-h-550a-l/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C30')

akb = Site('https://1akb.by/', 'https://1akb.by/catalog/zubr-ultra-asia-91a-h-800a-r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb.parser('span', 'detail_price', find_str, 'C33')