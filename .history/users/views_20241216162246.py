from django import forms
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
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nom d’utilisateur', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Adresse email', 'required': True}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'required': True}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe', 'required': True}),
        }
    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})  # Utilise l'ID de l'utilisateur créé
    def form_invalid(self, form):
        print(form.errors)  # Affiche les erreurs du formulaire dans la console
        return super().form_invalid(form)
    
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