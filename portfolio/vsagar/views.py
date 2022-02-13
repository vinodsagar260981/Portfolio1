from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio
# Create your views here.
def index(request):
    #Home
    home = Home.objects.latest('updated')

    #About
    about = About.objects.latest('update')
    profiles = Profile.objects.filter(about=about)
    link_li = Profile.objects.all()[0].link
    link_git = Profile.objects.all()[1].link
    link_fb = Profile.objects.all()[2].link

    #skills
    caterogies = Category.objects.all()

    #Portfolio
    portfolio = Portfolio.objects.all()


    context = {
        'home' : home,
        'about' : about,
        'profiles' : profiles,
        'caterogies': caterogies,
        'portfolio': portfolio,
        'link_li': link_li,
        'link_git': link_git,
        'link_fb': link_fb
    }

    return render(request, 'index.html', context)