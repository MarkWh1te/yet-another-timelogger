from django.urls import path, include, re_path
from record import views as v

urlpatterns = [
    path('record', v.record, name="record"),
    re_path(r'^delete/(?P<part_id>[0-9]+)/$', v.delete, name='delete_view'),
]
