from main import Site

auto = Site('https://autosup.by/', 'https://autosup.by/akkum/A-mega/a-mega-premium-60l')
find_str = "find('div', 'f16 bold').get_text(strip=True)"
auto.parser('div', 'f16 bold', find_str, 'E3')