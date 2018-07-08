from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articlesApp.models import Article

@login_required
def article_data(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'article_data.html', context)
    except:
        return redirect('/')

@login_required
def article_data_admin(request, article_id):
    if not request.user.is_staff:
        return redirect('/')
    else:
        try:
            article = Article.objects.get(id=article_id)
            context = {
                'article': article
            }
            return render(request, 'article_data_admin.html', context)
        except:
            return redirect('/')
