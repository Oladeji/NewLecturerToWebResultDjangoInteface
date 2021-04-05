from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
  
    path('', views.landing,name='landing'),
    path('login_view', views.login_view,name='login_view'),
    path('logout_view', auth_views.LogoutView.as_view(template_name='GradeManagerapp/landing.html'), name='logout_view'),
    path('register_view', views.register_view, name='register_view'),
    path('reports_view', views.reports_view, name='reports_view'),
    path('processcourses_view', views.processcourses_view, name='processcourses_view'), 
    path('displayCourseview', views.displayCourse_view, name='displayCourse_view'), 
    path('downloadScoresheet_xls', views.downloadScoresheet_xls, name='downloadScoresheet_xls'),
    path('downloadScoreSheetPdf', views.downloadScoreSheetPdf, name='downloadScoreSheetPdf'),
    path('downloadPdfReports', views.downloadPdfReports, name='downloadPdfReports'),
    path('uploadScoresheet_xls', views.uploadScoresheet_xls, name='uploadScoresheet_xls'),


]