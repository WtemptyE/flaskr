from app import app

@app.route('/')
def hemepage():
    return "Home page"