from main import Site

sivana862 = Site('https://sivana.by/', 'https://sivana.by/maslo-tp-22s-marka-1-boch-205l')
find_str = "find('span', class_='single-product-price')"
sivana862.parser('div', 'single-product-price-block-content', find_str, 'C862')

sivana864 = Site('https://sivana.by/', 'https://sivana.by/maslo-tp-30-205l')
find_str = "find('span', class_='single-product-price')"
sivana864.parser('div', 'single-product-price-block-content', find_str, 'C864')