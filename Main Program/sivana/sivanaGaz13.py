from main import Site

sivana889 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-formwork-oil-c-10-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana889.parser('div', 'single-product-price-block-content', find_str, 'C889')