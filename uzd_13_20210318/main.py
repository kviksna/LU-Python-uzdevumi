#2021.03.18

# Izveidot WSGI aplikāciju.
# “/university” atbild ar  formu, kas prasa lietotājam ievadīt savu vārdu un vērtējumu matemātikas,
# latviešu valodas un svešvalodas  vidusskolas eksāmenos (0–100).
# Kad forma tiek iesniegta, tiek atvērts “/university_response”. Tiek parādīts, vai cilvēks var stāties universitātē.
# Cilvēks var stāties universitāte, ja visos eksāmenos ir ne mazāk kā 40 balles.
# Opcionāli:
# Kad forma tiek iesniegta, lietotājs paliek “/university” lapā, bet tiek parādīts, vai cilvēks var stāties universitātē.

from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def form(environ):

    response_content = """
        <form action="/university" method="post" autocomplete="off">
            Full name: <input type="text" name="name"></br>
            Math: <input type="text" name="grade_math" placeholder="Math grade 0..100"></br>
            LV: <input type="text" name="grade_lv" placeholder="LV grade 0..100"></br>
            RU: <input type="text" name="grade_ru" placeholder="RU grade 0..100"></br>
            <input type="submit">
        </form>
        """

    return [response_content.encode()]


def name(environ):
    try:
        length = int(environ["CONTENT_LENGTH"])
    except ValueError:
        length = 0

    wsgi_input = environ["wsgi.input"].read(length).decode()
    form_data = parse_qs(wsgi_input)

    try:
        grade_math = int(form_data["grade_math"][0])
        grade_lv = int(form_data["grade_lv"][0])
        grade_ru = int(form_data["grade_ru"][0])
    except:  # PEP 8: E722 do not use bare 'except'
        return ["Wrong or no values given!".encode()]

    can_apply = "can"
    if grade_math < 40 or grade_lv < 40 or grade_ru < 40:
        can_apply = "can not"

    response_content = f"""
    Name: {form_data["name"][0]}</br>
    Math: {form_data["grade_math"][0]}</br>
    LV: {form_data["grade_lv"][0]}</br>
    RU: {form_data["grade_ru"][0]}</br>
    </br>
    {form_data["name"][0]} {can_apply} apply to the university
    """

    return [response_content.encode()]


def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html")]

    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]

    if path == "/university":
        if method == "GET":
            response_content = form(environ)
        if method == "POST":
            response_content = name(environ)
    else:
        response_content = [f"<h1>Welcome to homepage!</h1>You browsed for: {path}".encode()]

    start_response(status, headers)

    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}")
    server.serve_forever()
