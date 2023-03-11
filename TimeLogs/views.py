from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from  rest_framework.response import Response
from .models import TimeLogs
from .serializers import TimelogSerializer

# Create your views here.

@api_view()
def timelog_list(request):
    queryset = TimeLogs.objects.all()
    serializer = TimelogSerializer(queryset, many=True)

    return Response(serializer.data)   