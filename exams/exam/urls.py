from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name="exam"
urlpatterns = [
path('createexam/',views.CreatExam,name="createexam"),
path('createexam/update/<int:pk>',views.UpdateExam,name="updateexam"),
path('createexam/delete/<int:pk>',views.DeleteExam,name="deleteexam"),
path('createquestion/<int:pk>',views.CreatQuestions,name="createquestion"),
path('updatequestion/<int:pk>',views.UpdateQuestions,name="updatequestion"),
path('deletequestion/<int:pk>',views.DeleteQuestions,name="deletequestion"),
path('exams/',views.admin_index,name="index"),
path('exams/<int:pk>',views.exam_detail,name="exam_detail"),
path('signup/',views.signup_view,name="signup"),
path('login/',views.login_view,name="login"),
path('logout/',views.logout_view,name="logout"),
path('',views.user_index,name="user-index"),
path('user/write/<int:pk>',views.write_exam,name="write_exam"),
path('test',TemplateView.as_view(template_name="exam/test.html"),name="test"),

]
