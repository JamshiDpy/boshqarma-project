from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'speciality', SpecialityView, basename="spec-api")
router.register(r'boshqarma', BoshqarmaView, basename="boshqarma-api")
router.register(r'rahbariyat', RahbariyatView, basename="rahbariyat-api")
router.register(r'news', NewsView, basename="news-api")
router.register(r'murojaat', MurojaatView, basename="murojaat-api")
router.register(r'events', EventsView, basename="events-api")
router.register(r'regions', RegionView, basename="events-api")
router.register(r'hujjatlar', HujjatlarView, basename="hujjatlar-api")
router.register(r'fotos', FotosView, basename="fotos-api")
router.register(r'presentations', PresentationsView, basename="presentations-api")
router.register(r'projects', ProjectsView, basename="projects-api")
router.register(r'comments', CommentsView, basename="comments-api")





urlpatterns = [
    # path('boshqarma/', BoshqarmaView.as_view(), name="boshqarma-api"),
    # path('rahbariyat/', RahbariyatView.as_view(), name="rahbariyat-api"),
    # path('speciality/', SpecialityView.as_view(), name="speciality-api"),
    # path('speciality/<int:pk>/', SpecialityView.as_view(), name="speciality-put-api"),
    # path('news/', NewsView.as_view(), name="news-api"),
    # path('murojaat/', MurojaatView.as_view(), name="murojaat-api"),
]
urlpatterns += router.urls