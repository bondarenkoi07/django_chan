from django.conf.urls.static import static

from hello_world import views
from django.contrib import admin
from django.urls import path, re_path, include

from learning import settings
# TODO: add eraser of deleted comment's files (DONE)
# TODO: add units list to imageboard header (DONE)
# TODO: try to create some tests (+-DONE)
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'^(?P<_unit>[_\-\w\d]+)$', views.unit, name='unit'),
    re_path(r'^(?P<_unit>[_\-\w\d]+)/(?P<_thread>\d+)$', views.thread, name='thread'),
    re_path(r'^(?P<_unit>[_\-\w\d]+)/newthread$', views.createThread, name='newthread'),
    re_path(r'^(?P<_unit>[_\-\w\d]+)/(?P<_thread>\d+)/create$', views.createComment, name='create'),
    re_path(r'^(?P<_unit>[_\-\w\d]+)/(?P<_thread>\d+)/delete', views.deleteComment, name='delete'),
    re_path(r'^(?P<_unit>[_\-\w\d]+)/(?P<_thread>\d+)/update/(?P<id>\d+)$', views.updateComment, name='update'),
    path('utils/', include('utils.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
