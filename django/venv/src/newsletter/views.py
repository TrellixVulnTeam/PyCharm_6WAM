from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp


# Create your views here.
def home(request):
    title = "Keep Updated"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "L. Li"
        instance.full_name = full_name

        # if not instance.full_name:
        #     instance.full_name = "Charlie"

        instance.save()
        context = {
            "title": "Thank you",
        }
    if request.user.is_authenticated() and request.user.is_staff:
        # for instance in SignUp.objects.all():
        #     print(instance.email)
        queryset = SignUp.objects.all().order_by('-timestamp')  # .filter(full_name__icontains="abc")
        context = {
            "queryset": queryset,
        }
    return render(request, "home.html", context)


def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print(key, value)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print(email, message, full_name)
        subject = "Site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, ]
        contact_message = "{0}: {1} via {2}".format(form_full_name,
                                                    form_message,
                                                    form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)
    context = {
        "form": form,
        "title": title
    }
    return render(request, "forms.html", context)