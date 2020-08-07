from main import Site

sivana830 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-compressor-oil-100-216-5l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana830.parser('div', 'single-product-price-block-content', find_str, 'C830')

sivana832 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-compressor-oil-220-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana832.parser('div', 'single-product-price-block-content', find_str, 'C832')

sivana834 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-compressor-s-synth-46-20l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana834.parser('div', 'single-product-price-block-content', find_str, 'C834')

sivana837 = Site('https://sivana.by/', 'https://sivana.by/maslo-gazpromneft-compressor-s-synth-100-1l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana837.parser('div', 'single-product-price-block-content', find_str, 'C837')

sivana838 = Site('https://sivana.by/', 'https://sivana.by/masla/industrialnyiy-sektor/compressor-s-synth-100-2165l-179-kg/')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana838.parser('div', 'single-product-price-block-content', find_str, 'C838')