from flask import Flask, request
import caesar


app = Flask(__name__)
form = """

<!DOCTYPE html>
         
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px {0};
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <form action=" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value={0}>
                <p class="error"></p>
            </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html> """