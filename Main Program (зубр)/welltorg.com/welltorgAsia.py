from main import Site

auto = Site('https://welltorg.com/', 'https://welltorg.com/akkumulyator-55559-hagen-55ah-460a')
find_str = "find_all('div', 'h2')[1].get_text(strip=True)"
auto.parser('div', 'h2', find_str, 'E3')

auto = Site('https://welltorg.com/', 'https://welltorg.com/akkumulyator-55559-zap-plus-55ah-460a')
find_str = "find_all('div', 'h2')[1].get_text(strip=True)"
auto.parser('div', 'h2', find_str, 'E4')