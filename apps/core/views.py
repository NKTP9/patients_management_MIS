# from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.users.models import CustomUser, Paramedic, MedicalFacility
from django.db.models import Q


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
    search_post = request.GET.get('search')
    if search_post:
        paramedic = Paramedic.objects.filter(Q(last_name__icontains=search_post))
    else:
        # If not searched, return default posts
        paramedic = Paramedic.objects.all()
    return render(request, 'pages/doctors.html', {'paramedic': paramedic})


def hospitals(request):
    search_post = request.GET.get('search')
    if search_post:
        hospital = MedicalFacility.objects.filter(Q(name__icontains=search_post))
    else:
        # If not searched, return default posts
        hospital = MedicalFacility.objects.all()
    return render(request, 'pages/hospitals.html', {'hospital': hospital})


def get_hospital(request, medical_facility_id):
    try:
        hospital = MedicalFacility.objects.get(medical_facility_id=medical_facility_id)
        return render(request, 'pages/hospital_info.html', {"hospital": hospital})
    except MedicalFacility.DoesNotExist:
        raise Http404


def appointment(request, paramedic_id):
    try:
        doctor = Paramedic.objects.get(paramedic_id=paramedic_id)
        current_user = CustomUser.objects.get(id=request.user.id)
        return render(request, 'pages/appointment.html', {"doctor": doctor})
    except Paramedic.DoesNotExist:
        raise Http404
