from main import Site

sivana250 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-special-to-4-10w-20l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana250.parser('div', 'single-product-price-block-content', find_str, 'C250')

sivana251 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-special-to-4-10w-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana251.parser('div', 'single-product-price-block-content', find_str, 'C251')

sivana262 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-special-stou-10w-40-20-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana262.parser('div', 'single-product-price-block-content', find_str, 'C262')

sivana263 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-special-stou-10w-40-boch-205-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana263.parser('div', 'single-product-price-block-content', find_str, 'C263')

sivana266 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-special-utto-10w-30-20l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana266.parser('div', 'single-product-price-block-content', find_str, 'C266')

sivana267 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-special-utto-10w-30-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana267.parser('div', 'single-product-price-block-content', find_str, 'C267')