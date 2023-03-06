from bottle import get, post, request, run, template
import sqlite3


@get('/chat-room')  # GET メソッドで /login にアクセスしたときの処理
def chat_from():
    return '''
        <form action = "/chat" method = "post">
            Username: <input name = "username" type = "text" />
            text: <textarea name="chat" rows="5" cols="40"></textarea>
            <input value = "投稿" type = "submit"/>
        </form>
    '''
@post('/chat')
def chat():
    
    name=request.forms.username
    chats=str(request.forms.chat)
    with sqlite3.connect("chat.db") as conn:
        cur=conn.cursor()
        cur.execute('CREATE TABLE chat_room(id int, title varchar(1024), data varchar(1024))')
        cur.execute(f"INSERT INTO chat_room VALUES(1,'{name}','{chats}')")
        conn.commit()
    with sqlite3.connect("chat.db") as conn:
        cur=conn.cursor()
        cur.execute('select * from chat_room')
        html='<table style=word-break: break-word;>'
        for row in cur:
            html=html + f"\n<tr>\n<th>{row[1]}</th>\n<th>{row[2]}</th>\n</tr>\n"
        html=f"{html}</table>"
    return html
run(host="localhost",port="8880",debug=True)
