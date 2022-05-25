from rest_framework import serializers
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import *
from django.conf import settings

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto_lavhalar
        fields = "__all__"

        
class BoshqarmaSerializer(serializers.ModelSerializer):
    youtube_videos = serializers.ListField(child=serializers.CharField(max_length=150))
    params = serializers.ListField(child=serializers.FloatField())
    class Meta:
        model = Boshqarma
        fields = '__all__'
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = "__all__"

class HujjatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hujjatlar
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class RahbariyatSerializer(serializers.ModelSerializer):
    # spec = SpecialitySerializer(required=False)
    # boshqarma = BoshqarmaSerializer(required=False)

    class Meta:
        model = Rahbariyat
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    # boshqarma = BoshqarmaSerializer(required=False)
    class Meta:
        model = News
        fields = "__all__"

class MurojaatSerializer(serializers.ModelSerializer):
    # boshqarma = BoshqarmaSerializer(required=False)
    class Meta:
        model = Murojaat
        fields = "__all__"

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def save(self, attrs):
        print("email: ", attrs.validated_data.get("email"))
        try:
            user = User.objects.get(email=attrs.validated_data.get("email"))
            verification, created = Verification.objects.get_or_create(user=user)
            verification.save()
            send_mail(
                "Tasdiqlash kodi",
                f'''
                    Assalomu alaykum, kimdir sizning nomingizdan parolni qayta tiklash so'rovini jo'natdi.
                    Agar bu siz bo'lmasangiz, bu xabarni e'tiborsiz qoldiring.
                    Sizning tasdiqlash kodingiz: {verification.code} .
                    Bu kodni hech kimga bermang.
                ''',
                settings.EMAIL_HOST_USER,
                [attrs.validated_data.get("email"),],
                fail_silently=False
            )
        except Exception as e:
            raise e


class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()
    extra_kwargs = {
        'new_password1':{'write_only':True},
        'new_password2':{'write_only':True}
    }
    # def validate(self, attrs):
    #     try:
    #         print("attrs: ", attrs)
    #         email = attrs["email"]
    #         code = attrs["code"]
    #         user = User.objects.get(email=email)
    #         verification = Verification.objects.filter(user=user).last()
    #         # print(verification["code"],  "   ", verification.code)
    #         if code == verification.code:
    #             verification.delete()
    #             return True
    #         return False
    #     except Exception as e:
    #         raise e

    def save(self, attrs):
        try:
            print("attrs: ", attrs)
            email = attrs["email"]
            code = attrs["code"]
            print(email)

            user = User.objects.get(email=email)
            verification = Verification.objects.filter(user=user).last()
            print(verification)
            if code == verification.code:
                verification.delete()
                new_password = attrs["new_password1"]
                email = attrs["email"]

                # user = User.objects.get(email='aahmadov271101@gmail.com')
                user.set_password(new_password)
                user.save()
                return user
            return False
        except Exception as e:
            raise e


class PresentationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentations
        fields = "__all__"

        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

        extra_kwargs = {
            "date_created":{"read_only":True}
        }