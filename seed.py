import random
from myapp.models import Post
from myapp import db

# List of random titles and content
titles = ['Hello World', 'GraphQL is cool', 'Python rocks', 'Flask is awesome']
content = ['Lorem ipsum dolor sit amet', 'Consectetur adipiscing elit', 'Sed do eiusmod tempor incididunt', 'Ut enim ad minim veniam']

# Create 100 posts
for i in range(100):
    title = random.choice(titles)
    body = random.choice(content)
    post = Post(title=title, content=content)
    db.session.add(post)

db.session.commit()
