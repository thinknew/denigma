from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext
from django.views.generic.edit import FormView

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import ContactForm, NameContactForm


def contact(request):
    errors = []
    if request.method == 'POST':
        #if not request.POST.get('subject', ''): errors.append('Enter a subject.')
        #if not requesst.POST.get('message', ''): errors.append('Enter a message.')
        #if not request.POST.get('email') and '@' not in request.POST['emal']: errors.append('Enter a valid e-mail address.')
##        if not errors:
##            send_mail(
##                request.POST['subject'],
##                request.POST['message'],
##                request.POST.get('emal', 'noreply@example.com'),
##                ['siteowner@example.com'],

##            )
##            return HttpResponseRedirect('/contact/thanks/')
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                send_mail(
                    cd['subject'],
                    cd['message'] + " Send by " + cd['email'],
                    cd.get('email', 'hevok@denigma.de'), #'noreply@example.com'),
                    ['age@liv.ac.uk'],                #['siteowner@example.com'],
                )
            except:
                 # Because of the verfication problem with SES.
                 send_mail(
                    cd['subject'],
                    cd['message'] + " Send by " + cd['email'],
                    cd.get('mail', 'hevok@denigma.de'),
                    ['age@liv.ac.uk'],
                 )

            messages.add_message(request, messages.SUCCESS,
                ugettext("The enquiry has been sent."))
            #return HttpResponseRedirect('/contact/thanks') # thanks/
            return render_to_response('contact/thanks.html', context_instance=RequestContext(request))

    else:
        form = ContactForm(
            initial={'subject':'For the singularity!'})
    return render_to_response('contact/form.html', {'form':form}, context_instance=RequestContext(request))

##    return render_to_response('contact_form.html', {
##        'errors':errors,
##        'subject':request.POST.get('subject', ''),
##        'message':request.POST.get('message', ''),
##        'email':request.POST.get('email', ''),
##    })

# Not yet implemented:
class ContactView(FormView):
    template_name = 'contact/html'
    form_class = NameContactForm
    success_url = '/thanks'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)