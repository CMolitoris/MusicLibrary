from django.http import response
from django.http.response import Http404
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

class SongList(APIView):
    def get(self,request):
        song = Song.objects.all()
        serializer =  SongSerializer(song,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     

class SongDetail(APIView):
    def get_object(self,pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song,data=request.data)                       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object(pk)  
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    def patch(self, request, pk, field, updated_info=None ):
        song = self.get_object(pk)
        if field=='likes':
            updated_info=song.likes +1
        # if field=='dislikes':
        #     if song.dislikes==0:
        #         serializer = SongSerializer(song)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     updated_info=song.dislikes -1    
        data = {field: updated_info}
        serializer = SongSerializer(song, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    # def like(self,request,pk):
    #     song = SongDetail.get_object(pk)
    #     data = song.likes + 1
    #     SongDetail.patch(request,pk,"likes",data)

