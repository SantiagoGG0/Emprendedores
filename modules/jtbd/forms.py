from django import forms


class JTBDForm(forms.Form):
    """Form para Jobs To Be Done"""
    
    situacion = forms.CharField(
        label="¿En qué situación se encuentra la persona?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Ej: Cuando tiene que ir al pueblo a vender sus productos...',
            'class': 'form-input'
        }),
        help_text="Cuando [situacion especifica]... Describe el contexto o momento exacto. Ejemplos: Cuando necesita llevar sus productos al mercado los sabados, Cuando sus hijos llegan de la escuela y tienen hambre, Cuando se le dana una herramienta y no tiene como repararla. Se especifico en el momento."
    )
    
    motivacion = forms.CharField(
        label="¿Qué motivación tiene? ¿Por qué quiere hacer esto?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Porque necesita generar ingresos para su familia...',
            'class': 'form-input'
        }),
        help_text="Quiero [motivacion]... Que quiere hacer o lograr en esa situacion? Que la impulsa? Ejemplos: Quiero vender rapido antes que se dane el producto, Quiero que mis hijos coman bien, Quiero seguir trabajando sin parar. Enfocate en la accion que quiere tomar."
    )
    
    resultado_esperado = forms.CharField(
        label="¿Qué resultado espera lograr?",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Poder vender más productos a mejor precio...',
            'class': 'form-input'
        }),
        help_text="Para [resultado deseado]... Que resultado final quiere? Como se veria el exito? Ejemplos: Para tener ingresos todos los dias no solo los sabados, Para que mis hijos crezcan sanos y fuertes, Para no perder tiempo ni plata en reparaciones. Piensa en el impacto que busca."
    )
    
    job_statement = forms.CharField(
        label="Declaración del 'Trabajo' (Job Statement)",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Cuando [situación], quiero [motivación], para [resultado]',
            'class': 'form-input'
        }),
        help_text="Ahora une las 3 partes en una sola frase: Cuando [situacion], quiero [motivacion], para [resultado]. Ejemplo completo: Cuando tengo que llevar mis productos al mercado los sabados, quiero vender rapido y al mejor precio, para tener ingresos estables y no perder producto. Esta frase define el trabajo que tu solucion debe hacer."
    )
    
    def clean_situacion(self):
        value = self.cleaned_data.get('situacion', '')
        if len(value) < 20:
            raise forms.ValidationError('Describe más la situación (mínimo 20 caracteres)')
        return value
    
    def clean_job_statement(self):
        value = self.cleaned_data.get('job_statement', '')
        if len(value) < 30:
            raise forms.ValidationError('El Job Statement debe ser más completo (mínimo 30 caracteres)')
        return value
