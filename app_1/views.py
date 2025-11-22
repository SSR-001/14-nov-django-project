from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
# from .forms import CommentForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

# maybe redundant now:
# def indexblah(request):

#     queryset = Post.objects
#     post = get_object_or_404(queryset)

#     return render(
#         request,
#         "app_1\index.html",
#         {
#             "post": post,
#         }
#     )

