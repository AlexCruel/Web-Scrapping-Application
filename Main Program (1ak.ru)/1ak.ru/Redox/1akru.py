from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/75-ah-redox-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C135')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/60-ah-redox-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C136')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/75-ah-redox-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C137')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/60-ah-redox-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C138')