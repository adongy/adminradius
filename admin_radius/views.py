from django.shortcuts import render, get_object_or_404, redirect
import datetime
from .models import RadUser, RadPass, RadStartDate, RadEndDate, Radacct
from .forms import RadUserForm, RadPassForm, RadStartDateForm, RadEndDateForm
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'admin_radius/home.html')

    
def user_list(request):
    users = RadUser.objects.select_related('start_date', 'end_date').all().order_by('username')

    query = request.GET.get('username')
    if query:
        users = users.filter(username__icontains=query)
        
    num_per_page = int(request.GET.get('num', 25))
    page = request.GET.get('page')
    paginator = Paginator(users, num_per_page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator(paginator.num_pages)
    
    return render(request, 'admin_radius/user_list.html', {
        'users': users,
        'today': datetime.datetime.now(),
    })
    

def user_delete(request, username):
    raduser = get_object_or_404(RadUser, username=username)
    raduser.delete()
    return redirect('admin_radius:home')

    
def user_detail(request, username=None):
    if username:
        raduser = get_object_or_404(RadUser, username=username)
        start_date = get_object_or_404(RadStartDate, username=username)
        end_date = get_object_or_404(RadEndDate, username=username)
        try:
            password = RadPass.objects.get(username=username)
        except RadPass.DoesNotExist:
            password = RadPass()
    else:
        raduser = RadUser()
        password = RadPass()
        start_date = RadStartDate()
        end_date = RadEndDate()

    if request.method == 'POST':
        user_form = RadUserForm(request.POST, instance=raduser, prefix="user")
        pass_form = RadPassForm(request.POST, instance=password, prefix="password")
        start_date_form = RadStartDateForm(request.POST, instance=start_date, prefix="start")
        end_date_form = RadEndDateForm(request.POST, instance=end_date, prefix="end")
        
        if user_form.is_valid() and pass_form.is_valid() and start_date_form.is_valid() and end_date_form.is_valid():
            if not username:
                username = user_form.cleaned_data['username']
            raduser = user_form.save(commit=False)
            if pass_form.cleaned_data['value']:
                password = pass_form.save(commit=False)
                password.username = username
                password.save()
                raduser.password = password
            start_date = start_date_form.save(commit=False)
            start_date.username = username
            start_date.save()
            end_date = end_date_form.save(commit=False)
            end_date.username = username
            end_date.save()
            raduser.start_date = start_date
            raduser.end_date = end_date
            raduser.save()
            redirect(raduser)
    else:
        user_form = RadUserForm(instance=raduser, prefix="user")
        pass_form = RadPassForm(instance=password, prefix="password")
        start_date_form = RadStartDateForm(instance=start_date, prefix="start")
        end_date_form = RadEndDateForm(instance=end_date, prefix="end")

    return render(request, 'admin_radius/user_edit.html', {
        'username': username,
        'user_form': user_form,
        'pass_form': pass_form,
        'start_date_form': start_date_form,
        'end_date_form': end_date_form,
    })
    
    
def acct_detail(request, username=None, format=None):

    if username:
        raduser = get_object_or_404(RadUser, username=username)
        objects = Radacct.objects.filter(username=username)
    else:
        raduser = None
        objects = Radacct.objects.all()
        
    format = format if format else 'month'
    today = datetime.date.today()
    
    if format == 'month':
        format_date = datetime.date(today.year, today.month, 1)
    elif format == 'week':
        # This week's Monday
        format_date = today - datetime.timedelta(days=today.weekday())
    elif format == 'today':
        format_date = today
    elif format == 'all':
        # Smallest date possible to get everything
        format_date = datetime.date(datetime.MINYEAR, 1, 1)
        
    sessions = objects.filter(acctstarttime__gt=format_date).order_by('-acctstarttime')
    # TODO: Be able to sort for different columns
    traffics = sessions.values('username').annotate(download=Sum('acctinputoctets'), upload=Sum('acctoutputoctets')).order_by('username')
    
    num_per_page = int(request.GET.get('num', 25))
    
    page_traffic = request.GET.get('page_traffic')
    page_session = request.GET.get('page_session')
    paginator_traffic = Paginator(traffics, num_per_page)
    paginator_session = Paginator(sessions, num_per_page)
    try:
        traffics_paged = paginator_traffic.page(page_traffic)
    except PageNotAnInteger:
        traffics_paged = paginator_traffic.page(1)
    except EmptyPage:
        traffics_paged = paginator_traffic(paginator_traffic.num_pages)
    try:
        sessions_paged = paginator_session.page(page_session)
    except PageNotAnInteger:
        sessions_paged = paginator_session.page(1)
    except EmptyPage:
        sessions_paged = paginator_session(paginator_session.num_pages)
    
    return render(request, 'admin_radius/acct.html', {
        'raduser': raduser,
        'sessions': sessions_paged,
        'traffics': traffics_paged,
    })