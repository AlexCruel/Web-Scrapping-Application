from main import Site

akm26 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/tab-polar-blue-60-a-middot-ch-121060/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm26.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'AH26')

akm27 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/tab-polar-blue-66-a-middot-ch-121066/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm27.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'AH27')

akm31 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/tab-polar-blue-75-a-middot-ch-121075/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm31.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'AH31')

akm33 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/tab-polar-blue-100-a-middot-ch-121100/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm33.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'AH33')