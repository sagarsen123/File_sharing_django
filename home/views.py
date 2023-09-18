from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser
from django.template import Context
def home(request):
    return render(request, 'home.html')


def download(request, uid):

    return render(request, 'download.html', context = {"uid" : uid})

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data = data)

            if serializer.is_valid():
                serializer.save()
                print("serializer", serializer.data)
                return Response({
                    'status' : 200,
                    'message' : 'files Uploaded Successfully',
                    'data' : serializer.data
                })
            return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : serializer.errors
            })
        except Exception as e:
            # print(e)
            return Response({
                'status' : 404,
                'message' : e,
            })