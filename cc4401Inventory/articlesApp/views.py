from django.shortcuts import render, redirect
from articlesApp.models import Article


def article_data(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'article_data.html', context)
    except:
        return redirect('/')


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
