from flask import Flask ,request,redirect, url_for,flash
from werkzeug.utils import secure_filename
from config import Config
import pymysql
from flask import jsonify
from PIL import Image
import os
from werkzeug.exceptions import abort
from flask import send_from_directory


app=Flask(__name__)
UPLOAD_FOLDER = './uploads'
UPLOAD_PDF_FOLDER ='./pdf'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PDF_FOLDER']=UPLOAD_PDF_FOLDER
app.config.from_object(Config)
db = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

def get_user(user_id):
    conn = db.cursor()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user
@app.route('/')
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return jsonify(users)


@app.route('/<int:user_id>')
def user(user_id):
    user = get_user(user_id)
    return jsonify(user)

@app.route('/create',methods=['POST'])
def create():   
    try:
        print(request.form['nom'])
        nom=request.form['nom']
        prenom=request.form['prenom']
        date_de_naissance=request.form['date_de_naissance']
        lieu_de_naissance=request.form['lieu_de_naissance']
        signe=request.form['signe']
        numero=request.form['numero']
        lieu=request.form['lieu']
        profession=request.form['profession']
        pere=request.form['pere']
        mere=request.form['mere']
        fait=request.form['fait']
        le=request.form['le']
        file1=request.files["file1"]
        img_list = []
        if file1 and allowed_file(file1.filename):
            filename = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image1=Image.open(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image_convert1=image1.convert('RGB')
            # img_list.append(image_convert1)

        file2=request.files["file2"]
        if file2 and allowed_file(file2.filename):
            filename = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image2=Image.open(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image_convert2=image2.convert('RGB')
            # img_list.append(image_convert1)
        img_list=[image_convert2]

        image_convert1.save("./pdf/"+numero+".pdf",save_all=True,append_images=img_list)

        file_path=".pdf/"+numero+".pdf"
        cursor=db.cursor()
        cursor.execute("INSERT INTO users (nom, prenom,date_de_naissance,lieu_de_naissance,signe,numero,lieu,profession,pere,mere,fait,le,file_path) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (nom, prenom,date_de_naissance,lieu_de_naissance,signe,numero,lieu,profession,pere,mere,fait,le,file_path))
        db.commit()
        cursor.close()
        return get_users()
    except Exception as e:
    
        print("eto le olana",e)

# import os
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename

#upload file 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  



@app.route('/uploads', methods=['POST'])
def upload_file():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files= request.files.getlist("file")
        print(files)
      
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        img_list = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image=Image.open(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                image_convert=image.convert('RGB')
                img_list.append(image_convert)
                image_convert.save("./pdf/imageTopdf2.pdf",save_all=True,append_images=img_list)
            
        return 'ok'


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)

    # app.run(ssl_context=('cert.pem', 'key.pem'))

# def get_db_connection():
#     conn = sqlite3.connect('applitest.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/')
# def index():
#     conn=get_db_connection()
#     users=conn.execute('SELECT * FROM USER').fetchall()
#     conn.close()
#     return render_template("index.html",users=users)
      

