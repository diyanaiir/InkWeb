from flaskblog import create_app,db
app=create_app()

if __name__ == '__main__': 
    with app.app_context():
        db.create_all()#true only when script run directly
    app.run(debug=True)

