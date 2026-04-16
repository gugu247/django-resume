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
    return render(request, 'resume/resume.html', context)

def skills_category(request):
    profile = get_object_or_404(Profile)
    skills = profile.skills.all()
    grouped = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(skill)
    return render(request, 'resume/skills.html', {'grouped': grouped})


