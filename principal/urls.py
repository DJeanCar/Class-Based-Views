from django.conf.urls import patterns, url
from .views import (IndexView1, IndexView2, IndexView3,
				OtraUrlView, DetalleView, ListaView, FormularioView,
				CreacionView,ActualizarView, BorrarView)

urlpatterns = patterns('',
	
	# View
    url(r'^view/$', IndexView1.as_view()),
    
    # TemplateView
    url(r'^templateview/$', IndexView2.as_view()),

    #RedirectView
    url(r'^redirectview/$', IndexView3.as_view(), name="index3"),
    url(r'^otra-url/$', OtraUrlView.as_view()),

    # DetailView
    url(r'^autor/(?P<slug>[-\w]+)/$', DetalleView.as_view()),

    # ListView
    url(r'^autores/$', ListaView.as_view()),

    # FormView
    url(r'^formview/$', FormularioView.as_view()),

    # CreateView
    url(r'^createview/$', CreacionView.as_view()),

    # UpdateView
    url(r'^autor/(?P<slug>[-\w]+)/actualizar/$', ActualizarView.as_view()),

    # DeleteView
    url(r'^autor/(?P<slug>[-\w]+)/borrar/$', BorrarView.as_view()),

)
