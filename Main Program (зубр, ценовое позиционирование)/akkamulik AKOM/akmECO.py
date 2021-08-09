from main import Site

akm5 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/bravo-6ct-55-55-a-ch/')
find_str = "find_all('div', 'product-info__cost')[1].get_text(strip=True)"
akm5.parser('div', 'product-info__cost', find_str, 'F5')

# akm6 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/bravo-6ct-60-r-60-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm6.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F6')

# akm7 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/bravo-6ct-74-74-a-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm7.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F7')

# akm8 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/bravo-6ct-90-90-a-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm8.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F8')

# akm9 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/bravo-6ct-140-140-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm9.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F9')

# akm10 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/bravo-6ct-190-190-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm10.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F10')

# akm12 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-rusbat-6st-55e-55-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm12.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F12')

# akm14 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-rusbat-6st-75e--75-a-ch-/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm14.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F14')

# akm15 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-rusbat-6st-90e-90-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm15.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F15')

# akm19 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-rusbat-6st-75e-75-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm19.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F19')

# akm20 = Site('https://akkamulik.by/', 'https://akkamulik.by/catalog/avtomobilnye-akkumulyatory/akom-rusbat-6st-100e-100-a-middot-ch/')
# find_str = "find('div', style='padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;').get_text(strip=True)"
# akm20.parser('div', 'padding-top: 2.5px;font-weight: bold;font-size: 26px;line-height: 32px;color: #033460;height: 50%;width: 100%;box-sizing: border-box;', find_str, 'F20')