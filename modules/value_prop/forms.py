from django import forms


class ValuePropForm(forms.Form):
    """Form para Propuesta de Valor (Value Proposition Canvas)"""
    
    # Frustraciones del cliente
    frustracion_1 = forms.CharField(
        label="Frustración 1",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Primera frustración o dolor del cliente...',
            'class': 'form-input'
        }),
        help_text="Identifica las 3 mayores frustraciones, dolores o problemas de tu cliente. Que le causa estres? Que obstaculos enfrenta? Que riesgos le preocupan? Ejemplos: Pierde dinero por producto danado, gasta mucho en transporte, no tiene acceso a credito, no sabe como vender online."
    )
    
    frustracion_2 = forms.CharField(
        label="Frustración 2",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Segunda frustración...',
            'class': 'form-input'
        })
    )
    
    frustracion_3 = forms.CharField(
        label="Frustración 3",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Tercera frustración...',
            'class': 'form-input'
        })
    )
    
    # Ganancias deseadas
    ganancia_1 = forms.CharField(
        label="Ganancia Deseada 1",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Primera ganancia que el cliente quiere...',
            'class': 'form-input'
        }),
        help_text="Que resultados positivos quiere tu cliente? Que lo haria feliz? Que beneficios busca? Ejemplos: Ahorrar tiempo, ganar mas dinero, sentirse seguro, ser reconocido en su comunidad, tener vida mas facil."
    )
    
    ganancia_2 = forms.CharField(
        label="Ganancia Deseada 2",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Segunda ganancia...',
            'class': 'form-input'
        })
    )
    
    ganancia_3 = forms.CharField(
        label="Ganancia Deseada 3",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Tercera ganancia...',
            'class': 'form-input'
        })
    )
    
    # Productos/Servicios
    producto_1 = forms.CharField(
        label="Producto/Servicio 1",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Primer producto o servicio que ofreces...',
            'class': 'form-input'
        }),
        help_text="Lista los productos o servicios concretos que ofreces. Que entregas exactamente al cliente? Ejemplos: Servicio de entrega a domicilio, plataforma web para vender, capacitacion en redes sociales, empaque especial para productos."
    )
    
    producto_2 = forms.CharField(
        label="Producto/Servicio 2",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Segundo producto/servicio...',
            'class': 'form-input'
        })
    )
    
    # Aliviadores de frustraciones
    aliviador_1 = forms.CharField(
        label="Cómo alivias Frustración 1",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Cómo tu solución alivia esta frustración...',
            'class': 'form-input'
        }),
        help_text="Para cada frustracion del cliente, explica COMO tu producto/servicio la alivia o elimina. Conecta directamente: Frustracion X -> Mi solucion hace Y -> Resultado: frustracion aliviada. Se especifico."
    )
    
    aliviador_2 = forms.CharField(
        label="Cómo alivias Frustración 2",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Cómo alivias esta frustración...',
            'class': 'form-input'
        })
    )
    
    # Creadores de ganancias
    creador_1 = forms.CharField(
        label="Cómo generas Ganancia 1",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Cómo tu solución genera esta ganancia...',
            'class': 'form-input'
        }),
        help_text="Para cada ganancia que el cliente desea, explica COMO tu producto/servicio la crea o maximiza. Conecta: Ganancia deseada X -> Mi solucion hace Y -> Resultado: cliente obtiene ganancia. Ejemplos concretos."
    )
    
    creador_2 = forms.CharField(
        label="Cómo generas Ganancia 2",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Cómo generas esta ganancia...',
            'class': 'form-input'
        })
    )
    
    # Propuesta de valor resumida
    propuesta_valor = forms.CharField(
        label="Propuesta de Valor (Resumen)",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Resume tu propuesta de valor en 2-3 oraciones...',
            'class': 'form-input'
        }),
        help_text="Ahora sintetiza todo en 2-3 oraciones: Que valor UNICO ofreces? Por que tu cliente debe elegirte a ti y no otra opcion? Formato sugerido: Para [cliente], que tiene [problema], mi [solucion] ofrece [beneficio unico] a diferencia de [alternativas]. Hazlo simple y potente."
    )
    
    def clean_propuesta_valor(self):
        value = self.cleaned_data.get('propuesta_valor', '')
        if len(value) < 50:
            raise forms.ValidationError('La propuesta de valor debe ser más descriptiva (mínimo 50 caracteres)')
        return value
