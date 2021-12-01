from django.urls import path
from blog import views

app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),
    path("detail", views.detail, name="detail"),
    path("cover", views.cover, name="cover"),
    path("recommend", views.recommend, name="recommend"),
    path("result", views.result, name="result"),
    path("about", views.about, name="about"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_view, name="login"),
    path("coin", views.coin, name="coin"),
    path("btc", views.btc, name="btc"),
    path("ada", views.ada, name="ada"),
    path("doge", views.doge, name="doge"),
    path("omg", views.omg, name="omg"),
    path("bch", views.bch, name="bch"),
    path("eos", views.eos, name="eos"),
    path("snt", views.snt, name="snt"),
    path("eth", views.eth, name="eth"),
    path("xrp", views.xrp, name="xrp"),
]