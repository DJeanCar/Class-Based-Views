# encoding: utf-8
from django.shortcuts import render, redirect
from django.views.generic import (View, TemplateView, RedirectView, 
					DetailView, ListView, FormView, 
					CreateView, UpdateView, DeleteView)
from .models import Author
from .forms import AuthorForm

class IndexView1(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'view.html')

	def post(self, request, *args, **kwargs):
		return render(request, 'view.html')

class IndexView2(TemplateView):

	template_name = 'templateview.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView2, self).get_context_data(**kwargs)
		context['name'] = 'Jean Carlos'
		return context

class IndexView3(TemplateView):

	template_name = 'redirectview.html'

class OtraUrlView(RedirectView):

	# url = '/redirectview/'
	pattern_name = 'index3'

	def get_redirect_url(self, *args, **kwargs):
		# Aquí podemos poner nuestra lógica
		print "algo"
		return super(OtraUrlView, self).get_redirect_url(*args, **kwargs)

class DetalleView(DetailView):

	template_name = 'detalle.html'
	model = Author
	slug_field = 'name'
	context_object_name = 'author'


class ListaView(ListView):

	template_name = 'lista.html'
	model = Author
	context_object_name = 'authors'
	queryset = Author.objects.filter(age__lt = 18)

class FormularioView(FormView):

	template_name = 'formview.html'
	form_class = AuthorForm
	success_url = '/'

	def form_valid(self, form):
		# Aqui entra cuando los datos del formulario son validos
		form.save()
		return super(FormularioView, self).form_valid(form)

	def form_invalid(self, form):
		# Aqui entra cuando los datos del formulario son invalidos
		return super(FormularioView, self).form_invalid(form)


class CreacionView(CreateView):

	# form_class = AuthorForm
	model = Author
	template_name = 'createview.html'
	success_url = '/'
	fields = ('name', 'age', 'birth_date')


class ActualizarView(UpdateView):

	model = Author
	template_name = 'updateview.html'
	# success_url = '/'

	def get_success_url(self):
		return self.request.path

class BorrarView(DeleteView):

	model = Author
	template_name = 'deleteview.html'
	success_url = '/'