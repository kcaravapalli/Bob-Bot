import json,time
from flask import Flask, render_template, request, jsonify, Response


#app = Flask(__name__)
# app=Flask(__name__)
app = Flask(__name__, template_folder='templates',
            static_folder='templates', static_url_path='')
output=[]#("message stark","hi")]
@app.route('/')
def home_page():
    return render_template("index.html",result=output)

@app.route('/result',methods=["POST","GET"])
def Result():
    if request.method=="POST":
        print(list(request.form.values()))
        result=list(request.form.values())[0]
        if result.lower()=="restart":
            output.clear()
        else:
            try:
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                print("Bot says, ")
                for i in r.json():
                    bot_message = i['text']
                    print(f"{i['text']}")
                output.extend([("message parker",result),("message stark",bot_message)])
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])

        print(output)
        return render_template("index.html",result=output)



if __name__ == "__main__":
    app.run(debug=True)#,host="192.168.43.161")
