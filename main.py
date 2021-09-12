from website import create_app

app = create_app()

#website will run only if you run this file directly
if __name__ == '__main__':
    app.run(debug=True) #everytime change is made to code, will rerun web server. turn off for production