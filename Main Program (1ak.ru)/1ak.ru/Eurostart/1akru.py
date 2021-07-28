from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/55-ah-eurostart-extra-power-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C398')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/55-ah-eurostart-extra-power-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C399')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/60-ah-eurostart-extra-power-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C400')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/60-ah-eurostart-extra-power-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C401')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/75-ah-eurostart-extra-power-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C402')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/75-ah-eurostart-extra-power-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C403')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/90-ah-eurostart-extra-power-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C404')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/90-ah-eurostart-extra-power-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C405')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/eurostart-extra-power-100-ah-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C406')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/eurostart-extra-power-100-ah-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C407')