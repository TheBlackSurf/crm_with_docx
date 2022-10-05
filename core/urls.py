from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-form/', views.add_form, name='add_form'),
    path('edit-form/<str:pk>/', views.edit_form, name='edit_form'),
    path('remove-form/<str:pk>/', views.remove_form, name='remove_form'),
    path('pdf/<str:pk>/', views.pdf, name='render_pdf_view'),
    path('docx/<str:pk>/', views.docx, name='render_docx_view'),
    path('add-area/<str:pk>/', views.add_area, name='add_area'),
    path('edit-area/<str:pk>/', views.edit_area, name='edit_area'),
    path('delete-area/<str:pk>/', views.delete_area, name='delete_area'),
    path('area/<str:pk>/', views.area, name='area'),
    # experience
    path('experience/<str:pk>/', views.experience, name='experience'),
    path('delete-experience/<str:pk>/', views.delete_experience, name='delete_experience'),
    path('edit-experience/<str:pk>/', views.edit_experience, name='edit_experience'),
    path('add-experience/<str:pk>/', views.add_experience, name='add_experience'),


]
