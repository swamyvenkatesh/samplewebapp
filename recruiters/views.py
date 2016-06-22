from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Applicants
from django.db.models import Q
import csv
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def getData(query):

    candidate_list = Applicants.objects.filter(Q(experience__icontains=query) | Q(current_location__icontains=query) | Q(skills__icontains=query))

    all_details = candidate_list
    print type(candidate_list)
    for c in candidate_list:
        print c.experience
        print c.current_location
        print c.skills


    return all_details

def search(request):
    '''Seadrch View'''
    form = Searchform()
    query = ""
    print "search view"
    
    all_details = []   
    if request.method == 'GET':        
        query = request.GET.get('q') 
        data = getData(query) 
        print "lllllllllllllllllll"
        print data
        print "lllllllllllllllllll"
        request.session['some'] = query        
        return render(request, 'index.html', {"form":form, 'details':data})
    else:
        form = Searchform()
    return render(request, 'index.html', {"form":form})



def download(request):
    query  = request.session.get('some')
    print "((((((((((((("
    print query 
    data = getData(query) 
    
    response = HttpResponse(content_type='text/csv')
    response['data'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['Location', 'experience'])
    for i in data:
        writer.writerow([i.current_location, i.experience])
    return response
