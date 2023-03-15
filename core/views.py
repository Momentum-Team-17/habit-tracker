from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm, RecordForm


# view details, add records for the habit, list all records for the habit
def view_habit_details():
    pass


def add_habit(request):
    if request.method == 'POST':
        new_habit = HabitForm(request.POST)
        if new_habit.is_valid():
            new_habit.save()
            return redirect('home')
    form = HabitForm()
    return render(request, 'core/add_habit.html', {'form': form})


def edit_habit():
    pass


def edit_record():
    pass
