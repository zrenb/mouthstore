# _*_coding:utf-8_*_
"""
+-----------------------------------------------------------------------------------------------------------

@Auth |     'Toss'

@Data |     '2019-03-12 16:01'

+-----------------------------------------------------------------------------------------------------------

"""
from django.conf.urls import url

from .views import ArticlesView

urlpatterns = [
    url(r'info/', ArticlesView.as_view(), name="article")
]
