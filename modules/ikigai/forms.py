from django import forms
from django.core.exceptions import ValidationError


class IkigaiForm(forms.Form):
    """
    Formulario Ikigai: 4 preguntas fundamentales
    Usuario ingresa mínimo 3 respuestas por pregunta
    """
    
    # Pregunta 1: ¿Qué amas hacer?
    amas_1 = forms.CharField(
        label="Primera cosa que amas hacer",
        max_length=200,
        help_text="Que actividades haces con gusto, incluso sin que te paguen? Ejemplos: Cocinar para otros, reparar cosas, cuidar animales, enseñar a vecinos, organizar eventos, cultivar. Escribe al menos 3 respuestas. No hay respuestas correctas ni incorrectas.",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ej: Cocinar platos tradicionales'
        })
    )
    amas_2 = forms.CharField(
        label="Segunda cosa que amas hacer",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    amas_3 = forms.CharField(
        label="Tercera cosa que amas hacer",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    amas_4 = forms.CharField(
        label="Cuarta (opcional)",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    
    # Pregunta 2: ¿En qué eres bueno/a?
    bueno_1 = forms.CharField(
        label="Primera habilidad",
        max_length=200,
        help_text="En que te dicen los demas que eres bueno/a? Ejemplos: Eres muy detallista, siempre arreglas todo, cocinas sabroso, sabes tratar a los ninos, eres organizado/a. Piensa en lo que otros reconocen en ti.",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ej: Tejer mochilas wayuu'
        })
    )
    bueno_2 = forms.CharField(
        label="Segunda habilidad",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    bueno_3 = forms.CharField(
        label="Tercera habilidad",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    bueno_4 = forms.CharField(
        label="Cuarta (opcional)",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    
    # Pregunta 3: ¿Qué necesita tu comunidad?
    necesita_1 = forms.CharField(
        label="Primera necesidad",
        max_length=200,
        help_text="Que problemas ves en tu comunidad que a nadie mas parece importarle o que nadie ha resuelto? Ejemplos: Falta de mercado cercano, transporte caro, residuos sin manejo, productos agricolas sin procesar.",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ej: Transporte al pueblo'
        })
    )
    necesita_2 = forms.CharField(
        label="Segunda necesidad",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    necesita_3 = forms.CharField(
        label="Tercera necesidad",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    necesita_4 = forms.CharField(
        label="Cuarta (opcional)",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    
    # Pregunta 4: ¿Por qué pagarían?
    pagarian_1 = forms.CharField(
        label="Primer motivo de pago",
        max_length=200,
        help_text="Por que cosas estarian dispuestos a pagar las personas de tu comunidad? Ejemplos: Productos elaborados, servicios de limpieza, transporte, cuidado de adultos mayores, comida lista.",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ej: Productos frescos a domicilio'
        })
    )
    pagarian_2 = forms.CharField(
        label="Segundo motivo de pago",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    pagarian_3 = forms.CharField(
        label="Tercer motivo de pago",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    pagarian_4 = forms.CharField(
        label="Cuarto (opcional)",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    
    # Frase de intersección: síntesis del Ikigai
    interseccion = forms.CharField(
        label="Tu propósito (frase que conecte las 4 áreas)",
        max_length=500,
        help_text="Revisa tus respuestas y busca donde se cruzan. Hay algo que yo amo hacer, que se hacer bien, que mi comunidad necesita y que alguien pagaria por ello? Escribe esa interseccion en una sola frase. Ejemplo: Me encanta cocinar, soy buena en eso, en mi vereda no hay donde comprar comida preparada y las familias que trabajan todo el dia pagarian por un almuerzo listo.",
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'rows': 4,
            'placeholder': 'Ej: Ayudar a mi comunidad produciendo y vendiendo artesanías tradicionales que preservan nuestra cultura'
        })
    )
    
    def clean_interseccion(self):
        interseccion = self.cleaned_data.get('interseccion', '')
        if len(interseccion) < 50:
            raise ValidationError(
                "La frase de intersección debe tener al menos 50 caracteres para reflejar tu propósito completo"
            )
        return interseccion
    
    def get_ikigai_data(self):
        """Retorna datos estructurados para guardar como JSON en TextDeliverable"""
        if not self.is_valid():
            return None
        
        data = self.cleaned_data
        return {
            'que_amas': [
                data['amas_1'],
                data['amas_2'],
                data['amas_3'],
                data.get('amas_4', '')
            ],
            'en_que_eres_bueno': [
                data['bueno_1'],
                data['bueno_2'],
                data['bueno_3'],
                data.get('bueno_4', '')
            ],
            'que_necesita_comunidad': [
                data['necesita_1'],
                data['necesita_2'],
                data['necesita_3'],
                data.get('necesita_4', '')
            ],
            'por_que_pagarian': [
                data['pagarian_1'],
                data['pagarian_2'],
                data['pagarian_3'],
                data.get('pagarian_4', '')
            ],
            'frase_interseccion': data['interseccion']
        }
