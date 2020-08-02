from rest_framework.routers import DefaultRouter
from ui import views as uv

ui_router = DefaultRouter()
ui_router.register("app", uv.AppViewSet, basename="app")
ui_router.register("page", uv.PageViewSet, basename="page")
ui_router.register("element", uv.ElementViewSet, basename="element")