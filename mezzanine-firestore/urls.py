from django.conf.urls import url, include#, patterns  
#from django.conf.urls.defaults import *
from mezzanine_firestore.views import Patient_View

#import views

urlpatterns = [
     url(r'^(?P<patient_code>[^/]+)/patient/$', Patient_View.as_view()), 
     ##url(r'^(?P<cod_rep>[^/]+)/saved-pacient/$', Pacient_Saved_View.as_view()), 
     #url(r'^paciente-lista', Paciente_List_View.as_view()),
     ##url(r'^(?P<id_report>[^/]+)/-content/$', Report_Content_View.as_view()),
     #url(r'^(?P<id_report>[^/]+)/paciente-borrar/$', Paciente_Delete_View.as_view()),
     #url(r'^(?P<id_report>[^/]+)/paciente-mostrar/$', Paciente_Show_View.as_view()),
     #url(r'^(?P<id_report>[^/]+)/empleo-lista/$',Empleo_List_View.as_view()),
     #url(r'^(?P<id_report>[^/]+)/(?P<id_empleo>[^/]+)/empleo/$',Empleo_View.as_view()),
     #url(r'^(?P<id_report>[^/]+)/(?P<id_empleo>[^/]+)/empleo-mostrar/$',Empleo_Show_View.as_view()),
     #url(r'^(?P<id_report>[^/]+)/(?P<id_empleo>[^/]+)/empleo-borrar/$',Empleo_Delete_View.as_view()),    
     #url(r'^(?P<id_pacient>[^/]+)/apnp/$',APNP_View.as_view()),
     #url(r'^(?P<id_patient>[^/]+)/ago/$',  AGO_View.as_view()),
     #url(r'^(?P<id_patient>[^/]+)/app/$',  APP_View.as_view()),
     #url(r'^(?P<id_patient>[^/]+)/ahf/$',  AHF_View.as_view()),
     #url(r'^statistics/$',  Statistics_View.as_view()),
     #
     #url(r'^equations/$',  Equation_List_View.as_view()),
     #url(r'^(?P<id_equation>[^/]+)/equation/$',Equation_View.as_view()),
     #
     ##url(r'^(?P<id_report>[^/]+)/paciente-nuevo/$', Paciente_View.as_view()),
     #
     ##url(r'^(?P<code>[^/]+)/slide/$', Slide_View.as_view()),
     ##url(r'^(?P<code>[^/]+)/save-slide/$', Slide_show_View.as_view()),                 
     ##url(r'^slide-list', Slide_List_View.as_view()), 
     ##url(r'^(?P<id_slide>[^/]+)/delete-slide/$', Delete_Slide_View.as_view()),
]
