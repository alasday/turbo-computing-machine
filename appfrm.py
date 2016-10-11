##Asher Lasday
##SoftDev1 pd 8
##HW 04 -- Into a Zone of Danger
##2016-09-29

from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import csv
import os
appfrm = Flask(__name__)##creates an instance of a flask and instatiates its name
data = dict()
appfrm.secret_key=os.urandom(32)

@appfrm.route("/")
def home():
    '''
    print "\n\n\n"
    print ":::DIAG::: this flask obj"
    print appfrm
    print ":::DIAG::: this request obj"
    print request
    print ":::DIAG::: this request.headers obj"
    print request.headers
    print ":::DIAG::: this request.method obj"
    print request.method
    #print ":::DIAG::: this request.args[username] obj"
    #print request.args["username"]
    #print ":::DIAG::: this request.args obj"
    #print request.args 
    print ":::DIAG::: this request.from obj"
    print request.form
    '''
    readFile()
    return render_template("form.html")
    
@appfrm.route("/jacobo")
def js():
    print url_for("js")
    return redirect("http://xkcd.com")


        
    
    
    
    
@appfrm.route("/login", methods = ['POST'])
def login():
    hashObj = hashlib.sha1()
    user = request.form["username"]
    passw = request.form["password"]
    hashObj.update(passw)
    lr.request.form["lorr"]

    if lr == "register":
        direc=writeFile(user, hashObj)
        return render_template("result.html", Status="account created")
    if lr == "login":
        if user in data:
            if data[user] == hashObj.hexdigest():
                return render_template("result.html", Status = "Success, you're logged in")
        return render_template("result.html", Status= "incorrect log in infod")
    
    if lr == "logout":
        session.pop('user')
        return redner_template("result.html", Status = "logged out!")
    


def readFile():
    with open('data.csv','r') as csvfile:
        readr = csv.reader(csvfile)
        for row in readr:
            if row[0] != "user" and row[1] != "passw" and (row[0] not in data):
                data[row[0]] = row[1]

def writeFile(u,p):
  with open ('data.csv', 'w') as csvfile:
      writr = csv.writer(csvfile)
      writr.writerow([u,p])
 
    

    
if __name__=="__main__":
    appfrm.debug = True
    appfrm.run()

        
