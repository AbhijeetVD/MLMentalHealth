from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import csv
import pandas as pd

data=pd.read_csv("patientinfo.csv")
data=np.array(data)
x=data[:,0:2]

database=dict(x)
database2=data[:,2:]
rows = len(x)

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))



@app.route('/')
def LoginPage():
    return render_template("Login.html")


@app.route('/register')
def RegisterPage():
    return render_template("Register.html")


@app.route('/register',methods=['POST','GET'])
def Register():
    global names, pwd, phone, email,name1
    names=request.form['usn']
    name1 = request.form['usn']
    pwd=request.form['psd']
    phone=request.form['phn']
    email=request.form['email']
    if names not in database:
        database.update({names:pwd})
        global df
        df = pd.read_csv("patientinfo.csv")
        df.loc[rows, 'name'] = names
        df.loc[rows, 'password'] = pwd
        df.loc[rows, 'phonenumber'] = phone
        df.loc[rows, 'email'] = email
        df.to_csv("patientinfo.csv", index=False)
        with open(f'{names}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "jtitle","jtext"])
        return render_template('First.html')
    else:
        return render_template('Register.html',error="This username is taken")

@app.route('/first',methods=['POST','GET'])
def First():
    menhel=request.form['mh']
    slep=request.form['sleep']
    slepqual=request.form['slq']
    act=request.form['phy']
    adc=request.form['add']
    dx = pd.read_csv("patient.csv")
    xd = np.array(dx)
    ros = len(xd)
    if menhel == '1':
        dx.loc[ros, 'name'] = names
        dx.loc[ros,'phonenumber'] = phone
        dx.loc[ros, 'email'] = email
        dx.loc[ros,'mental health'] = 'excellent'
    else:
        if menhel == '2':
            dx.loc[ros, 'name'] = names
            dx.loc[ros, 'phonenumber'] = phone
            dx.loc[ros, 'email'] = email
            dx.loc[ros, 'mental health'] = 'good'
        else:
            if menhel == '3':
                dx.loc[ros, 'name'] = names
                dx.loc[ros, 'phonenumber'] = phone
                dx.loc[ros, 'email'] = email
                dx.loc[ros, 'mental health'] = 'average'
            else:
                if menhel == '4':
                    dx.loc[ros, 'name'] = names
                    dx.loc[ros, 'phonenumber'] = phone
                    dx.loc[ros, 'email'] = email
                    dx.loc[ros, 'mental health'] = 'poor'
    if slep=='1':
        dx.loc[ros, 'sleep'] = '9+hours'
    else:
        if slep=='2':
            dx.loc[ros, 'sleep'] = '7-9hours'
        else:
            if slep=='3':
                dx.loc[ros, 'sleep'] = '4-6hours'
            else:
                if slep=='4':
                    dx.loc[ros, 'sleep'] = '>4hours'
    if slepqual=='1':
        dx.loc[ros, 'quality of sleep'] = 'excellent'
    else:
        if slepqual=='2':
            dx.loc[ros, 'quality of sleep'] = 'good'
        else:
            if slepqual=='3':
                dx.loc[ros, 'quality of sleep'] = 'average'
            else:
                if slepqual=='4':
                    dx.loc[ros, 'quality of sleep'] = 'poor'
    if act=='1':
        dx.loc[ros, 'physically active'] = 'heavy'
    else:
        if act=='2':
            dx.loc[ros, 'physically active'] = 'moderate'
        else:
            if act=='3':
                dx.loc[ros, 'physically active'] = 'light'
            else:
                if act=='4':
                    dx.loc[ros, 'physically active'] = 'no'
    if adc=='1':
        dx.loc[ros, 'addictions'] = 'no'
    else:
        if adc=='2':
            dx.loc[ros, 'addictions'] = 'Once a month'
        else:
            if adc=='3':
                dx.loc[ros, 'addictions'] = 'Once a week'
            else:
                if adc=='4':
                    dx.loc[ros, 'addictions'] = 'Everyday'
    dx.to_csv("patient.csv", index=False)
    return render_template('Home.html',name=names)

@app.route('/login',methods=['POST','GET'])
def Login():
    global name1,pwd,names,phone, email
    name1=request.form['username']
    names = request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('Login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('Login.html',info='Invalid User')
        else:

            return render_template('Home.html',name=name1)



@app.route('/home',methods=['POST','GET'])
def HomePage():
    return render_template("Home.html")

@app.route('/predict')
def Forest():
    return render_template("Forest.html")

@app.route('/journal')
def JournalPage():
    return render_template("Journal.html")

@app.route('/journal', methods=['POST','GET'])
def Journal():
    jtitle=request.form['yus']
    jtext=request.form['yis']
    jd=pd.read_csv(f'{names}.csv')
    jdr=np.array(jd)
    jdr1=len(jdr)
    jd.loc[jdr1, 'Name'] = names
    jd.loc[jdr1, 'jtitle'] = jtitle
    jd.loc[jdr1, 'jtext'] = jtext
    jd.to_csv(f"{names}.csv", index=False)
    return render_template("Journal.html")

@app.route('/viewjournal')
def viewJournal():
    kl=pd.read_csv(f'{names}.csv')
    kla=np.array(kl)
    klax=kla[-1,1]
    klaz=kla[-1,2]
    r2d2=pd.read_csv('patient.csv')
    r2d3=np.array(r2d2)
    lenth= len(r2d3)
    for i in range(0,lenth):
        if names==r2d3[i,0]:
            return render_template("ViewJournal.html",namee1=names,ph1=r2d3[i,1],email1=r2d3[i,2] ,mhe=r2d3[i,3] ,slep1=r2d3[i,4] ,qos=r2d3[i,5] ,phya=r2d3[i,6] ,adit=r2d3[i,7] , xyz = klax, ijk = klaz)


@app.route('/activities')
def ActivityPage():
    return render_template("Activity.html")

@app.route('/vidoes')
def VideosPage():
    return render_template("Videos.html")

@app.route('/reminders')
def RemindersPage():
    return render_template("Reminders.html")

@app.route('/services')
def ServicesPage():
    return render_template("Services.html")

@app.route('/profile')
def ProfilePage():
    da = pd.read_csv("patientinfo.csv")
    da = np.array(da)
    namee = da[:, 0]
    lent = len(namee)
    for i in range(0, lent):

        if (namee[i] == names or namee[i]==name1):
            print(namee[i])
            return render_template("Profile.html", namep=namee[i])

@app.route('/profile', methods=["POST","GET"])
def Profile():
    return 0


@app.route('/predict',methods=['POST','GET'])
def Predict():
    print(request.form)
    dx = pd.read_csv("patient.csv")
    xd = np.array(dx)
    xd1=xd[1:,0]
    xd2 = xd[1:, 3:]
    leng = len(xd1)
    int_features = [int(x) for x in request.form.values()]
    for i in range(0,leng):
        if(xd1[i] == names or xd1[i] == name1):
            print(xd1[i])
            if(xd2[i][0] == 'excellent'):
                a=1
                int_features.append(a)
                break
            else:
                if(xd2[i][0] == 'good'):
                    a=2
                    int_features.append(a)
                    break
                else:
                    if (xd2[i][0] == 'average'):
                        a=3
                        int_features.append(a)
                        break
                    else:
                        if (xd2[i][0] == 'poor'):
                            a=4
                            int_features.append(a)
                            break
    for i in range(0,leng):
        if(xd1[i] == names or xd1[i] == name1):
            print(xd1[i])
            if(xd2[i][1] == '9+hours'):
                b=1
                int_features.append(b)
                break
            else:
                if(xd2[i][1] == '7-9hours'):
                    b=2
                    int_features.append(b)
                    break
                else:
                    if (xd2[i][1] == '4-6hours'):
                        b=3
                        int_features.append(b)
                        break
                    else:
                        if (xd2[i][1] == '>4hours'):
                            b=4
                            int_features.append(b)
                            break
    for i in range(0, leng):
        if (xd1[i] == names or xd1[i] == name1):
            print(xd1[i])
            if (xd2[i][2] == 'excellent'):
                c = 1
                int_features.append(c)
                break
            else:
                if (xd2[i][2] == 'good'):
                    c = 2
                    int_features.append(c)
                    break
                else:
                    if (xd2[i][2] == 'average'):
                        c = 3
                        int_features.append(c)
                        break
                    else:
                        if (xd2[i][2] == 'poor'):
                            c = 4
                            int_features.append(c)
                            break
    for i in range(0, leng):
        if (xd1[i] == names or xd1[i] == name1):
            print(xd1[i])
            if (xd2[i][3] == 'heavy'):
                d = 1
                int_features.append(d)
                break
            else:
                if (xd2[i][3] == 'moderate'):
                    d = 2
                    int_features.append(d)
                    break
                else:
                    if (xd2[i][3] == 'light'):
                        d = 3
                        int_features.append(d)
                        break
                    else:
                        if (xd2[i][3] == 'no'):
                            d = 4
                            int_features.append(d)
                            break
    for i in range(0, leng):
        if (xd1[i] == names or xd1[i] == name1):
            print(xd1[i])
            if (xd2[i][4] == 'no'):
                e = 1
                int_features.append(e)
                break
            else:
                if (xd2[i][4] == 'Once a month'):
                    e = 2
                    int_features.append(e)
                    break
                else:
                    if (xd2[i][4] == 'Once a week'):
                        e = 3
                        int_features.append(e)
                        break
                    else:
                        if (xd2[i][4] == 'Everyday'):
                            e = 4
                            int_features.append(e)
                            break
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.7):
        return render_template('Login.html')
    else:
        if output>str(0.4) and output<=str(0.6):
            return render_template('Login.html')
        else:
            return render_template('Login.html')


if __name__ == '__main__':
    app.run(debug=True)