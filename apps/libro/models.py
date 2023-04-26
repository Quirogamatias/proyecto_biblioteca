from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save,pre_save
from apps.usuario.models import Usuario
from datetime import timedelta

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key= True)
    dni = models.CharField('DNI del alumno',max_length=100, null=False, blank = False)
    nombre = models.CharField('Nombre del Alumno',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del alumno',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    domicilio = models.CharField('domicilio del alumno',max_length=100, null=False, blank = False)
    telefono = models.CharField('telefono del alumno',max_length=100, null=False, blank = False)
    estado = models.BooleanField('Alumno activado/no activado', default= True)
    notificacion = models.BooleanField('notificacion activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
    id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, null=True, blank = True)
    
    def natural_key(self):
        #return self.apellido
        return f'Apellido {self.apellido}, Nombre {self.nombre}'
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['apellido']

    def __str__(self):
        return f'Apellido {self.apellido}, Nombre {self.nombre}'

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre del Administrador',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del Administrador',max_length=100, null=False, blank = False)
    telefono =models.CharField('Telefono del Administrador',max_length=100, null=False, blank = False)
    domicilio = models.CharField('Domicilio del Administrador',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    estado = models.BooleanField('Administrador activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, null=True, blank = True)
    
    def natural_key(self):
        return f'Administrador {self.apellido}, Nombre {self.nombre}'

    class Meta:
        verbose_name = 'Bibliotecario'
        verbose_name_plural = 'Bibliotecarios'
        ordering = ['apellido']

    def __str__(self):
        return f'Administrador {self.apellido}, Nombre {self.nombre}'

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key= True)
    dni = models.CharField('Dni',max_length=100, null=False, blank = False)
    nombre = models.CharField('Nombre del profesor',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del profesor',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    estado = models.BooleanField('Profesor activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, null=True, blank = True)
    #t = (
     #   (True,'activo'),
      #  (False,'desactivado'),
    #)
    #notificacion = models.BooleanField('notificacion activado/no activado',choices=t, default= True,null=True, blank = True)
    #id_materia = models.ManyToManyField(Materia)
    
    def natural_key(self):
        return f'Profesor {self.apellido}, Nombre {self.nombre}'
        
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['apellido']

    def __str__(self):
        return f'Profesor {self.apellido}, Nombre {self.nombre}'

"""class Autor(models.Model):
    id: models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=200, blank= False,null=False)
    apellidos = models.CharField(max_length=200, blank= False,null=False)
    nacionalidad = models.CharField(max_length= 100,blank=False, null=False)
    descripcion = models.TextField(blank=False, null= False,default='')
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
    
    def natural_key(self):
        return f'{self.nombre} {self.apellidos}'

    def __str__(self):
        return self.nombre"""

class Libro(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('titulo',max_length= 255,blank=False,null=False)
    fecha_publicacion = models.DateField('fecha de publicacion',blank= False,null=False)
    descripcion = models.TextField('Descripción',null = True,blank = True)
    cantidad = models.PositiveIntegerField('Cantidad o Stock',default = 1)
    imagen = models.ImageField('Imagen', upload_to='libros/',max_length=255,null = True,blank = True)
    cant_pedido = models.PositiveIntegerField('cantidad de pedidos',default = 0)
    #autor_id = models.ManyToManyField(Autor)
    e = (
        ('Buena','Buena'),
        ('Mala','Mala'),
        ('Perdido','Perdido'),
    )
    estado_libro =  models.CharField('estado del libro',max_length=100,choices=e, null=False, blank = False)   
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)
    estado = models.BooleanField(default = True,verbose_name = 'Estado')

    def natural_key(self):
        return self.titulo
        
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
    
    #def obtener_autores(self):
     #   autores = str([autor for autor in self.autor_id.all().values_list('nombre',flat = True)]).replace("[","").replace("]","").replace("'","")
      #  return autores

class Reserva(models.Model):
    """Model definition for Reserva."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_dias = models.SmallIntegerField('Cantidad de Dias a Reservar',default = 7)    
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_vencimiento = models.DateField('Fecha de vencimiento de la reserva', auto_now=False, auto_now_add=False, null = True, blank = True)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        return f'Reserva de Libro: {self.libro}, por el usuario: {self.usuario}'

    class Meta:
        """Meta definition for Reserva."""

        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        """Unicode representation of Reserva."""
        return f'Reserva de Libro: {self.libro}, por el usuario: {self.usuario}'

#def quitar_relacion_autor_libro(sender,instance,**kwargs):
 #   if instance.estado == False:
  #      autor = instance.id
   #     libros = Libro.objects.filter(autor_id=autor)
    #    for libro in libros:
     #       libro.autor_id.remove(autor)

def reducir_cantidad_libro(sender,instance,**kwargs):
    libro = instance.libro
    if libro.cantidad > 0:
        libro.cantidad = libro.cantidad - 1
        libro.save()

def validar_creacion_reserva(sender,instance,**kwargs):
    libro = instance.libro
    if libro.cantidad < 1:
        raise Exception("No puede realizar esta reserva")

def agregar_fecha_vencimiento_reserva(sender,instance,**kwargs):
    if instance.fecha_vencimiento is None or instance.fecha_vencimiento == '':
        instance.fecha_vencimiento = instance.fecha_creacion + timedelta(days = instance.cantidad_dias)
        instance.save()

class Entrega_libro(models.Model):
    id = models.AutoField(primary_key= True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha_entrega = models.DateField('fecha de entrega',blank= False,null=False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)
    estado = models.BooleanField(default = True,verbose_name = 'Estado')

    def natural_key(self):
        #return str(self.fecha_entrega)
        return f'{self.id_reserva}, Fecha de entrega del libro: {self.fecha_entrega}'
        
    class Meta:
        verbose_name = 'fecha de entrega del libro al alumno'
        verbose_name_plural = 'fecha de entrega del libro al alumno'
        ordering = ['fecha_entrega']

    def __str__(self):
        #return str(self.fecha_entrega)
        return f'{self.id_reserva}, Fecha de entrega del libro: {self.fecha_entrega}'

class Devolucion_libro(models.Model):
    id = models.AutoField(primary_key= True)
    id_entrega = models.ForeignKey(Entrega_libro, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField('fecha de devolucion',blank= False,null=False)
    e = (
        ('Buena','Buena'),
        ('Mala','Mala'),
        ('Perdido','Perdido'),
    )
    estado_libro =  models.CharField('estado del libro',max_length=100,choices=e, null=False, blank = False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)
    estado = models.BooleanField(default = True,verbose_name = 'Estado')

    def natural_key(self):
        return str(self.fecha_devolucion)
        
    class Meta:
        verbose_name = 'fecha de devolucion del libro a la biblioteca'
        verbose_name_plural = 'fecha de devolucion del libro a la biblioteca'
        ordering = ['fecha_devolucion']

    def __str__(self):
        return str(self.fecha_devolucion)

#post_save.connect(quitar_relacion_autor_libro,sender = Autor)
post_save.connect(reducir_cantidad_libro,sender = Reserva)
pre_save.connect(validar_creacion_reserva,sender = Reserva)
post_save.connect(agregar_fecha_vencimiento_reserva,sender = Reserva)

