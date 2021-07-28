from main import Site

lauto6 = Site('https://auto1.by/', 'https://auto1.by/masla-motornye-i-industrialnye/motornoe-maslo/2282016')
find_str = "find('span', class_='strikethrough')"
lauto6.parser('span', 'strikethrough', find_str, 'E12')