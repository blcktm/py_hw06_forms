from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.db.models import Avg, Max, Min, Count
from django.views.generic import FormView
from core.models import Student, Group
from core.forms import GroupCreateForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        groups = Group.objects.all().values('name', 'teacher_name').annotate(
            student_count=Count('students'),
            student_avg=Avg('students__age'),
            student_max=Max('students__age'),
            student_min=Min('students__age'),
        )
        return {
                'groups': groups,
            }


class StudentCreateView(CreateView):
    template_name = 'create_student.html'
    success_url = '/'
    model = Student
    fields = '__all__'


class GroupCreateView(FormView):
    template_name = 'create_group.html'
    form_class = GroupCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(GroupCreateView, self).form_valid(form)
