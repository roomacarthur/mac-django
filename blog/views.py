from django.views.generic import TemplateView


class Blog(TemplateView):
    template_name = "blog/blog_list.html"