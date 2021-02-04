from flask import Flask, render_template, request
app = Flask(__name__)

bot_response_list=['What is your name?',
            'What is your Email?',
            'What is your address?',
            'What you are looking for?',
            'Thank you.']


@app.route("/")
def home_page():
    print("Home page called")
    return render_template("chat_window.html")


@app.route("/get")
def get_bot_response():
    #print("bot_response_list",bot_response_list)
    userText = request.args.get('msg')
    #print("UserText :",userText)
    output=bot_response_list[0]
    #print("output:",output)
    bot_response_list.pop(0)
    return output

if __name__ == "__main__":
    app.run(host='localhost',port=1020,debug=True)
