from main import Site

akm34 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-6st-100e-100-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm34.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F34')

akm49 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-asia-65e-65-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm49.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F49')

akm50 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-asia-75e-75-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm50.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F50')

akm51 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-asia-90e-90-a-middot-ch/')
find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
akm51.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F51')