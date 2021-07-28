from main import Site

akb53 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_magic_55_a_h_560a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb53.parser('span', 'detail_price', find_str, 'AJ53')

akb54 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_magic_62_a_ch_189063/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb54.parser('span', 'detail_price', find_str, 'AJ54')

akb55 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_magic_75_a_ch_189080_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb55.parser('span', 'detail_price', find_str, 'AJ55')

akb56 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_magic_78_a_h_750a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb56.parser('span', 'detail_price', find_str, 'AJ56')

akb61 = Site('https://1akb.by/', 'https://1akb.by/catalog/tab_stop_go_agm_213080_80_a_ch_800a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb61.parser('span', 'detail_price', find_str, 'AJ61')