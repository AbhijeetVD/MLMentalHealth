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
    username=request.form['name03']
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
        with open(f'static/{names}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "jtitle","jtext"])
        with open(f'static/user/{names}c.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Count"])
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
    ages=request.form['age']
    genders=request.form['gender']
    countries=request.form['country']
    famh=request.form['fh']
    rmwrk=request.form['rw']
    dx1=pd.read_csv("ml1.csv")
    dxt=np.array(dx1)
    dxr=len(dxt)
    dx1.loc[dxr, 'name']=names
    dx1.loc[dxr, 'mental health']=menhel
    dx1.loc[dxr, 'day'] = slep
    dx1.loc[dxr, 'sleep quality'] = slepqual
    dx1.loc[dxr, 'physically active'] = act
    dx1.loc[dxr, 'addictions'] = adc
    dx1.loc[dxr, 'age'] = ages
    dx1.loc[dxr, 'gender'] = genders
    dx1.loc[dxr, 'family history'] = famh
    dx1.loc[dxr, 'remote work'] = rmwrk
    dx1.to_csv("ml1.csv",index=False)
    dx = pd.read_csv("patient.csv")
    xd = np.array(dx)
    ros = len(xd)
    dx.loc[ros,'country'] = countries
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
    if ages=='1':
        dx.loc[ros, 'age'] = '18-28'
    else:
        if ages=='2':
            dx.loc[ros, 'age'] = '29-45'
        else:
            if ages=='3':
                dx.loc[ros, 'age'] = '46-65'
            else:
                if ages=='4':
                    dx.loc[ros, 'age'] = '65+'
    if genders=='1':
        dx.loc[ros, 'gender'] = 'male'
    else:
        if genders=='2':
            dx.loc[ros, 'gender'] = 'female'
        else:
            if genders=='3':
                dx.loc[ros, 'gender'] = 'transgender'
            else:
                if genders=='4':
                    dx.loc[ros, 'gender'] = 'prefer not to say'
    if famh=='1':
        dx.loc[ros, 'family history'] = 'Yes'
    else:
        if famh=='2':
            dx.loc[ros, 'family history'] = 'No'
    if rmwrk=='1':
        dx.loc[ros, 'remote work'] = 'Yes'
    else:
        if rmwrk=='2':
            dx.loc[ros, 'remote work'] = 'No'
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

@app.route('/journals', methods=['POST','GET'])
def Journal():
    print(names)
    jtitle=request.form['yus']
    jtext=request.form['yis']
    jd=pd.read_csv(f'static/{names}.csv')
    jdr = np.array(jd)
    jdr1 = len(jdr)
    d12=jdr[:,0]
    counter=pd.read_csv(f'static/user/{names}c.csv')
    cr=np.array(counter)
    crs=len(cr)
    counter.loc[crs,'Count']= '1'
    counter.to_csv(f'static/user/{names}c.csv', index=False)
    for i in range(0, 5):
        if names in d12 :
            with open(f'static/{names}{crs}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "jtitle", "jtext"])
                writer.writerow([names, jtitle, jtext])
            return render_template("Journal.html")
        else :
            jd.loc[jdr1, 'Name'] = names
            jd.loc[jdr1, 'jtitle'] = jtitle
            jd.loc[jdr1, 'jtext'] = jtext
            jd.to_csv(f'static/{names}.csv', index=False)
            return render_template("Journal.html")




@app.route('/viewjournal')
def viewJournal():
    print(names)
    kl=pd.read_csv(f'static/{names}.csv')
    kla=np.array(kl)
    klar=len(kla)
    v = {}
    counter=pd.read_csv(f'static/user/{names}c.csv')
    cr=np.array(counter)
    crs=len(cr)
    rand=cr[0:].astype('int')
    if crs==5:
        for i in range(4, 5):
            v['m1' + str(i)] = pd.read_csv(f'static/{names}{i}.csv')
            v['m2' + str(i)] = np.array(v['m1' + str(i)])
            v['m3' + str(i)] = v['m2' + str(i)][:, 1]
            v['m4' + str(i)] = v['m2' + str(i)][:, 2]
            print(v['m3' + str(i)])
    klax=kla[:,1]
    klaz=kla[:,2]
    return render_template("ViewJournal.html", xyz = klax, ijk = klaz)




@app.route('/vidoes')
def VideosPage():
    return render_template("Videos.html")



@app.route('/services')
def ServicesPage():
    return render_template("Services.html")

@app.route('/profile')
def ProfilePage():
    r2d2 = pd.read_csv('patient.csv')
    r2d3 = np.array(r2d2)
    lenth = len(r2d3)
    for i in range(0, lenth):
        if name1 == r2d3[i, 0]:
            return render_template("Profile.html", namep=name1, ph1=r2d3[i, 1], em1=r2d3[i, 2], Age=r2d3[i, 8],
                                   gender=r2d3[i, 9], country=r2d3[i, 10], family=r2d3[i, 11], remote=r2d3[i, 12])

@app.route('/profile', methods=["POST","GET"])
def Profile():
    return 0


@app.route('/predict',methods=['POST','GET'])
def Predict():
    print(request.form)
    dx = pd.read_csv("ml1.csv")
    xd = np.array(dx)
    xd1=xd[1:,0]
    print(xd1)
    xd2 = xd[1:, 1:]
    leng = len(xd1)
    int_features = [int(x) for x in request.form.values()]
    int_featuresa = np.array(int_features)
    for i in range(0, leng):
        if name1 == xd1[i]:
            new = np.append(int_featuresa, xd2[i, :])
            new = new.astype('int')
            print(new)
            final = [np.array(new)]
            print(final)
            prediction = model.predict_proba(final)
            output = '{0:.{1}f}'.format(prediction[0][1], 2)
            output1= float(output)
            if output > str(0.7):
                return render_template('forest.html',sc=100-(output1*100))
            else:
                if output > str(0.4) and output <= str(0.6):
                    return render_template('forest.html',sc=100-(output1*100))
                else:
                    return render_template('forest.html',sc=100-(output1*100))


    return render_template("forest.html")


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')