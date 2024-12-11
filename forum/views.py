from django.views.generic import TemplateView


class Forum(TemplateView):
    template_name = "forum/forum.html"