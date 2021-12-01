from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta
from .final import input_n_bounds_alevel_output_crypto, Recommendation_DB
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def main(request):
    data = {
            }

    return render(request, "Main.html", data)


def cover(request):
    context = {

    }

    return render(request, "Cover.html", context=context)


@login_required(login_url='/blog/login')
def detail(request):
    context = {

    }

    return render(request, "More-in-crypto.html", context=context)


@login_required(login_url='/blog/login')
def recommend(request):
    context = {

    }

    return render(request, "Recommendation.html", context=context)


modeling={}


def result(request):
    if request.method == "POST":
        select = request.POST.getlist('select')
        data = {'select': select}
        print(data["select"][0:4])
        global modeling
        modeling = {
            'model': input_n_bounds_alevel_output_crypto(int(data["select"][2]), int(data["select"][3]), int(data["select"][0]), int(data["select"][1]))
        }
        print(modeling)
    return render(request, "Result.html", modeling)


def about(request):
    context = {

    }

    return render(request, "About.html", context=context)


def signup(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        phonenumber = request.POST["phonenumber"]

        user = User.objects.create_user(username, email, password)
        user.phonenumber = phonenumber
        user.save()
        return redirect("user:login")

    return render(request, "Signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
            return redirect("user:main")
        else:
            return render(request, "login.html", {
                'error': '비밀번호가 틀립니다.'
            })
            print("인증 실패")
    return render(request, "login.html")


def coin(request):
    if modeling["model"][0] == 'BTC':
        return render(request, "BTC.html")
    elif modeling["model"][0] == 'ADA':
        return render(request, "ADA.html")
    elif modeling["model"][0] == 'DOGE':
        return render(request, "DOGE.html")
    elif modeling["model"][0] == 'OMG':
        return render(request, "OMG.html")
    elif modeling["model"][0] == 'BCH':
        return render(request, "BCH.html")
    elif modeling["model"][0] == 'EOS':
        return render(request, "EOS.html")
    elif modeling["model"][0] == 'SNT':
        return render(request, "SNT.html")
    elif modeling["model"][0] == 'ETH':
        return render(request, "ETH.html")
    else:
        return render(request, "XRP.html")
    return render(request, "Main.html", context=context)


def btc(request):
    context = {

    }

    return render(request, "BTC.html", context=context)


def ada(request):
    context = {

    }

    return render(request, "ADA.html", context=context)


def doge(request):
    context = {

    }

    return render(request, "DOGE.html", context=context)


def omg(request):
    context = {

    }

    return render(request, "OMG.html", context=context)


def bch(request):
    context = {

    }

    return render(request, "BCH.html", context=context)


def eos(request):
    context = {

    }

    return render(request, "EOS.html", context=context)


def snt(request):
    context = {

    }

    return render(request, "SNT.html", context=context)


def eth(request):
    context = {

    }

    return render(request, "ETH.html", context=context)


def xrp(request):
    context = {

    }

    return render(request, "XRP.html", context=context)