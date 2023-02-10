from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('instagram/', include('instagram.urls')),
		#첫번째 인자의 url요청은 include안의 파일에서 찾아라
]