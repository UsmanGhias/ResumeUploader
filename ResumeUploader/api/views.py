from rest_framework.response import Response
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status


class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializer.save()
            return response({'msg' : 'Profile created Successfully', 'status' : 'success', 'candidate' :'serializer.data' },status=status.HTTP_201_CREATED)
        return response(serializer.error)


def get(self, request, format=None):
    candidate = Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return response({'candidate' : serializer.data, 'status' : 'success'},  status=status.HTTP_200_OK)
    return response(serializer.data)
