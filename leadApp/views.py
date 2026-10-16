from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from leadApp.models import Lead
from leadApp.serializers import LeadSerializer
from rest_framework import authentication,permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
         DjangoFilterBackend,
         SearchFilter,
         OrderingFilter
    ]
    filter_setfields=['status','sourse']
    search_fields=['name','email','status','sourse']
    ordering_fields=['name','added_date']

class LeadRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
     authentication_classes=[authentication.BasicAuthentication]
     permission_classes=[permissions.IsAuthenticated]
     serializer_class=LeadSerializer
     queryset=Lead.objects.all()
     lookup_url_kwarg="id"


# class StatusLevelLeadView(ListAPIView):
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     serializer_class=LeadSerializer
#     def get(self,request,*args,**kwargs):
#         new_leads=Lead.objects.filter(status="new")
#         contacted_lead=Lead.objects.filter(status="contacted")
#         converted_lead=Lead.objects.filter(status="converted")
#         lost_lead=Lead.objects.filter(status="lost")
#         new_lead_ser=LeadSerializer(new_leads,many=True)
#         contacted_ser=LeadSerializer(contacted_lead,many=True)


#         result={
#             "new_leads":new_leads,
#             "contacted_leads":contacted_lead,
#             "converted_leads":converted_lead,
#             "lost_lead":lost_lead
#         }
#         return Response(result)