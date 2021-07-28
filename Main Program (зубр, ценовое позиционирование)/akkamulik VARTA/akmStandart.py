from main import Site

akm39 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/varta-blue-dynamic-efb-560-500-056-60-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm39.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'V39')

akm41 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/varta-blue-dynamic-efb-570-500-065-70-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm41.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'V41')

akm42 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/varta-blue-dynamic-efb-575-500-073-75-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm42.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'V42')