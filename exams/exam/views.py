from django.shortcuts import render,get_object_or_404,redirect
from .models import Exam,Questions
from .forms import ExamForm,QuestionsForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def CreatExam(request):
    form=ExamForm()
    if request.method=="POST":
        form=ExamForm(request.POST)
        if form.is_valid():
            exam=form.save()
            return redirect('exam:index')
    return render(request,'exam/create_exam.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def UpdateExam(request,pk):
    instance=get_object_or_404(Exam,id=pk)
    form=ExamForm(instance=instance)
    if request.method=="POST":
        form=ExamForm(request.POST,instance=instance)
        if form.is_valid():
            exam=form.save()
            return redirect('exam:index')
    return render(request,'exam/create_exam.html',{'form':form,'theme':'Update'})
@user_passes_test(lambda u: u.is_superuser)
def DeleteExam(request,pk):
    exam=get_object_or_404(Exam,id=pk)
    if request.method=="POST":
        exam.delete()
        return redirect('exam:index')
    return render(request,'exam/confirm.html',{'exam':exam,'theme':'exam'})

@user_passes_test(lambda u: u.is_superuser)
def CreatQuestions(request,pk):
    question_exam=get_object_or_404(Exam,id=pk)
    form=QuestionsForm()
    if request.method=="POST":
        form=QuestionsForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.exam=question_exam
            question.save()
            return redirect('exam:exam_detail',pk=pk)
    return render(request,'exam/create_question.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def UpdateQuestions(request,pk):
    question=get_object_or_404(Questions,id=pk)
    form=QuestionsForm(instance=question)
    if request.method=="POST":
        form=QuestionsForm(request.POST,instance=question)
        if form.is_valid():
            question=form.save()
            return redirect('exam:index')
    return render(request,'exam/create_question.html',{'form':form,'theme':'Create'})
@user_passes_test(lambda u: u.is_superuser)
def DeleteQuestions(request,pk):
    question=get_object_or_404(Questions,id=pk)
    if request.method=="POST":
        question.delete()
        return redirect('exam:index')
    return render(request,'exam/confirm.html',{'exam':question,'theme':'Question'})
@user_passes_test(lambda u: u.is_superuser)
def admin_index(request):
    exams=Exam.objects.all()
    return render(request,'exam/admin-index.html',{'exams':exams})
@user_passes_test(lambda u: u.is_superuser)
def exam_detail(request,pk):
    exam=get_object_or_404(Exam,id=pk)
    questions=exam.questions_set.all()
    return render(request,'exam/exam-deatil.html',{'exam':exam,'questions':questions})
def signup_view(request):
    form = SignUpForm()
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request,"Account created succesfully")
            return redirect('exam:login')
    return render(request, 'exam/signup.html', {'form': form})
def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            if (user.is_superuser):
                return redirect('exam:index')
            else:
                return redirect('exam:user-index')
        messages.error(request,"Your Username or Password in correct")
    return render(request, 'exam/login.html')
def logout_view(request):
    logout(request)
    return HttpResponse('<h1>Signed out<h1>Login again <a href="/login/">Login</a>')
def user_index(request):
    if request.user.is_superuser:
        return redirect('exam:index')
    exams=Exam.objects.all()
    return render(request,'exam/user-index.html',{'exams':exams})
@login_required(login_url='/login/')
def write_exam(request,pk):
    exam=get_object_or_404(Exam,id=pk)
    questions=exam.questions_set.all().order_by('?')
    if request.method=="POST":
        result=0
        total=len(questions)
        for question in questions:
            if(request.POST.get(str(question.id))==question.solution):
                result=result+1
        return HttpResponse("<h1>Result:{}/{}</h1><h4>Back to <a href='/'>Exams</a></h4>".format(result,total))
    return render(request,'exam/write-exam.html',{'exam':exam,'questions':questions})
