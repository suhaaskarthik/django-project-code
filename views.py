from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from .models import sign_up_email, Query, Answers
import smtplib
from django.utils import timezone
def error(request):

    return render(request, 'error_page.html')
def logout(request):
    try:
        return render(request, 'logout.html')
    except:
        return HttpResponseRedirect(reverse('error'))
def logout_(request):
    try:
        x = request.GET.get('logout')
        y = request.GET.get('cancel')
        print(x,y)
        if x == None:
            pass

        else:
            try:
                sign_up_email.objects.get(username = username_sign).delete()
                return HttpResponseRedirect(reverse('searching'))
            except NameError:
                sign_up_email.objects.get(username=username_).delete()
                return HttpResponseRedirect(reverse('searching'))
        if y == 'cancel':
            return HttpResponseRedirect(reverse('ourquestion'))

    except:
        return HttpResponseRedirect(reverse('error'))



def ourquestion(request):
    try:
        answered = []
        gh = []
        val = []
        total = []
        strings = []
        arranged_total = {}
        rating = {}
        publisher = {}
        published_at = {}
        answer_count = {}
        expectations = {}
        queries = []
        rating_ = {}
        answer_count_ = {}
        new_answer = []
        boolean = False
        username__ = ''
        msg = ''
        msg2 = ''
        try:
            q = sign_up_email.objects.get(username = username_sign)
        except NameError:
            q = sign_up_email.objects.get(username=username_)
        if list(q.query_set.all()) == []:
            msg = 'none'

        for i in Query.objects.all():
            if i.answers_set.count()==0:
                answer_count[str(i)] = 0
                if i.publisher == q.username:
                    val.append(0)
                    total.append(0)
                    strings.append(str(i))
            else:
                gh = []
                n = Query.objects.get(product_name=str(i))

                for z in n.answers_set.all():
                    gh.append(int(z.star_rating))
                addition = sum(gh)
                print(addition)
                print('count', n.answers_set.count())
                queries.append(str(i))
                round_val = round(addition / int(n.answers_set.count()))
                if i.publisher == q.username:
                    total.append(int(n.answers_set.count()) * int(round_val))
                    strings.append(str(i))
                    val.append(int(n.answers_set.count()) * int(round_val))
                    boolean = True

                rating[str(i)] = round_val
                publisher[str(i)] = i.publisher
                published_at[str(i)] = i.pub_date
                answer_count[str(i)] = i.answers_set.count()
                expectations[str(i)] = i.expectations
        print(boolean)
        val.sort()
        val.reverse()
        print('this is ', val)
        for i in val:
            x = total.index(i)
            print(x)

            arranged_total[strings[x]] = str(i)
            strings.remove(strings[x])
            total.remove(i)
        for i in Answers.objects.all():
            if i.publisher == str(q.username):

                answered.append(i.answer_question)
        if answered == []:
            msg2 = 'none2'



        answer = set(answered)
        for x in answer:
            rating_[str(x)] = rating[str(x)]
            answer_count_[str(x)] = str(x.answers_set.count())
        for i in answer:
            new_answer.append(str(i))
        try:
            username__ = username_sign
        except NameError:
            username__ = username_
        return render(request, 'ourquestion.html', {'username':username__,'arranged':arranged_total, 'rating':rating,'publisher':publisher,
                                                  'published':published_at, 'count':answer_count, 'expectations':expectations, 'answer':new_answer,
                                                    'rating_':rating_, 'answer_count_':answer_count_, 'msg':msg, 'msg2':msg2})
    except:
        return HttpResponseRedirect(reverse('error'))

def forgotpassword(request):
    try:
        return render(request, 'forgotpassword.html')
    except:
        return HttpResponseRedirect(reverse('error'))
def forgotpassword_(request):
    try:
        msg = ''
        message = ''
        boolean = False
        v = request.GET.get('username')
        email = ''
        password = ''
        for i in sign_up_email.objects.all():
            if str(i.username) == v:
                password = str(i.password)
                email = str(i)
                boolean = True
        print(password)
        print(email)
        if boolean == False:
            msg = 'Username is invalid'
        else:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("suhaaskarthikeyan13@gmail.com", "suhaas@123")
                s.sendmail("suhaaskarthikeyan13@gmail.com", str(email), str(password))
                s.quit()
                msg = 'Successfully sent password, please check your email'
            except:
                msg = 'An error occurred, please try again'
    except:
        return HttpResponseRedirect(reverse('error'))



    return render(request,'forgotpassword_.html', {'msg':msg})

def sign(request):
    try:
        return render(request, 'base.html')
    except:
        return HttpResponseRedirect(reverse('error'))
def login(request):
    try:
        return render(request, 'login.html')
    except:
        return HttpResponseRedirect(reverse('error'))
def login_(request):
    try:
        ft = False
        global username_
        global password_
        colour = ''
        password_ = request.POST.get('password_')
        username_ = request.POST.get('username_')

        for i in sign_up_email.objects.all():
            if str(i.username) == username_:
                correct_password = i.password
                print(i.password)
                ft = True

        if ft == False:
            message = 'You have not signed up, sign up for free now'
            color = 'yellow'
        if ft == True:
            if correct_password == password_:
                message = 'successful login'

            else:
                message = 'wrong password'
                color = 'red'
        if message == 'successful login':
            return HttpResponseRedirect(reverse('ourquestion'))
        else:
            return render(request, 'login_.html',{ 'message': message, 'colour':colour})
    except:
        return HttpResponseRedirect(reverse('error'))
def ourquestion_(request):
    x = {}
    m = {}
    s = {}
    p = {}
    val = []
    total = []
    strings = []
    arranged_total = {}
    average = {}
    rating_ = {}
    answer_count_ = {}
    new_answer = []
    username__ = ''
    msg = ''
    msg2 = ''
    search = request.GET.get('ourquestion')
    try:
        queries = sign_up_email.objects.get(username = username_sign)

    except NameError:
        queries = sign_up_email.objects.get(username=username_)

    print(queries.query_set.all())
    try:
        for i in Query.objects.all():
            gh = []
            n = Query.objects.get(product_name=str(i))
            if search in str(i):
                if i.answers_set.count() == 0:
                    if i.publisher == queries.username:
                        val.append(0)
                        total.append(0)
                        strings.append(str(i))
                    else:
                        pass

                else:
                    for z in n.answers_set.all():
                        gh.append(int(z.star_rating))
                    addition = sum(gh)
                    print(addition)
                    print('count', n.answers_set.count())
                    round_val = round(addition / int(n.answers_set.count()))
                    average[str(i)] = round_val
                    if i.publisher == queries.username:
                        total.append(int(n.answers_set.count()) * int(round_val))
                        strings.append(str(i))
                        val.append(int(n.answers_set.count()) * int(round_val))

                m[str(i)] = n.answers_set.count()
                x[str(i)] = n.expectations
                print(str(i))
                p[str(i)] = n.publisher
                s[str(i)] = n.pub_date

        if x == {}:
            for i in Query.objects.all():
                gh = []
                n = Query.objects.get(product_name=str(i))
                if str(i) in search:
                    if i.answers_set.count() == 0:
                        if i.publisher == queries.username:
                            val.append(0)
                            total.append(0)
                            strings.append(str(i))
                    else:
                        for i in n.answers_set.all():
                            gh.append(int(i.star_rating))
                        addition = sum(gh)
                        round_val = round(addition / int(n.answers_set.count()))
                        average[str(i)] = round_val
                        if i.publisher == queries.username:
                            total.append(int(n.answers_set.count()) * int(round_val))
                            strings.append(str(i))
                            val.append(int(n.answers_set.count()) * int(round_val))
                    x[str(i)] = n.expectations
                    m[str(i)] = n.answers_set.count()
                    p[str(i)] = n.publisher
                    s[str(i)] = n.pub_date
        val.sort()
        val.reverse()
        print(val)
        for i in val:
            x = total.index(i)
            print(x)

            arranged_total[strings[x]]= str(i)
            strings.remove(strings[x])
            total.remove(i)
        print(arranged_total)
        if val == []:
            msg = 'none'
        print(p)


        b = []
        for k in Answers.objects.all():
            if k.publisher == queries.username and search in str(k.answer_question):
                b.append(str(k.answer_question))
                rating_[str(k.answer_question)] = int(average[str(k.answer_question)])
                answer_count_[str(k.answer_question)] = k.answer_question.answers_set.count()
            elif k.publisher == queries.username and search in str(k.answer_question):
                b.append(str(k.answer_question))
                rating_[str(k.answer_question)] = int(average[str(k.answer_question)])
                answer_count_[str(k.answer_question)] = k.answer_question.answers_set.count()
        b = list(dict.fromkeys(b))
        if b== []:
            msg2 = 'none'
        try:
            username__ = username_sign
        except NameError:
            username__ = username_
        return render(request, 'ourquestion_.html', {'b': b, 'username': username__, 'arranged': arranged_total,
                                                     'counts': m, 'p': p, 's': s, 'average': average, 'x': x,
                                                     'rating_': rating_, 'answer_count': answer_count_, 'msg': msg,
                                                     'msg2': msg2})
    except:
        return HttpResponseRedirect(reverse('error'))
def post(request):
    try:
        global username__
        try:
            username__ = username_sign
        except NameError:
            try:
                username__ = username_
            except NameError:
                username__ = 'You have not signed up yet'
    except:
        return HttpResponseRedirect(reverse('error'))


    return render(request, 'question.html')
def post_(request):
    try:
        global product_name
        global description
        product_name = request.POST.get('product')
        description = request.POST.get('questions')
        sets = {}
        sets_ex = {}
        msg = ''

        sets = set(list(product_name))
        sets_ex = set(list(description))
        for x in Query.objects.all():
            if str(x) == product_name:
                msg = 'same'
        if sets == {' '} or sets == {''} or sets == set():
            msg = 'invalid'
        elif sets_ex == {' '} or sets_ex == {''} or sets_ex == set():
            msg = 'invalid'
        return render(request, 'post_.html', {'msg':msg})
    except NameError:
        return HttpResponseRedirect(reverse('error'))
def post__(request):
    try:
        bool  = False

        b = False
        value = 1
        for i in Query.objects.all():
            if str(i) == product_name:
                msg = 'somebody else has asked a similar query'
                colour = 'red'
                bool = True
        if bool == False:
            for i in sign_up_email.objects.all():
                print(i)
                if str(i.username) == username__:
                    q = sign_up_email.objects.get(email = i)
                    try:
                        q.query_set.create(product_name=product_name, expectations=description, pub_date=timezone.now(),
                                           publisher=username_sign)

                    except NameError:
                        q.query_set.create(product_name=product_name, expectations=description, pub_date = timezone.now(), publisher = username__)

                    b = True
                value+=1
            if b ==False:
                print('not working')
            msg = 'successfully logged in'
            colour = 'green'
        return HttpResponseRedirect(reverse('postquestion'))
    except NameError:
        return HttpResponseRedirect(reverse('error'))
def searching(request):
    try:
        gh = []
        val = []
        arranged_total = {}
        rating = {}
        publisher = {}
        published_at = {}
        answer_count = {}
        expectations = {}
        queries = []
        round_val = 0
        ratings = []
        answer_ratings = {}
        worst_rating = 0
        best_rating = 0
        worst = {}
        best = {}
        worst_answer = {}
        best_answer = {}
        values = []
        items = []
        total = []
        strings = []
        for i in Query.objects.all():
            gh = []
            ratings = []
            n = Query.objects.get(product_name=str(i))


            if list(n.answers_set.all()) == []:
                pass
            else:
                if i.answers_set.count() == 0:
                    val.append(0)
                    total.append(str(i))
                    strings.append(str(i))
                else:
                    for z in n.answers_set.all():
                        gh.append(int(z.star_rating))
                        answer_ratings[int(z.star_rating)] = str(z)
                        ratings.append(int(z.star_rating))

                    ratings.sort()
                    worst_rating = ratings[0]
                    best_rating = ratings[-1]
                    if worst_rating == best_rating:
                        best[str(n)] = best_rating
                        best_answer[str(n)] = answer_ratings[best_rating]

                    else:
                        worst[str(n)] = worst_rating
                        best[str(n)] = best_rating
                        worst_answer[str(n)] = answer_ratings[worst_rating]
                        best_answer[str(n)] = answer_ratings[best_rating]
                        items.append(str(n))
                    addition = sum(gh)
                    queries.append(str(i))
                    round_val = round(addition / int(n.answers_set.count()))

                    total.append(int(n.answers_set.count())* int(round_val))
                    strings.append(str(i))
                    val.append(int(n.answers_set.count())* int(round_val))
            rating[str(i)] = round_val
            publisher[str(i)] = i.publisher
            published_at[str(i)] = i.pub_date
            answer_count[str(i)] = i.answers_set.count()
            expectations[str(i)] = i.expectations
            queries.append(str(i))
        val.sort()
        val.reverse()
        for i in val:
            x = total.index(i)
            print(x)

            arranged_total[strings[x]]= str(i)
            strings.remove(strings[x])
            total.remove(i)

        print(strings)


        print(worst, best)
        print(worst_answer, best_answer)
        return render(request, 'searching.html', {'arranged':arranged_total, 'rating':rating,'publisher':publisher,
                                                  'published':published_at, 'count':answer_count, 'expectations':expectations, 'queries':queries,
                                                  'best':best, 'worst':worst, 'worst_answer':worst_answer, 'best_answer':best_answer, 'items':items})
    except:
        return HttpResponseRedirect(reverse('error'))
def searching_(request):
    try:
        x = {}
        m = {}
        s = {}
        p = {}
        val = []
        total = []
        arranged_total = {}
        average = {}
        strings = []
        search = request.GET.get('search')
        for i in Query.objects.all():
            gh = []
            if search in str(i):
                n = Query.objects.get(product_name=str(i))
                if i.answers_set.count()==0:
                    total.append(0)
                    strings.append(str(i))
                    val.append(0)
                else:
                    for z in n.answers_set.all():
                        gh.append(int(z.star_rating))
                    addition = sum(gh)
                    print(addition)
                    print('count', n.answers_set.count())
                    round_val = round(addition / int(n.answers_set.count()))
                    average[str(i)] = round_val
                    total.append(int(n.answers_set.count()) * int(round_val))
                    strings.append(str(i))
                    val.append(int(n.answers_set.count()) * int(round_val))
                m[str(i)] = n.answers_set.count()
                x[str(i)] =n.expectations
                print(str(i))
                p[str(i)] = n.publisher
                s[str(i)] = n.pub_date

        if x == {}:
            for i in Query.objects.all():
                if str(i) in search:
                    gh = []
                    n = Query.objects.get(product_name=str(i))
                    if i.answers_set.count()==0:
                        strings.append(str(i))
                        total.append(0)
                        val.append(0)
                    else:
                        for i in n.answers_set.all():
                            gh.append(int(i.star_rating))
                        addition = sum(gh)
                        round_val = round(addition / int(n.answers_set.count()))
                        average[str(i)] = round_val
                        total.append(int(n.answers_set.count()) * int(round_val))
                        strings.append(str(i))
                        val.append(int(n.answers_set.count()) * int(round_val))
                    x[str(i)] = n.expectations
                    m[str(i)] = n.answers_set.count()
                    p[str(i)] = n.publisher
                    s[str(i)] = n.pub_date
        val.sort()
        val.reverse()
        print(val)
        for i in val:
            x = total.index(i)
            print(x)

            arranged_total[strings[x]] = str(i)
            strings.remove(strings[x])
            total.remove(i)
        print(arranged_total)

        print(p)

        return render(request, 'searching_.html',{'arranged':arranged_total, 'counts':m, 'p':p, 's':s, 'average':average , 'x':x})
    except:
        return HttpResponseRedirect(reverse('error'))
def answer(request, query):
    try:
        global question
        k = {}
        l = {}
        m = {}
        try:
            username = username_
        except NameError:
            username = username_sign

        question = query
        n = ''
        expectation = ''
        a = ''
        o =''
        s = ''
        try:

            n = Query.objects.get(product_name=question)
            s = str(n.answers_set.count())
            expectation = n.expectations
            a = n.publisher
            o = n.pub_date
            for i in n.answers_set.all():
                print(i)
                k[str(i)]= i.publisher
                l[str(i)] = i.pub_date
                m[str(i)] = i.star_rating
        except:
            pass

        print(k, l)
        ms = 'not checked'
        boolean = False
        msg = ''
        try:
            for i in n.answers_set.all():
                if str(i.publisher)==username_:
                    boolean = True
            if boolean == False:
                msg= 'Correct'
        except NameError:
            for i in n.answers_set.all():
                if str(i.publisher)==username_sign:
                    boolean = True
            if boolean == False:
                msg= 'Correct'

        return render(request, 'answer.html',{'username':username, 'expectations':expectation, 'name':query, 'k':k, 'l':l, 'a':a, 'o':o,'m':m , 'count':s, 'msg':msg})
    except:
        return HttpResponseRedirect(reverse('error'))
def postanswer(request):
    try:

        global review
        global rate
        sets = {}
        msg = ''
        review = request.POST.get('questions')
        rate = request.POST['rate']

        sets = set(list(review))
        print('list', list(review))
        print('sets', sets)

        if sets == {' '} or sets == {''} or sets == set( ):
            msg = 'invalid'
        else:
            msg = 'perfect'
    except:
        msg = 'no rating'

    return render(request, 'answer_.html', {'query':question, 'msg':msg})
def postanswer_(request):
    try:
        lists = []
        q = Query.objects.get(product_name=question)
        add_count = (int(q.answers_set.count()))
        new_count = add_count+1
        final_reveiw = str(new_count)+ ')  '+review
        try:
            q.answers_set.create(answer=final_reveiw, pub_date=timezone.now(), publisher=username_sign,
                                 star_rating=rate)
        except NameError:
            q.answers_set.create(answer=final_reveiw, pub_date=timezone.now(), publisher=username_, star_rating=rate)

        print(str(q.product_name))
        for  i in list(Answers.objects.all()):
            lists.append(str(i))
        return HttpResponseRedirect(reverse('answer', args=(question,)))
    except:
        return HttpResponseRedirect(reverse('error'))





def sign_up(request):
    global username_sign

    bool = False
    email_id = request.POST.get('email')
    password = request.POST.get('password')
    username_sign = request.POST.get('username')
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("suhaaskarthikeyan13@gmail.com", "suhaas@123")
        message = "You have successfully signed up"
        s.sendmail("suhaaskarthikeyan13@gmail.com", email_id, message)
        s.quit()
        for i in sign_up_email.objects.all():
            if email_id == str(i):
                msg = 'You have already signed up with this email'
                bool = True
            print(i)
        print(email_id)
        print(bool)
        tf = False
        if bool == False:
            for x in sign_up_email.objects.all():
                if str(x.password) == password:
                    msg = 'Somebody has already used your password please enter another'
                    tf = True
                if str(x.username) == username_sign:
                    msg = 'Somebody has used your username please enter another'
                    tf = True

            if tf== False:
                msg = 'Successfully signed up'

                q = sign_up_email(email=email_id, password=password, username = username_sign, pub_date = timezone.now())

                q.save()
    except:
        msg = 'Error occured please check your credentials'
    if msg == 'Successfully signed up':
        return HttpResponseRedirect(reverse('ourquestion'))
    else:
        return render(request, 'signed_up.html',{'id' : email_id, 'msg':msg})






