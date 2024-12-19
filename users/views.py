from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.shortcuts import redirect
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

class UserCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    form_class = CustomUserCreationForm
    template_name = 'user/sign_up.html'
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            ]
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

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = User
    template_name = 'user/sign_up.html'
    fields = [
        'username',
        'email',
        'last_name',
        'first_name',
    ]
    def get_success_url(self):
        # Utilisation de self.object.pk pour récupérer l'ID de l'utilisateur mis à jour
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})
    
    def form_invalid(self, form):
        print(form.errors)  # Affiche les erreurs du formulaire dans la console
        return super().form_invalid(form)
    
    def test_func(self):
        # Seul l'utilisateur connecté ou un superadmin peut modifier
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user

    def handle_no_permission(self):
        # Redirige vers la page du profil si l'utilisateur n'a pas la permission
        return redirect('home')

    def get_success_url(self):
        # Redirige vers le profil de l'utilisateur modifié après succès
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def test_func(self):
        # Seul l'utilisateur connecté ou un superadmin peut modifier
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user

    def handle_no_permission(self):
        # Redirige vers la page du profil si l'utilisateur n'a pas la permission
        return redirect('home')