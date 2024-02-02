from django.shortcuts import render, redirect
from .models import Note

def index(request):
    note = Note.objects.all()
    if request.method == 'POST':
        title = request.POST.get('note')
        return redirect('delete', title)
    return render(request, 'index.html', {'note':note})


def add_notes(request):
    if request.method == 'POST':
        new_note = Note(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            date_created = request.POST.get('date_created')
        )
        new_note.save()
        return redirect('index.html')
    return render(request, 'add_notes.html')


def note_detals(request, NOTE):
    note = Note.objects.get(title=NOTE)
    return render(request, 'note_detals.html', {'note':note})


def edit_note(request, title):
    note = Note.objects.get(title=title)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.date_created = request.POST.get('date_created')
        note.save()
        return redirect('index.html')
    return render(request, 'edit_note.html', {'note':note})


def delete_note(request,title):
    note= Note.objects.get(title=title)
    if request.method == 'POST':
        note.delete()
        return redirect('index.html')
    return render(request, 'delete.html', {'note':note})
