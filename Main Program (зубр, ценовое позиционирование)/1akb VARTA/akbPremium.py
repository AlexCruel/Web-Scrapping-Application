from main import Site

akb59 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_plus_d52_560_901_068_60_a_ch_680a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb59.parser('span', 'detail_price', find_str, 'X59')

akb60 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_plus_e39_570_901_076_70_a_ch_/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb60.parser('span', 'detail_price', find_str, 'X60')

akb61 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_plus_f21_580_901_080_80_a_ch_800a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb61.parser('span', 'detail_price', find_str, 'X61')

akb62 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_plus_g14_595_901_085_95_a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb62.parser('span', 'detail_price', find_str, 'X62')

akb63 = Site('https://1akb.by/', 'https://1akb.by/catalog/varta_start_stop_plus_h15_605_901_095_105_a_ch_950a/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb63.parser('span', 'detail_price', find_str, 'X63')