from main import Site

sivana1031 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-snf-40-5-kg-krasnyy')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1031.parser('div', 'single-product-price-block-content', find_str, 'C1031')

sivana1033 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-snf-40-220-kg-krasnyy')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1033.parser('div', 'single-product-price-block-content', find_str, 'C1033')

sivana1036 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-nf-40-5-kg-sine-zelenyy')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1036.parser('div', 'single-product-price-block-content', find_str, 'C1036')

sivana1038 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-nf-40-220-kg')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1038.parser('div', 'single-product-price-block-content', find_str, 'C1038')

sivana1044 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-40-1-kg-zelenyy')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1044.parser('div', 'single-product-price-block-content', find_str, 'C1044')

sivana1056 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-hd-40-220-kg')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1056.parser('div', 'single-product-price-block-content', find_str, 'C1056')

sivana1062 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-si-oat-40-10-kg')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1062.parser('div', 'single-product-price-block-content', find_str, 'C1062')

sivana1063 = Site('https://sivana.by/', 'https://sivana.by/antifriz-g-energy-antifreeze-si-oat-40-220-kg')
find_str = "find('span', class_='single-product-price').get_text(strip=True)"
sivana1063.parser('div', 'single-product-price-block-content', find_str, 'C1063')