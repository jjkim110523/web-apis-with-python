# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from itsdangerous import json
from pyparsing import Word
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    response = {"usage": "/dict?=<word>"}
    return jsonify(response)


@app.get("/dict")
def dictionary():
    words = request.args.getlist("word")    
    
    if not words:
        response = {"status": "error", "word": words, "data": "word not found"}
        return jsonify(response)
    
    response = {"words": []}

    for word in words:
        definitions = match_exact(word)
        if definitions:
            response["words"].append({"status": "sucess", "word": word, "data": definitions})
        else:
            definitions = match_like(word)
            if definitions:
                response["words"].append({"status": "partial", "word": word, "data": definitions})
            else:
                response["words"].append({"status": "error", "word": word, "data": "word not found"})
    return jsonify(response)



if __name__ == "__main__":
    app.run()
