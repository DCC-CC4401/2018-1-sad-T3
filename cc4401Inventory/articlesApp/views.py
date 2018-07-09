from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articlesApp.models import Article
from loansApp.models import Loan
from datetime import datetime
import random, os
import pytz


@login_required
def article_data(request, article_id):
    try:
        article = Article.objects.get(id=article_id)

        last_loans = Loan.objects.filter(article=article,
                                         ending_date_time__lt=datetime.now(tz=pytz.utc)
                                         ).order_by('-ending_date_time')[:10]

        loan_list = list()
        for loan in last_loans:

            starting_day = loan.starting_date_time.strftime("%d-%m-%Y")
            ending_day = loan.ending_date_time.strftime("%d-%m-%Y")
            starting_hour = loan.starting_date_time.strftime("%H:%M")
            ending_hour = loan.ending_date_time.strftime("%H:%M")

            if starting_day == ending_day:
                loan_list.append(starting_day+" "+starting_hour+" a "+ending_hour)
            else:
                loan_list.append(starting_day + ", " + starting_hour + " a " +ending_day + ", " +ending_hour)


        context = {
            'article': article,
            'last_loans': loan_list
        }

        return render(request, 'article_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')

@login_required
def article_request(request):
    return render(request, 'article_data.html')


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



@login_required
def article_edit_name(request, article_id):

    if request.method == "POST":
        a = Article.objects.get(id=article_id)
        a.name = request.POST["name"]
        a.save()
    return redirect('/article/'+str(article_id)+'/edit')


@login_required
def article_edit_image(request, article_id):

    if request.method == "POST":
        u_file = request.FILES["image"]
        extension = os.path.splitext(u_file.name)[1]
        a = Article.objects.get(id=article_id)
        a.image.save(str(article_id)+"_image"+extension, u_file)
        a.save()

    return redirect('/article/' + str(article_id) + '/edit')



@login_required
def article_edit_description(request, article_id):
    if request.method == "POST":
        a = Article.objects.get(id=article_id)
        a.description = request.POST["description"]
        a.save()

    return redirect('/article/' + str(article_id) + '/edit')
