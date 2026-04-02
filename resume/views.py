from django.shortcuts import render, get_object_or_404
from .models import Profile,Education,Skill
# Create your views here.

def resume_view(request):
    profile = get_object_or_404(Profile, pk=1)
    context = {
        "profile": profile,
        "experiences": profile.experiences.all(),
        "education": profile.education.all(),
        "skill": profile.skill.all(),
    }
    return render(request, template_name:'resume/resume.html', context)
