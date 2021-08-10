from main import Site

auto = Site('https://avd.by/', 'https://avd.by/avtomobilnye-akkumulyatory/westa/westa-premium-6st-60-aze-60-a-ch/')
find_str = "find_all('font', 'pr1')[1].get_text(strip=True)"
auto.parser('font', 'pr1', find_str, 'E3')