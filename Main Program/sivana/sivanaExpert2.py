from main import Site

sivana289 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-box-expert-gl-4-75w-90-1l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana289.parser('div', 'single-product-price-block-content', find_str, 'C289')

sivana293 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-box-expert-gl-5-75w-90-1l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana293.parser('div', 'single-product-price-block-content', find_str, 'C293')

sivana303 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-box-expert-atf-dx-iii-1l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana303.parser('div', 'single-product-price-block-content', find_str, 'C303')