from flask import *
import sqlite3
import pywhatkit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add")
def add():
    return render_template("addstd.html")

@app.route("/savestd",methods=["POST","GET"])
def save():
    if request.method=="POST":
        name=request.form["name"]
        mobile=request.form["mobile"]
        email=request.form["email"]
        dept=request.form["dept"]
        year=request.form["year"]
        with sqlite3.connect("SDM.db") as conn:
            cur = conn.cursor()
            cur.execute("Insert into Student(sname,email,mobile,dept,year) values(?,?,?,?,?)",(name,email,mobile,dept,year))
            conn.commit()
            print("Saved successfully")
    return render_template("home.html")

@app.route("/display")
def display():
    con = sqlite3.connect("SDM.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("Select * from Student")
    rows = cur.fetchall()
    return render_template("displaystd.html",rows=rows)

@app.route("/remove")
def remove():
    return render_template("removestd.html")

@app.route("/removestd",methods=["POST"])
def removestd():
    if request.method=="POST":
        rollno = request.form["rollno"]
        with sqlite3.connect("SDM.db") as conn:
            cur = conn.cursor()
            cur.execute("delete from Student where rollno=?",rollno)
            conn.commit()
        return render_template("home.html")

##@app.route("/video")
##def convert(file,e="mp3"):
##    fname,ext = os.path.splitext(file)
##    VideoFileClip(file).audio.write_audiofile(f"{fname}.{e}")
##
##convert("")
##print("Done")
    
               
@app.route("/search")
def search():
    return render_template("search.html")  

@app.route("/google",methods=["POST"])
def google():
    if request.method=="POST":
        keyword = request.form["keyword"]
        pywhatkit.search(keyword)
        return render_template("home.html")


@app.route("/youtube")
def youtube():
    return render_template("youtube.html")

@app.route("/youtubevideo",methods=["POST"])
def youtubevideo():
    if request.method=="POST":
        keyword = request.form["keyword"]
        pywhatkit.playonyt(keyword)
        return render_template("home.html")
        

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/information",methods=["POST"])
def information():
    if request.method=="POST":
        keyword = request.form["keyword"]
        pywhatkit.info(keyword)
    return render_template("home.html")    
app.run()
