# from django.shortcuts import render
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from .models import Post
from datetime import datetime

class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context


# создаём представление, в котором будут детали конкретного отдельного поста
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного поста
    template_name = 'post.html'  # название шаблона будет post.html
    context_object_name = 'post'  # название объекта. в нём будет


