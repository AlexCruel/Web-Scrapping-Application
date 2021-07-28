from main import Site

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=212')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'AC59')

zav60 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=210')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav60.parser('div', 'product-price-old', find_str, 'AC60')

zav61 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=213')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav61.parser('div', 'product-price-old', find_str, 'AC61')

zav62 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=179&product_id=211')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav62.parser('div', 'product-price-old', find_str, 'AC62')

zav63 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=209')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav63.parser('div', 'product-price-old', find_str, 'AC63')