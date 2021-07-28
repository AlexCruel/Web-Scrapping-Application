from main import Site

lauto6 = Site('https://auto1.by/', 'https://auto1.by/masla-motornye-i-industrialnye/motornoe-maslo/2282016')
find_str = "find('meta', {'itemprop':'price'})['content']"
lauto6.parser('div', 'details', find_str, 'E12')

lauto10 = Site('https://auto1.by/', 'https://auto1.by/masla-motornye-i-industrialnye/motornoe-maslo/2282016')
find_str = "find('meta', {'itemprop':'price'})['content']"
lauto10.parser('div', 'details', find_str, 'E10')

lauto13 = Site('https://auto1.by/', 'https://auto1.by/masla-motornye-i-industrialnye/motornoe-maslo/3073125')
find_str = "find('meta', {'itemprop':'price'})['content']"
lauto13.parser('div', 'details', find_str, 'E13')