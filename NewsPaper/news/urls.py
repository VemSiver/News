from django.urls import path
from .views import PostList, PostDetail  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем постам у нас останется пустым, позже станет ясно, почему
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    # pk — это первичный ключ, который будет выводиться у нас в шаблон
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]
