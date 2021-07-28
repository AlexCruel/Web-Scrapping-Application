from main import Site

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-original-66-a-h-660a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D25')

zav = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-akb-po-emkocti/akkumulyator-zubr-original-74-a-h-840a-r')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav.parser('div', 'product-price-old', find_str, 'D26')