from django.contrib import admin
from django.urls import path, include

from code_test import user_views, auth_views
from code_test import views
from code_test import sql
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from django_email_verification import urls as email_urls
# admin1
# admin234567

# requestor1
# re234567

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include(email_urls)),

    path('', include('code_test.urls')),
     path('api/wishList/', user_views.wishList.as_view()),
     path('api/wishList/status/', user_views.getWishStatus),
     path('api/wishList/post/', user_views.writeWishList.as_view()),
     path('api/wishList/put/<int:wish_id>/', user_views.singleWishList.as_view()),
     path('api/status/post/', user_views.createStatus.as_view()),

    path('api/token/', auth_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/auth/status/', auth_views.check_is_logged_in.as_view()),

    path('api/auth/signup/', auth_views.signup),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
