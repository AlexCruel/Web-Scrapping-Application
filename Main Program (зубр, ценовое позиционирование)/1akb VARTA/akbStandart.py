from main import Site

akb39 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_d53_560_500_056_60_a_ch_560a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb39.parser('span', 'detail_price', find_str, 'X39')

akb40 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_d54_565_500_065_65_a_ch_650a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb40.parser('span', 'detail_price', find_str, 'X40')

akb41 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_e45_570_500_065_70_a_ch_650a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb41.parser('span', 'detail_price', find_str, 'X41')

akb42 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_e46_575_500_073_75_a_ch_730a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb42.parser('span', 'detail_price', find_str, 'X42')

akb43 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_f22_580_500_073_80_a_ch_730a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb43.parser('span', 'detail_price', find_str, 'X43')