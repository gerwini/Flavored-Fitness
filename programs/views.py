from django.shortcuts import render
from .models import Program


def view_programs(request):
    """ A view to list all Programs """

    programs = Program.objects.all()

    context = {
        'programs': programs,
    }

    return render(request, 'programs/programs.html', context)
