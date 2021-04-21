#2021.04.01

# Izveidot Flask aplikāciju. “/add_user” atvēr formu, kurā ir jāievada lietotājvārds un e-pasts.
# Nospiežot “Submit” tiek veidots User klases objekts, kura instances atribūti ir username un email.
# Lietotājs redz uzrakstu ievadīto lietotajvādu un e-pastu.
# Opcionāli:
# “/” atver sarakstu ar pievienotiem lietotājiem. Saraksts ir tukšs katru reizi, kas(-d) startē aplikāciju.
# Table style: https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l

import flask


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


app = flask.Flask(__name__)
# users = []
users = [
    User("Me", "my@e.mail"),
    User("Me2", "my2@e.mail"),
    User("Me3", "my3@e.mail"),
]

html_header = """"
<!DOCTYPE html>
<HTML>
<HEAD>
    <style>
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            border-radius: 6px;
            -moz-border-radius: 6px;
        }
        .styled-table thead tr {
            background-color: #2980b9;
            color: #ffffff;
            text-align: left;
        }
        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }
        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }
        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }
        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #2980b9;
        }
        .styled-table tbody tr.active-row {
            font-weight: bold;
            color: #009879;
        }
        .styled-table tbody tr.input-row {
            font-weight: bold;
            color: #009879;
        }
    </style>
</HEAD>
<body bgcolor="#2b2b2b">
    <form method=post>
    <table class="styled-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
"""

html_footer = """"
        </tbody>
    </table>
    </form>
</body>
</html>
"""

html_input_row = """"
            <tr class="input-row">
                <td><input type=text name=name placeholder=Name></td>
                <td><input type=email name=email placeholder=Email></td>
                <td><input type=submit></td>
            </tr>
"""


def list_users():
    html = html_header
    # html += "List:</br>"
    html_table_tr = """
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td></td>
            </tr>
                    """
    for i in users:
        html += html_table_tr.format(i.name, i.email)

    html += html_input_row
    html += html_footer
    return html


@app.route('/')
def index():
    response = list_users()
    return response


@app.route('/', methods=['POST'])
def hello():
    name = flask.request.form['name']
    email = flask.request.form['email']
    users.append(User(name, email))
    response = f"<h1 style=\"color:#FFFFFF\">Added {name} ({email})</h1>"
    response += list_users()
    return response

app.run(host='127.0.0.1', port=80, debug=True)
