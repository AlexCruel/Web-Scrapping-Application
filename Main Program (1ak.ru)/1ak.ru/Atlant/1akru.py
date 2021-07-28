from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/55-ah-atlant-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C414')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/60-ah-atlant-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C416')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/75-ah-atlant-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C418')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/90-ah-atlant-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C419')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/atlant-90-ah-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C420')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/100-ah-atlant-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C421')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/100-ah-atlant-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C422')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/140-ah-atlant-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C423')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/avtomobilnyj-akkumulyator-atlant-190-ah-r')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C425')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/avtomobilnyj-akkumulyator-atlant-190-ah-l')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C426')