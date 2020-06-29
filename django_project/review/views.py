from django.shortcuts import get_object_or_404,render
from .models import Post, Course
from .forms import ReviewForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
def front_page(request):
	return render(request, 'review/front_page.html', {'title': 'Kelasku'})

def home(request):
	context = {
		'posts': Post.objects.order_by('-date_posted')
	}
	return render(request, 'review/home.html', context)

def about(request):
	return render(request, 'review/about.html', {'title': 'About'})

def courses(request):
	course_list = Course.objects.order_by('-name')

	context = {
	'course_list':course_list
	}
	return render(request, 'review/courses.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = ReviewForm()
    return render(request, 'review/course_detail.html', {'course': course, 'form': form})

@login_required
def add_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        content = form.cleaned_data['content']
        title = form.cleaned_data['title']
        author = request.user

        post = Post()
        post.title = title
        post.author = author
        post.course = course
        post.content = content
        post.rating = rating
        post.date_posted = datetime.datetime.now()
        post.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('course_detail', args=(course.id,)))

    return render(request, 'review/course_detail.html', {'course': course, 'form': form})

def campus_weather(request):
	return render(request, 'review/campus_weather.html', {'title': 'Weather'})