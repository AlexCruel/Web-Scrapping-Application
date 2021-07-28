from main import Site

akb25 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_polar_blue_55_a_ch_121055_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb25.parser('span', 'detail_price', find_str, 'AJ25')

akb26 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_polar_blue_60_a_ch_121060_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb26.parser('span', 'detail_price', find_str, 'AJ26')

akb27 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_polar_blue_66_a_h_620a_121066/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb27.parser('span', 'detail_price', find_str, 'AJ27')

akb31 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_polar_blue_75_a_ch_121075_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb31.parser('span', 'detail_price', find_str, 'AJ31')

akb33 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_polar_blue_100_a_h_920a_121100/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb33.parser('span', 'detail_price', find_str, 'AJ33')