from flask import Flask
from flask_graphql import GraphQLView
from app.schema import schema
from app.database import init_db

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    init_db()
    app.run()
