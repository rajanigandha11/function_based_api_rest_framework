from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.serializer import serializers

@api_view(['GET','PUT','POST','DELETE'])
def student_app(request):
	if request.method == 'GET':
		id=request.data.get('id')
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu=Student.objects.all()
		serializer = StudentSerializer(stu,many=True)
		return Response(serializer.data)

	if request.method =='POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'data created'})
		return Response(serializers.errors)

	if request.method =='PUT':
		id=request.data.get('id')
		stu=Student.objects.get(pk=id)
		serializer=StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'data updated'})
		return Response(serializers.errors)

	if request.method =='DELETE':
		id = request.data.get('id')
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response({"msg":'deleted successfully'})




