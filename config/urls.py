from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic.base import RedirectView

admin.site.site_header = "Boilerplate"
admin.site.site_title = "Boilerplate Django Admin"
admin.site.index_title = "Django Admin LTE"

urlpatterns = (
    [
        path(settings.ADMIN_URL, admin.site.urls),
        path("", RedirectView.as_view(url=settings.ADMIN_URL)),
        path(
            "users/",
            include("my_boilerplate_django_admin.users.urls", namespace="users"),
        ),
        path("favicon.ico", RedirectView.as_view(url="/static/images/favicon.ico")),
        path("robots.txt", RedirectView.as_view(url="/static/robots.txt")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)


if settings.DEBUG:
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
