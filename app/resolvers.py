import graphene
from .models import Post
from .database import db_session

class PostQuery:
    posts = graphene.List(Post)

    def resolve_posts(self, info):
        return db_session.query(Post).all()

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(Post)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        db_session.add(post)
        db_session.commit()
        return CreatePost(post=post)

class PostMutation:
    create_post = CreatePost.Field()
