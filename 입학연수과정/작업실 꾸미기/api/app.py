from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)  # 서비스 이름으로 연결!

@app.route('/')
def index():
    count = r.incr('hits')  # 방문할 때마다 +1
    return f'<h1>방문 횟수: {count}번</h1>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)