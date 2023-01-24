from website import create_app

app=create_app()

if __name__== '__main__': #this means that oonly if we run thsi file (main.py), not import it will we exceute the line below i.e run the app
    app.run(debug=True) #debug=True signifies that everytime we make a change to our python code it's going to automatically rerun the web server.

