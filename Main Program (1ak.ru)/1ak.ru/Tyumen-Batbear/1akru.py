from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/62-ah-tyumen-batbear-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C214')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/62-ah-tyumen-batbear-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C215')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/66-ah-tyumen-batbear-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C216')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/75-ah-tyumen-batbear-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C217')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/90-ah-tyumen-batbear-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C218')