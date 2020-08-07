from main import Site

sivana282 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-energy-expert-l-10w-40-1l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana282.parser('div', 'single-product-price-block-content', find_str, 'C282')

sivana284 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-energy-expert-l-10w-40-5l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana284.parser('div', 'single-product-price-block-content', find_str, 'C284')

sivana285 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-energy-expert-l-10w-40-20l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana285.parser('div', 'single-product-price-block-content', find_str, 'C285')

sivana286 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-energy-expert-l-10w-40-b-50l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana286.parser('div', 'single-product-price-block-content', find_str, 'C286')

sivana287 = Site('https://sivana.by/', 'https://sivana.by/maslo-g-energy-expert-l-10w-40-205l')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana287.parser('div', 'single-product-price-block-content', find_str, 'C287')