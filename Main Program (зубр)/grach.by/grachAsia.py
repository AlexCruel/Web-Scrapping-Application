from main import Site

auto = Site('https://grach.by/', 'https://grach.by/akkumulyatoryi/akkumulyatoryi-mototehniki/akkumulyator-dlya-motocikla-lider-9ah/')
find_str = "find('span', 'h1').get_text(strip=True)"
auto.parser('span', 'h1', find_str, 'E3')