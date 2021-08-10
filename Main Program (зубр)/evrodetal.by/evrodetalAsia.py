from main import Site

auto = Site('https://evrodetal.by/', 'https://evrodetal.by/akkumulyatoryi/akkumulyator-security-power-sp-12-45-12v-45ah/')
find_str = "find('div', 'h1-pprice').get_text(strip=True)"
auto.parser('div', 'h1-pprice', find_str, 'E3')