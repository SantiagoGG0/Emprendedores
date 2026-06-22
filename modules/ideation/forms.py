from django import forms


class IdeationForm(forms.Form):
    """Form para generación de ideas"""
    
    # Generar múltiples ideas (mínimo 5)
    idea_1 = forms.CharField(
        label="Idea 1",
        widget=forms.TextInput(attrs={
            'placeholder': 'Primera idea de solución...',
            'class': 'form-input'
        }),
        help_text="Genera MINIMO 5 ideas de solucion al problema. En esta fase, cantidad importa mas que calidad. No te censures, escribe todas las ideas que se te ocurran, asi parezcan locas o imposibles. Lluvia de ideas! Ejemplos: App para conectar compradores, servicio de transporte compartido, cooperativa de productores, mercado movil que va a las veredas."
    )
    
    idea_2 = forms.CharField(
        label="Idea 2",
        widget=forms.TextInput(attrs={
            'placeholder': 'Segunda idea...',
            'class': 'form-input'
        })
    )
    
    idea_3 = forms.CharField(
        label="Idea 3",
        widget=forms.TextInput(attrs={
            'placeholder': 'Tercera idea...',
            'class': 'form-input'
        })
    )
    
    idea_4 = forms.CharField(
        label="Idea 4",
        widget=forms.TextInput(attrs={
            'placeholder': 'Cuarta idea...',
            'class': 'form-input'
        })
    )
    
    idea_5 = forms.CharField(
        label="Idea 5",
        widget=forms.TextInput(attrs={
            'placeholder': 'Quinta idea...',
            'class': 'form-input'
        })
    )
    
    idea_6 = forms.CharField(
        label="Idea 6 (opcional)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Sexta idea (opcional)...',
            'class': 'form-input'
        })
    )
    
    # Selección de top 3
    top_1 = forms.CharField(
        label="Mejor Idea #1",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Describe tu mejor idea y por qué la elegiste...',
            'class': 'form-input'
        }),
        help_text="Ahora revisa tus 5+ ideas y elige las 3 MEJORES. Para cada una, explica POR QUE la elegiste. Considera: Es viable con tus recursos? Resuelve el problema real? La gente pagaria por esto? Puedes empezar pequeno y crecer? Cual tiene mas potencial?"
    )
    
    top_2 = forms.CharField(
        label="Mejor Idea #2",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Segunda mejor idea...',
            'class': 'form-input'
        }),
        help_text="Segunda opción más prometedora"
    )
    
    top_3 = forms.CharField(
        label="Mejor Idea #3",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Tercera mejor idea...',
            'class': 'form-input'
        }),
        help_text="Tercera opción"
    )
    
    idea_final = forms.CharField(
        label="Idea Final Seleccionada",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Describe la idea que vas a desarrollar...',
            'class': 'form-input'
        }),
        help_text="De tus 3 mejores ideas, elige UNA para desarrollar en los siguientes modulos. Describe esta idea con detalle: Que producto o servicio es exactamente? A quien le sirve? Como funciona? Por que crees que funcionara? Esta sera tu idea emprendedora para el resto del proceso."
    )
    
    def clean_top_1(self):
        value = self.cleaned_data.get('top_1', '')
        if len(value) < 30:
            raise forms.ValidationError('Explica más tu mejor idea (mínimo 30 caracteres)')
        return value
    
    def clean_idea_final(self):
        value = self.cleaned_data.get('idea_final', '')
        if len(value) < 50:
            raise forms.ValidationError('Describe tu idea final con más detalle (mínimo 50 caracteres)')
        return value
