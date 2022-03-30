from urllib.request import urlopen
import sys
html = urlopen(sys.argv[1]).read().decode('utf-8')
print(html)