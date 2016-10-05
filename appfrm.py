##Asher Lasday
##SoftDev1 pd 8
##HW 04 -- Into a Zone of Danger
##2016-09-29

from flask import Flask, render_template, request
import hashlib
import csv
appfrm = Flask(__name__)##creates an instance of a flask and instatiates its name
data = dict()


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
    return render_template("index.html")
    

@appfrm.route("/reg", methods= ["POST"])
def register():
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
    print ":::DIAG::: this request.args[username] obj"
    print request.args["username"]
    print ":::DIAG::: this request.args obj"
    print request.args 
    print ":::DIAG::: this request.from obj"
    print request.form
    return render_template("form.html")
    '''
    user = request.form["username"]
    passw = request.form["password"]

    if user in usrpw:
        return render_template("result.html", outcome = "username already exists, try logging in")
    else:
        hashObj = hashlib.sha1()
        hashObj.update(passw)
        hashtPass = hashObj.hexdigest()
        writeFile(user,hashtPass)
        readfile()
        return  render_template("result.html", outcome = "Success")

@appfrm.route("/login", methods = ['POST'])
def login():
    hashObj = hashlib.sha1()
    user = request.form["username"]
    passw = request.form["password"]
    hashObj.update(passw)
    if user in data:
        if data[user] == hasgObj.hexdigest():
            return render_template("result.html", outcome = "Success, you're logged in")
        return render_template("result.html", outcome = "incorrect password")
    return render_template("result.html", outcome = "user does not exist")


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

        
