import graphene
from api.models import Author, Publisher, Book
from .types import BookType, PublisherType, AuthorType

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.String(required=True))
    all_authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.String())
    all_publishers = graphene.List(PublisherType)
    publisher = graphene.Field(PublisherType)
   


    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()
 
    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')
    
        try:
            return Book.objects.get(pk=id)
        except Exception as e:
            return Exception("Invalid Book id")
  

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_author(self, info, **kwargs):

        id = kwargs.get('id')

        try:
            return Author.objects.get(pk=id)
        except Exception as e:
            return Exception("Invalid Author id")

    def resolve_all_publishers(self, info, **kwargs):
        return Publisher.objects.all()

    def resolve_publisher(self, info, **kwargs):

        id = kwargs.get('id')

        try:
            return Publisher.objects.get(pk=id)
        except Exception as e:
            return Exception("Invalid Publisher id")