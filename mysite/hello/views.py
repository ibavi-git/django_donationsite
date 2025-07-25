from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import DonationForm, SignUpForm
from .models import DonorProfile, Donation

from django.utils.timezone import now

from django.db.models import Sum


def index(request):
    return render(request, 'hello/index.html')

def about(request):
    return render(request, 'hello/about.html')

def service(request):
    return render(request, 'hello/service.html')

def donation_success(request):
    return render(request, 'hello/donation_success.html')

def privacy(request):
    return render(request, 'hello/privacy.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if DonorProfile.objects.filter(email=email).exists():
            return render(request, 'hello/signup.html', {'error': 'Email already exists'})

        user = DonorProfile(name=name, email=email, password=password)
        user.save()

        return redirect('login')  # 🚀 redirect after signup
    return render(request, 'hello/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = DonorProfile.objects.get(email=email, password=password)
            request.session['user_id'] = user.id  # simple login system
            return redirect('donate')  # 🚀 redirect after login
        except DonorProfile.DoesNotExist:
            return render(request, 'hello/login.html', {'error': 'Invalid credentials'})

    return render(request, 'hello/login.html')


def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user  # Store the logged-in user
            donation.save()
            return render(request, 'hello/donation_success.html', {'donation': donation})
    else:
        form = DonationForm()
    return render(request, 'hello/donate.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'hello/signup.html', {"form": form})
    


def donation_dashboard(request):
    donations = Donation.objects.all().order_by('-date')
    
    # Total donation amount
    total_amount = donations.aggregate(Sum('amount'))['amount__sum'] or 0

    # Total number of unique donors (based on name or user)
    donor_count = donations.values('name').distinct().count()

    # Donations made this month
    today = now()
    this_month_donations = donations.filter(date__month=today.month, date__year=today.year)
    this_month_amount = this_month_donations.aggregate(Sum('amount'))['amount__sum'] or 0

    # Largest donation
    largest_donation = donations.order_by('-amount').first()

    context = {
        'donations': donations,
        'total_amount': total_amount,
        'donor_count': donor_count,
        'this_month_amount': this_month_amount,
        'largest_donation': largest_donation or {'amount': 0}
    }
    return render(request, 'hello/donation_dashboard.html', context)


def donation_success(request):
    # Fetch latest donation made by the current user
    latest_donation = Donation.objects.filter(user=request.user).order_by('-date').first()

    return render(request, 'hello/donation_success.html', {
        'donation': latest_donation
    })