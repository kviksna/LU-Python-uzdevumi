# 2021.03.04:
# Izveidot sarakstu ar motivējošiem citātiem. Izveidot WSGI aplikāciju, kura atbild
# ar nejaušu citātu no izveidotā saraksta. Citāts ir pirmā līmeņa virsraksts.
# https://blog.hubspot.com/sales/famous-quotes

from wsgiref.simple_server import make_server
from random import choice

quotes = [
    '"The greatest glory in living lies not in never falling, but in rising every time we fall." -Nelson Mandela',
    '"The way to get started is to quit talking and begin doing." -Walt Disney',
    '"Your time is limited, so don\'t waste it living someone else\'s life. Don\'t be trapped by dogma – which '
    'is living with the results of other people\'s thinking." -Steve Jobs',
    '"If life were predictable it would cease to be life, and be without flavor." -Eleanor Roosevelt',
    '"If you look at what you have in life, you\'ll always have more. If you look at what you don\'t have in life, '
    'you\'ll never have enough." -Oprah Winfrey',
    '"If you set your goals ridiculously high and it\'s a failure, you will fail above everyone '
    'else\'s success." -James Cameron',
    '"Life is what happens when you\'re busy making other plans." -John Lennon',
]

tmpl_old = """
<html>
<head>
</head>
<body bgcolor=black>
    <p align=center>
        <h1>
            <font color="gray">
                {}
            </font>
        </h1>
    </p>
</body>
</html>
"""

tmpl = """
<body bgcolor="black">
<div style="display:flex; justify-content:center; align-items:center; height:100%; color:gray;">
<h1>{}</h1>
</div>
"""


def simple_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
    ]

    start_response(status, headers)

    return [tmpl.format(choice(quotes)).encode()]


SERVER_PORT = 8000

with make_server(
        host='127.0.0.1',
        port=SERVER_PORT,
        app=simple_application,
) as wsgi_server:
    print(f'Starting server on {SERVER_PORT} port.')
    wsgi_server.serve_forever()
