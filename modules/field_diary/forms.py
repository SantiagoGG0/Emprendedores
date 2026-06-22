from django import forms


class DiaryEntryForm(forms.Form):
    """Form para una entrada del diario de campo"""
    
    situacion = forms.CharField(
        label="Situación problemática observada",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Describe la situación o problema que observaste en tu comunidad...',
            'class': 'form-input'
        }),
        help_text="Sal a tu comunidad y observa con ojos nuevos. Que problema, necesidad o situacion dificil ves? Describe lo que observaste como si le contaras a alguien que nunca ha estado alli. Ejemplos: No hay transporte despues de las 6pm, las madres tienen que cargar agua desde lejos, los jovenes no tienen donde reunirse. Se especifico y concreto."
    )
    
    personas_afectadas = forms.CharField(
        label="¿Quiénes están afectados?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Ej: Madres cabeza de familia, jóvenes sin empleo, comerciantes locales...',
            'class': 'form-input'
        }),
        help_text="Quienes sufren este problema? Piensa en grupos especificos: madres cabeza de familia, campesinos, comerciantes, estudiantes, adultos mayores. Cuantas personas aproximadamente? Son del casco urbano o la zona rural?"
    )
    
    contexto = forms.CharField(
        label="Contexto y detalles",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Describe dónde, cuándo y en qué circunstancias ocurre...',
            'class': 'form-input'
        }),
        help_text="Donde ocurre? (barrio, vereda, lugar especifico). Cuando pasa? (todo el tiempo, solo en ciertas horas/dias). Que mas notaste? Temperatura, olores, sonidos, expresiones de la gente. Estos detalles ayudan a entender mejor el problema."
    )
    
    foto = forms.ImageField(
        label="Foto (opcional)",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-input',
            'accept': 'image/*'
        }),
        help_text="Puedes subir una foto que ilustre la situación observada"
    )
    
    def clean_situacion(self):
        situacion = self.cleaned_data.get('situacion', '')
        if len(situacion) < 20:
            raise forms.ValidationError('Describe la situación con más detalle (mínimo 20 caracteres)')
        return situacion
    
    def clean_personas_afectadas(self):
        personas = self.cleaned_data.get('personas_afectadas', '')
        if len(personas) < 10:
            raise forms.ValidationError('Describe quiénes están afectados (mínimo 10 caracteres)')
        return personas
    
    def clean_contexto(self):
        contexto = self.cleaned_data.get('contexto', '')
        if len(contexto) < 20:
            raise forms.ValidationError('Agrega más contexto sobre la situación (mínimo 20 caracteres)')
        return contexto
