from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    context = {
        "test": "TEST",
    }
    return render(request, "core/home.html", context=context)


def something_cool(request):
    if request.method == "POST":
        print("hlw")
        print(request.POST.get("user_mail"))
        subject = "Subscription"
        message = "Thanks for sbscribe"
        from_mail = settings.EMAIL_HOST_USER
        to_mails = [request.POST.get("user_mail")]
        send_mail(
            subject,
            message,
            from_mail,
            to_mails,
            fail_silently=False,
        )
        print("done")

    context = {
        "test": "something_cool",
    }
    return render(request, "core/something_cool.html", context=context)


class SomethingCoolView(TemplateView):
    template_name = "something_cool.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Something Cool View"
        context["page_title"] = title
        return context
