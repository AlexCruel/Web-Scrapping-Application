from main import Site

akm11 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-premium-57-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm11.parser('div', 'cost', find_str, 'K11')

akm12 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-premium--63-a-ch-/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm12.parser('div', 'cost', find_str, 'K12')

akm13 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-premium-77-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm13.parser('div', 'cost', find_str, 'K13')

akm14 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-premium-80-a-middot-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm14.parser('div', 'cost', find_str, 'K14')

akm15 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-premium-105-a-middot-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm15.parser('div', 'cost', find_str, 'K15')