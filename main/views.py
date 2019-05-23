from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from scraper.scraper import scrape
import random

class main_view(APIView):
    
    def get(self, request, format=None):
        type_no=random.choice([1, 2, 3, 4])
        type_question = 'school'
        if(type_no==2):
            type_question = 'easy'
        if(type_no==3):
            type_question = 'medium'
        if(type_no==4):
            type_question = 'hard'
        data=scrape(type_question)
        print(data)
        try:
            return Response({"success": True, "data":data}, status=status.HTTP_200_OK)
        except:
            return Response({"success": False, "message": "No Photos Available"}, status=status.HTTP_400_BAD_REQUEST)