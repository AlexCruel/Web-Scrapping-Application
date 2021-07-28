from main import Site

akru = Site('https://akb.ru/', 'https://akb.ru/product/225-Mutlu_75L_720A_278x175x190.html')
find_str = "find('span', itemprop='price').get_text(strip=True)"
akru.parser('span', 'price', find_str, 'D129')