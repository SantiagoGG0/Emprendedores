from django import forms


class ValidationEntryForm(forms.Form):
    """Form para una entrevista de validación"""
    
    entrevistado = forms.CharField(
        label="Nombre/Perfil del entrevistado",
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Juan, agricultor de 45 años',
            'class': 'form-input'
        }),
        help_text="Sal a la calle y habla con minimo 3 personas de tu cliente ideal. A quien entrevistaste? Da nombre (puede ser ficticio), edad, ocupacion. Ejemplo: Pedro, 52 anos, dueno de tienda en el casco urbano."
    )
    
    pregunta_problema = forms.CharField(
        label="¿Confirmó tener el problema?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Sí/No y qué dijo exactamente...',
            'class': 'form-input'
        }),
        help_text="Primero valida el PROBLEMA antes de hablar de tu solucion. Pregunta: Ha tenido este problema? Con que frecuencia? Que tan grave es para usted? Escribe Si/No y copia textual lo que dijo. Esto es oro."
    )
    
    solucion_actual = forms.CharField(
        label="¿Cómo lo resuelve actualmente?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Qué hace hoy para resolver el problema...',
            'class': 'form-input'
        }),
        help_text="Pregunta: Como maneja este problema hoy? Que hace para resolverlo? Usa algun producto o servicio? Cuanto le cuesta (tiempo, plata, esfuerzo)? Entender su solucion actual te dice cuanto valor debes crear."
    )
    
    reaccion_idea = forms.CharField(
        label="Reacción a tu idea de solución",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Qué opinó de tu propuesta...',
            'class': 'form-input'
        }),
        help_text="Ahora SI presenta tu idea (no antes). Explica tu solucion en 2-3 oraciones. Cual fue su reaccion? Se emociono? Hizo preguntas? Fue indiferente? Que dijo textual? Busca senales genuinas de interes, no solo ser amable."
    )
    
    pagaria = forms.ChoiceField(
        label="¿Pagaría por tu solución?",
        choices=[
            ('si_seguro', 'Sí, definitivamente'),
            ('si_quizas', 'Tal vez'),
            ('no_seguro', 'Probablemente no'),
            ('no', 'No')
        ],
        widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
        help_text="Pregunta DIRECTA: Pagaria por esta solucion? Cuanto? La pregunta de dinero es incomoda pero ESENCIAL. Si dice Si pero no menciona precio, no es Si real. Si dice Tal vez, probablemente es No. Busca compromiso real."
    )
    
    precio_sugerido = forms.CharField(
        label="¿Cuánto pagaría?",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: $10,000 pesos por mes',
            'class': 'form-input'
        }),
        help_text="Si mencionó un precio, escríbelo"
    )
    
    aprendizajes = forms.CharField(
        label="Aprendizajes clave de esta entrevista",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Qué aprendiste de esta conversación...',
            'class': 'form-input'
        }),
        help_text="Reflexiona: Que aprendiste? Te sorprendio algo? Confirmo tus suposiciones o las contradijo? Necesitas cambiar algo de tu idea? Que harias diferente en la proxima entrevista? Estos aprendizajes son MAS valiosos que un Si."
    )
    
    def clean_pregunta_problema(self):
        value = self.cleaned_data.get('pregunta_problema', '')
        if len(value) < 20:
            raise forms.ValidationError('Describe más la respuesta (mínimo 20 caracteres)')
        return value
