from MecanicaApp.models import Station
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re


class registerForm(forms.Form):
    user = forms.CharField(label="Usuario", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su usuario'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese una contraseña'}))
    name = forms.CharField(label="Nombre", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(label="Apellido", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su apellido'}))
    cellphone = forms.CharField(label="Teléfono", max_length=10, widget=forms.NumberInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su teléfono'}))
    ci = forms.CharField(label="Cédula", max_length=10, widget=forms.NumberInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su cédula'}))
    direction = forms.CharField(label="Dirección", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su dirección'}))
    email = forms.EmailField(label="Correo", widget=forms.EmailInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su correo'}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.search(r'\d', name):
            raise ValidationError('El nombre no puede contener números.')
        return name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.search(r'\d', last_name):
            raise ValidationError('El apellido no puede contener números.')
        return last_name

    def clean_cellphone(self):
        cellphone = self.cleaned_data.get('cellphone')
        if not cellphone.isdigit() or len(cellphone) != 10:
            raise ValidationError('El teléfono debe contener exactamente 10 dígitos.')
        return cellphone

    def clean_ci(self):
        ci = self.cleaned_data.get('ci')
        if not ci.isdigit() or len(ci) != 10:
            raise ValidationError('La cédula debe contener exactamente 10 dígitos.')
        return ci


# class customer_form(forms.Form):
class EmailForm(forms.Form):
    email = forms.EmailField(label="Ingresa tu correo", widget=forms.EmailInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su corrreo'}))


class passwordForm(forms.Form):
    password = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese una contraseña'}))
    password_confirmation = forms.CharField(label="Confirmar nueva contraseña", widget=forms.PasswordInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese una contraseña'}))


class tokenForm(forms.Form):
    token = forms.CharField(label="Ingrese el token enviado a su correo", max_length=10, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese el token'}))


class loginForm(forms.Form):
    user = forms.CharField(label="Usuario", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': 'input form-control', 'placeholder': 'Contraseña'}))


class crearEmpleadoForm(forms.Form):
    nombreEmpleado = forms.CharField(
        label="Nombre",
        max_length=400,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2',
            'placeholder': 'Ingrese el nombre del empleado'
        })
    )

    apellidoEmpleado = forms.CharField(
        label="Apellido",
        max_length=800,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2',
            'placeholder': 'Ingrese el apellido del empleado'
        })
    )

    estacionEmpleado = forms.ModelChoiceField(
        label="Estación",
        queryset=Station.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mt-2'})
    )

    correoEmpleado = forms.CharField(
        label="Correo",
        required=False,  # Aseguramos que no sea obligatorio
        max_length=800,
        widget=forms.EmailInput(attrs={
            'class': 'form-control mt-2',
            'placeholder': 'Ingrese el correo del empleado'
        }),
        validators=[EmailValidator(message="Ingrese un correo electrónico válido.")]
        # Correcto uso de EmailValidator
    )


# Validación personalizada para nombre (solo letras)
def clean_nombreEmpleado(self):
    nombre = self.cleaned_data.get('nombreEmpleado')
    if not nombre.isalpha():
        raise ValidationError('El nombre solo puede contener letras.')
    return nombre


# Validación personalizada para apellido (solo letras)
def clean_apellidoEmpleado(self):
    apellido = self.cleaned_data.get('apellidoEmpleado')
    if not apellido.isalpha():
        raise ValidationError('El apellido solo puede contener letras.')
    return apellido


# Validación de correo (debe ser un correo válido)
def clean_correoEmpleado(self):
    correo = self.cleaned_data.get('correoEmpleado')
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        raise ValidationError('Ingrese un correo electrónico válido.')
    return correo

    # Validación personalizada para el año
    def clean_año(self):
        año = self.cleaned_data.get('año')
        if len(año) != 4 or not año.isdigit():
            raise forms.ValidationError("El año debe contener exactamente 4 dígitos.")
        return año

    # Validación personalizada para la placa
    def clean_placa(self):
        placa = self.cleaned_data.get('placa')
        if not placa.isupper():
            raise forms.ValidationError("La placa debe estar en mayúsculas.")
        if len(placa) < 7 or len(placa) > 8:
            raise forms.ValidationError("La placa debe tener entre 7 y 8 caracteres.")
        return placa

    # Validación personalizada para el color
    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color.isalpha():
            raise forms.ValidationError("El color solo puede contener letras.")
        return color

class crearServicioForm(forms.Form):
    nombreServicio = forms.CharField(
        label="Nombre",
        max_length=400,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2',
            'placeholder': 'Ingrese el nombre del servicio'
        })
    )
    descripcionServicio = forms.CharField(
        label="Descripción",
        max_length=800,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2',
            'placeholder': 'Ingrese la descripción del servicio'
        })
    )
    precioServicio = forms.DecimalField(
        label="Precio",
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2',
            'placeholder': 'Ingrese el precio del servicio'
        }),
        error_messages={
            'invalid': 'Por favor, ingrese un valor numérico válido.',
        }
    )

    estacionServicio = forms.ModelChoiceField(
        label="Estación",
        queryset=Station.objects.all(),  # Obtiene todas las estaciones de la base de datos
        widget=forms.Select(attrs={'class': 'form-control mt-2'})  # Estilo para la lista desplegable
    )

    def clean_precioServicio(self):
        precio = self.cleaned_data.get('precioServicio')
        if precio is not None and precio.as_integer_ratio()[1] > 100:  # Chequea los decimales
            raise ValidationError('El precio no puede tener más de 2 decimales.')
        return precio


class QRCodeForm(forms.Form):
    qr_code = forms.ImageField()


class PaymentForm(forms.Form):
    METODO_PAGO_CHOICES = [
        ('transferencia', 'Transferencia'),
        ('ventanilla', 'Pago en ventanilla'),
    ]

    metodo_pago = forms.ChoiceField(
        choices=METODO_PAGO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-label'})
    )


class TransferenciaForm(forms.Form):
    file = forms.FileField(label='Selecciona un archivo', widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'id': 'formFile', 'accept': 'image/*,.pdf'}))


class PaymentForm(forms.Form):
    METODO_PAGO_CHOICES = [
        ('transferencia', 'Transferencia'),
        ('ventanilla', 'Pago en ventanilla'),
    ]

    metodo_pago = forms.ChoiceField(
        choices=METODO_PAGO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-label'})
    )


class TransferenciaImgForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'style': 'padding: 10px; font-size: 1rem; border: 1px solid #ccc; border-radius: 5px;'
        })
    )
class retirarAutoForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(label="Apellido", max_length=200, widget=forms.TextInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su apellido'}))
    ci = forms.CharField(label="Cédula", max_length=200, widget=forms.NumberInput(
        attrs={'class': 'input form-control', 'placeholder': 'Ingrese su cédula'}))
    file = forms.ImageField(label='Selecciona un archivo', widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'id': 'formFile', 'accept': 'image/*,.pdf'}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.search(r'\d', name):
            raise ValidationError('El nombre no puede contener números.')
        return name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.search(r'\d', last_name):
            raise ValidationError('El apellido no puede contener números.')
        return last_name

    def clean_cellphone(self):
        cellphone = self.cleaned_data.get('cellphone')
        if not cellphone.isdigit() or len(cellphone) != 10:
            raise ValidationError('El teléfono debe contener exactamente 10 dígitos.')
        return cellphone

    def clean_ci(self):
        ci = self.cleaned_data.get('ci')
        if not ci.isdigit() or len(ci) != 10:
            raise ValidationError('La cédula debe contener exactamente 10 dígitos.')
        return ci


# 4 QR
class QRCodeForm(forms.Form):
    qr_code = forms.ImageField(
        label="Sube tu código QR",
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'formFile',
                'accept': 'image/*',
                'style': 'max-width: 560px; width: 100%; font-size: 18px; margin-top:18px'
            }
        )
    )

