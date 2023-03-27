from sanic import Sanic, Request
from sanic.response import text
app = Sanic("index")
 
 
@app.route('/')
async def index(request:Request):
    print("foejfoiwejfo")
    return text("hello sanic + vercel")