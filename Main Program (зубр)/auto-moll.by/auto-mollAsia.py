from main import Site

auto = Site('http://auto-moll.by/', 'http://auto-moll.by/magazin/akkumulyatory-dlya-legkovyh-avtomobilej/a-mega/avtomobilnyy-akkumulyator-a-mega-premium-60-r/')
find_str = "find('span', 'shk-price').get_text(strip=True)"
auto.parser('span', 'shk-price', find_str, 'E3')