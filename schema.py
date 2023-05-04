import graphene

class Post(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    content = graphene.String()

class Query(graphene.ObjectType):
    posts = graphene.List(Post)

    def resolve_posts(self, info):
        #return a list of posts from your data source
        return [...]
    

schema = graphene.Schema(query=Query)