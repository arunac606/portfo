from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html') 

@app.route('/<string:page>')
def html_page(page):
    return render_template(page)

def write_to_file(data):
    with open("database.txt","a") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
        except:
            return 'Data not saved'
        return redirect('/thankyou.html')
    else:
        return 'something went wrong, Try again!'