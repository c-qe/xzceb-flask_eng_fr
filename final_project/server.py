"""
server.py

@author: c-qe
"""
from machinetranslation.tests import translator
from flask import Flask, render_template, request
 
app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    en_fr=translator.english_to_french(textToTranslate)
    return en_fr

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    fr_en=translator.french_to_english(textToTranslate)
    return fr_en

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    """ Initilise and bind server using default address and port - http://127.0.0.1:5000 """
    app.run(debug=True)
    
