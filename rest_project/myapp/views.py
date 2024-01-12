from django.shortcuts import render
from . models import employee
from . serializers import EmployeeSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
@csrf_exempt
def employeelistView(request):
    if request.method == 'GET':
        employees = employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        # return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data)
    elif request.method=="POST":
         jsonData=JSONParser().parse(request)
         serializer=EmployeeSerializer(data=jsonData)
         if serializer.is_valid():
             serializer.save()
        
            #  return JsonResponse(serializer.data,safe=False)
             return Response(serializer.data)
             
         else:
            
            #  return JsonResponse(serializer.errors,safe=False)
            return Response(serializer.errors)
         
@api_view(['DELETE','GET','PUT'])
def employeeDetailView(request,pk):
    try:
        
      employee_o=employee.objects.get(pk=pk)
      # return JsonResponse("Employee "+str(pk), safe=False) 
      # print(employee) 
    except employee.DoesNotExist:
        return Response(status=404)
      #   return HttpResponse(status=404)

      

    if request.method=="DELETE":
        employee_o.delete()
        print('Data Deleted Successfully')
        return Response(status.HTTP_204_NO_CONTENT)
      #   return JsonResponse(status.HTTP_204_NO_CONTENT,safe=False)
    elif request.method=="GET":
        serializer=EmployeeSerializer(employee_o)
        return Response(serializer.data) 
      #   return JsonResponse(serializer.data, safe=False) 
    elif request.method=="PUT":
         # jsonData=JSONParser().parse(request)
         serializer=EmployeeSerializer(employee_o,data=request.data)
         if serializer.is_valid():
             serializer.save()
         # print(jsonData)
             return Response(serializer.data)
            #  return JsonResponse(serializer.data,safe=False)
         else:
             return Response(serializer.errors)
            #  return JsonResponse(serializer.errors,safe=False)
    
        
            
        
        
      
      

     


    

        

    
        

