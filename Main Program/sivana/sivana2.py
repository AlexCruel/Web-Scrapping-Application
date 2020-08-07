from main import Site

sivana128 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msj-10w-30-20-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana128.parser('div', 'single-product-price-block-content', find_str, 'C128')

sivana138 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msi-10w-40-5l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana138.parser('div', 'single-product-price-block-content', find_str, 'C138')

sivana139 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msi-10w-40-10-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana139.parser('div', 'single-product-price-block-content', find_str, 'C139')

sivana140 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msi-10w-40-20-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana140.parser('div', 'single-product-price-block-content', find_str, 'C140')

sivana142 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msi-10w-40-205-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana142.parser('div', 'single-product-price-block-content', find_str, 'C142')

sivana146 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msi-plus-15w-40-5l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana146.parser('div', 'single-product-price-block-content', find_str, 'C146')

sivana148 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-msi-plus-15w-40-20-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana148.parser('div', 'single-product-price-block-content', find_str, 'C148')

sivana172 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-gt-10w-40-20l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana172.parser('div', 'single-product-price-block-content', find_str, 'C172')

sivana173 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-gt-10w-40-205-l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana173.parser('div', 'single-product-price-block-content', find_str, 'C173')

sivana175 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-profi-gt-la-10w-40-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana175.parser('div', 'single-product-price-block-content', find_str, 'C175')