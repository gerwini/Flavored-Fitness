from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Program
from .forms import ProgramForm
from django.contrib.auth.decorators import login_required


def view_programs(request):  # View for people to view the programs
    """ A view to list all Programs """

    programs = Program.objects.all()

    context = {
        'programs': programs,
    }

    return render(request, 'programs/programs.html', context)


def program_info(request, program_id):  # View to view the program info

    programs = get_object_or_404(Program, pk=program_id)

    context = {
        'program': programs,
    }

    return render(request, 'programs/program_info.html', context)


@login_required
def add_program(request):  # View for admins to add a program
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            program = form.save()
            messages.success(request, 'Successfully added program!')
            return redirect(reverse('program_info', args=[program.id]))
        else:
            messages.error(request, 'Failed to add program. Please ensure the form is valid.')
    else:
        form = ProgramForm()

    template = 'programs/add_program.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_program(request, program_id):  # View for admins to edit programs
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    program = get_object_or_404(Program, pk=program_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated program!')
            return redirect(reverse('program_info', args=[program.id]))
        else:
            messages.error(request, 'Failed to update program. Please ensure the form is valid.')
    else:
        form = ProgramForm(instance=program)
        messages.info(request, f'You are editing {program.name}')

    template = 'programs/edit_program.html'
    context = {
        'form': form,
        'program': program,
    }

    return render(request, template, context)


@login_required
def delete_program(request, program_id):  # View for admins to delete programs
    """ Delete a program from the program List """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    program = get_object_or_404(Program, pk=program_id)
    program.delete()
    messages.success(request, 'program deleted!')
    return redirect(reverse('programs'))
