from django.shortcuts import render
from django.views.generic import TemplateView


# Классы вместо функций
class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


# Обработчики ошибок оставляем как функции
def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    context = {'title': 'Ошибка сервера'}
    return render(request, 'pages/500.html', context, status=500)
