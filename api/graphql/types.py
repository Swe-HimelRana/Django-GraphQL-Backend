import graphene
from graphene_django import DjangoObjectType
from api.models import Author, Publisher, Book
 

class BookType(DjangoObjectType):

    class Meta:
        model = Book
        field = ('id', 'name', 'pages', 'author', 'publisher', 'created_at')
 
 

class AuthorType(DjangoObjectType):

    class Meta:
        model = Author
        
    author_status = graphene.String()
     
    def resolve_author_status(self, info, **kwargs):
        return "New Author" if self.age < 25 else "Experienced Author"
 


class PublisherType(DjangoObjectType):

    class Meta:
        model = Publisher
        fields = "__all__"
