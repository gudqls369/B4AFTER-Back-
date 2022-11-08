from django.urls import path
from books import views

urlpatterns = [
    # path('', views.Books_Home.as_view(), name='books_home'),
    path('explore/', views.Book_List.as_view(), name='book_list_view'),
    path('community/', views.Review_List.as_view(), name='review_list'),
    # path('search/', BookSearchView.as_view(), name='book_list_view'),
    path('<str:isbn>/', views.Book_Detail.as_view(), name='bookdetail'),
    path('<str:book_id>/review/', views.Book_Review.as_view(), name='bookreview'),
    path('<str:book_id>/review/<int:review_id>/', views.Book_Review_Detail.as_view(), name='book_review_detail'),
    path('<int:book_id>/like/', views.Book_Like.as_view(), name='like_view'),
]
