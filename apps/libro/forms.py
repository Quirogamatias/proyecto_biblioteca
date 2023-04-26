from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms.widgets import SelectDateWidget

"""class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre': 'Nombre del autor',
            'apellidos': 'Apellidos del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Pequeña descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del autor'
                }
            ),
            'nacionalidad':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una nacionalidad para el autor'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion para el autor'
                }
            )
        }
        """

class ReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['libro'].queryset = Libro.objects.filter(estado = True,cantidad__gte = 1)

    class Meta:
        model = Reserva
        fields = '__all__'
    
    def clean_libro(self):
        libro = self.cleaned_data['libro']
        if libro.cantidad < 1:
            raise ValidationError('No se puede reservar este libro, deben existir unidades disponibles.')

        return libro

class LibroForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['autor_id'].queryset = Autor.objects.filter(estado = True)
        
    class Meta:
        model = Libro
        fields = ['titulo','fecha_publicacion','descripcion','imagen','cantidad','estado_libro']
        label = {
            'titulo': 'Titulo del libro',
            'fecha_publicacion': 'Fecha de Publicacion del libro',
            'estado_libro': 'estado del libro',
        }
        widgets = {
            'titulo':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese titulo de libro'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }
    
class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','notificacion','id_usuario']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',            
            'notificacion': 'notificacion del Alumno',
            'id_usuario': 'id_usuario',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del alumno'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del alumno'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Alumno2Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_carrera'].queryset = Carrera.objects.filter(estado = True)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','notificacion','id_usuario']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'notificacion': 'notificacion del Alumno',
            'id_usuario': 'id_usuario',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del alumno'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del alumno'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                    
                }
            ),
            'id_usuario':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            )
        }

class Alumno3Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['id_carrera'].queryset = Carrera.objects.filter(estado = True)
        #self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','notificacion']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'notificacion': 'notificacion del Alumno',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                    
                }
            )
        }


class Entrega_libroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_reserva'].queryset = Entrega_libro.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro
        fields = ('id_reserva','fecha_entrega')
        label = {
            'id_reserva': 'reserva del libro',
            'fecha_entrega': 'Fecha de entrega del libro'
        }
        widgets = {
            'id_reserva': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
    

class AdministradorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Administrador
        fields = ['nombre','apellido','telefono','domicilio','email','id_usuario']
        labels = {
            'nombre': 'nombre del administrador',
            'apellido': 'apellido del administrador',
            'telefono': 'telefono del administrador',
            'domicilio': 'domicilio del administrador ',
            'email': 'email del administrador',
            'id_usuario': 'id_usuario',

        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del administrador'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del administrador'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del administrador'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del administrador'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del administrador'
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )          
        }

class ProfesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Profesor
        fields = ['dni','nombre','apellido','email','id_usuario']
        labels = {
            'dni': 'dni del profesor',
            'nombre': 'nombre del profesor',
            'apellido': 'apellido del profesor',
            'email': 'email del profesor ',
            'id_usuario': 'id_usuario',

        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del profesor'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del profesor'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del profesor'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del profesor'
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Profesor2Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Profesor
        fields = ['dni','nombre','apellido','email']
        labels = {
            'dni': 'dni del profesor',
            'nombre': 'nombre del profesor',
            'apellido': 'apellido del profesor',
            'email': 'email del profesor ',

        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del profesor'
                }
            )
        }

class Entrega_libroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_reserva'].queryset = Reserva.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro
        fields = ['id_reserva','fecha_entrega']
        label = {
            'id_reserva': 'reserva del libro',
            'fecha_entrega': 'Fecha de entreg del libro al alumno',
        }
        widgets = {
            'id_reserva': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            )
        }
    
class Devolucion_libroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_entrega'].queryset = Entrega_libro.objects.filter(estado = True)
        
    class Meta:
        model = Devolucion_libro
        fields = ['id_entrega','fecha_devolucion','estado_libro']
        label = {
            'id_entrega': 'Entrega del libro',
            'fecha_devolucion': 'Fecha de devolucion del libro a la biblioteca',
            'estado_libro': 'estado del libro en la devolucion',
        }
        widgets = {
            'id_entrega': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_devolucion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }
    