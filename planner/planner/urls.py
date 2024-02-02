
from django.contrib import admin
from django.urls import path
from planner_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index.html'),
    path('note/<str:NOTE>', views.note_detals, name='note'),
    path('add_note', views.add_notes, name='add_note'),
    path('edit/<str:title>', views.edit_note, name='edit_note'),
    path('delete/<str:title>', views.delete_note, name='delete')
]
