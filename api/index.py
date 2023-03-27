from sanic import Sanic, Request
from sanic.response import text
app = Sanic("index")

 
@app.route('/')
async def index(request:Request):
    return text("hello sanic + vercel")

if __name__ == "__main__":
    app.run(single_process=True)