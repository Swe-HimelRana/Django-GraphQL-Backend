 
import graphene
from api.models import Author, Publisher, Book
from .types import BookType, PublisherType, AuthorType
from .inputs import AuthorInput, AuthorUpdateInput, BookInput, BookUpdateInput, PublisherInput
 



class AuthorCreateMutation(graphene.Mutation):
    
    class Arguments:
        author_data = AuthorInput(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, author_data):
     
        author = Author.objects.create(**author_data)  

        return AuthorCreateMutation(author=author)


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        author_data = AuthorUpdateInput(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, author_data):

        print(author_data.items())
        
        author = Author.objects.get(pk=id)
 

        for item in author_data.items():
            setattr(author, item[0], item[1])
            author.save()

        return AuthorUpdateMutation(author=author)

class AuthorDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    
    author = graphene.Field(AuthorType)

    def mutate(self, info, id):

        if Author.objects.filter(pk=id).exists() == False:
            return Exception("Author not availabe")

        try:
            author = Author.objects.get(pk=id)
            author.delete()

        except Exception as e:
            return Exception(str(e))

        return None


class PublisherCreateMutation(graphene.Mutation):

    class Arguments:
        publisher_data = PublisherInput(required=True)

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, publisher_data):

        if publisher_data.name is None: 
            return Exception("Name is required")

        publisher = Publisher.objects.create(**publisher_data)
        

        return PublisherCreateMutation(publisher=publisher)

class PublisherUpdateMutation(graphene.Mutation):

    class Arguments:
        id = graphene.String(required=True)
        publisher_data = PublisherInput(required=True)

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, id, publisher_data):

        if Publisher.objects.filter(pk=id).exists() == False:
            return Exception("Publisher not available")

        publisher = Publisher.objects.get(pk=id)

        for item in publisher_data.items():
            setattr(publisher, item[0], item[1])
            publisher.save()
        
        return PublisherUpdateMutation(publisher=publisher)

class PublisherDeleteMutation(graphene.Mutation):

    class Arguments:
        id = graphene.String(required=True)

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, id):
        try:
            author = Publisher.objects.get(pk=id)
            author.delete()

        except Exception as e:
            return Exception(str(e))

        return None


class BookCreateMutation(graphene.Mutation):
    class Arguments:
        book = BookInput(required=True)

        
    book = graphene.Field(BookType)

    def mutate(self, info, book):

        if Publisher.objects.filter(pk=book.publisher_id).exists() == False:
            return Exception("Publisher not available")

        if Author.objects.filter(pk=book.author_id).exists() == False:
            return Exception("Author not available")

        publisher = Publisher.objects.get(pk=book.publisher_id)
        author = Author.objects.get(pk=book.author_id)
    
        book = Book.objects.create(publisher=publisher, author=author, name=book.name, pages=book.pages)

        return BookCreateMutation(book=book)


class BookUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        book_data = BookUpdateInput()

    book = graphene.Field(BookType)

    def mutate(self, info, id, book_data):

        if Book.objects.filter(pk=id).exists() == False:
            return Exception("Book not availalbe")

        book = Book.objects.get(pk=id)
        
        if book_data.author is not None:
            if Author.objects.filter(pk=book_data.author).exists() == False:
                return Exception("Author not available")

            author = Author.objects.get(pk=book_data.author)
            book.author = author

        if book_data.publisher is not None:
            if Publisher.objects.filter(pk=book_data.publisher).exists() == False:
                return Exception("Publisher not available")

            publisher = Publisher.objects.get(pk=book_data.publisher)
            book.publisher = publisher
        
        if book_data.name is not None:
            book.name = book_data.name

        if book_data.pages is not None:
            book.pages = book_data.pages

        book.save()

        return BookUpdateMutation(book=book)
        

class BookDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, id):
        if Book.objects.filter(pk=id).exists() == False:
            return Exception("Book not availabe")
        
        Book.objects.get(pk=id).delete()

        return None
 

class Mutation:
    # Auth Mutation
 

    # Author Mutations
    author_create = AuthorCreateMutation.Field()
    author_update = AuthorUpdateMutation.Field()
    author_delete = AuthorDeleteMutation.Field()

    # Publisher Mutations
    publisher_create = PublisherCreateMutation.Field()
    publisher_update = PublisherUpdateMutation.Field()
    publisher_delete = PublisherDeleteMutation.Field()
 
    # Book Mutations
    book_create = BookCreateMutation.Field()
    book_update = BookUpdateMutation.Field()
    book_delete = BookDeleteMutation.Field()
