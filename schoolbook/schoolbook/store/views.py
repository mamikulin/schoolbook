from django.shortcuts import render, redirect
from .models import book
from .forms import bookform
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q 


def index(request):
    
	search = request.GET.get('search')

	if search:
   		books = book.objects.filter(Q(author__icontains=search) | Q(name__icontains=search) | Q(owner__icontains=search)  |  Q(publisher__icontains=search))[::-1]

	else:
		books = book.objects.order_by('-id')
	return render(request, 'store/index.html', {'Title': 'Главная Страница сайта', 'Name': 0, 'books': books})
	
def user(request):
	books = book.objects.order_by('-id')
	name = request.GET.get("name")
	if name!=None:
		
		return render(request, 'store/index.html', {'Title': 'rb вск книги {}'.format(name), 'Name': name, 'books': books})
	else:
		search = request.GET.get('search')

		if search:
			books = book.objects.filter(Q(author__icontains=search) | Q(name__icontains=search) | Q(owner__icontains=search)  |  Q(publisher__icontains=search))
		else:
			books = book.objects.order_by('-id')
		return render(request, 'store/index.html', {'Title': 'Главная Страница сайта', 'Name': 0, 'books': books})

def goodcard(request):
	books = book.objects.order_by('-id')
	try:
		ids = request.GET.get("id")
		return render(request, 'store/goodcard.html', {'Title': 'rb товар номер: {}'.format(ids),'ID': int(ids), 'books': books})
	except:
		search = request.GET.get('search')

		if search:
			books = book.objects.filter(Q(author__icontains=search) | Q(name__icontains=search) | Q(owner__icontains=search)  |  Q(publisher__icontains=search))
		else:
			books = book.objects.order_by('-id')
		return render(request, 'store/index.html', {'Title': 'Главная Страница сайта', 'Name': 0, 'books': books})

def createanapplication(request):
    error = 'всё так'
    if request.method == 'POST':
        form = bookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store:home')
        else:
            error = 'что-то не так '

    form = bookform()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'store/createanapplication.html', context)

def delete(request, id):
	booktodel = book.objects.get(id=id)
	booktodel.delete()
	return redirect('store:home')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid(): 
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("store:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="store/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("store:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="store/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("store:home")


