from mongoengine import connect

connect('makerhub_db', host='mongodb://localhost:27017/makerhub_db')