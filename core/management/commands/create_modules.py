from django.core.management.base import BaseCommand
from core.models import Module


class Command(BaseCommand):
    help = 'Crea los 7 módulos de ideación en la base de datos'

    def handle(self, *args, **options):
        modules_data = [
            {
                'key': 'ikigai',
                'order': 1,
                'title': 'Ikigai',
                'description': 'Descubre tu propósito conectando lo que amas, en lo que eres bueno, lo que tu comunidad necesita y por lo que pagarían.',
                'instructions': 'Completa cada una de las 4 preguntas con al menos 3 respuestas. Luego escribe una frase que conecte todas las áreas.',
                'estimated_time_minutes': 30,
                'is_active': True
            },
            {
                'key': 'field_diary',
                'order': 2,
                'title': 'Diario de Campo',
                'description': 'Observa y documenta problemas reales en tu comunidad. Registra situaciones, personas afectadas y contexto.',
                'instructions': 'Registra al menos 5 observaciones diferentes. Puedes usar texto, voz o fotos. Luego selecciona el problema más importante.',
                'estimated_time_minutes': 60,
                'is_active': True
            },
            {
                'key': 'empathy',
                'order': 3,
                'title': 'Mapa de Empatía + POV',
                'description': 'Comprende profundamente a la persona que enfrenta el problema. Define un punto de vista claro.',
                'instructions': 'Completa el mapa de empatía explorando qué piensa, siente, ve, escucha, dice y hace tu cliente. Define su necesidad y sorpresa clave.',
                'estimated_time_minutes': 45,
                'is_active': True
            },
            {
                'key': 'jtbd',
                'order': 4,
                'title': 'Jobs To Be Done',
                'description': 'Define el "trabajo" que tu cliente quiere realizar. Identifica la situación, motivación y resultado esperado.',
                'instructions': 'Completa el canvas JTBD con las 3 dimensiones: situación, motivación y resultado. Desglosa los pasos del trabajo.',
                'estimated_time_minutes': 40,
                'is_active': True
            },
            {
                'key': 'ideation',
                'order': 5,
                'title': 'Ideación',
                'description': 'Genera múltiples ideas de solución. Usa técnicas creativas y selecciona las 3 mejores.',
                'instructions': 'Genera al menos 10 ideas usando brainstorming y SCAMPER. Evalúa con matriz de viabilidad-impacto. Selecciona top 3.',
                'estimated_time_minutes': 50,
                'is_active': True
            },
            {
                'key': 'value_prop',
                'order': 6,
                'title': 'Propuesta de Valor',
                'description': 'Define claramente cómo tu solución alivia frustraciones y genera ganancias para tu cliente.',
                'instructions': 'Completa el Value Proposition Canvas: perfil del cliente (trabajos, frustraciones, ganancias) y mapa de valor (productos, aliviadores, creadores).',
                'estimated_time_minutes': 45,
                'is_active': True
            },
            {
                'key': 'validation',
                'order': 7,
                'title': 'Validación',
                'description': 'Valida tu idea con entrevistas a clientes potenciales. Busca señales claras de interés real.',
                'instructions': 'Realiza 7-10 entrevistas de validación. Registra señales clave: dolor, contexto, sueño, dinero y tiempo.',
                'estimated_time_minutes': 120,
                'is_active': True
            }
        ]

        for module_data in modules_data:
            module, created = Module.objects.update_or_create(
                key=module_data['key'],
                defaults=module_data
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Módulo creado: {module.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⟳ Módulo actualizado: {module.title}')
                )

        self.stdout.write(
            self.style.SUCCESS('\n¡Todos los módulos están listos!')
        )
