from flask import Flask

host = 'cluster0.lwvc7cn.mongodb.net'
usuario = 'carlotarojano99'
passwd = 'Harrybieber6795'
bd = 'dbb'

app = Flask(__name__)

app.config['MONGO_URI'] = f'mongodb+srv://{usuario}:{passwd}@{host}/{bd}'