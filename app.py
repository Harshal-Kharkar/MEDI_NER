from flask import Flask , render_template, request
import pickle
import spacy
app = Flask(__name__)

@app.route("/")
def fun1():
    return render_template("t1.html")

@app.route("/predict", methods=["post"])
def fun2():
    text=request.form['text']
    nlp_ner = spacy.load(open("../medi_ner/saved_model/model-best"),'rb')
    doc = nlp_ner(text)

    colors = {"DRUG": "#F67DE3"}
    options = {"colors": colors} 

    output=spacy.displacy.render(doc, style="ent", options= options)
    
    return render_template("t2.html",text=text, output=output)

if __name__ == '__main__':
    app.run(debug=True)
