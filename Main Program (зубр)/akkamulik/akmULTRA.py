from main import Site

akm3 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra-55-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm3.parser('div', 'cost', find_str, 'K3')

akm4 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra--60-a-ch-/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm4.parser('div', 'cost', find_str, 'K4')

akm5 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra-66-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm5.parser('div', 'cost', find_str, 'K5')

akm6 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra-74-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm6.parser('div', 'cost', find_str, 'K6')

akm7 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra-90-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm7.parser('div', 'cost', find_str, 'K7')

akm8 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/zubr-ultra-100-a-ch/')
find_str = "find('div', class_='flex costArea').get_text(strip=True)"
akm8.parser('div', 'cost', find_str, 'K8')