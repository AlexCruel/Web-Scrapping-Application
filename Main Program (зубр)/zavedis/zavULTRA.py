from main import Site

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-ultra-55-a-h-530a-en')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D3')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-ultra-60-a-h-590a-en')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D5')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-ultra-66-a-h-640a-l')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D7')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-ultra-74-a-h-710a-r-nizkij')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D8')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=179&product_id=112')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D9')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-ultra-90-a-h-720a')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D10')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/index.php?route=product/product&path=179&product_id=109')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D12')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-ultra-100-a-h-940a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D13')