from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/12-ah-exide-bike')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C112')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/95-ah-exide-bike')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C113')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/6-ah-exide-bike')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C114')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/4-ah-exide-bike')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C115')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/23-ah-exide-bike')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C116')