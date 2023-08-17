from django.db import models


# Create your models here.
class Perfil(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    edad = models.SmallIntegerField()
    sexo = models.PositiveSmallIntegerField(choices=((1, 'M'), (2, 'F'), (3, 'NB'),))
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"""{self.nombre.upper()}"""


class Categoria(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return f"""{self.nombre.upper()}"""


class Trabajador(models.Model):
    info_trabajador = models.TextField()
    calificacion = models.PositiveSmallIntegerField()
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f"""{self.perfil.nombre} - {self.categoria.nombre}"""


class MetodoTransaccion(models.Model):
    tipo = models.PositiveSmallIntegerField(choices=((1, 'Cobro'), (2, 'Pago')))
    forma = models.PositiveSmallIntegerField(choices=(
        (1, 'Tarjeta de Crédito'),
        (2, 'Tarjeta de Débito'),
        (3, 'Paypal'),
        (4, 'MercadoPago'),
    ))
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE)

    def __str__(self):
        return f"""{self.get_forma_display()}"""


class Cliente(models.Model):
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE)

    def __str__(self):
        return f"""Cliente {self.perfil.nombre}"""


class Solicitud(models.Model):
    descripcion = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=(
        (1, 'Enviada'),
        (2, 'Recibida'),
        (3, 'Aceptada'),
        (4, 'Cancelada'),
    ))
    detalle_fecha = models.DateTimeField()
    detalle_duracion = models.CharField(max_length=25)
    trabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    Cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)


class Trabajo(models.Model):
    status = models.PositiveSmallIntegerField(choices=(
        (1, 'Aceptado'),
        (2, 'En progeso'),
        (3, 'Completado'),
        (4, 'Cancelado'),
    ))
    monto = models.FloatField()
    Solicitud = models.ForeignKey('Solicitud', on_delete=models.CASCADE)


class Critica(models.Model):
    mensaje = models.TextField()
    calificacion = models.DecimalField(decimal_places=2, max_digits=3)
    trabajo = models.ForeignKey('Trabajo', on_delete=models.CASCADE)
