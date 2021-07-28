from main import Site

akm23 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-asia--60-a-ch---jca-/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm23.parser('div', 'cost', find_str, 'D23')

akm24 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-asia--68-a-ch---jca-/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm24.parser('div', 'cost', find_str, 'D24')

akm25 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra--80-a-ch--jca-/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm25.parser('div', 'cost', find_str, 'D25')

akm26 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-asia--91-a-ch---jca-/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm26.parser('div', 'cost', find_str, 'D26')