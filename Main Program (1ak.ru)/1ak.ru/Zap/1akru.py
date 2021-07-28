from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/45-ah-zap-silver-japan-magic-eye-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C289')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/45-ah-zap-silver-japan-magic-eye-')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C290')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/80-ah-zap-silver-japan-magic-eye-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C291')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/80-ah-zap-silver-japan-magic-eye-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C292')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/54-ah-zap-silver-premium-lb1-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C293')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/55-ah-zap-silver-premium-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C294')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/62-ah-zap-silver-premium-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C295')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/62-ah-zap-silver-premium-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C296')