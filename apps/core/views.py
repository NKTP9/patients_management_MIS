# from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.users.models import CustomUser, Paramedic, MedicalFacility


class HomepageView(TemplateView):
    template_name = 'pages/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная'
        return context


def main(request):
    return render(request, 'pages/main.html')


def profile(request):
    current_user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'pages/profile.html', {'user': current_user})


def doctors(request):
    paramedic = Paramedic.objects.all()
    return render(request, 'pages/doctors.html', {'paramedic': paramedic})


def hospitals(request):
    hospital = MedicalFacility.objects.all()
    return render(request, 'pages/hospitals.html', {'hospital': hospital})
