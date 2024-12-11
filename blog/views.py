from django.views.generic import TemplateView

class Blog(TemplateView):
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_path'] = self.request.path
        return context