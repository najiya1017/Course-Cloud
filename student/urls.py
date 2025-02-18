from django.urls import path

from student import views


urlpatterns=[

    path('register/',views.StudentCreateView.as_view(),name='student-register'),
    path('login/',views.StudentLoginView.as_view(),name='student-login'),
    path('index/',views.IndexView.as_view(),name='index'),
    path('logout/',views.SignOutView.as_view(),name='sign-out'),
    path('courses/<int:pk>/',views.CourseDetailView.as_view(),name='course-detail'),
    path('courses/<int:pk>/add-to-cart/',views.AddToCartView.as_view(),name='add-to-cart'),
    path('cart/summary/',views.CartSummaryView.as_view(),name='cart-summary'),
    path('cart/summary/<int:pk>/remove/',views.CartItemDelete.as_view(),name='cart-item-delete'),
    path('checkout/',views.CheckOutView.as_view(),name='checkout'),
    path('mycourses/',views.MyCoursesView.as_view(),name='my-courses'),
    path('courses/<int:pk>/watch',views.LessonDetailView.as_view(),name='lesson-detail'),
    path('payment/verify/',views.PaymentVerificationView.as_view(),name='payment-verify')
] 