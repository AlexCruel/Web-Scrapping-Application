from main import Site

akm59 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-ultimatum-agm-r-60-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm59.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F59')

akm60 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-ultimatum-agm-r-70-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm60.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F60')

akm62 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-ultimatum-agm-r-95-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm62.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F62')