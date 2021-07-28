from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/60-ah-hagen-starter-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C118')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/74-ah-hagen-starter-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C119')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/74-ah-hagen-starter-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C120')