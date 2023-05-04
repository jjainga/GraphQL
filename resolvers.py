import graphene
from schema import Post, Query

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(Post)

    def mutate(self, info, title, content):
        post = create_post(title, content) # create_post is a function that saves the new post to your data source
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()