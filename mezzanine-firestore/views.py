from django.views.generic import View
from mezzanine_firestore.models import Patient
from mezzanine_firestore.forms import Patient_Form
from django.shortcuts import render

class Patient_View(View):  
    initial={'key':'value'}
    form_class = Patient_Form
    template_name = 'mezzanine_firestore/patient.html'

    def get(self, request, *args, **kwargs):        
        patient_code = self.kwargs['patient_code']  
        try:
            patient = Patient.objects.get(id=patient_code)            
            form= self.form_class(instance=patient)
        except Patient.DoesNotExist:
            form=self.form_class(initial=self.initial)
            #paciente_count = Paciente.objects.filter().count()
            patient_code = 0 # request.user.username +'-'+ str(pacient_count)
        return render(request, self.template_name, {'form':form, 'patient_code':patient_code})#nos muestra el formulario para llenar
        
    def post(self, request, *args, **kwargs): 
        
        if 'cancel_page_button' in request.POST:
            return HttpResponseRedirect('/mdrecords/paciente-lista')
        
        patient_code = self.kwargs['patient_code']
        ###
        ###if 'empleo_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/empleo-lista/')
        ###
        ###if 'apnp_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/apnp/')
        ###
        ###if 'ago_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/ago/')
        ###
        ###if 'app_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/app/')
        ###
        ###if 'ahf_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/ahf/')
        ###
        if 'save_page_button' in request.POST:
        #    #cod_rep = self.kwargs['cod_rep']
            try:
                instance=Patient.objects.get(id=patient_code)
                form = self.form_class(request.POST or None, instance=instance)            
            except Patient.DoesNotExist:
                #form=self.form_class(instance=pacient)
                form = self.form_class(request.POST)       
            if form.is_valid():
                patient = form.save()#commit=False)
                #print 'pacient saved'
                #pacient.id = self.kwargs['cod_rep']                
                #pacient.save()
                #return HttpResponseRedirect('/mdrecords/'+pacient.id+'/pacient-saved/')
                return render(request, 'amendez_mdrecords/paciente-guardado.html' , {'patient': patient})
        ###    print 'form not valid'
        ###    return render(request, self.template_name, {'form': form})
        return HttpResponseRedirect('/')

    ###@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Patient_View, self).dispatch(*args, **kwargs)
