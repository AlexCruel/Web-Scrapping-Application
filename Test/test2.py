from main import Site

site_1ak = Site('https://1ak.by/', 'https://1ak.by/mag/brands/zubr/')
find_str = "find('div', class_='product__price').find('span').get_text(strip=True)"
site_1ak.parser('div', 'product', find_str, 'B2')