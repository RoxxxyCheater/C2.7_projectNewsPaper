# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post,Author
from datetime import datetime
 
 
class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news_all.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news_all'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id') # По такому запросу сформируется список объектов, которые будут выводиться в представлении/если не указывать по умолчанию сработает не .order_by('-id'), а .all()
    #.order_by('-id') сортировка от нового к старому

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['value1'] = Author.objects.all().order_by('-rateAuthor').values('authors_id', 'rateAuthor')[0] # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context
        
class PostDetail(DetailView): # адресс в котором будет лежать информация о конкретном товаре
    model = Post
    template_name ='news.html'
    context_object_name = 'news'
    