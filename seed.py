from app.models import Post
from app.database import db_session

def create_post(title, content):
    post = Post(title=title, content=content)
    db_session.add(post)
    db_session.commit()
    return post

for i in range(100):
    create_post(f'Title {i}', f'Content {i}')
