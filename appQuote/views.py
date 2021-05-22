from django.shortcuts import render, redirect
from django.contrib import messages
from appLogin.models import *
from .models import *

def index(request):
    context = {
        'user' : User.objects.get(id=request.session['userid']),
        'quotes' : Quote.objects.all()
    }
    return render(request, "appQuote/index.html", context)

def addQuote(request):
    errors = Quote.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/appQuote')
    else:
        sessionUser=User.objects.get(id=request.session['userid'])
        Quote.objects.create(content=request.POST['quote'], author=request.POST['author'], user=sessionUser)
        return redirect('/appQuote')

def userQuotes(request, user_id):
    choosenUser = User.objects.get(id=user_id)
    context={
        'user' : User.objects.get(id=request.session['userid']),
        'selectUser':choosenUser,
        'usersQuotes':Quote.objects.filter(user=choosenUser)
        # 'usersQuotes':Quote.objects.all()
    }
    return render(request, "appQuote/userQuotes.html", context)

def myAccount(request, user_id):
    updateUser = User.objects.get(id=user_id)
    if request.method == 'GET':
        context={
            'user':updateUser
        }
        return render(request, "appQuote/editAccount.html", context)
    else:
        errors = User.objects.update_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/appQuote/myaccount/{user_id}')
        else:
            updateUser.fname=request.POST['fname']
            updateUser.lname=request.POST['lname']
            updateUser.email=request.POST['email']
            updateUser.save()
            return redirect ('/appQuote')

def like(request, quote_id):
    likeUser = User.objects.get(id=request.session['userid'])
    likeQuote = Quote.objects.get(id=quote_id)
    likeQuote.likes.add(likeUser)
    return redirect('/appQuote')

def unlike(request, quote_id):
    likeUser = User.objects.get(id=request.session['userid'])
    likeQuote = Quote.objects.get(id=quote_id)
    likeQuote.likes.remove(likeUser)
    return redirect('/appQuote')

def delete(request, quote_id):
    deleteQuote = Quote.objects.get(id=quote_id)
    deleteQuote.delete()
    return redirect('/appQuote')
