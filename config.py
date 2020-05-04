class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:tulip@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'upload'