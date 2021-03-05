# 2021.03.04, Uzd 2:
# Izveidot funkciju, kuras arguments ir saraksts ar mājaslapu adresēm. Funkcija atgriež sarakstu ar
# top-level domain (.com, .net, .lv).
# https://www.iana.org/domains/root/db

def extract_tld(url):
    url = url.replace("/", "")
    url = url.split('.')[-1]
    return url

def extract_tlds(adresses):
    tlds = []
    for i in adresses:
        tlds.append(extract_tld(i))
    return tlds

addr = ['https://www.iana.org/', 'http://www.gov.au/', 'http://www.gov.no/', 'https://ts.la/', 'https://deepmind.com']

print("Addresses: ", addr)
print("TLDs: ", extract_tlds(addr))
