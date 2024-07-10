import os


class Config:
    SECRET_KEY='5710908c5b9efc07d76a3d908a97f5db' #set in command line using secret.toeken_hex(16)-- 16 bytes
    #SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI  ='sqlite:///site.db' #specifing relative path
    #SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME= os.getenv('Flask_DB_USER')
    MAIL_PASSWORD= os.getenv('Flask_DB_PASSWORD2')
    #MAIL_USERNAME='diyahere25@gmail.com'
    #MAIL_PASSWORD='vbmg jvtg gqde ampz'