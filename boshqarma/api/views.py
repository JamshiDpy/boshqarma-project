from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .serializers import *

class FotosView(ModelViewSet):
    queryset = Foto_lavhalar.objects.all()
    serializer_class = FotoSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser, )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'pk'
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        foto_object = self.get_object()
        serializer = self.serializer_class(foto_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request):
        try:
            object = self.get_object()
            object.delete()
            return Response({"detail":"Successfully deleted. "})
        except Exception as e:
            return Response({"detail":f"{e}. "})

class RegionView(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class HujjatlarView(ModelViewSet):
    queryset = Hujjatlar.objects.all()
    serializer_class = HujjatlarSerializer
    parser_classes = (JSONParser, ) #MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class BoshqarmaView(ModelViewSet):
    queryset = Boshqarma.objects.all()
    serializer_class = BoshqarmaSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def list(self, request):
        queryset = Boshqarma.objects.all()
        query_photos = Foto_lavhalar.objects.all()
        print(queryset[0])
        for object in queryset:
            object.fotos = [fotoObject.FotoURL for fotoObject in Foto_lavhalar.objects.all()]
            object.save()
        serializer = self.serializer_class(Boshqarma.objects.all(), many=True)
        return Response(serializer.data, status=200)
    
    def create(self, request):
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

    def retrieve(self, request, pk):
        object = Boshqarma.objects.first()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=301)
        return Response(serializer.errors)



class EventsView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SpecialityView(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RahbariyatView(ModelViewSet):
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MurojaatView(ModelViewSet):
    queryset = Murojaat.objects.all()
    serializer_class = MurojaatSerializer
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(serializer)
            return Response({"detail": "Emailga kod yuborildi",}, status=201)
        return Response(serializer.errors, status=400)

class PasswordResetConfirmView(APIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(serializer)
            email = serializer.validated_data.get('email')
            code = serializer.validated_data.get('code')
            new_password2 = serializer.validated_data.get('new_password2')
            new_password1 = serializer.validated_data.get('new_password1')
            user = User.objects.get(email=email)
            verification = Verification.objects.filter(user=user).last()
            print(verification)
            if code == verification.code:
                if new_password1 == new_password2:
                    verification.delete()
                    user.set_password(new_password1)
                    user.save()
                    return Response({"detail": "Parol muvaffaqiyatli almashtirildi"}, status=201)
                else:
                    return Response({"detail": "Ikkala parol mos kelmadi."}, status=400)

        return Response(serializer.errors, status=400)

class VerifyEmailView(ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated,]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            user.email = serializer.validated_data.get("email")
            user.save()
            verification = Verification.objects.create(user=user)
            verification.save()
            send_mail(
                "Tasdiqlash kodi",
                f'''Ushbu email sizning akkountingizga ulanish tasdiq kodi: {verification.code}''',
                settings.EMAIL_HOST_USER,
                [user.email,],
                fail_silently=False,
            )
            return Response({"detail":"Ushbu emailga tasdiqlash kodi yuborildi. "}, status=201)
        return Response(serializer.errors, status=400)


class PresentationsView(ModelViewSet):
    queryset = Presentations.objects.all()
    serializer_class = PresentationsSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class ProjectsView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class CommentsView(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = (AllowAny,)

    def get_queryset(self, project=None):
        if project is not None:
            return Comments.objects.filter(project=project)
        else:
            return Comments.objects.all().order_by("-date_created")


    def list(self, request):
        if request.query_params and request.query_params["project"]:
            project = Projects.objects.get(id=request.query_params["project"])
            queryset = self.get_queryset(project=project)
        else:
            queryset = self.get_queryset()
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)