from django.urls import path
from .views import (
    # work_item_detail,
    WorkItemDetailView,
    WorkItemUpdateView,
    WorkItemListView,
    WorkItemCreateView,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView)

app_name = "tasks"

urlpatterns = [
    path('item_list', WorkItemListView.as_view(), name="work_item_list"),
    path('create_item', WorkItemCreateView.as_view(), name="work_item_create"),
    path('item/<pk>/update', WorkItemUpdateView.as_view(), name="work_item_update"),
    path('item/<pk>/', WorkItemDetailView.as_view(), name="work_item_detail"),
    path('task_list', TaskListView.as_view(), name="task_list"),
    path('task_detail/<pk>', TaskDetailView.as_view(), name="task_detail"),
    path('task_create', TaskCreateView.as_view(), name="task_create"),
    path('task_update/<pk>', TaskUpdateView.as_view(), name="task_update"),

]