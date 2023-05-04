import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Post as PostModel
from .database import db_session

class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    posts = graphene.List(Post)
    post = graphene.Field(Post, id=graphene.Int())

    def resolve_posts(self, info):
        query = Post.get_query(info)
        return query.all()
    
    def resolve_post(self, info, id):
        query = Post.get_query(info)
        return query.filter(PostModel.id==id).first()

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
    
class UpdatePostInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    title = graphene.String()
    content = graphene.String()

class UpdatePost(graphene.Mutation):
    class Arguments:
        input = UpdatePostInput(required=True)

    post = graphene.Field(Post)

    def mutate(self, info, input):
        post = PostModel.query.get(input.id)

        if not post:
            raise GraphQLError(f"Post with id {input.id} not found")

        if input.title:
            post.title = input.title

        if input.content:
            post.content = input.content

        db_session.commit()

        return UpdatePost(post=post)

        

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
