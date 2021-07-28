from main import Site

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/avtomobilnyj-akkumulyator-autopart-62-ah-arl562-galaxy-efb')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C7')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/avtomobilnyj-akkumulyator-autopart-72-ah-arl572-galaxy-efb')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C8')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/avtomobilnyj-akkumulyator-autopart-100-ah-arl600-galaxy-efb')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C9')

akru = Site('https://1ak.ru/', 'https://1ak.ru/products/95-ah-autopart-galaxy-efb')
find_str = "find('span', class_='js-price-change').get_text(strip=True)"
akru.parser('span', 'js-price-change', find_str, 'C10')