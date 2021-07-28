from main import Site

zav62 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=331')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav62.parser('div', 'product-price-old', find_str, 'G53')

zav62 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=333')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav62.parser('div', 'product-price-old', find_str, 'G54')

zav62 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=334')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav62.parser('div', 'product-price-old', find_str, 'G55')

zav62 = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=61&product_id=332')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav62.parser('div', 'product-price-old', find_str, 'G57')

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-akom-ultimatum-60-agm-evro-60-a-h-680a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G59')

zav60 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-akom-ultimatum-70-agm-evro-70-a-h-760a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav60.parser('div', 'product-price-old', find_str, 'G60')

zav62 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-akom-ultimatum-95-agm-evro-95-a-h-850a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav62.parser('div', 'product-price-old', find_str, 'G62')