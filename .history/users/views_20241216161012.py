from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

from users.forms import CustomUserCreationForm


User = get_user_model()
# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/sign_up.html'
    success_url = reverse_lazy('user_detail')
    
class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_update.html'
    fields = [
        'username',
        'email',
        'last_name',
        'first_name',
    ]
    success_url = reverse_lazy('user_detail')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')