from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET', 'POST'])
def book_list(request, format=None):
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk, format=None):
	try:
		book = Book.objects.get(pk=pk)
	except Book.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = BookSerializer(book)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = BookSerializer(book, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET', 'POST'])
def author_list(request, format=None):
	if request.method == 'GET':
		authors = Author.objects.all()
		serializer = AuthorSerializer(authors, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = AuthorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@ratelimit(key='ip', rate='10/m', block=True)
@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk, format=None):
	try:
		author = Author.objects.get(pk=pk)
	except Author.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = AuthorSerializer(author)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = AuthorSerializer(author, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		author.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
