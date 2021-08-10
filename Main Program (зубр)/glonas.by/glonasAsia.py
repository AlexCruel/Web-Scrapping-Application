from main import Site

auto = Site('https://glonas.by/', 'https://glonas.by/akkumulator/A-Mega/Standard/A-Mega_Standard_50Ah/')
find_str = "find('span', 'FirstPrice').get_text(strip=True)"
auto.parser('span', 'FirstPrice', find_str, 'E3')