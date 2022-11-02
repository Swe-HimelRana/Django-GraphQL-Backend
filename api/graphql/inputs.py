import graphene


class AuthorInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.Int(required=True)
    famous = graphene.Boolean(default_value=False)
    country = graphene.String(required=True)
    address = graphene.String(required=True)

class AuthorUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()
    famous = graphene.Boolean()
    country = graphene.String()
    address = graphene.String()

class PublisherInput(graphene.InputObjectType):
    name = graphene.String()
    website = graphene.String()

class BookInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    pages = graphene.Int(required=True)
    author_id = graphene.String(required=True)
    publisher_id = graphene.String(required=True)

class BookUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    pages = graphene.Int()
    author = graphene.String()
    publisher = graphene.String()