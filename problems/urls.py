from django.conf.urls import url
from django.contrib import admin

from problems.views import ProblemListView

urlpatterns = [
    # 1  Create url: generic form view
    # 2  Search url
    # 3  Index
    url(r'^$', ProblemListView.as_view(), name='problem-list'),
]

