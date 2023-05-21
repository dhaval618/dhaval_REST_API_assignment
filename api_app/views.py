from django.shortcuts import render
from rest_framework.views import APIView
from .serilizers import *
from rest_framework.response import Response

# Create your views here.
class CreateData(APIView):

    def post(self, request):
        d1 = request.data #request mein data JSON wala aaya hai
        ser_obj = SerializerMachine(data = d1)
        if ser_obj.is_valid():
            ser_obj.save() # iss line pe db mein row create ho rha hai

            #successfully create ke baad db mein all entries show karva rahe hai
            all_users = User.objects.all()
            s_obj = SerializerMachine(all_users, many = True)
            return Response(s_obj.data)
        else:
            return Response(ser_obj.errors)


class ReadData(APIView):

    def get(self, request, pk):
        u1 = User.objects.get(id = pk)
        ser_obj = SerializerMachine(u1)
        return Response(ser_obj.data)
    

class UpdateData(APIView):

    def put(self, request, pk):
        d1 = request.data
        u1 = User.objects.get(id = pk)
        ser_obj = SerializerMachine(u1, data=d1)
        if ser_obj.is_valid():
            ser_obj.save() # jo id di thi uss row pe data update ho gaya

            all_users = User.objects.all()
            s_obj = SerializerMachine(all_users, many = True)
            return Response(s_obj.data)
        else:
            return Response(ser_obj.errors)
        

class DeleteData(APIView):

    def delete(self, request, pk):
        u1 = User.objects.get(id = pk)
        u1.delete()

        all_users = User.objects.all()
        s_obj = SerializerMachine(all_users, many = True)
        return Response(s_obj.data)