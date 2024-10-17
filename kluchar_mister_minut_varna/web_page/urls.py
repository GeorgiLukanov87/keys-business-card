from django.urls import path

from kluchar_mister_minut_varna.web_page.views import index_view, about_view, service_view, contacts_view, project_view

urlpatterns = (
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('service', service_view, name='service'),
    path('contacts', contacts_view, name='contacts'),
    path('project', project_view, name='project'),
)
