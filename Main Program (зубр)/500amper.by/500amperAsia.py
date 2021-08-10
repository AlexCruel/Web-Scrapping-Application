from main import Site

auto = Site('https://500amper.by/', 'https://500amper.by/catalog/akkumulyatori/akkumulyatori-avtomobilnie/akkumulyator-eurostart-55ah-.html')
find_str = "find('div', 'price').get_text(strip=True)"
auto.parser('div', 'price', find_str, 'E3')