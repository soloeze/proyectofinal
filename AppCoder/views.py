from django.shortcuts import render
from .models import Tarea, Personas_del_equipo, Contacto
from .forms import CustomUserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def home(request):
    return render(request,'AppCoder/home.html')

#@login_required
@method_decorator(login_required, name='dispatch')
class TareaList(ListView):
    model = Tarea
    template_name="AppCoder/Tarea/tareas_list.html"

@method_decorator(login_required, name='dispatch')
class TareaCreacion(CreateView):
    model = Tarea
    fields = '__all__'
    template_name="AppCoder/Tarea/tarea_form.html"
    success_url = '/tarea/list/'

@method_decorator(login_required, name='dispatch')
class TareaEdit(UpdateView):
    model = Tarea
    fields= '__all__'
    template_name="AppCoder/Tarea/tarea_modificar.html"
    success_url= '/tarea/list'

@method_decorator(login_required, name='dispatch')
class TareaDelete(DeleteView):
    model = Tarea
    template_name="AppCoder/Tarea/tarea_confirm_delete.html"
    success_url= '/tarea/list'  

@method_decorator(login_required, name='dispatch')
class TareaDetail(DetailView):
    model = Tarea
    template_name="AppCoder/Tarea/tarea_detail.html"

@login_required
def buscarResultadoTarea(request):
    nombre_bus_views = request.GET['nombreBuscado']
    nombre_bus_res = Tarea.objects.filter(nombre=nombre_bus_views.strip())
    return render(request,'AppCoder/Tarea/resultadoDeBusqueda.html',{"nombre_view":nombre_bus_views, "nom_res":nombre_bus_res})

@login_required
def buscarTarea(request):
    return render(request,'AppCoder/Tarea/busqueda.html')


# Personas del Equipo
@method_decorator(login_required, name='dispatch')
class PersonasDelEquipoList(ListView):
    model = Personas_del_equipo
    template_name="AppCoder/PersonasDelEquipo/pde_list.html"

@method_decorator(login_required, name='dispatch')
class PersonasDelEquipoCreacion(CreateView):
    model = Personas_del_equipo
    fields = '__all__'
    template_name="AppCoder/PersonasDelEquipo/pde_form.html"
    success_url = '/personasdelequipo/list/'

@method_decorator(login_required, name='dispatch')
class PersonasDelEquipoEdit(UpdateView):
    model = Personas_del_equipo
    fields= '__all__'
    template_name="AppCoder/PersonasDelEquipo/pde_modificar.html"
    success_url= '/personasdelequipo/list'

@method_decorator(login_required, name='dispatch')
class PersonasDelEquipoDelete(DeleteView):
    model = Personas_del_equipo
    template_name="AppCoder/PersonasDelEquipo/pde_confirm_delete.html"
    success_url= '/personasdelequipo/list'  

@method_decorator(login_required, name='dispatch')
class PersonasDelEquipoDetail(DetailView):
    model = Personas_del_equipo
    template_name="AppCoder/PersonasDelEquipo/pde_detail.html"

@login_required
def buscarResultadoPersonasDelEquipo(request):
    nombre_bus_views = request.GET['nombreBuscado']
    nombre_bus_res = Personas_del_equipo.objects.filter(nombre=nombre_bus_views.strip())
    return render(request,'AppCoder/PersonasDelEquipo/resultadoDeBusqueda.html',{"nombre_view":nombre_bus_views, "nom_res":nombre_bus_res})

@login_required
def buscarPersonasDelEquipo(request):
    return render(request,'AppCoder/PersonasDelEquipo/busqueda.html')

# Contacto
@method_decorator(login_required, name='dispatch')
class ContactoList(ListView):
    model = Contacto
    template_name="AppCoder/Contacto/contacto_list.html"

@method_decorator(login_required, name='dispatch')
class ContactoCreacion(CreateView):
    model = Contacto
    fields = '__all__'
    template_name="AppCoder/Contacto/contacto_form.html"
    success_url = '/contacto/list/'

@method_decorator(login_required, name='dispatch')
class ContactoEdit(UpdateView):
    model = Contacto
    fields= '__all__'
    template_name="AppCoder/Contacto/contacto_modificar.html"
    success_url= '/contacto/list'

@method_decorator(login_required, name='dispatch')
class ContactoDelete(DeleteView):
    model = Contacto
    template_name="AppCoder/Contacto/contacto_confirm_delete.html"
    success_url= '/contacto/list'  

@method_decorator(login_required, name='dispatch')
class ContactoDetail(DetailView):
    model = Contacto
    template_name="AppCoder/Contacto/contacto_detail.html"

@login_required
def buscarResultadoContacto(request):
    nombre_bus_views = request.GET['nombreBuscado']
    nombre_bus_res = Contacto.objects.filter(nombre=nombre_bus_views.strip())
    return render(request,'AppCoder/Contacto/resultadoDeBusqueda.html',{"nombre_view":nombre_bus_views, "nom_res":nombre_bus_res})

@login_required
def buscarContacto(request):
    return render(request,'AppCoder/Contacto/busqueda.html')

# Login 
def registro(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #Redirigir al home
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            return redirect(to='home')
        data['form']=formulario
    return render(request, 'registration/registro.html',data)