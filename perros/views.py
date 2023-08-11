from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from perros.models import Perro,Comentario
from perros.forms import PerroFormulario,FormularioComentario

def sobre_mi(request):
    return render(request, 'perros/sobre_mi.html', {})

class PerroListView(LoginRequiredMixin, ListView):
    model = Perro
    context_object_name = 'perros'
    template_name = 'perros/lista_perros.html'

#class PerroCreateView(LoginRequiredMixin, CreateView):
#    model = Perro
#    fields = ('nombre', 'raza', 'edad', 'telefono','duenio','foto')
#    success_url = reverse_lazy('lista_perros')

class PerroCreateView(LoginRequiredMixin, CreateView):
    model = Perro
    form_class = PerroFormulario
    success_url = reverse_lazy('inicio')
    template_name = 'perros/perro_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PerroCreateView, self).form_valid(form)

#def PerroCreateView(request):
#    if request.method == "POST":
#        formulario = PerroFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

#        if formulario.is_valid():
#            perro = formulario.save()
#            perro.user = request.user
#            perro.save()
#           url_exitosa = reverse('inicio')
#            return redirect(url_exitosa)
#    else:  # GET
#        formulario = PerroFormulario()
#    return render(
#        request=request,
#        template_name="perros/perro_form.html",
 #       context={'form': formulario},
  #  )

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'perros/comentario.html'
    success_url = reverse_lazy('lista_perros')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)


class PerroDetailView(LoginRequiredMixin, DetailView):
    model = Perro
    success_url = reverse_lazy('lista_perros')


class PerroUpdateView(LoginRequiredMixin, UpdateView):
    model = Perro
    fields = ('nombre', 'raza', 'edad', 'telefono','duenio','foto')
    success_url = reverse_lazy('lista_perros')


class PerroDeleteView(LoginRequiredMixin, DeleteView):
    model = Perro
    success_url = reverse_lazy('lista_perros')