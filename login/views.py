from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.expressions import RawSQL
from django.shortcuts import render, redirect
import pandas as pd
# Create your views here.
from login import forms, models


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        # return redirect('/index?page=1')
        return redirect('/index')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index')
                # return redirect('/index?page=1')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # return redirect('/index?page=1')
        return redirect('/index')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'index.html')


def show_customer(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    objects = models.Customer.objects.all()
    pages = Paginator(objects, 10)
    page_number = request.GET["page"]
    page = pages.get_page(page_number)
    print(page)
    return render(request, 'data/customer.html', {"data": page})


def show_order(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    objects = models.Order.objects.all()
    pages = Paginator(objects, 10)
    page_number = request.GET["page"]
    page = pages.get_page(page_number)
    print(page)
    return render(request, 'data/order.html', {"data": page})


def show_supplier(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    objects = models.Supplier.objects.all()
    pages = Paginator(objects, 10)
    page_number = request.GET["page"]
    page = pages.get_page(page_number)
    print(page)
    return render(request, 'data/supplier.html', {"data": page})


def get_order_data():
    order = models.Order.objects.all()
    data_order = pd.DataFrame(order.values_list(),
                            columns=['id', 'customer_id', 'order_name', 'Signed_time', 'cost', 'price', 'order_status'])
    print(data_order)
    return data_order


def get_supplier_data():
    supplier = models.Supplier.objects.all()
    data_supplier = pd.DataFrame(supplier.values_list(),
                                columns=['id', 'name', 'category', 'city', 'phone', 'time'])
    print(data_supplier)
    return data_supplier


def get_customer_data():
    customer = models.Customer.objects.all()
    data_customer = pd.DataFrame(customer.values_list(),
                                columns=['id', 'name', 'phone', 'email', 'sex', 'register_time', 'recent_time', 'credibility',
                                        'job', 'industry', 'place', 'company', 'value'])
    return data_customer


def show_line(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data_order = get_order_data()
    data = pd.to_datetime(data_order['Signed_time'])
    data['year'] = data.dt.year
    data_year = data['year'].value_counts().sort_index()
    index = data_year.index.tolist()
    data_year = data_year.values.tolist()
    return render(request, 'charts/line.html', {"index": index, "data_year": data_year})


def show_bar(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data_order = get_order_data()
    data = data_order['order_name'].value_counts()
    index = data.index.tolist()
    data = data.values.tolist()
    return render(request, 'charts/bar.html', {"index": index, "data": data})


def show_pie(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data_order = get_order_data()
    data = data_order['order_status'].value_counts()
    label = data.index.tolist()
    data = data.values.tolist()
    v1 = data[0]
    v2 = data[1]
    v3 = data[2]
    return render(request, 'charts/pie.html', {'v1': v1, 'v2': v2, 'v3': v3})


def show_scatter(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data_order = get_order_data()
    price = data_order['price'].values.tolist()
    cost = data_order['cost'].values.tolist()
    data = []
    for i in range(len(price)):
        data.append([price[i], cost[i]])
    return render(request, 'charts/scatter.html', {"data": data})


def show_radar(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data_supplier = get_supplier_data()
    data = data_supplier['category'].value_counts()
    label = data.index.tolist()
    data = data.values.tolist()
    print(label, data)
    return render(request, 'charts/radar.html', {'data': data})


def show_dashboard(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    data_customer = get_customer_data()
    data = data_customer['credibility'].value_counts()
    label = data.index.tolist()
    data = data.values.tolist()
    middle = data[0]*100/sum(data)
    low = data[1]*100/sum(data)
    high = data[2]*100/sum(data)
    return render(request, 'charts/dashboard.html', {'middle': middle, 'low': low, 'high': high})