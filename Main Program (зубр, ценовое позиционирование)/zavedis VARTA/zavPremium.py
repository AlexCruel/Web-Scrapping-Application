from main import Site

zav53 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=410')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav53.parser('div', 'product-price-old', find_str, 'W53')

zav54 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=409')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav54.parser('div', 'product-price-old', find_str, 'W54')

zav55 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=408')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav55.parser('div', 'product-price-old', find_str, 'W55')

zav56 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=407')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav56.parser('div', 'product-price-old', find_str, 'W56')

zav57 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=405')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav57.parser('div', 'product-price-old', find_str, 'W57')