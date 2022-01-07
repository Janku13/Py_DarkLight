from flask import Flask , render_template,request,redirect,url_for
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def write_to_file(data):
    with open("database.csv",mode='a',newline='') as database2:
        nome  = data['name']
        email = data['email']
        subject= data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([nome,email,subject,message])


#para me mandar e-mail
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)

        return render_template('thanks.html')

    else:
        return "somthing wrong"

if __name__ == "__main__":
    app.run(debug=True)