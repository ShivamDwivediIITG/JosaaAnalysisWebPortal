from django.shortcuts import render
from .models import rec
from django.db.models import Count,Min


# Create your views here.
# from django.http import JsonResponse

from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chartjs/index.html')
class iitview(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chartjs/iit.html')
class branchview(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chartjs/branch.html')


class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format = None):
		
		queryset = rec.objects.values('institute').annotate(count=Count('*')).order_by('-count')

		labels = [record['institute'] for record in queryset]
		chartLabel = "IIT SEAT INTAKE"
		chartdata = [record['count'] for record in queryset]

		
		data ={
					"labels":labels,
					"chartLabel":chartLabel,
					"chartdata":chartdata,
			}
		return Response(data)

class Alpha(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format = None):
		
		queryset = rec.objects.filter(year__gte=2018).values('gender').annotate(count=Count('*'))

		labels = [record['gender'] for record in queryset]
		chartLabel = "GENDER WISE INTAKE"
		chartdata = [record['count'] for record in queryset]
		
		data ={
					"labels":labels,
					"chartLabel":chartLabel,
					"chartdata":chartdata,
			}
		return Response(data)

class Bar(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format = None):
		
		queryset = rec.objects.filter(year=2022).values('academic').annotate(count=Count('*')).order_by('-count')[:5]

		labels = [record['academic'] for record in queryset]
		chartdata = [record['count'] for record in queryset]
		chartLabel = "Branch wise seat intake"

		
		data ={
					"labels":labels,
					"chartLabel":chartLabel,
					"chartdata":chartdata,
			}
		return Response(data)
	
class LineData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format = None):
		
		from django.db.models import Min

		queryset = (rec.objects.filter(seattype='OPEN', year=2022).values('academic', 'institute').annotate(min_openingrank=Min('openingrank')).order_by('min_openingrank'))[:10]
		labels = [record['academic'] + ' - ' + record['institute'] for record in queryset]
		chartdata = [record['min_openingrank'] for record in queryset]
		chartLabel = "Opening Rank"

		
		data ={
					"labels":labels,
					"chartLabel":chartLabel,
					"chartdata":chartdata,
			}
		return Response(data)
	
class LineData2(APIView):
            authentication_classes = []
            permission_classes = []
        
            def get(self, request, format = None):
                
                    queryset1 = rec.objects.filter(
                    institute='Indian Institute of Technology Bhubaneswar',
                    academic='Civil Engineering (4 Years, Bachelor of Technology)',
                    quota='AI',
                    seattype='OPEN',
                    gender='Gender-Neutral',
                    year='2022'
                    ).values_list('round', flat=True)
               
                    queryset2 = rec.objects.filter(
                    institute='Indian Institute of Technology Bhubaneswar',
                    academic='Civil Engineering (4 Years, Bachelor of Technology)',
                    quota='AI',
                    seattype='OPEN',
                    gender='Gender-Neutral',
                    year='2022'
                    ).values_list('closingrank', flat=True)
                    
                    
                    labels =list(queryset1)
                    chartdata =list(queryset2)
        
                    chartLabel = "Round vs closing rank"
        
                
                    data ={
                            "labels":labels,
                            "chartLabel":chartLabel,
                            "chartdata":chartdata,
                    }
                    return Response(data)
        


	####################################################

## if you don't want to user rest_framework

# def get_data(request, *args, **kwargs):
#
# data ={
#			 "sales" : 100,
#			 "person": 10000,
#	 }
#                
# return JsonResponse(data) # http response


#######################################################

## using rest_framework classes
