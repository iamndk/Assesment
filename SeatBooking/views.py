from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .form1 import SignUpForm
# Create your views here.

def index(request):
    return render(request,"index.html")

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or any other page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Movie, Showtime, Booking
from .form1 import BookingForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'booking/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    showtimes = Showtime.objects.filter(movie=movie)
    return render(request, 'booking/movie_detail.html', {'movie': movie, 'showtimes': showtimes})

@login_required
def book_ticket(request, pk):
    showtime = get_object_or_404(Showtime, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.showtime = showtime
            booking.save()
            showtime.seats_available -= booking.seats_booked
            showtime.save()
            return redirect('movie_list')
    else:
        form = BookingForm()
    return render(request, 'booking/book_ticket.html', {'form': form, 'showtime': showtime})
