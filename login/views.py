
from .models import Event
from .models import Schedule
from django.shortcuts import get_object_or_404, render
from .models import Tip, Review
from django.contrib.auth.decorators import login_required
import os, json
from django.core.exceptions import ImproperlyConfigured
from django.views.decorators.http import require_POST
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def kuniv(request):
    return render(request, 'kuniv.html')
    
def detail(request, id):
    event = Event.objects.get(event_id=id)
    return render(request, 'detail.html', {'event':event})

def main(request):
    schedule = Schedule.objects.all().order_by('-id')
    return render(request, 'main.html', {'schedule_show':schedule})

def suniv(request):
    tips=Tip.objects
    reviews=Review.objects
    return render(request, 'suniv.html', {'tips' : tips, 'reviews': reviews})

def detail_tip(request, tip_id):
    tip_detail=get_object_or_404(Tip, pk=tip_id)
    return render(request, 'detail_tip.html', {'tip' : tip_detail})

def detail_review(request, review_id):
    review_detail=get_object_or_404(Review, pk=review_id)
    return render(request, 'detail_review.html', {'review' : review_detail})

@login_required
@require_POST
def tip_like(request):
    user = request.user
    
    pk = request.POST.get('pk', None)
    tip = get_object_or_404(Tip, pk=pk)

    if tip.like_user_set.filter(id=user.id).exists():
        tip.like_user_set.remove(user)
        message = "좋아요 취소"
    else:
        tip.like_user_set.add(user)
        message = "좋아요"
    context = {
        'like_count': tip.like_count,
        'message': message
    }
    return HttpResponse(json.dumps(context), content_type="application/json")