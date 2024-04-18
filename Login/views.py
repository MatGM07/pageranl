from django.shortcuts import render, redirect
from .forms import UserCreationWithEmailForm
from django.contrib.auth import logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationWithEmailForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de inicio de sesión u otra página
            return redirect('Tienda')  # Reemplaza 'login' con el nombre de la URL de tu página de inicio de sesión
    else:
        form = UserCreationWithEmailForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')