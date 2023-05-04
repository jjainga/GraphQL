import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import db_session, Post as PostModel

class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    posts = graphene.List(Post)

    def resolve_posts(self, info):
        query = Post.get_query(info)
        return query.all()

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(lambda: Post)

    def mutate(self, info, title, content):
        post = PostModel(title=title, content=content)
        db_session.add(post)
        db_session.commit()
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
