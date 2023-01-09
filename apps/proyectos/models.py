from django.db import models

# Create your models here.

class Compra(models.Model):
    id_compra = models.AutoField(db_column='ID_Compra', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    proveedor = models.CharField(max_length = 50)  # Field name made lowercase.
    pagado = models.CharField(max_length = 50)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    id_proyecto = models.ForeignKey('Proyecto',db_column='ID_Proyecto', related_name = 'Compra', on_delete=models.SET_NULL, null = True)  # Field name made lowercase.
    id_materialconstruccion = models.ForeignKey('Materialconstruccion',  related_name = 'Compra', db_column='ID_MaterialConstruccion', on_delete=models.SET_NULL, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Compra'

    def __str__(self) -> str:
        texto = "{0} ({1})"
        return texto.format(self.cantidad, self.proveedor)


class Lider(models.Model):
    id_lider = models.AutoField(db_column='ID_Lider', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length = 50)  # Field name made lowercase.
    primer_apellido = models.CharField(max_length = 50)  # Field name made lowercase.
    segundo_apellido = models.CharField(max_length = 50)  # Field name made lowercase.
    salario = models.IntegerField(db_column='Salario')  # Field name made lowercase.
    ciudad_residencia = models.CharField(max_length = 50)  # Field name made lowercase.
    cargo = models.CharField(max_length = 50)  # Field name made lowercase.
    clasificacion = models.FloatField(db_column='Clasificacion')  # Field name made lowercase.
    documento_identidad = models.CharField(max_length = 50)  # Field name made lowercase.
    fecha_nacimiento = models.DateTimeField(db_column='Fecha_Nacimiento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lider'


class Materialconstruccion(models.Model):
    id_materialconstruccion = models.AutoField(db_column='ID_MaterialConstruccion', primary_key=True)  # Field name made lowercase.
    nombre_material = models.CharField(max_length = 50)  # Field name made lowercase.
    importado = models.CharField(max_length = 50)  # Field name made lowercase.
    precio_unidad = models.IntegerField(db_column='Precio_Unidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaterialConstruccion'


class Proyecto(models.Model):
    id_proyecto = models.AutoField(db_column='ID_Proyecto', primary_key=True)  # Field name made lowercase.
    fecha_inicio = models.DateTimeField(db_column='Fecha_Inicio')  # Field name made lowercase.
    constructora = models.CharField(max_length = 50)  # Field name made lowercase.
    numero_banos = models.FloatField(db_column='Numero_Banos')  # Field name made lowercase.
    numero_habitaciones = models.FloatField(db_column='Numero_Habitaciones')  # Field name made lowercase.
    banco_vinculado = models.CharField(max_length = 50)  # Field name made lowercase.
    porcentaje_cuota_inicial = models.FloatField(db_column='Porcentaje_Cuota_Inicial')  # Field name made lowercase.
    ciudad = models.CharField(max_length = 50)  # Field name made lowercase.
    clasificacion = models.CharField(max_length = 50)  # Field name made lowercase.
    acabados = models.CharField(max_length = 50)  # Field name made lowercase.
    serial = models.CharField(max_length = 50)  # Field name made lowercase.
    id_tipo = models.ForeignKey('Tipo', db_column='ID_Tipo',related_name = 'Proyecto',on_delete=models.SET_NULL, null = True)  # Field name made lowercase.
    id_lider = models.ForeignKey('Lider',db_column='ID_Lider',related_name = 'Proyecto',on_delete=models.SET_NULL, null = True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proyecto'


class Tipo(models.Model):
    id_tipo = models.AutoField(db_column='ID_Tipo', primary_key=True)  # Field name made lowercase.
    codigo_tipo = models.IntegerField(db_column='Codigo_Tipo')  # Field name made lowercase.
    area_max = models.IntegerField(db_column='Area_Max')  # Field name made lowercase.
    financiable = models.IntegerField(db_column='Financiable')  # Field name made lowercase.
    estrato = models.IntegerField(db_column='Estrato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo'
