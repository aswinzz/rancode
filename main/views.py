from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from scraper.scraper import scrape
import random
from .models import Problem

class main_view(APIView):
    
    def get(self, request, format=None):
        type_no=random.choice([1, 2, 3, 4])
        type_question = 'beginner'
        if(type_no==2):
            type_question = 'easy'
        if(type_no==3):
            type_question = 'medium'
        if(type_no==4):
            type_question = 'hard'
        data=Problem.objects.filter(question_type=type_question)
        total=len(data)
        index=random.randint(0,total)
        print(data[index])
        item=data[index]
        problem={}
        problem['code']=item.code
        problem['name']=item.name
        problem['submissions']=item.submissions
        problem['accuracy']=item.accuracy
        problem['status']=item.status
        problem['submit_url']=item.submit_url
        problem['url']=item.url
        problem['type']=item.question_type
        try:
            return Response({"success": True, "data":problem}, status=status.HTTP_200_OK)
        except:
            return Response({"success": False, "message": "No Problem Available"}, status=status.HTTP_400_BAD_REQUEST)

class scrape_view(APIView):
    
    def get(self, request, format=None):
        problems=[]
        type_question = 'school'
        data=scrape(type_question)
        for i in data:
            problems.append(i)
            if not Problem.objects.filter(code=i['code']).exists():
                problem = Problem.objects.create(code=i['code'],name=i['name'], question_type=i['type'], url=i['url'], submissions=i['submissions'],accuracy=i['accuracy'],submit_url=i['submit_url'],status=i['status'])
                problem.save()
        type_question = 'easy'
        data=scrape(type_question)
        for i in data:
            problems.append(i)
            if not Problem.objects.filter(code=i['code']).exists():
                problem = Problem.objects.create(code=i['code'],name=i['name'], question_type=i['type'], url=i['url'], submissions=i['submissions'],accuracy=i['accuracy'],submit_url=i['submit_url'],status=i['status'])
                problem.save()
        type_question = 'medium'
        data=scrape(type_question)
        for i in data:
            problems.append(i)
            if not Problem.objects.filter(code=i['code']).exists():
                problem = Problem.objects.create(code=i['code'],name=i['name'], question_type=i['type'], url=i['url'], submissions=i['submissions'],accuracy=i['accuracy'],submit_url=i['submit_url'],status=i['status'])
                problem.save()
        type_question = 'hard'
        data=scrape(type_question)
        for i in data:
            problems.append(i)
            if not Problem.objects.filter(code=i['code']).exists():
                problem = Problem.objects.create(code=i['code'],name=i['name'], question_type=i['type'], url=i['url'], submissions=i['submissions'],accuracy=i['accuracy'],submit_url=i['submit_url'],status=i['status'])
                problem.save()
        try:
            return Response({"success": True, "data":problems}, status=status.HTTP_200_OK)
        except:
            return Response({"success": False, "message": "No Problems Available"}, status=status.HTTP_400_BAD_REQUEST)