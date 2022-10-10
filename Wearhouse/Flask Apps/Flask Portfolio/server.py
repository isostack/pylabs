from flask import Flask , render_template , request , redirect , url_for , session , flash

app = Flask ( __name__ )

@app.route ( '/' )
def index ():
    return render_template ( 'index.html' )

@app.route ( '/about' )
def about ():
    return render_template ( 'http://127.0.0.1:5500/templates/index.html#about' )

@app.route ( '/resume' )
def resume ():
    return render_template ( 'http://127.0.0.1:5500/templates/index.html#resume' ) 

@app.route ( '/portfolio' )
def portfolio ():
    return render_template ( 'http://127.0.0.1:5500/templates/index.html#portfolio' ) 

@app.route ( '/services' )
def services ():
    return render_template ( 'http://127.0.0.1:5500/templates/index.html#services' ) 

@app.route ( '/contacts' )
def contacts ():
    return render_template ( 'http://127.0.0.1:5500/templates/index.html#contact' ) 

if __name__ == "__main__" :
    app.run ( debug = True )


