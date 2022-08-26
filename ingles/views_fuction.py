"""
def crearEstudiante(request):
    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST)
        if estudiante_form.is_valid():
            estudiante_form.save()
            return redirect('index')
        
    else:
        estudiante_form = EstudianteForm()
    return render(request,'ingles/crear_estudiante.html',{'estudiante_form':estudiante_form})

def listaEstudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'ingles/listar_estudiante.html', {'estudiantes': estudiantes})

def editarEstudiante(request, idestudiante):
    estudiante_form = None
    error = None
    try:
        estudiante = Estudiante.objects.get(idestudiante = idestudiante )
        if request.method == 'GET':
            estudiante_form = EstudianteForm(instance = estudiante)
        else:
            estudiante_form = EstudianteForm(request.POST, instance = estudiante)
            if estudiante_form.is_valid():
                estudiante_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'ingles/crear_estudiante.html',{'estudiante_form':estudiante_form, 'error':error})

def elimarEstudiante(request, idestudiante):
    estudiante = Estudiante.objects.get(idestudiante = idestudiante )
    if request.method == 'POST':
        estudiante.delete()
        return redirect('ingles:listar_estudiante')
    return render(request, 'ingles/eliminar_autor.html', {'estudiante': estudiante})
    """