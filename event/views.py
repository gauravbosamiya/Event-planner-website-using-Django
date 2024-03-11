import os
import uuid
# import segno
from django.shortcuts import render, redirect
from .models import User, EventCategory, Event, EventMember, Contact, Suggestion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreateForm


# Create your views here.

def login_page(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin-home')
            else:
                if not user.is_staff and user.type == 'participant':
                    login(request, user)
                    return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    context = {'page': page}
    return render(request, 'login_register.html', context)


def register_page(request):
    page = 'register'
    form = CustomUserCreateForm()

    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            form = CustomUserCreateForm()

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def home_page(request):
    users = User.objects.filter(heckathon_participant=True)
    org = User.objects.filter(type='organizers')
    events = Event.objects.all()
    category = EventCategory.objects.all()
    context = {'users': users, 'events': events, 'category': category, 'org': org}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def event_category(request):
    category = EventCategory.objects.all()
    context = {'category': category}
    return render(request, 'event_category.html', context)


def category_wise_events_list(request, pk):
    if EventCategory.objects.filter(id=pk):
        event_list = Event.objects.filter(category=pk)
    context = {'event_list': event_list}
    return render(request, 'category_wise_event_list.html', context)


# def user_profile(request, pk):
#     user = User.objects.get(id=pk)
#     context = {'user': user}
#     return render(request, 'profile.html', context)


@login_required(login_url='login/')
def account_page(request):
    user = request.user
    context = {'user': user}
    return render(request, 'account.html', context)


def event_page(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)
        registered = request.user.events.filter(id=event.id).exists()
        context = {'event': event, 'registered': registered}
    else:
        return redirect('login')
    return render(request, 'event.html', context)


@login_required(login_url='login/')
def event_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        user = event.participants.add(request.user)
        eventmembers = EventMember(event=event, user=request.user)
        eventmembers.save()
        return redirect('event', pk=event.id)

    context = {'event': event}
    return render(request, 'event_confirmation.html', context)


@login_required(login_url='login/')
def generate_ticket(request, pk):
    event = Event.objects.get(id=pk)
    ticket_number = str(uuid.uuid4().int)[:6]

    try:
        qr = segno.make_qr(event.name)
        qr_path = os.path.join('event_images/', f'{request.user.username}.png')
        qr.save(qr_path)
    except Exception as e:
        print(f"Error saving QR code image: {e}")
        qr_path = None

    context = {'event': event,
               'ticket_number': ticket_number,
               'qr_path': qr_path,
               'participant': request.user}
    return render(request, 'ticket.html', context)


def upcoming_event(request):
    active_event = Event.objects.filter(status='active')
    context = {'active_event': active_event}
    return render(request, 'upcoming_past_event.html', context)


def past_event(request):
    active_event = Event.objects.filter(status='completed')
    context = {'active_event': active_event}
    return render(request, 'upcoming_past_event.html', context)


def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        try:
            if user.is_staff:
                login(request, user)
                return redirect('admin-home')
            else:
                messages.error(request, 'You Are Not Admin Brother!')
        except:
            pass
    return render(request, 'admin/admin_login.html')


@login_required(login_url='login/')
def admin_home(request):
    users = User.objects.filter(heckathon_participant=True)
    org = User.objects.filter(type='organizers')
    events = Event.objects.all()
    category = EventCategory.objects.all()
    context = {'users': users, 'events': events, 'category': category, 'org': org}
    return render(request, 'admin/admin_home.html', context)


def admin_logout(request):
    logout(request)
    return redirect('login')


def all_events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'admin/all_events.html', context)


def delete_event(request, pk):
    event_delete = Event.object.get(id=pk)
    event_delete.delete()
    return redirect('all-event')


def update_event(request, pk):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    data = Event.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('event_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')
        scheduled_status = request.POST.get('scheduled_status')
        venue = request.POST.get('venue')
        status = request.POST.get('status')

        data.name = name
        data.start_date = start_date
        data.end_date = end_date
        data.description = description
        data.scheduled_status = scheduled_status
        data.venue = venue
        data.status = status
        data.save()
        messages.success(request, 'Event Details Updated')
        return redirect('all-events')
    context = {'data': data}

    return render(request, 'admin/update_event.html', context)


def add_event(request):

    return render(request, 'admin/add-event.html')


def add_event_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        img = request.POST['img']
        created_user = request.user
        updated_user = request.user
        status = request.POST.get('status')

        event_category = EventCategory(name=name, image=img, created_user=created_user, updated_user=updated_user,
                                       status=status)
        event_category.save()
    context = {}
    return render(request, 'admin/add_event_category.html', context)


def admin_upcoming_event(request):
    events = Event.objects.filter(status='active')
    context = {'events': events}
    return render(request, 'admin/upcoming_event.html', context)


def delete_upcoming_event(request, pk):
    events = Event.objects.get(id=pk)
    events.delete()
    return redirect('delete-upcoming-event')


def admin_past_event(request):
    events = Event.objects.filter(status='completed')
    context = {'events': events}
    return render(request, 'admin/past_event.html', context)


def delete_past_event(request, pk):
    events = Event.objects.get(id=pk)
    events.delete()
    return redirect('delete-past-event')


def all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin/admin_home.html', context)


def delete_user(request, pk):
    delete_user = User.objects.get(id=pk)
    delete_user.delete()


def contact_page(request):
    if request.method == 'POST':
        # name = request.user.name
        # email = request.user
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(email=request.user, subject=subject, message=message)
        data.save()
        return redirect('home')
    return render(request, 'contact.html')


def event_suggestion(request, event_id):
    if request.method == "POST":
        suggest = request.POST.get('suggest')
        event = Event.objects.get(id=event_id)
        suggestion = Suggestion(event=event, suggestion=suggest)
        suggestion.save()
        return redirect('event', pk=event_id)
    else:
        return redirect('home')


def new_index(request):
    return render(request, 'new_index.html')
