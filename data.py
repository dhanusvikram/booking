from zoneinfo import available_timezones
from flask import Flask,request,render_template,redirect, url_for
app = Flask(__name__,template_folder='template')
list=[]

@app.route('/')
def hello_world():
    return render_template("login.html")

database={'dhanush':'123','vikram':'abc','sanorac':'abcdef'}
trip1={'coimbatore':'chennai'}
trip2={'coimbatore':'erode'}
trip3={'chennai':'madurai'}
total_seats= int(30)

@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template("travel.html",name=name1)

@app.route('/travel', methods=['POST', 'GET'])
def travel():
    return render_template('travel.html')


@app.route('/Bus', methods=['POST', 'GET'])
def bus():
    return render_template("bus.html")

@app.route('/trip', methods=['POST', 'GET'])
def trip():
    sou=request.form['source']
    des=request.form['destination']
    if trip1[sou]==des:
        return render_template("trip1.html")
    elif trip2[sou]==des:
        return render_template("trip2.html")
    elif trip3[sou]==des:
        return render_template("trip3.html")
    else:
        return render_template("bus.html")


@app.route('/avb', methods=['POST', 'GET'])
def avb():
    ab=total_seats
    return render_template("detail.html",info = "available seats %s" %ab)

@app.route('/bb', methods=['POST', 'GET'])
def bb():
    name=request.form.get('name')
    ticket=request.form.get('ticket')
    age=request.form.get('age')
    gender=request.form.get('gender')
    list.append({'name':name,'ticket booked':ticket,'age':age,'gender':gender})

    td=int(ticket)
    avb= total_seats-td
    pay=550*td
    return render_template('payment.html',info="available seats%d" %avb,info2="total amount %d"%pay)

@app.route('/msg', methods=['POST', 'GET'])
def pay():
     return render_template('pay.html')

@app.route('/pay', methods=['POST', 'GET'])
def mainmenu():
    return render_template('msg.html',info="payment successful")

@app.route('/booking', methods=['POST', 'GET'])
def booking():
    return render_template('index.html', toys=list)




if __name__ == '__main__':
    app.run()