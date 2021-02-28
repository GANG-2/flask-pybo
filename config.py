db={
        'user' : 'flask',
        'password' : 'toor',
        'host' : '127.0.0.1',
        'port' : '3306',
        'database' : 'joo'
}

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS =False


SECRET_KEY="dev"
