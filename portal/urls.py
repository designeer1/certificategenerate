from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    # Students URLs
    path('students/', views.students, name='students'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:sno>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:sno>/delete/', views.student_delete, name='student_delete'),
    path('students/export/', views.students_export_csv, name='students_export_csv'),
    path('students/import/', views.students_import_csv, name='students_import_csv'),
    path('students/<int:sno>/send/', views.send_single, name='send_single'),
    path('students/bulk-send/', views.bulk_send, name='bulk_send'),
    
    # Reports URLs
    path('reports/', views.reports, name='reports'),
    path('reports/<int:log_id>/resend/', views.log_resend, name='log_resend'),
    path('reports/<int:log_id>/download/', views.log_download, name='log_download'),
    
    # Templates URLs
    path('templates/', views.templates_list, name='templates_list'),
    path('templates/create/', views.template_create, name='template_create'),
    path('templates/<int:sno>/edit/', views.template_edit, name='template_edit'),
    path('templates/<int:sno>/delete/', views.template_delete, name='template_delete'),
    path('templates/export/', views.templates_export_csv, name='templates_export_csv'),
    path('templates/import/', views.templates_import_csv, name='templates_import_csv'),
    
    # Root URL redirects to students page
    path('', views.students, name='index'),
]