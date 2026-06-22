# encoding: utf-8
"""
Management command to populate Example model with territorial cases from PDF.
Simplified version without complex formatting.
"""

from django.core.management.base import BaseCommand
from core.models import Module, Example


class Command(BaseCommand):
    help = 'Populate Example model with Colombian territory cases from the Suluhisho PDF guide'

    def handle(self, *args, **options):
        self.stdout.write('Populating territorial examples...')
        
        # Clear existing examples
        Example.objects.all().delete()
        self.stdout.write('  Cleared existing examples')
        
        # Module 1: Ikigai
        ikigai = Module.objects.get(key=Module.IKIGAI)
        Example.objects.create(
            module=ikigai,
            title='Artesanias en fique - Ituango, Antioquia',
            territory_context='Municipio de Ituango, Antioquia (Territorio PDET)',
            description="Emprendedora: Mujer campesina, desplazada interna. Lo que ama: tejer con fibras naturales. En que es buena: artesanias en fique. Interseccion Ikigai: Emprendimiento de artesanias con identidad territorial vinculado a turismo y comercio justo.",
            key_learnings='Conectar habilidad tradicional con mercados emergentes que valoran lo local y sostenible',
            is_featured=True
        )
        
        # Module 2: Field Diary
        field_diary = Module.objects.get(key=Module.FIELD_DIARY)
        Example.objects.create(
            module=field_diary,
            title='Perdida de cosecha - Choco rural',
            territory_context='Municipio rural, departamento del Choco',
            description="Observaciones: 1. Mamas caminan 1 hora al puesto de salud. 2. Agricultores tiran fruta que no venden por falta de compradores. 3. Jovenes sin donde trabajar. 4. Sin transporte confiable. 5. Productos de aseo muy costosos. Problema candidato: Perdida de fruta por falta de transformacion y comercializacion.",
            key_learnings='La observacion sistematica revela el problema que mas se repite y afecta a mas personas',
            is_featured=True
        )
        
        # Module 3: Empathy
        empathy = Module.objects.get(key=Module.EMPATHY)
        Example.objects.create(
            module=empathy,
            title='Transporte a salud - Antioquia rural',
            territory_context='Veredas alejadas, municipio de Ituango, Antioquia',
            description="Mapa de Empatia - Madre campesina. Piensa: angustia por no llevar hijos al medico sin sacrificar dia de trabajo. Ve: puesto salud abre solo hasta 2pm. Dolores: pierde jornal, debe elegir entre salud hijos y trabajo. POV: Madres campesinas necesitan acceder a atencion medica basica sin perder dia de trabajo porque puesto de salud esta a mas de una hora y horarios no se adaptan a jornadas agricolas.",
            key_learnings='El Mapa de Empatia usa palabras exactas de la persona. Dimension emocional tan importante como funcional',
            is_featured=True
        )
        
        # Module 4: JTBD
        jtbd = Module.objects.get(key=Module.JTBD)
        Example.objects.create(
            module=jtbd,
            title='Procesamiento de cacao - Putumayo PDET',
            territory_context='Zona PDET, departamento del Putumayo',
            description="Trabajo: Procesar y vender cosecha de cacao antes de deteriorarse. Funcional: transformar cacao en pasta o chocolate. Social: ser reconocido como productor que agrega valor. Emocional: sentir orgullo por vivir del trabajo propio. Job Steps: Cosechar -> Fermentar -> Secar -> Tostar -> Moler -> Envasar -> Distribuir. Mayor dolor: transformacion y comercializacion (no tiene equipos ni canales).",
            key_learnings='Los Job Steps revelan exactamente donde la persona esta bloqueada',
            is_featured=True
        )
        
        # Module 5: Ideation
        ideation = Module.objects.get(key=Module.IDEATION)
        Example.objects.create(
            module=ideation,
            title='Transformacion de tomate - Norte de Santander',
            territory_context='Municipio PDET, Norte de Santander',
            description="Problema: agricultores pierden 40% de produccion de tomate por falta compradores y refrigeracion. Ideas SCAMPER: Sustituir (espacio colectivo), Combinar (salsas y conservas artesanales), Adaptar (modelo CSA), Modificar (canastas semanales), Otro uso (compost), Eliminar (venta directa restaurantes), Reorganizar (adopcion de planta). Top 3: 1. Salsas artesanales 2. Venta directa restaurantes 3. Canastas prepagadas.",
            key_learnings='SCAMPER fuerza a pensar mas alla de lo obvio. Tecnica Combinar genero la idea ganadora',
            is_featured=True
        )
        
        # Module 6: Value Proposition
        value_prop = Module.objects.get(key=Module.VALUE_PROP)
        Example.objects.create(
            module=value_prop,
            title='Conservas artesanales - Putumayo',
            territory_context='Municipio del Putumayo, zona rural',
            description="Propuesta: Salsas y conservas de tomate artesanales para familias que quieren productos naturales locales, diferente de salsas industriales porque estan hechas con tomates frescos sin conservantes. Verificacion Fit: Desconfianza ingredientes -> Ingredientes naturales (FIT). Quiere apoyar economia local -> Conexion directa productor (FIT). Resultado: Todos dolores tienen aliviador. La propuesta tiene Fit.",
            key_learnings='El VPC verifica que no haya brechas. Si dolor o ganancia sin respuesta, ajustar antes de validar',
            is_featured=True
        )
        
        # Module 7: Validation
        validation = Module.objects.get(key=Module.VALIDATION)
        Example.objects.create(
            module=validation,
            title='Entrevista agricultora - Cordoba',
            territory_context='Zona rural, departamento de Cordoba',
            description="Entrevista validacion: Agricultora perdio 3 arrobas de platano semana pasada porque camion comprador no llego. Ocurre cada dos semanas en temporada. Urgencia: 8/10 porque afecta economia familiar. No tiene solucion actual satisfactoria. Mostro interes espontaneo en servicio de transformacion de platano. Pregunto por precio. Analisis: 5/5 senales positivas. Problema validado.",
            key_learnings='Senal clave: cuando persona hace preguntas de compra (precio, cuando empieza). Indica interes genuino',
            is_featured=True
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {Example.objects.count()} territorial examples'))
