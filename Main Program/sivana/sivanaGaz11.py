from main import Site

sivana867 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-slide-way-68-kan-20l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana867.parser('div', 'single-product-price-block-content', find_str, 'C867')

sivana868 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-slide-way-68-bochka-205l-181-kg')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana868.parser('div', 'single-product-price-block-content', find_str, 'C868')