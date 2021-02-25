from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages


def view_programs(request):
    return render(request, 'programs/programs.html')
