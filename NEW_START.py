# Flask를 시작하는 방법! (WSGI 어플리케이션)
# Web Service Gateway Interface / 파이썬 어플리케이션이 웹 어플리케이션과 통신하기 위한 인터페이스. (일종의 프로토콜)
# 1. Flask 클래스를 import한다.
# 2. Flask class의 인스턴스를 생성한다. (인자로 모듈이나 패키지의 이름을 넣는다, 여기서는 단일 모듈이기 때문에 __name__을 사용)
# 3. route() 데코레이터를 사용해서 Flask에게 원하는 URL과 함수를 서로 연결시킨다.
# 4. 작성된 함수의 이름은 그 함수에 대한 URL을 생성하는데 사용되며, 브라우저에게 보여줄 메시지를 리턴한다.
# 5. run() 함수를 사용해서 어플리케이션을 로컬서버로 실행한다.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/user/<username>')
def show_user_profile(username):
    return "User {}".format(username)

if __name__ == "__main__":
    app.run(debug=True) # 디버그 모드를 사용하면 코드 변경을 자동으로 감지해서 리로드해준다!