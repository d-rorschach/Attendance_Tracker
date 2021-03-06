from django.shortcuts import render
from .models import subject,attend
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
# Create your views here.

def home(rq):
    print('***********************')
    print(rq.user.id)
    print(len( subject.objects.filter(user=rq.user)))

    param={'sub': subject.objects.filter(user=rq.user)}
    return render(rq,'tracker/home.html', param)


def input(rq):
    return render(rq,'tracker/input.html')


def calender(rq):
    param={
        'sun': subject.objects.filter(sunday=True, user=rq.user),
        'mon': subject.objects.filter(monday=True, user=rq.user),
        'tue': subject.objects.filter(tuesday=True, user=rq.user),
        'wed': subject.objects.filter(wednesday=True, user=rq.user),
        'thu': subject.objects.filter(thursday=True, user=rq.user),
        'fri': subject.objects.filter(friday=True, user=rq.user),
        'sat': subject.objects.filter(saturday=True, user=rq.user),
        'sunlen': len(subject.objects.filter(sunday=True, user=rq.user)),
        'monlen': len(subject.objects.filter(monday=True, user=rq.user)),
        'tuelen': len(subject.objects.filter(tuesday=True, user=rq.user)),
        'wedlen': len(subject.objects.filter(wednesday=True, user=rq.user)),
        'thulen': len(subject.objects.filter(thursday=True, user=rq.user)),
        'frilen': len(subject.objects.filter(friday=True, user=rq.user)),
        'satlen': len(subject.objects.filter(saturday=True, user=rq.user)),
    }
    return render(rq,'tracker/calender.html',param)


def stats(rq):
    param={'sub': subject.objects.filter(user=rq.user)}
    return render(rq,'tracker/stats.html', param)

def new_schedule(rq):
    print('**************start*********************')
    #sub = subject.objects.filter(user=rq.user)
    #sub.delete()
    
    n=int(rq.POST['no_of_sub'])

    for i in range(n):
        x= subject(sub_name=rq.POST['sub'+str(i+1)],
        prof=rq.POST['prof'+str(i+1)],
        sunday=rq.POST.get('sub'+str(i+1)+'day'+str(0),False),
        monday=rq.POST.get('sub'+str(i+1)+'day'+str(1),False),
        tuesday=rq.POST.get('sub'+str(i+1)+'day'+str(2),False),
        wednesday=rq.POST.get('sub'+str(i+1)+'day'+str(3),False),
        thursday=rq.POST.get('sub'+str(i+1)+'day'+str(4),False),
        friday=rq.POST.get('sub'+str(i+1)+'day'+str(5),False),
        saturday=rq.POST.get('sub'+str(i+1)+'day'+str(6),False),
        user=rq.user)
        
        x.save()

    
    print('*******************done*****************')

    param={'sub': subject.objects.filter(user=rq.user)}
    return HttpResponseRedirect('/tracker',param)

        
def store_attendance(rq):
    n=int(rq.POST['no_of_sub'])
    print('*************************************')
    
    newdate = rq.POST['date']
    #newdate = datetime.strptime(rq.POST['date'],'%Y-%m-%d').date()
    #newdate=strptime(rq.POST['date'],YYYY-MM-DD)
    a=attend(date=newdate, user=rq.user)
    a.save()
    print(newdate)
    for i in range(n):
        if rq.POST['attend'+str(i)]==True:
            subject_name=rq.POST['subject'+str(i)]
            o=subject.objects.get(sub_name=subject_name)
            a.listed_subjects.add(o)


    param={'sub': subject.objects.all()}
    return HttpResponseRedirect('/tracker',param)


