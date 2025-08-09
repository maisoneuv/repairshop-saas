from django.shortcuts import render, redirect, reverse

from customers.models import Customer
from service.models import Employee, Location
from .models import WorkItem, Task
from .forms import WorkItemForm, TaskForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView


# def work_item_list(request):
#     items = WorkItem.objects.all()
#     context = {
#         "items": items
#     }
#     return render(request, "tasks/work_item_list.html", context)


class WorkItemListView(ListView):
    template_name = "tasks/work_item_list.html"
    queryset = WorkItem.objects.all()
    context_object_name = "items"


class WorkItemDetailView(DetailView):
    template_name = "tasks/work_item_detail.html"
    model = WorkItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # `self.object` is the WorkItem instance being displayed.
        context["tasks"] = self.object.tasks.all()

        return context


# def work_item_detail(request, pk):
#     print(pk)
#     item = WorkItem.objects.get(id=pk)
#     context = {
#         "item": item
#     }
#     return render(request, "tasks/work_item_detail.html", context)

class WorkItemCreateView(CreateView):
    template_name = "tasks/work_item_create.html"
    # template_name = "tasks/create_work_item.html"
    form_class = WorkItemForm
    model = WorkItem

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user

        if hasattr(user, 'employee'):
            initial['owner'] = user.employee
            initial['customer_dropoff_point'] = user.employee.location

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'employee'):
            context['initial_owner'] = user.employee
            context['initial_customer_dropoff_point'] = user.employee.location
        else:
            None

        context['employees'] = Employee.objects.all() 
        context['locations'] = Location.objects.all() 

        return context
    
    def form_valid(self, form):
        request = self.request.POST

        print(request)
        response = super().form_valid(form)
        form.save()
        print(response)
        return response
    
    def form_invalid(self, form):
        request = self.request.POST

        print(request)
        print("Form is invalid. Errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
    


# def work_item_create(request):
#     form = WorkItemForm()
#     if request.method == "POST":
#         form = WorkItemForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/tasks")
#     context = {
#         "form": form
#     }
#
#     return render(request, "tasks/work_item_create.html", context)


class WorkItemUpdateView(UpdateView):
    template_name = "tasks/work_item_update.html"
    queryset = WorkItem.objects.all()
    form_class = WorkItemForm

    def get_success_url(self):
        return reverse("tasks:work_item_list")


# def work_item_update(request, pk):
#     item = WorkItem.objects.get(id=pk)
#     form = WorkItemForm(instance=item)
#     if request.method == "POST":
#         form = WorkItemForm(request.POST, instance=item)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/tasks/item/" + pk)
#     context = {
#         "form": form,
#         "item": item
#     }
#
#     return render(request, "tasks/work_item_update.html", context)


class TaskListView(ListView):
    template_name = "tasks/task_list.html"
    queryset = Task.objects.all()
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    template_name = "tasks/task_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"


class TaskCreateView(CreateView):
    template_name = "tasks/task_create.html"
    form_class = TaskForm

    def get_success_url(self):
        return reverse("tasks:task_list")


class TaskUpdateView(UpdateView):
    template_name = "tasks/task_update.html"
    queryset = Task.objects.all()
    form_class = TaskForm

    def get_success_url(self):
        return reverse("tasks:task_list")
