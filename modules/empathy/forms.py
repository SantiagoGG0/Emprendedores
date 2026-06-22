from django import forms


class EmpathyMapForm(forms.Form):
    """Form para Mapa de Empatía + POV"""
    
    # Persona seleccionada
    persona = forms.CharField(
        label="¿Quién es la persona?",
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: María, madre soltera de 35 años, vende arepas en la plaza',
            'class': 'form-input'
        }),
        help_text="Elige UNA persona especifica que hayas observado en tu Diario de Campo. Dale un nombre (puede ser ficticio), edad aproximada y describela en una linea. Ejemplo: Juana, 28 anos, agricultora de cafe en la vereda."
    )
    
    # ¿Qué piensa y siente?
    piensa_siente = forms.CharField(
        label="¿Qué piensa y siente?",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Sus preocupaciones, sueños, miedos...',
            'class': 'form-input'
        }),
        help_text="Ponte en sus zapatos. Que le preocupa dia a dia? Que suena? Que le da miedo? Que la hace feliz? Piensa como si fueras esa persona. Ejemplos: Le preocupa no tener plata para el estudio de los hijos, suena con tener su propio negocio, le da miedo enfermarse y no poder trabajar."
    )
    
    # ¿Qué ve?
    ve = forms.CharField(
        label="¿Qué ve?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Su entorno, lo que observa en su día a día...',
            'class': 'form-input'
        }),
        help_text="Que ve esta persona en su entorno? Su casa, su barrio/vereda, la gente alrededor, los servicios disponibles o no disponibles. Ejemplo: Ve calles destapadas cuando llueve, ve que sus vecinos tambien luchan, ve negocios cerrados."
    )
    
    # ¿Qué dice y hace?
    dice_hace = forms.CharField(
        label="¿Qué dice y hace?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Sus acciones, comportamientos, lo que dice...',
            'class': 'form-input'
        }),
        help_text="Que dice en voz alta sobre su situacion? Que acciones toma dia a dia para resolver sus problemas? Ejemplo: Dice que todo esta muy caro, se levanta a las 4am para llegar al pueblo, busca trabajo por todos lados."
    )
    
    # ¿Qué oye?
    oye = forms.CharField(
        label="¿Qué oye?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Lo que escucha de otros, opiniones, comentarios...',
            'class': 'form-input'
        }),
        help_text="Que escucha de su familia, vecinos, autoridades, medios? Que le dicen otros sobre su problema? Ejemplo: Los vecinos le dicen que asi es la vida, en la tele hablan de oportunidades pero ella no las ve, su familia le pide que consiga mas plata."
    )
    
    # Frustraciones
    frustraciones = forms.CharField(
        label="Frustraciones y dolores",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Sus problemas, obstáculos, miedos...',
            'class': 'form-input'
        }),
        help_text="Cuales son los mayores dolores y frustraciones de esta persona? Que obstaculos enfrenta? Ejemplo: No tiene plata para insumos, el transporte es caro y dificil, tiene miedo de endeudarse, siente que nadie la apoya."
    )
    
    # Necesidades y ganancias
    necesidades = forms.CharField(
        label="Necesidades y ganancias deseadas",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Lo que quiere lograr, sus objetivos...',
            'class': 'form-input'
        }),
        help_text="Que quiere lograr? Cuales son sus deseos y objetivos? Ejemplo: Quiere ingresos estables, quiere tiempo para sus hijos, quiere sentirse segura economicamente, quiere que la respeten en su comunidad."
    )
    
    # POV (Point of View)
    pov = forms.CharField(
        label="Punto de Vista (POV)",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': '[Persona] necesita [necesidad] porque [insight sorprendente]',
            'class': 'form-input'
        }),
        help_text="Ahora sintetiza todo en una frase POV siguiendo este formato: [Persona] necesita [que necesidad especifica] porque [insight o razon profunda que descubriste]. Ejemplo: Maria necesita una forma de vender sus productos desde casa porque el transporte al pueblo le cuesta mas de lo que gana."
    )
    
    def clean_piensa_siente(self):
        value = self.cleaned_data.get('piensa_siente', '')
        if len(value) < 20:
            raise forms.ValidationError('Describe con más detalle (mínimo 20 caracteres)')
        return value
    
    def clean_pov(self):
        value = self.cleaned_data.get('pov', '')
        if len(value) < 30:
            raise forms.ValidationError('El POV debe ser más descriptivo (mínimo 30 caracteres)')
        return value
