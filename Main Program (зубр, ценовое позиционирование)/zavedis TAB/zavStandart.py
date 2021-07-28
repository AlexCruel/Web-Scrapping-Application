from main import Site

zav25 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-tab-polar-55-a-h-550a-en')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav25.parser('div', 'product-price-old', find_str, 'AI25')

zav26 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=296')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav26.parser('div', 'product-price-old', find_str, 'AI26')

zav31 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=295')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav31.parser('div', 'product-price-old', find_str, 'AI31')

zav32 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=294')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav32.parser('div', 'product-price-old', find_str, 'AI32')

zav33 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-tab-polar-100-a-h-900a-en')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav33.parser('div', 'product-price-old', find_str, 'AI33')