from main import Site

zav = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=179&product_id=113')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D16')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-premium-63-a-ch-640a')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D17')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-premium-77-a-h-730a-r-nizkij')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D19')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-premium-77-a-ch-720a-l')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D20')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-premium-80-a-h-780a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D21')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-premium-105-a-h-1000a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D22')