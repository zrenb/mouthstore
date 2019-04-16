from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View



class ArticlesView(View):
    def get(self, request):

        return render(request, 'articles/index.html')


class IndexView(View):
    """
    博客首页
    """

    def get(self, request):
        return render(request, 'articles/index.html')
