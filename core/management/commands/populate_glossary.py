"""
Management command to populate ReferenceContent glossary with 50+ terms.
"""

from django.core.management.base import BaseCommand
from core.models import ReferenceContent, Module


class Command(BaseCommand):
    help = 'Poblar glosario con 50+ términos (metodología, territorial, plataforma)'

    def handle(self, *args, **options):
        self.stdout.write('🔄 Poblando glosario...')
        
        # Clear existing
        ReferenceContent.objects.all().delete()
        
        # Get modules for M2M relationships
        modules = {m.key: m for m in Module.objects.all()}
        
        terms = self.get_glossary_terms()
        
        created_count = 0
        for term_data in terms:
            module_keys = term_data.pop('module_keys', [])
            ref = ReferenceContent.objects.create(**term_data)
            
            # Add related modules
            for key in module_keys:
                if key in modules:
                    ref.related_modules.add(modules[key])
            
            created_count += 1
            self.stdout.write(f'  ✅ {ref.title}')
        
        self.stdout.write(self.style.SUCCESS(f'\n✨ Creados {created_count} términos'))

    def get_glossary_terms(self):
        """Returns list of 50+ glossary term dictionaries"""
        return [
            # ============ METODOLOGÍA (20 términos) ============
            {
                'key': 'jtbd',
                'category': 'methodology',
                'title': 'Jobs To Be Done (JTBD)',
                'short_definition': 'Marco conceptual que describe el "trabajo" que un cliente "contrata" a un producto/servicio para resolver. No es sobre el producto, sino sobre el progreso que el cliente busca.',
                'detailed_explanation': '''**Jobs To Be Done (JTBD)** es una metodología que cambia la pregunta de "¿qué producto vender?" a "¿qué trabajo necesita hacer mi cliente?".

**Estructura JTBD:**
- **Cuando** [situación específica]
- **Quiero** [motivación/acción]
- **Para** [resultado deseado]

**Ejemplo rural:** "Cuando termina la cosecha de café, quiero transformar los granos en café tostado, para venderlo a mejor precio en lugar de vender cereza cruda."

El JTBD revela que el cliente no compra café tostado, sino **autonomía económica** y **mejor margen**.''',
                'keywords': ['jtbd', 'trabajo por hacer', 'progreso', 'cliente', 'necesidad'],
                'external_links': [
                    {'title': 'Jobs To Be Done explicado (video)', 'url': 'https://www.youtube.com/watch?v=f84LymEs67Y', 'type': 'video'},
                    {'title': 'Guía práctica JTBD', 'url': 'https://jtbd.info/2-what-is-jobs-to-be-done-jtbd-796b82081cca', 'type': 'article'},
                ],
                'module_keys': ['jtbd'],
                'order': 1,
            },
            {
                'key': 'pov',
                'category': 'methodology',
                'title': 'Point of View (POV)',
                'short_definition': 'Declaración que sintetiza el problema desde la perspectiva del usuario. Formato: [Usuario] necesita [necesidad] porque [insight revelador].',
                'detailed_explanation': '''**Point of View (POV)** es la síntesis del Mapa de Empatía. Transforma observaciones en una declaración accionable.

**Estructura POV:**
[Persona específica] necesita [necesidad concreta] porque [razón profunda descubierta]

**Ejemplo:** "María, agricultora de plátano en Putumayo, necesita una forma de vender sus excedentes sin intermediarios porque pierde el 60% del precio final cuando vende al 'comisionista'."

**Por qué importa:** El POV guía TODO tu proceso de ideación. Si tu idea no resuelve el POV, no sirve.''',
                'keywords': ['pov', 'punto de vista', 'empatía', 'problema', 'usuario'],
                'external_links': [
                    {'title': 'Cómo escribir un POV efectivo', 'url': 'https://www.designkit.org/methods/define-your-point-of-view', 'type': 'article'},
                ],
                'module_keys': ['empathy'],
                'order': 2,
            },
            {
                'key': 'empathy_map',
                'category': 'methodology',
                'title': 'Mapa de Empatía',
                'short_definition': 'Herramienta visual para entender profundamente a tu cliente: qué piensa, siente, ve, oye, dice y hace.',
                'detailed_explanation': '''**Mapa de Empatía** te obliga a PONERTE EN LOS ZAPATOS de tu cliente.

**6 dimensiones:**
1. **Piensa y siente:** Preocupaciones, sueños, miedos internos
2. **Ve:** Su entorno (casa, vereda, infraestructura)
3. **Oye:** Qué le dicen otros (familia, vecinos, autoridades)
4. **Dice y hace:** Sus acciones diarias, comportamientos
5. **Frustraciones:** Problemas, obstáculos, dolores
6. **Necesidades:** Qué quiere lograr, deseos profundos

**Clave en zonas PDET:** No asumas. Una madre cabeza de familia en zona rural enfrenta realidades que solo conoces si observas y preguntas.''',
                'keywords': ['empatía', 'cliente', 'usuario', 'perspectiva', 'observación'],
                'external_links': [
                    {'title': 'Mapa de Empatía explicado', 'url': 'https://www.youtube.com/watch?v=QwF9a56WFWA', 'type': 'video'},
                    {'title': 'Plantilla Mapa de Empatía', 'url': 'https://www.canva.com/es_mx/plantillas/mapas/empatia/', 'type': 'tool'},
                ],
                'module_keys': ['empathy'],
                'order': 3,
            },
            {
                'key': 'value_proposition',
                'category': 'methodology',
                'title': 'Propuesta de Valor',
                'short_definition': 'Lo que hace único a tu producto/servicio: cómo alivia dolores y crea ganancias para tu cliente específico.',
                'detailed_explanation': '''**Propuesta de Valor** responde: ¿Por qué alguien elegiría TU solución y no otra?

**Canvas de Propuesta de Valor:**
- **Lado Cliente:** Frustraciones + Ganancias deseadas
- **Lado Oferta:** Productos/servicios + Aliviadores de dolor + Creadores de ganancia

**Ejemplo:** "Para agricultores de cacao sin acceso a compradores directos, que pierden 40% del precio vendiendo a intermediarios, mi cooperativa conecta directamente con exportadores certificados, asegurando precio justo y pago en 7 días."

**Error común:** Decir "mi producto es mejor". ❌ Correcto: Especificar CÓMO alivia un dolor CONCRETO. ✅''',
                'keywords': ['valor', 'propuesta', 'diferenciación', 'cliente', 'producto'],
                'external_links': [
                    {'title': 'Value Proposition Canvas explicado', 'url': 'https://www.youtube.com/watch?v=ReM1uqmVfP0', 'type': 'video'},
                    {'title': 'Plantilla editable', 'url': 'https://www.strategyzer.com/canvas/value-proposition-canvas', 'type': 'tool'},
                ],
                'module_keys': ['value_prop'],
                'order': 4,
            },
            {
                'key': 'design_thinking',
                'category': 'methodology',
                'title': 'Design Thinking',
                'short_definition': 'Proceso de innovación centrado en el ser humano. 5 etapas: Empatizar, Definir, Idear, Prototipar, Validar.',
                'detailed_explanation': '''**Design Thinking** es la metodología madre que guía Suluhisho.

**5 Etapas:**
1. **Empatizar:** Observar (Diario de Campo) y entender (Mapa de Empatía)
2. **Definir:** Sintetizar problema (POV + JTBD)
3. **Idear:** Generar muchas ideas (Brainstorming)
4. **Prototipar:** Construir solución mínima (Value Prop)
5. **Validar:** Probar con clientes reales (Entrevistas)

**No es lineal:** Puedes volver atrás si descubres algo nuevo. El Módulo 7 (Validación) puede llevarte a revisar tu idea (Módulo 5).''',
                'keywords': ['design thinking', 'innovación', 'proceso', 'metodología', 'empatía'],
                'external_links': [
                    {'title': 'Design Thinking 101 (video)', 'url': 'https://www.youtube.com/watch?v=_r0VX-aU_T8', 'type': 'video'},
                ],
                'module_keys': ['ikigai', 'field_diary', 'empathy', 'jtbd', 'ideation', 'value_prop', 'validation'],
                'order': 5,
            },
            {
                'key': 'lean_startup',
                'category': 'methodology',
                'title': 'Lean Startup',
                'short_definition': 'Metodología para crear negocios validando suposiciones rápido y con pocos recursos. Ciclo: Construir-Medir-Aprender.',
                'detailed_explanation': '''**Lean Startup** dice: no gastes tiempo/plata en un producto que nadie quiere.

**Ciclo iterativo:**
1. **Construir:** MVP (Producto Mínimo Viable)
2. **Medir:** Validar con clientes reales (Módulo 7)
3. **Aprender:** Pivotar o perseverar

**En zonas PDET:** Especialmente importante porque recursos son limitados. Mejor hacer 3 entrevistas ANTES de invertir en maquinaria.

**Ejemplo:** Antes de montar una panadería, vende pan casa por casa 1 semana. Si nadie compra, ahorraste $5 millones.''',
                'keywords': ['lean', 'startup', 'mvp', 'validación', 'iteración'],
                'external_links': [
                    {'title': 'Lean Startup explicado', 'url': 'https://www.youtube.com/watch?v=fEvKo90qBns', 'type': 'video'},
                    {'title': 'Libro: The Lean Startup (PDF)', 'url': 'http://theleanstartup.com/principles', 'type': 'article'},
                ],
                'module_keys': ['validation', 'ideation'],
                'order': 6,
            },
            {
                'key': 'pmf',
                'category': 'methodology',
                'title': 'Product-Market Fit (PMF)',
                'short_definition': 'Cuando tu producto resuelve un problema real de un mercado lo suficientemente grande y dispuesto a pagar.',
                'detailed_explanation': '''**Product-Market Fit** es el Santo Grial del emprendimiento. Sabes que lo lograste cuando:

- Clientes te buscan (no tú a ellos)
- Te recomiendan sin que pidas
- Se quejan si el servicio falla (porque lo NECESITAN)
- Pagan sin regatear mucho

**En rural:** PMF puede ser local. No necesitas 10,000 clientes. Si 50 familias de tu vereda compran religiosamente tu servicio de transporte compartido, tienes PMF local.

**Señal de NO-PMF:** Haces 20 entrevistas y todos dicen "interesante" pero nadie compra.''',
                'keywords': ['pmf', 'product market fit', 'ajuste', 'mercado', 'validación'],
                'external_links': [
                    {'title': 'Cómo saber si tienes PMF', 'url': 'https://www.youtube.com/watch?v=_6pl5GG8RQ4', 'type': 'video'},
                ],
                'module_keys': ['validation', 'value_prop'],
                'order': 7,
            },
            {
                'key': 'scamper',
                'category': 'methodology',
                'title': 'SCAMPER',
                'short_definition': 'Técnica de creatividad. 7 preguntas para transformar ideas: Sustituir, Combinar, Adaptar, Modificar, Poner otros usos, Eliminar, Reordenar.',
                'detailed_explanation': '''**SCAMPER** te ayuda a generar variaciones de una idea base.

**7 Preguntas:**
- **S**ustituir: ¿Qué material/proceso cambiar?
- **C**ombinar: ¿Qué servicios unir?
- **A**daptar: ¿Qué funciona en otro contexto?
- **M**odificar: ¿Más grande/pequeño/rápido?
- **P**oner otros usos: ¿Otro mercado/cliente?
- **E**liminar: ¿Qué simplificar?
- **R**eordenar: ¿Cambiar secuencia/ubicación?

**Ejemplo:** Idea base "vender café tostado". SCAMPER: ¿Y si **combino** con tours de finca? (Agroturismo cafetalero)''',
                'keywords': ['scamper', 'creatividad', 'ideación', 'brainstorming', 'innovación'],
                'external_links': [
                    {'title': 'SCAMPER en español', 'url': 'https://www.youtube.com/watch?v=3k8kRbZhVXg', 'type': 'video'},
                ],
                'module_keys': ['ideation'],
                'order': 8,
            },
            {
                'key': 'brainstorming',
                'category': 'methodology',
                'title': 'Brainstorming (Lluvia de Ideas)',
                'short_definition': 'Técnica para generar MUCHAS ideas sin juzgar. Reglas: cantidad > calidad, no criticar, ideas locas bienvenidas.',
                'detailed_explanation': '''**Brainstorming efectivo:**

**Reglas sagradas:**
1. **Cantidad importa:** 20 ideas mejor que 3
2. **No juzgar:** Ninguna idea es "mala" en esta etapa
3. **Ideas locas OK:** A veces las "imposibles" inspiran las viables
4. **Construir sobre otras:** "Sí, y además..."

**Clave rural:** No necesitas sala con post-its. Puedes hacer brainstorming caminando por la vereda, preguntando a vecinos "¿Qué harías tú si...?"

**Después del brainstorming:** AHÍ sí evalúas (Módulo 5 pide elegir Top 3).''',
                'keywords': ['brainstorming', 'ideas', 'creatividad', 'generación', 'cantidad'],
                'external_links': [
                    {'title': 'Cómo hacer brainstorming efectivo', 'url': 'https://www.youtube.com/watch?v=W1h5L_0rFz8', 'type': 'video'},
                ],
                'module_keys': ['ideation'],
                'order': 9,
            },
            {
                'key': 'mvp',
                'category': 'methodology',
                'title': 'MVP (Producto Mínimo Viable)',
                'short_definition': 'Versión más simple de tu producto que permite validar si resuelve el problema. No es "producto malo", es "suficiente para aprender".',
                'detailed_explanation': '''**MVP no significa producto feo o incompleto.** Significa: lo MÍNIMO necesario para probar tu hipótesis clave.

**Ejemplos MVP rural:**
- **Idea:** App de pedidos para tienda rural → **MVP:** Grupo de WhatsApp donde tomas pedidos
- **Idea:** Restaurante de comida típica → **MVP:** Vender almuerzos 3 días/semana desde tu casa
- **Idea:** Transporte colectivo → **MVP:** Hacer 1 ruta de prueba con tu moto

**Pregunta clave:** "¿Qué es lo MENOS que puedo hacer para saber si esto funciona?"''',
                'keywords': ['mvp', 'mínimo viable', 'prototipo', 'validación', 'experimento'],
                'external_links': [
                    {'title': 'Qué es un MVP (video)', 'url': 'https://www.youtube.com/watch?v=0P7nCmln7PM', 'type': 'video'},
                ],
                'module_keys': ['validation', 'ideation'],
                'order': 10,
            },
            {
                'key': 'user_persona',
                'category': 'methodology',
                'title': 'User Persona (Persona Usuario)',
                'short_definition': 'Representación semi-ficticia de tu cliente ideal basada en observación real. Tiene nombre, edad, contexto, problemas, deseos.',
                'detailed_explanation': '''**User Persona** es tu cliente en papel. No es "todos los campesinos", es "Juan, 45 años, caficultor de Putumayo con 2 hectáreas".

**Por qué ayuda:** Es más fácil diseñar para UNA persona específica que para "el mercado".

**Cómo crearla:**
1. Observa clientes reales (Diario de Campo)
2. Entrevista 3-5 personas similares
3. Identifica patrones (edad, ocupación, problemas comunes)
4. Dale nombre e historia

**En Suluhisho:** Tu persona viene del Mapa de Empatía (Módulo 3).''',
                'keywords': ['persona', 'usuario', 'cliente', 'perfil', 'arquetipo'],
                'external_links': [
                    {'title': 'Cómo crear user personas', 'url': 'https://www.youtube.com/watch?v=XnG4c4gXaQY', 'type': 'video'},
                ],
                'module_keys': ['empathy', 'field_diary'],
                'order': 11,
            },
            {
                'key': 'insight',
                'category': 'methodology',
                'title': 'Insight',
                'short_definition': 'Descubrimiento profundo sobre tu cliente que no es obvio. La "verdad oculta" detrás del comportamiento.',
                'detailed_explanation': '''**Insight** es oro para emprendedores. Es la diferencia entre conocer el síntoma y entender la causa.

**Ejemplo:**
- **Obvio:** "La gente no compra verduras frescas en mi vereda"
- **Insight:** "Porque el camión del pueblo solo viene martes/viernes y para entonces ya compraron en la tienda local (aunque sean viejas)"

**Cómo encontrar insights:**
1. Pregunta "¿por qué?" 5 veces
2. Observa COMPORTAMIENTOS, no solo lo que dicen
3. Busca contradicciones (dicen X pero hacen Y)

**En POV:** El "porque" es tu insight.''',
                'keywords': ['insight', 'descubrimiento', 'verdad', 'comprensión', 'observación'],
                'external_links': [
                    {'title': 'Qué son los insights', 'url': 'https://www.youtube.com/watch?v=4Cw3AzYVNZg', 'type': 'video'},
                ],
                'module_keys': ['empathy', 'field_diary'],
                'order': 12,
            },
            {
                'key': 'pain_points',
                'category': 'methodology',
                'title': 'Pain Points (Puntos de Dolor)',
                'short_definition': 'Problemas, frustraciones u obstáculos específicos que enfrenta tu cliente en su día a día.',
                'detailed_explanation': '''**Pain Points** son los dolores que tu producto debe aliviar.

**Tipos de dolor:**
1. **Financiero:** Gasta mucho, gana poco
2. **Tiempo:** Procesos lentos, esperas largas
3. **Soporte:** No encuentra ayuda cuando falla algo
4. **Proceso:** Pasos complicados, burocracia

**Ejemplo rural:** Agricultor de tomate pierde 30% cosecha porque transporte tarda 5 horas y tomate se daña. **Pain point:** Logística lenta mata producto perecedero.

**En Value Prop Canvas:** Pain Points = Frustraciones del cliente.''',
                'keywords': ['dolor', 'frustración', 'problema', 'obstáculo', 'fricción'],
                'external_links': [
                    {'title': 'Identificar pain points', 'url': 'https://blog.hubspot.com/service/customer-pain-points', 'type': 'article'},
                ],
                'module_keys': ['empathy', 'value_prop'],
                'order': 13,
            },
            {
                'key': 'customer_gain',
                'category': 'methodology',
                'title': 'Customer Gain (Ganancia del Cliente)',
                'short_definition': 'Beneficios, resultados positivos o deseos que tu cliente quiere lograr. Lo opuesto a Pain Points.',
                'detailed_explanation': '''**Customer Gain:** No solo quitar dolores, también crear alegrías.

**Tipos de ganancia:**
1. **Ahorro:** Tiempo, dinero, esfuerzo
2. **Social:** Reconocimiento, pertenencia, respeto
3. **Emocional:** Tranquilidad, seguridad, orgullo
4. **Funcional:** Más productividad, mejor calidad

**Ejemplo:** Cooperativa de mujeres artesanas. **Gain funcional:** Venden 3x más. **Gain social:** Respeto en la comunidad por ser "empresarias". **Gain emocional:** Autonomía económica de sus esposos.

**En Value Prop:** Tus productos deben ser "Creadores de Ganancia".''',
                'keywords': ['ganancia', 'beneficio', 'resultado', 'deseo', 'valor'],
                'external_links': [
                    {'title': 'Customer Gains explicado', 'url': 'https://www.strategyzer.com/library/the-customer-gains', 'type': 'article'},
                ],
                'module_keys': ['value_prop'],
                'order': 14,
            },
            {
                'key': 'iteration',
                'category': 'methodology',
                'title': 'Iteración',
                'short_definition': 'Proceso de mejorar tu idea/producto en ciclos repetidos. Versión 1 → Aprender → Versión 2 → Aprender → Versión 3...',
                'detailed_explanation': '''**Iteración** es clave en Lean Startup. Tu primera idea casi nunca es la final.

**Ejemplo real:** Empiezas vendiendo "café orgánico". Después de 10 entrevistas descubres que clientes valoran más "café de origen único trazable". Iteras: cambias mensaje y empaque. Ventas suben 40%.

**No es fallar:** Es aprender rápido.

**En Suluhisho:** El Módulo 7 (Validación) puede llevarte a iterar tu Value Prop (Módulo 6) o incluso tu idea (Módulo 5). Eso es BUENO, no malo.''',
                'keywords': ['iteración', 'mejora', 'ciclo', 'aprendizaje', 'evolución'],
                'external_links': [
                    {'title': 'Iteración en startups', 'url': 'https://www.youtube.com/watch?v=7ZTFPLAgInA', 'type': 'video'},
                ],
                'module_keys': ['validation', 'ideation'],
                'order': 15,
            },
            {
                'key': 'prototype',
                'category': 'methodology',
                'title': 'Prototipo',
                'short_definition': 'Versión temprana de tu producto usada para probar y aprender. Puede ser desde un dibujo hasta un producto funcional básico.',
                'detailed_explanation': '''**Prototipo** puede ser:
- **Papel:** Dibujo de tu app/servicio
- **Presentación:** PowerPoint explicando tu idea
- **Mockup:** Foto/video simulando el producto
- **Funcional:** Versión básica que SÍ funciona

**Regla:** Prototipo más simple que responda tu pregunta clave.

**Ejemplo rural:** Quieres saber si la gente compraría mermeladas artesanales. **Prototipo:** Haces 10 frascos en tu cocina, diseñas etiqueta en Canva, vendes casa por casa. Costo: $30,000. Aprendes TODO lo que necesitas sin montar fábrica.''',
                'keywords': ['prototipo', 'prueba', 'mockup', 'versión', 'experimento'],
                'external_links': [
                    {'title': 'Tipos de prototipos', 'url': 'https://www.youtube.com/watch?v=Q4MzT2MEDHA', 'type': 'video'},
                ],
                'module_keys': ['validation', 'ideation'],
                'order': 16,
            },
            {
                'key': 'pivot',
                'category': 'methodology',
                'title': 'Pivotar',
                'short_definition': 'Cambio estratégico en tu idea de negocio basado en aprendizajes. No es "rendirse", es ajustar el rumbo.',
                'detailed_explanation': '''**Pivotar** es cuando la validación (Módulo 7) te dice que tu idea original no funciona, pero descubriste algo mejor.

**Tipos de pivote:**
- **Cliente:** Cambias a quién vendes (de restaurantes a hogares)
- **Problema:** Resuelves otro dolor (de "app pedidos" a "logística rural")
- **Solución:** Mismo problema, otra solución (de app a WhatsApp)

**Caso real:** Empiezas con "tours ecoturísticos" pero descubres que turistas no llegan. Pivotas a "eventos corporativos de team building" en tu finca. Mismo activo (finca), otro cliente.

**No es fracaso:** Instagram empezó como app de check-in. Pivotó a fotos. Hoy vale billones.''',
                'keywords': ['pivotar', 'cambio', 'ajuste', 'estrategia', 'aprendizaje'],
                'external_links': [
                    {'title': 'Cuándo pivotar', 'url': 'https://www.youtube.com/watch?v=0LNQxT9LvM0', 'type': 'video'},
                ],
                'module_keys': ['validation'],
                'order': 17,
            },
            {
                'key': 'customer_discovery',
                'category': 'methodology',
                'title': 'Customer Discovery (Descubrimiento del Cliente)',
                'short_definition': 'Proceso de salir a hablar con clientes potenciales ANTES de construir tu producto. Validas problema, no solución.',
                'detailed_explanation': '''**Customer Discovery:** Regla #1 del emprendimiento lean.

**Qué NO es:** Preguntar "¿Comprarías mi producto X?"
**Qué SÍ es:** Preguntar "¿Cuál es tu mayor frustración con [tema]?"

**Proceso:**
1. Observa (Diario de Campo - Módulo 2)
2. Entrevista sobre PROBLEMA (no solución)
3. Identifica patrones (¿20 personas dicen lo mismo?)
4. Solo ENTONCES diseñas solución

**En Suluhisho:** Módulos 2-4 son Customer Discovery. Módulo 7 es Customer Validation.''',
                'keywords': ['descubrimiento', 'cliente', 'problema', 'entrevista', 'validación'],
                'external_links': [
                    {'title': 'Customer Discovery proceso', 'url': 'https://www.youtube.com/watch?v=l-KMEr92oLo', 'type': 'video'},
                ],
                'module_keys': ['field_diary', 'empathy', 'jtbd'],
                'order': 18,
            },
            {
                'key': 'hypothesis',
                'category': 'methodology',
                'title': 'Hipótesis',
                'short_definition': 'Suposición que debes validar. Formato: "Creemos que [X] tiene problema [Y] y pagaría por solución [Z]".',
                'detailed_explanation': '''**Hipótesis** convierte tu idea en algo testeable.

**Hipótesis bien formulada:**
"Creo que [agricultores de cacao en Putumayo] tienen el problema de [vender barato a intermediarios] y estarían dispuestos a [pagar 5% comisión] por [acceso directo a exportadores certificados]."

**Por qué importa:** Una hipótesis clara te dice exactamente QUÉ validar en entrevistas (Módulo 7).

**Ejemplo malo:** "Mi app será exitosa". ❌ (No testeable)
**Ejemplo bueno:** "Madres cabeza de familia en Ituango pagarán $5,000/mes por servicio de guardería comunitaria". ✅ (Testeable)''',
                'keywords': ['hipótesis', 'suposición', 'validar', 'prueba', 'experimento'],
                'external_links': [
                    {'title': 'Cómo formular hipótesis', 'url': 'https://www.youtube.com/watch?v=MjuAJ1qyJj4', 'type': 'video'},
                ],
                'module_keys': ['validation', 'value_prop'],
                'order': 19,
            },
            {
                'key': 'feedback_loop',
                'category': 'methodology',
                'title': 'Feedback Loop (Ciclo de Retroalimentación)',
                'short_definition': 'Sistema donde aprendes de tus clientes continuamente y ajustas tu producto. Construir → Medir → Aprender → Repetir.',
                'detailed_explanation': '''**Feedback Loop:** Motor de mejora continua.

**Ciclo:**
1. **Construyes** algo (prototipo, MVP)
2. **Mides** reacción (ventas, entrevistas, uso)
3. **Aprendes** qué funciona / qué no
4. **Ajustas** y repites

**Clave:** Loops RÁPIDOS. Mejor hacer 10 ciclos de 1 semana que 1 ciclo de 10 semanas.

**Ejemplo rural:** Haces pan para vender. Semana 1: Nadie compra pan de yuca. Semana 2: Pruebas pan de maíz. Se agota. Semana 3: Solo haces pan de maíz + 2 sabores nuevos. **Loop de 1 semana = aprendes 10x más rápido.**''',
                'keywords': ['feedback', 'retroalimentación', 'ciclo', 'mejora', 'aprendizaje'],
                'external_links': [
                    {'title': 'Build-Measure-Learn loop', 'url': 'https://www.youtube.com/watch?v=QaoF-0u8C4E', 'type': 'video'},
                ],
                'module_keys': ['validation', 'ideation'],
                'order': 20,
            },

            # ============ TERRITORIAL (15 términos) ============
            {
                'key': 'pdet',
                'category': 'territorial',
                'title': 'PDET (Programas de Desarrollo con Enfoque Territorial)',
                'short_definition': 'Estrategia de Colombia para transformar 170 municipios afectados por conflicto armado, pobreza y débil presencia estatal.',
                'detailed_explanation': '''**PDET** son territorios prioritarios para paz y desarrollo. Incluyen 170 municipios en 16 regiones.

**Características PDET:**
- Zonas con historial de conflicto armado
- Alta pobreza rural
- Infraestructura limitada (vías, internet, servicios)
- Economía basada en agricultura familiar
- Oportunidades de emprendimiento con impacto social

**Ejemplos PDET:** Ituango (Antioquia), Putumayo, Caquetá, Chocó, Montes de María, Arauca.

**Por qué importa para emprendedores:** Hay subsidios, programas y mercados especiales para negocios en zonas PDET.''',
                'keywords': ['pdet', 'territorial', 'paz', 'conflicto', 'rural', 'colombia'],
                'external_links': [
                    {'title': 'Qué es PDET (oficial)', 'url': 'https://www.renovacionterritorio.gov.co/PDET', 'type': 'article'},
                    {'title': 'Mapa PDET Colombia', 'url': 'https://www.renovacionterritorio.gov.co/especiales/mapa_interactivo/', 'type': 'tool'},
                ],
                'module_keys': ['ikigai', 'field_diary'],
                'order': 21,
            },
            {
                'key': 'zona_posconflicto',
                'category': 'territorial',
                'title': 'Zona de Posconflicto',
                'short_definition': 'Territorios colombianos que vivieron presencia de grupos armados y están en proceso de construcción de paz.',
                'detailed_explanation': '''**Zonas posconflicto** enfrentan desafíos únicos:

**Realidad:**
- Desconfianza histórica en instituciones
- Población desplazada retornando
- Necesidad de reactivación económica
- Tierra disponible pero sin títulos claros
- Economías ilegales (coca, minería) en transición

**Oportunidad emprendedora:** Negocios que:
- Generan empleo local (no dependen de economía ilegal)
- Usan recursos legales (café, cacao, turismo)
- Reconstruyen tejido social (cooperativas, asociaciones)

**Contexto Suluhisho:** Si vienes de zona posconflicto, tu emprendimiento puede acceder a apoyos especiales (Fondo Colombia en Paz, USAID, UE).''',
                'keywords': ['posconflicto', 'paz', 'conflicto armado', 'reintegración', 'rural'],
                'external_links': [
                    {'title': 'Emprendimiento en posconflicto', 'url': 'https://www.youtube.com/watch?v=8Km5QgJpXo4', 'type': 'video'},
                ],
                'module_keys': ['ikigai', 'field_diary'],
                'order': 22,
            },
            {
                'key': 'vereda',
                'category': 'territorial',
                'title': 'Vereda',
                'short_definition': 'División territorial rural más pequeña en Colombia. Comunidad de 50-300 familias, generalmente sin servicios urbanos.',
                'detailed_explanation': '''**Vereda** es tu mercado local más inmediato.

**Características:**
- 5-20 km del casco municipal
- Sin agua potable / alcantarillado (usualmente)
- Electricidad limitada o sin ella
- Internet móvil (si hay señal)
- Economía de autoconsumo + venta de excedentes

**Implicaciones emprendimiento:**
- Tu primer cliente: tus vecinos de vereda
- Logística difícil (caminos destapados, lluvia)
- Pagos en efectivo (sin datáfono)
- Comunicación: voz a voz, WhatsApp (si hay señal)

**Ejemplo:** Si vendes "servicio de transporte compartido a cabecera municipal", tu mercado son las 80 familias de tu vereda + 3 veredas vecinas = 320 familias potenciales.''',
                'keywords': ['vereda', 'rural', 'comunidad', 'campo', 'territorio'],
                'external_links': [
                    {'title': 'Estructura territorial Colombia', 'url': 'https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=2876', 'type': 'article'},
                ],
                'module_keys': ['field_diary', 'ikigai'],
                'order': 23,
            },
            {
                'key': 'economia_comunitaria',
                'category': 'territorial',
                'title': 'Economía Comunitaria',
                'short_definition': 'Modelo económico donde la comunidad es dueña colectiva de recursos/negocios. Prioriza bienestar común sobre ganancia individual.',
                'detailed_explanation': '''**Economía Comunitaria** es alternativa al modelo capitalista tradicional.

**Principios:**
- Propiedad colectiva (cooperativas, asociaciones)
- Decisiones por consenso
- Ganancias se reinvierten en comunidad
- Trabajo colaborativo (mingas, convites)
- Respeto a naturaleza y territorio

**Ejemplos:**
- Cooperativa lechera: 30 familias venden leche juntas, comparten camión refrigerado
- Fondo rotativo: Comunidad presta semilla a miembros sin interés
- Mercado comunitario: Veredas vecinas intercambian productos sin dinero (trueque)

**Para emprendedores:** Tu negocio puede ser individual Y beneficiar lo comunitario (empleas vecinos, compras insumos locales).''',
                'keywords': ['economía', 'comunitaria', 'cooperativa', 'colectivo', 'solidaridad'],
                'external_links': [
                    {'title': 'Economía solidaria en Colombia', 'url': 'https://www.orgsolidarias.gov.co/', 'type': 'article'},
                ],
                'module_keys': ['ikigai', 'value_prop'],
                'order': 24,
            },
            {
                'key': 'emprendimiento_rural',
                'category': 'territorial',
                'title': 'Emprendimiento Rural',
                'short_definition': 'Negocios basados en actividades rurales: agricultura, ganadería, turismo, artesanía, servicios para campesinos.',
                'detailed_explanation': '''**Emprendimiento Rural** tiene ventajas Y desafíos únicos.

**Ventajas:**
- Menor competencia que ciudades
- Acceso a recursos naturales (tierra, agua, biodiversidad)
- Mano de obra disponible y solidaria
- Tradición de trabajo colaborativo
- Apoyos estatales específicos (Fondo Emprender, SENA rural)

**Desafíos:**
- Logística cara (transporte, empaques)
- Acceso limitado a tecnología/internet
- Clientes con menor poder adquisitivo
- Canales de venta limitados (no hay tiendas/restaurantes)

**Tipos exitosos:**
- Transformación de materias primas (café → café tostado)
- Servicios locales (transporte, reparaciones, salud)
- Agroturismo (hospedaje, tours, comida)
- Comercialización asociativa (cooperativas)''',
                'keywords': ['emprendimiento', 'rural', 'campo', 'agricultura', 'negocio'],
                'external_links': [
                    {'title': 'Casos emprendimiento rural Colombia', 'url': 'https://www.youtube.com/watch?v=RxGP4gVKLqE', 'type': 'video'},
                ],
                'module_keys': ['ikigai', 'ideation', 'value_prop'],
                'order': 25,
            },
            # Continúa con 10 términos territoriales más...
            {
                'key': 'agricultura_familiar',
                'category': 'territorial',
                'title': 'Agricultura Familiar',
                'short_definition': 'Producción agropecuaria gestionada por familia, en pequeña escala (< 5 hectáreas típicamente), para autoconsumo y venta de excedentes.',
                'detailed_explanation': '''**Agricultura Familiar** es el 85% de los productores rurales en Colombia.

**Características:**
- Fincas pequeñas (0.5-5 hectáreas)
- Trabajo familiar (no empleados)
- Cultivos mixtos (plátano, yuca, gallinas, café)
- Venta de excedentes en plaza de mercado

**Retos:**
- Baja tecnificación (herramientas manuales)
- Sin acceso a crédito formal
- Intermediarios se llevan 60-70% del precio final
- Post-cosecha: pérdidas por mal almacenamiento

**Oportunidades emprendimiento:**
- Servicios para agricultores (transporte, maquinaria compartida, insumos)
- Agregación de valor (procesar yuca → harina, plátano → snacks)
- Canales directos al consumidor (mercados campesinos, entregas domicilio)''',
                'keywords': ['agricultura', 'familia', 'campesino', 'pequeño productor', 'rural'],
                'external_links': [
                    {'title': 'Agricultura familiar en Colombia', 'url': 'https://www.fao.org/family-farming/detail/es/c/1273839/', 'type': 'article'},
                ],
                'module_keys': ['ikigai', 'field_diary', 'jtbd'],
                'order': 26,
            },
            {
                'key': 'mercado_local',
                'category': 'territorial',
                'title': 'Mercado Local',
                'short_definition': 'Plaza de mercado del pueblo/municipio. Centro comercial rural donde campesinos venden productos y compran insumos.',
                'detailed_explanation': '''**Mercado Local (plaza)** es corazón económico rural.

**Dinámica:**
- Día de mercado: sábado o domingo (varía por región)
- Campesinos llegan desde veredas 4am-6am
- Venden: plátano, yuca, gallinas, panela, queso
- Compran: arroz, aceite, ropa, herramientas
- Intercambio social (noticias, chismes, política)

**Oportunidades:**
- Logística de mercado (transporte compartido vereda-plaza)
- Puestos permanentes (alquiler de espacio)
- Servicios conexos (café, comida, guardería niños mientras padres venden)
- Agregación: comprar a varios campesinos, revender a restaurantes ciudad

**Insight:** Plaza es también "red social análoga". Allí validas ideas (conversa con 20 personas en 2 horas).''',
                'keywords': ['mercado', 'plaza', 'comercio', 'local', 'campesino'],
                'external_links': [
                    {'title': 'Mercados campesinos Colombia', 'url': 'https://www.youtube.com/watch?v=0XJKzJ2q2Cw', 'type': 'video'},
                ],
                'module_keys': ['field_diary', 'jtbd', 'validation'],
                'order': 27,
            },
            {
                'key': 'infraestructura_rural',
                'category': 'territorial',
                'title': 'Infraestructura Rural',
                'short_definition': 'Vías, energía, agua, internet, salud, educación en zonas rurales. Generalmente precaria o inexistente.',
                'detailed_explanation': '''**Infraestructura Rural** determina viabilidad de muchos negocios.

**Realidad:**
- **Vías:** 70% caminos destapados, intransitables en lluvia
- **Energía:** 20% hogares sin electricidad o muy inestable
- **Agua:** Aljibes, quebradas (no potable)
- **Internet:** 10% tiene conexión fija, móvil limitado
- **Salud:** Puesto de salud 1-2 horas caminando
- **Educación:** Escuela primaria en vereda, secundaria en pueblo

**Implicaciones negocio:**
- Si necesitas internet estable (ej: vender por web) → problemas
- Productos perecederos → difícil sin refrigeración/transporte rápido
- Servicios digitales → clientes no tienen smartphones

**Oportunidad:** Negocios QUE RESUELVEN infraestructura (ej: carga celulares solar, purificación agua, transporte).''',
                'keywords': ['infraestructura', 'vías', 'servicios', 'rural', 'acceso'],
                'external_links': [
                    {'title': 'Brecha infraestructura rural Colombia', 'url': 'https://www.repository.fedesarrollo.org.co/handle/11445/3878', 'type': 'article'},
                ],
                'module_keys': ['field_diary', 'jtbd'],
                'order': 28,
            },
            {
                'key': 'desplazamiento',
                'category': 'territorial',
                'title': 'Desplazamiento Forzado',
                'short_definition': 'Migración involuntaria por violencia armada. En Colombia, 8+ millones de personas desplazadas, mayoría del campo a ciudad.',
                'detailed_explanation': '''**Desplazamiento** es realidad de muchos emprendedores en zonas PDET.

**Contexto:**
- Familias huyeron de veredas por violencia (guerrillas, paras, ejército)
- Perdieron tierra, casa, animales
- Muchos en proceso de retorno (Ley de Víctimas)
- Otros quedaron en ciudades, quieren emprender

**Características emprendedores desplazados:**
- Resiliencia extrema (sobrevivieron conflicto)
- Habilidades rurales (agricultura, construcción, cocina)
- Poca educación formal pero mucha experiencia
- Desconfianza en instituciones
- Necesidad urgente de ingresos

**Apoyos:** Víctimas de conflicto acceden a:
- Créditos blandos (Bancóldex, Banco Agrario)
- Capacitaciones gratis (SENA)
- Subsidios para proyectos productivos
- Preferencia en contratos públicos''',
                'keywords': ['desplazamiento', 'víctima', 'conflicto', 'retorno', 'migración'],
                'external_links': [
                    {'title': 'Unidad de Víctimas Colombia', 'url': 'https://www.unidadvictimas.gov.co/', 'type': 'article'},
                ],
                'module_keys': ['ikigai', 'empathy'],
                'order': 29,
            },
            {
                'key': 'madre_cabeza_familia',
                'category': 'territorial',
                'title': 'Madre Cabeza de Familia',
                'short_definition': 'Mujer que es único sostén económico del hogar. En zonas rurales, 35-40% hogares. Vulnerabilidad económica alta.',
                'detailed_explanation': '''**Madres Cabeza de Familia** son segmento emprendedor crítico.

**Perfil:**
- Sola (viuda, separada, padre ausente)
- 2-4 hijos menores
- Trabaja en casa + cultivo
- Ingresos < $500,000/mes
- Sin tiempo para empleo formal (cuida hijos)

**Barreras emprendimiento:**
- Poco capital (ahorros $0-$200,000)
- Sin garantías para crédito (no tiene tierra a su nombre)
- Carga de cuidado 24/7 (no puede ausentarse)
- Baja autoestima empresarial ("no sé nada de negocios")

**Ideas exitosas:**
- Negocios desde casa (panadería, costura, venta por catálogo)
- Servicios de cuidado compartido (guardería comunitaria)
- Cooperativas mujeres (fuerza colectiva)

**Suluhisho:** Si eres madre cabeza de familia, hay subsidios específicos (Prosperidad Social, Min Trabajo).''',
                'keywords': ['madre', 'mujer', 'familia', 'vulnerabilidad', 'género'],
                'external_links': [
                    {'title': 'Emprendimiento mujeres rurales', 'url': 'https://www.youtube.com/watch?v=lH9vZt4jDRQ', 'type': 'video'},
                ],
                'module_keys': ['ikigai', 'empathy'],
                'order': 30,
            },
            {
                'key': 'artesania_tradicional',
                'category': 'territorial',
                'title': 'Artesanía Tradicional',
                'short_definition': 'Productos hechos a mano con técnicas ancestrales: tejidos, cerámica, cestería, talla en madera. Identidad cultural + ingreso.',
                'detailed_explanation': '''**Artesanía Tradicional** combina cultura + economía.

**Ejemplos Colombia:**
- Mochilas Wayuu (Guajira)
- Sombreros vueltiaos (Córdoba, Sucre)
- Tejidos en fique (Santander)
- Cerámica negra (Cauca)
- Talla tagua (Chocó, Nariño)

**Ventajas:**
- Diferenciación (no se puede copiar en fábrica)
- Mercado turístico dispuesto a pagar más
- Identidad cultural (orgullo, tradición)
- Materia prima local (fique, barro, palma)

**Retos:**
- Producción lenta (1 mochila = 15 días)
- Difícil escalar sin perder artesanía
- Distribución limitada (ferias, turistas)
- Competencia con productos industriales baratos

**Estrategia:** Vender historia (no solo objeto). "Esta mochila la tejió Sofía, Wayuu de Uribía, con técnicas de su abuela".''',
                'keywords': ['artesanía', 'tradicional', 'cultura', 'hecho a mano', 'tejido'],
                'external_links': [
                    {'title': 'Artesanías de Colombia', 'url': 'https://artesaniasdecolombia.com.co/', 'type': 'article'},
                ],
                'module_keys': ['ikigai', 'value_prop'],
                'order': 31,
            },
            {
                'key': 'transformacion_productiva',
                'category': 'territorial',
                'title': 'Transformación Productiva',
                'short_definition': 'Procesar materias primas para agregar valor. Ej: Cacao → chocolate, Plátano → chips, Leche → queso. Aumenta ingresos 3-10x.',
                'detailed_explanation': '''**Transformación Productiva** es clave para salir de pobreza rural.

**Problema:** Campesino vende materia prima cruda, gana poco.
- Café cereza: $2,500/kg → Café tostado: $25,000/kg (10x más)
- Leche cruda: $1,200/litro → Queso: $15,000/kg (6x más con 2 litros leche)
- Cacao baba: $4,000/kg → Chocolate: $40,000/kg (10x más)

**Barreras:**
- Equipos caros (tostadora, empacadora, refrigerador)
- Registros sanitarios (INVIMA) complejos
- Conocimiento técnico (cómo tostar, fermentar, curar)
- Canales de venta urbanos (no saben cómo llegar a tiendas)

**Solución asociativa:** 10 familias invierten juntas en equipos, comparten conocimiento, venden marca colectiva.

**Apoyos:** SENA tiene centros de transformación, Cámara Comercio ayuda con registros.''',
                'keywords': ['transformación', 'valor agregado', 'procesamiento', 'producto', 'cadena'],
                'external_links': [
                    {'title': 'Valor agregado productos rurales', 'url': 'https://www.youtube.com/watch?v=TG1z-J8qYzg', 'type': 'video'},
                ],
                'module_keys': ['ideation', 'value_prop'],
                'order': 32,
            },
            {
                'key': 'cadena_valor',
                'category': 'territorial',
                'title': 'Cadena de Valor',
                'short_definition': 'Todos los pasos desde producción hasta cliente final. Ej: Cultivar café → beneficio → tostado → empaque → venta → consumidor.',
                'detailed_explanation': '''**Cadena de Valor** muestra dónde se gana (y se pierde) plata.

**Ejemplo café:**
1. Agricultor cultiva cereza: Costo $1,000/kg, vende $2,500/kg → **gana $1,500**
2. Intermediario procesa pergamino: Compra $2,500/kg, vende $8,000/kg → **gana $5,500**
3. Tostadora tuest y empaca: Compra $8,000/kg, vende $25,000/kg → **gana $17,000**
4. Tienda vende al consumidor: Compra $25,000/kg, vende $35,000/kg → **gana $10,000**

**Total cadena:** $35,000. Agricultor se queda con 7% ($2,500). Intermediarios + procesadores se quedan con 93%.

**Estrategia emprendedor:** "Subir" en la cadena (no solo cultivar, también procesar) o "acortar" cadena (vender directo sin intermediarios).''',
                'keywords': ['cadena', 'valor', 'intermediario', 'margen', 'eslabón'],
                'external_links': [
                    {'title': 'Cadena de valor agropecuaria', 'url': 'https://repository.agrosavia.co/handle/20.500.12324/35687', 'type': 'article'},
                ],
                'module_keys': ['jtbd', 'value_prop'],
                'order': 33,
            },
            {
                'key': 'asociatividad',
                'category': 'territorial',
                'title': 'Asociatividad',
                'short_definition': 'Unir fuerzas con otros productores/emprendedores para acceder a recursos, mercados y poder de negociación.',
                'detailed_explanation': '''**Asociatividad** es clave en rural (individualmente no compites, juntos sí).

**Formas:**
- **Cooperativa:** Propiedad colectiva, 1 persona = 1 voto
- **Asociación:** Grupo organizado, toma decisiones conjunta
- **Alianza:** Pacto temporal para proyecto específico

**Ventajas:**
- Comprar insumos por volumen (descuentos)
- Acceder a créditos (aval colectivo)
- Compartir equipos caros (camión, tractor, procesadora)
- Negociar mejores precios con compradores
- Cumplir pedidos grandes (1 solo no puede)

**Ejemplo:** 15 caficultores solos venden a $2,500/kg. Asociados venden a exportadora a $6,000/kg (saltaron intermediario).

**Reto:** Requiere confianza, reglas claras, transparencia financiera. SENA y Cámaras Comercio ayudan a formalizar.''',
                'keywords': ['asociatividad', 'cooperativa', 'colectivo', 'unión', 'alianza'],
                'external_links': [
                    {'title': 'Modelos asociativos rurales', 'url': 'https://conectarural.org/wp-content/uploads/2019/07/Modelos-asociativos-rurales.pdf', 'type': 'article'},
                ],
                'module_keys': ['value_prop', 'ideation'],
                'order': 34,
            },
            {
                'key': 'comercializacion',
                'category': 'territorial',
                'title': 'Comercialización',
                'short_definition': 'Proceso de vender tu producto: encontrar clientes, fijar precio, entregar, cobrar. Mayor reto para emprendedores rurales.',
                'detailed_explanation': '''**Comercialización** mata más negocios rurales que producción.

**Canales tradicionales:**
- Plaza de mercado (margen bajo, competencia alta)
- Intermediario (paga poco pero compra TODO)
- Puerta a puerta (lento, demanda tiempo)

**Canales nuevos:**
- **Mercados campesinos ciudad:** Venta directa sábados
- **Entregas domicilio:** WhatsApp + delivery
- **Tiendas especializadas:** Orgánicos, gourmet
- **Restaurantes:** Volumen medio, pago regular
- **Cooperativas consumo:** Clientes fijos mensual

**Claves éxito:**
1. **Consistencia:** Entregar misma calidad/cantidad cada semana
2. **Comunicación:** Avisar si hay retrasos
3. **Empaque:** Presentación importa (no bolsa sucia)
4. **Precio justo:** Ni muy caro (no compran) ni muy barato (no ganas)

**Herramientas:** WhatsApp Business (gratis), Instagram (fotos), grupos Facebook locales.''',
                'keywords': ['comercialización', 'venta', 'canal', 'distribución', 'cliente'],
                'external_links': [
                    {'title': 'Comercialización productos rurales', 'url': 'https://www.youtube.com/watch?v=9mJ_kVj3q0g', 'type': 'video'},
                ],
                'module_keys': ['value_prop', 'validation', 'jtbd'],
                'order': 35,
            },

            # ============ PLATAFORMA (15+ términos) ============
            {
                'key': 'modulo_suluhisho',
                'category': 'platform',
                'title': 'Módulo',
                'short_definition': 'Cada uno de los 7 pasos del proceso Suluhisho. Completas secuencialmente: no puedes saltar al Módulo 4 sin terminar Módulo 3.',
                'detailed_explanation': '''**Módulos Suluhisho:**

1. **Ikigai:** Descubres tu propósito
2. **Diario de Campo:** Observas problemas reales
3. **Mapa de Empatía + POV:** Entiendes a tu cliente
4. **JTBD:** Defines el "trabajo" a resolver
5. **Ideación:** Generas muchas ideas
6. **Value Prop:** Construyes propuesta de valor
7. **Validación:** Pruebas con clientes reales

**Secuencial:** No puedes empezar Módulo 5 (ideas) si no terminaste Módulo 3 (empatía). ¿Por qué? Porque tus ideas deben resolver el problema que descubriste en empatía.

**Tiempo:** 30-60 minutos por módulo. Total proceso: 4-7 horas repartidas en varios días.''',
                'keywords': ['módulo', 'paso', 'etapa', 'proceso', 'suluhisho'],
                'external_links': [],
                'module_keys': [],
                'order': 36,
            },
            {
                'key': 'progreso_suluhisho',
                'category': 'platform',
                'title': 'Progreso',
                'short_definition': 'Seguimiento de tu avance en cada módulo. Estados: No iniciado, En progreso, Completado. Dashboard muestra tu % general.',
                'detailed_explanation': '''**Progreso** te indica dónde estás en el proceso.

**Estados por módulo:**
- **No iniciado:** Aún no empiezas (gris)
- **En progreso:** Guardaste pero no completaste (amarillo)
- **Completado:** Terminaste y validaste (verde)

**Dashboard:** Muestra barra con % completitud:
- Módulo 1 done + Módulo 2 done + Módulo 3 in progress = 28% completitud total (2/7)

**Nota:** Puedes editar módulos completados si necesitas ajustar (ej: después de validación descubres algo nuevo en Módulo 7, vuelves a Módulo 5 a ajustar idea).''',
                'keywords': ['progreso', 'avance', 'completitud', 'dashboard', 'estado'],
                'external_links': [],
                'module_keys': [],
                'order': 37,
            },
            {
                'key': 'entregable',
                'category': 'platform',
                'title': 'Entregable',
                'short_definition': 'Lo que produces en cada módulo: formularios, textos, audios, fotos. Se guarda en tu perfil y tu facilitador puede revisarlo.',
                'detailed_explanation': '''**Entregable** es la evidencia de tu trabajo.

**Tipos:**
- **Texto:** Respuestas formularios (mayoría módulos)
- **Audio:** Grabas voz si prefieres hablar que escribir
- **Imagen:** Fotos del Diario de Campo, bosquejos de ideas

**Versiones:** Si editas un módulo, se guarda versión nueva. Facilitador ve historial completo.

**Revisión:** Tu facilitador puede:
- Ver tus entregables
- Agregar comentarios
- Sugerir mejoras
- Aprobar o solicitar corrección

**Privacidad:** Solo tú y tu facilitador ven tus entregables. No son públicos.''',
                'keywords': ['entregable', 'evidencia', 'respuesta', 'formulario', 'resultado'],
                'external_links': [],
                'module_keys': [],
                'order': 38,
            },
            {
                'key': 'facilitador_suluhisho',
                'category': 'platform',
                'title': 'Facilitador',
                'short_definition': 'Mentor asignado que acompaña tu proceso. Revisa entregables, da retroalimentación, responde preguntas. Puede ser presencial o virtual.',
                'detailed_explanation': '''**Facilitador** es tu guía en Suluhisho.

**Rol:**
- Revisa tus entregables módulo por módulo
- Da retroalimentación específica (no solo "bien" o "mal")
- Responde dudas sobre metodología
- Te motiva cuando te atascas
- Conecta con recursos (créditos, capacitaciones, redes)

**No es jefe:** Es un mentor. Tú tomas decisiones sobre tu negocio.

**Comunicación:** Según modelo:
- Presencial: Reuniones en vereda/municipio cada semana
- Virtual: WhatsApp, llamadas, videollamadas
- Híbrido: Presencial 1x mes + virtual continuo

**Asignación:** Sistema te asigna facilitador según tu ubicación geográfica (idealmente alguien de tu región que conoce contexto).''',
                'keywords': ['facilitador', 'mentor', 'guía', 'acompañamiento', 'retroalimentación'],
                'external_links': [],
                'module_keys': [],
                'order': 39,
            },
            {
                'key': 'diario_campo',
                'category': 'platform',
                'title': 'Diario de Campo (Módulo 2)',
                'short_definition': 'Registro de observaciones de situaciones/problemas reales en tu territorio. Mínimo 3 observaciones diferentes antes de continuar.',
                'detailed_explanation': '''**Diario de Campo** es tu trabajo de etnografía.

**Qué registrar:**
- **Situación:** Qué observaste (sin juicio)
- **Personas afectadas:** Quiénes viven el problema
- **Contexto:** Cuándo, dónde, con qué frecuencia
- **Foto (opcional):** Evidencia visual

**Ejemplo buena observación:**
"Martes 7am, parada de bus vereda El Silencio. Vi 12 personas (8 mujeres, 4 niños) esperando bus que llega a las 10am. Hacía frío (12°C), no hay techo. Mujeres llevan canastas con gallinas para vender en plaza. Una señora me dijo que siempre llega tarde y pierde primeras ventas del día."

**Mínimo 3 observaciones:** Para ver patrones, no excepciones.''',
                'keywords': ['diario', 'campo', 'observación', 'problema', 'registro'],
                'external_links': [],
                'module_keys': ['field_diary'],
                'order': 40,
            },
            {
                'key': 'ikigai_suluhisho',
                'category': 'platform',
                'title': 'Ikigai (Módulo 1)',
                'short_definition': 'Descubres tu propósito respondiendo 4 preguntas: Qué amas, En qué eres bueno, Qué necesita tu comunidad, Por qué pagarían. Intersección = tu propósito.',
                'detailed_explanation': '''**Ikigai** (palabra japonesa = "razón de ser") adaptado a contexto emprendedor rural colombiano.

**4 Círculos:**
1. **Amas:** Actividades que haces con gusto
2. **Bueno:** Habilidades que otros reconocen en ti
3. **Necesita comunidad:** Problemas que ves sin resolver
4. **Pagarían:** Por qué servicios/productos la gente da dinero

**Intersección:** Donde se cruzan los 4 círculos está tu idea de negocio ideal.

**Ejemplo:** Amas cocinar + Eres buena en repostería + Tu comunidad no tiene panadería cerca + La gente paga por pan fresco = **Panadería artesanal en tu vereda**.

**No es obligatorio:** Puede que tu respuesta no sea perfecta al inicio. Está bien. Ikigai es guía, no camisa de fuerza.''',
                'keywords': ['ikigai', 'propósito', 'razón de ser', 'intersección', 'vocación'],
                'external_links': [],
                'module_keys': ['ikigai'],
                'order': 41,
            },
            {
                'key': 'mapa_empatia_suluhisho',
                'category': 'platform',
                'title': 'Mapa de Empatía (Módulo 3)',
                'short_definition': 'Describes 1 persona específica de tu Diario de Campo: qué piensa/siente, ve, oye, dice/hace, frustraciones, necesidades. Termina con POV.',
                'detailed_explanation': '''**Mapa de Empatía** te obliga a ver el mundo desde ojos de tu cliente.

**Proceso:**
1. Elige 1 persona de tu Diario de Campo
2. Dale nombre (puede ser ficticio)
3. Responde 6 dimensiones poniéndote en sus zapatos
4. Sintetiza en POV: [Persona] necesita [X] porque [Y]

**Clave:** Usa primera persona indirecta. "María piensa que...", "María siente que...", "María ve que..."

**Error común:** Describir en tercera persona analítica ("ella es una mujer de 30 años que trabaja..."). ❌ Correcto: Empático ("Le preocupa que sus hijos no estudien secundaria porque no hay colegio cerca y transporte cuesta $60,000/mes que ella no tiene"). ✅''',
                'keywords': ['empatía', 'mapa', 'persona', 'pov', 'cliente'],
                'external_links': [],
                'module_keys': ['empathy'],
                'order': 42,
            },
            {
                'key': 'jtbd_suluhisho',
                'category': 'platform',
                'title': 'JTBD (Módulo 4)',
                'short_definition': 'Defines el "trabajo" que tu cliente quiere hacer. Estructura: Cuando [situación], quiero [acción], para [resultado]. Síntesis del POV.',
                'detailed_explanation': '''**JTBD en Suluhisho** transforma tu POV en acción.

**De POV a JTBD:**
- **POV:** "María necesita vender sus verduras sin intermediario porque pierde 60% del precio"
- **JTBD:** "Cuando cosecho lechugas los viernes, quiero venderlas directo a restaurantes del pueblo, para quedarme con 80% del precio final en lugar de 40%"

**3 Partes obligatorias:**
- **Cuando:** Situación específica (no "siempre")
- **Quiero:** Acción/motivación clara
- **Para:** Resultado medible

**Por qué importa:** Tu idea (Módulo 5) debe resolver este JTBD. Si no, estás resolviendo problema equivocado.''',
                'keywords': ['jtbd', 'trabajo', 'necesidad', 'cliente', 'situación'],
                'external_links': [],
                'module_keys': ['jtbd'],
                'order': 43,
            },
            {
                'key': 'ideacion_suluhisho',
                'category': 'platform',
                'title': 'Ideación (Módulo 5)',
                'short_definition': 'Generas mínimo 5 ideas de solución para tu JTBD. Luego eliges Top 3 y finalmente 1 idea final a desarrollar.',
                'detailed_explanation': '''**Ideación** usa brainstorming + SCAMPER.

**Proceso:**
1. Genera 5-6 ideas SIN juzgar (cantidad > calidad)
2. Selecciona Top 3 explicando por qué las elegiste
3. Define 1 idea final (la más viable + impacto)

**Criterios selección:**
- **Resuelve JTBD:** ¿Aborda problema real?
- **Viable:** ¿Puedes hacerlo con tus recursos?
- **Demanda:** ¿La gente pagaría?
- **Diferente:** ¿Qué tiene que otros no?

**Ejemplo:**
- Idea 1: App pedidos verduras
- Idea 2: Grupo WhatsApp pedidos + delivery moto
- Idea 3: Puesto fijo plaza mercado
- Idea 4: Alianza restaurantes entrega semanal
- Idea 5: Cooperativa venta verduras colectiva

→ **Elijo Idea 4** (alianza restaurantes) porque ya tengo moto, restaurantes confirman interés, inversión mínima.''',
                'keywords': ['ideación', 'ideas', 'brainstorming', 'solución', 'creatividad'],
                'external_links': [],
                'module_keys': ['ideation'],
                'order': 44,
            },
            {
                'key': 'propuesta_valor_suluhisho',
                'category': 'platform',
                'title': 'Propuesta de Valor (Módulo 6)',
                'short_definition': 'Detallas tu idea: qué frustraciones alivia, qué ganancias crea, cómo es tu producto/servicio. Síntesis en 1 frase.',
                'detailed_explanation': '''**Propuesta de Valor** usa Value Proposition Canvas.

**2 Lados:**

**Lado Cliente (de Empatía):**
- 3 Frustraciones principales
- 3 Ganancias deseadas

**Lado Oferta (tu solución):**
- Productos/servicios (qué vendes)
- Aliviadores de dolor (cómo quitas frustraciones)
- Creadores de ganancia (cómo generas beneficios)

**Síntesis:** "Para [cliente] que tiene [problema], mi [solución] [diferenciador]."

**Ejemplo:** "Para restaurantes del pueblo que pierden tiempo yendo a plaza a comprar verduras variables en calidad, mi servicio de entrega semanal de verduras frescas certificadas orgánicas directamente de mi finca, garantiza ahorro de 4 horas/semana y calidad constante con precio fijo anual."''',
                'keywords': ['propuesta', 'valor', 'canvas', 'diferenciación', 'oferta'],
                'external_links': [],
                'module_keys': ['value_prop'],
                'order': 45,
            },
            {
                'key': 'validacion_suluhisho',
                'category': 'platform',
                'title': 'Validación (Módulo 7)',
                'short_definition': 'Haces mínimo 3 entrevistas con clientes reales. Preguntas: ¿Tiene el problema? ¿Cómo lo resuelve hoy? ¿Pagaría por tu solución? ¿Cuánto?',
                'detailed_explanation': '''**Validación** es el momento de la verdad.

**Proceso por entrevista:**
1. Elige persona de tu cliente ideal
2. **Primero:** Valida PROBLEMA (no hables aún de tu solución)
   - "¿Has experimentado [problema]?"
   - "¿Qué tan seguido?"
   - "¿Cómo lo manejas hoy?"
3. **Después:** Presenta tu solución
   - Explica en 2-3 oraciones
   - Observa reacción (¿se emociona? ¿indiferente?)
4. **Pregunta clave:** "¿Pagarías por esto? ¿Cuánto?"
5. **Aprende:** Qué te sorprendió, qué confirma/contradice tus suposiciones

**Mínimo 3 entrevistas:** Para ver patrones.

**Señales buenas:** Pregunta por precio/fecha lanzamiento, quiere ser beta tester, te recomienda con otros.
**Señales malas:** Dice "interesante" pero no compromete, pone objeciones que matan idea ("muy caro", "eso ya existe mejor").''',
                'keywords': ['validación', 'entrevista', 'cliente', 'prueba', 'feedback'],
                'external_links': [],
                'module_keys': ['validation'],
                'order': 46,
            },
            {
                'key': 'gating_secuencial',
                'category': 'platform',
                'title': 'Gating Secuencial',
                'short_definition': 'Sistema que te obliga a completar módulos en orden 1→2→3→4→5→6→7. No puedes saltar pasos. Asegura proceso riguroso.',
                'detailed_explanation': '''**Gating Secuencial** es regla de Suluhisho: no saltas módulos.

**Por qué:**
- Módulo 5 (ideas) necesita Módulo 3 (empatía) completado
- Módulo 6 (value prop) necesita Módulo 4 (JTBD) completado
- Módulo 7 (validación) necesita Módulo 6 (value prop) completado

**Excepción:** Puedes EDITAR módulos anteriores. Ejemplo: En Módulo 7 descubres que tu idea no funciona → Vuelves a Módulo 5 (ideación) → Eliges otra idea del Top 3 → Ajustas Módulo 6 → Repites Módulo 7.

**No es restricción:** Es guía para no inventar soluciones sin entender problema primero.''',
                'keywords': ['gating', 'secuencial', 'orden', 'bloqueo', 'proceso'],
                'external_links': [],
                'module_keys': [],
                'order': 47,
            },
            {
                'key': 'perfil_emprendedor',
                'category': 'platform',
                'title': 'Perfil Emprendedor',
                'short_definition': 'Tu información personal: nombre, ubicación (vereda/municipio), si eres PDET, víctima conflicto, madre cabeza familia. Ayuda a personalizar contenido.',
                'detailed_explanation': '''**Perfil Emprendedor** guarda tu contexto.

**Información:**
- Nombre completo
- Teléfono/WhatsApp (principal contacto)
- Departamento, Municipio, Vereda
- Flags especiales:
  - ¿Zona PDET?
  - ¿Víctima de conflicto?
  - ¿Madre/Padre cabeza de familia?
  - ¿Desplazado?
  - Nivel educativo

**Por qué importa:**
- Ejemplos territoriales se muestran según tu región
- Facilit ador asignado es de tu zona
- Acceso a subsidios específicos (si eres víctima, PDET, etc.)
- Lenguaje adaptado a nivel educativo

**Privacidad:** Info sensible (víctima conflicto) solo visible para ti y facilitador. No pública.''',
                'keywords': ['perfil', 'emprendedor', 'datos', 'información', 'contexto'],
                'external_links': [],
                'module_keys': [],
                'order': 48,
            },
            {
                'key': 'retroalimentacion',
                'category': 'platform',
                'title': 'Retroalimentación',
                'short_definition': 'Comentarios de tu facilitador sobre tus entregables. Puede ser aprobación, sugerencias mejora, o solicitud de corrección.',
                'detailed_explanation': '''**Retroalimentación** es clave para calidad.

**Tipos:**
- **Aprobación:** "Excelente trabajo. Tu POV está bien estructurado y específico. Puedes continuar."
- **Sugerencia:** "Buen inicio. Sugiero agregar más detalle en las frustraciones. Piensa: ¿qué palabras exactas usa tu cliente para describir su dolor?"
- **Corrección:** "Tu JTBD no sigue estructura Cuando/Quiero/Para. Por favor revisa el ejemplo y reescribe."

**Cuándo llega:** Facilitador revisa dentro de 24-48 horas después de que completas módulo.

**Cómo responder:** Si pide corrección, editas el módulo y reenvías. Facilitador recibe notificación.

**No es examen:** Es acompañamiento. Facilitador quiere que tengas mejor idea posible, no "aprobar o reprobar".''',
                'keywords': ['retroalimentación', 'feedback', 'comentario', 'revisión', 'mejora'],
                'external_links': [],
                'module_keys': [],
                'order': 49,
            },
            {
                'key': 'calidad_respuesta',
                'category': 'platform',
                'title': 'Calidad de Respuesta',
                'short_definition': 'Score automático 0-100 que evalúa tus entregables: longitud, especificidad, conexión entre módulos. Ayuda a mejorar antes de enviar.',
                'detailed_explanation': '''**Calidad de Respuesta** usa validadores automáticos.

**Criterios:**
- **Longitud:** Campos importantes necesitan detalle (no respuestas de 2 palabras)
- **Especificidad:** Menciona lugares, nombres, números (no genéricos como "la gente", "siempre")
- **Estructura:** Sigue templates (POV, JTBD, Value Prop)
- **Conexión:** Módulos 3→4→5→6 deben tener coherencia (keywords compartidos)

**Scores:**
- 0-40: ⚠️ Básico (necesita mucho trabajo)
- 41-69: ✅ Bueno (puede mejorar)
- 70-89: ✅ Muy Bueno
- 90-100: 🏆 Excepcional

**No bloquea:** Puedes completar módulo con score bajo, pero recibirás sugerencias de mejora. Facilitador puede pedirte revisar si calidad muy baja.''',
                'keywords': ['calidad', 'score', 'evaluación', 'validación', 'mejora'],
                'external_links': [],
                'module_keys': [],
                'order': 50,
            },
        ]


