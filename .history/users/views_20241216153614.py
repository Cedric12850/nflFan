from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    template_name = 'users/user_form.html'
    fields = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    ]
    success_url = reverse_lazy('user:user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password('defaultpassword')
        user.save()
        return super().form_valid(form)
    
class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

