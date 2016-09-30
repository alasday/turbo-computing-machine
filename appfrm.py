from flask import Flask, render_template, request
appfrm = Flask(__name__)##creates an instance of a flask and instatiates its name



@appfrm.route("/")
def login_info_w_auth():
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
    

@appfrm.route("/auth", methods= ["POST"])
def login_info():
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


    
if __name__=="__main__":
    appfrm.debug = True
    appfrm.run()

        
