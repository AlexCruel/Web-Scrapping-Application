from main import Site

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-rusbat-6st-75-evro')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G14')

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-rusbat-6st-90-evro')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G15')

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-rusbat-6st-55e')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G17')

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-rusbat-6st-60e-2')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G18')

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-rusbat-6st-75e')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G19')

zav59 = Site('https://www.rimir.by/', 'https://zavedis.by/vibor-po-marke-akb/akkumulyator-rusbat-6st-100e')
find_str = "find('div', class_='product-price-old').get_text(strip=True)"
zav59.parser('div', 'product-price-old', find_str, 'G20')