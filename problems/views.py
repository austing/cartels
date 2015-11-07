from django.views.generic import ListView
from problems.models import Problem

class ProblemListView(ListView):
    model = Problem
    template_name = "problems/problem_list.html"
