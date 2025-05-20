from django.views.generic import TemplateView
from books.models import Book

class HelloWorldView(TemplateView):
    template_name = "books/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(">>> Context", context)
        context["books"] = Book.objects.all()
        print(">>>", context)
        return context

