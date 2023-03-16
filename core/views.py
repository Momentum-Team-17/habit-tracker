from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm, RecordForm, ObserverForm


# view details, add records for the habit, list all records for the habit
def view_habits(request):
    habits = Habit.objects.all()
    for thing in habits:
        print(habits)
    return render(request, 'core/index.html', {'habits': habits})


def add_habit(request):
    if request.method == 'POST':
        new_habit = HabitForm(request.POST)
        if new_habit.is_valid():
            new_habit.save()
            return redirect('home')
    form = HabitForm()
    return render(request, 'core/add_habit.html', {'form': form})


def view_habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'core/habit_details.html', {'habit': habit})


def add_record(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)
    if request.method == 'POST':
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            new_record = record_form.save(commit=False)
            new_record.habit = habit
            new_record.save()
            return redirect('home')
    form = RecordForm()
    return render(request, 'core/add_record.html', {'form': form, 'habit': habit})


def edit_habit():
    pass


def edit_record():
    pass
