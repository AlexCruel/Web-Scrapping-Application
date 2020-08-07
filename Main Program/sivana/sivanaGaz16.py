from main import Site

sivana896 = Site('https://sivana.by/', 'https://sivana.by/maslo-industrial-noe-i-12a-boch-205l-177kg')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana896.parser('div', 'single-product-price-block-content', find_str, 'C896')