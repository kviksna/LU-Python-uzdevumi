# 2021.03.04, Uzd 3:
# Izveidot funkciju, kuras arguments ir mājaslapas adrese. Funkcija atgriež status code.
# https://www.shoutmeloud.com/worse-funny-domain-names-websites.html
# https://www.boredpanda.com/worst-domain-names/

import requests as req

def get_code(url):
    request = req.get(url)
    return request.status_code


print('HTTP Response code: ', get_code('http://penisland.net/'))
print('HTTP Response code: ', get_code('https://www.whorepresents.com/not/what/u/a/thinking/'))
print('HTTP Response code: ', get_code('http://httpstat.us/500'))
