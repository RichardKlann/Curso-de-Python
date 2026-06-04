'''
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
'''

import urllib.request
import urllib.error

url = "https://www.goog.com.br"

try:
    urllib.request.urlopen(url, timeout=5)

except urllib.error.HTTPError as e:
    print(f"Servidor respondeu (HTTP {e.code})")

except urllib.error.URLError:
    print("Servidor inacessível")

else:
    print("Servidor respondeu (HTTP 200)")