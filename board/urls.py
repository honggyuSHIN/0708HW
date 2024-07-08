from django.urls import path
from .views import *

app_name='board'

urlpatterns=[

    # 게시글 GET
    path('',board_list),

    # # 게시글 POST
    # path('',board_third),

    # 게시글 상세페이지
    path('<int:pk>/',board_detail),

    # 게시글 생성
    
    path('post/detail/<int:pk>/',board_detail),
    # path('post/update/<int:pk>/',board_fix),
    # path('post/delete/<int:pk>/',board_delete),
    # path('comment/create/<int:pk>',board_comment),

    path('<int:post_id>/comment/',create_comment),
    # path('comment/list/<int:post_id>/',get_comments),


    # 오류 생김
    # path('<int:post_id>/comment/<int:comment_id>/'),

    path('test/',board_list),
    

    
]