from main import Site

akb5 = Site('https://1akb.by/', 'https://1akb.by/catalog/bravo_6st_55_evro_55a_ch_430a_l/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb5.parser('span', 'detail_price', find_str, 'H5')

akb6 = Site('https://1akb.by/', 'https://1akb.by/catalog/bravo_6st_60_evro_60a_ch_480a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb6.parser('span', 'detail_price', find_str, 'H6')

akb7 = Site('https://1akb.by/', 'https://1akb.by/catalog/akkumulyator_bravo_6st_74/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb7.parser('span', 'detail_price', find_str, 'H7')

akb8 = Site('https://1akb.by/', 'https://1akb.by/catalog/bravo_6st_90_evro_90a_ch_760a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb8.parser('span', 'detail_price', find_str, 'H8')

akb12 = Site('https://1akb.by/', 'https://1akb.by/catalog/akom_rusbat_6st_55e_55_a_ch_430a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb12.parser('span', 'detail_price', find_str, 'H12')

akb17 = Site('https://1akb.by/', 'https://1akb.by/catalog/avtomobilnyy_akkumulyator_akom_rusbat_6st_55e_55_a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb17.parser('span', 'detail_price', find_str, 'H17')

akb18 = Site('https://1akb.by/', 'https://1akb.by/catalog/avtomobilnyy_akkumulyator_akom_rusbat_6st_60e_60_a_ch/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb18.parser('span', 'detail_price', find_str, 'H18')

akb22 = Site('https://1akb.by/', 'https://1akb.by/catalog/akom_autofan_6ct_55e_55_a_h_420a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb22.parser('span', 'detail_price', find_str, 'H22')

akb23 = Site('https://1akb.by/', 'https://1akb.by/catalog/akom_autofan_6st_60e_60_a_h_470a_r/')
find_str = "find('div', class_='price-card').find('ul', class_='list-inline mb-0').get_text(strip=True)"
akb23.parser('span', 'detail_price', find_str, 'H23')