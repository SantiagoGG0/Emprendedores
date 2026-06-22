"""
Management command to populate Module instructional content from PDF guide.
"""

from django.core.management.base import BaseCommand
from core.models import Module


class Command(BaseCommand):
    help = 'Populate instructional content for all 7 modules from Suluhisho PDF guide'

    def handle(self, *args, **options):
        self.stdout.write('Populating module instructional content...')
        
        # Module 1: Ikigai
        self.update_module(
            key=Module.IKIGAI,
            why_exists="""El error más frecuente al iniciar un emprendimiento es elegir una idea por moda, por imitación de otro negocio o por creer que "eso vende". La investigación sobre emprendimiento sostenible muestra que los negocios con mayor probabilidad de sobrevivir son los que conectan con el propósito personal del fundador, sus fortalezas reales y una necesidad genuina del entorno.

El Ikigai es un concepto japonés que significa "razón de ser". Cuando una persona encuentra la intersección entre lo que ama hacer, lo que sabe hacer bien, lo que el mundo necesita y lo que le pagarían, está en su zona de mayor potencial emprendedor. Este paso no es un trámite: es el cimiento emocional del proyecto.""",
            
            how_to_guide="""Tiempo estimado: 30–45 minutos
Materiales: Papel y lápiz, o el formulario de la plataforma

Instrucción 1 — Responde honestamente estas cuatro preguntas:

⚠ Escribe al menos 3 respuestas para cada pregunta. No hay respuestas correctas ni incorrectas.

Las 4 preguntas del Ikigai:

1. ¿Qué actividades haces con gusto, incluso sin que te paguen?
   Ejemplos: Cocinar para otros, reparar cosas, cuidar animales, enseñar a vecinos, organizar eventos, cultivar, construir

2. ¿En qué te dicen los demás que eres bueno/a?
   Ejemplos: "Eres muy detallista", "siempre arreglas todo", "cocinas sabroso", "sabes tratar a los niños"

3. ¿Qué problemas ves en tu comunidad que a nadie más parece importarle o que nadie ha resuelto?
   Ejemplos: Falta de mercado cercano, transporte caro, residuos sin manejo, productos agrícolas sin procesar

4. ¿Por qué cosas estarían dispuestos a pagar las personas de tu comunidad?
   Ejemplos: Productos elaborados, servicios de limpieza, transporte, cuidado de adultos mayores, comida lista

Instrucción 2 — Encuentra la zona de intersección:

Revisa tus respuestas y busca dónde se cruzan. Hazlo con esta pregunta:

"¿Hay algo que yo amo hacer, que sé hacer bien, que mi comunidad necesita y que alguien pagaría por ello?"

Escribe esa intersección en una sola frase.

Ejemplo:
"Me encanta cocinar, soy buena en eso, en mi vereda no hay dónde comprar comida preparada y las familias que trabajan todo el día pagarían por un almuerzo listo."

Ejemplo aplicado — Territorio PDET (Antioquia):

Emprendedora: Mujer campesina, municipio de Ituango, desplazada interna.
- Lo que ama: tejer y trabajar con fibras naturales.
- En qué es buena: artesanías en fique y caña.
- Qué necesita el mundo: productos artesanales con identidad territorial, demandados en ciudades y exportación.
- Qué pagarían: turistas, tiendas de diseño urbano, proyectos de economía circular.
- Intersección Ikigai: Emprendimiento de artesanías con identidad territorial, vinculado a circuitos de turismo y comercio justo.""",
            
            common_errors="""❌ Escribir lo que crees que "deberías" responder, no lo que realmente sientes

❌ Copiar la idea de negocio de alguien más sin pasar por esta reflexión

❌ Saltar este paso por considerarlo "filosófico" — es el anclaje emocional del proyecto""",
            
            deliverable_description="""✅ Cuatro respuestas completadas (mínimo 3 respuestas por pregunta) + Frase de intersección Ikigai registrada en el perfil del emprendedor."""
        )
        
        # Module 2: Field Diary
        self.update_module(
            key=Module.FIELD_DIARY,
            why_exists="""La mayor fuente de oportunidades de negocio no está en internet ni en libros: está en la vida cotidiana del territorio. Los emprendedores exitosos no inventan problemas — los descubren observando con atención lo que otros ignoran.

La investigación sobre reconocimiento de oportunidades identifica la alerta emprendedora (entrepreneurial alertness) como una habilidad que se puede entrenar. Se entrena haciendo exactamente esto: salir a observar, hacerse preguntas y registrar lo que se ve. Un estudio que analizó 60 artículos académicos confirmó que la observación sistemática del entorno es el método más accesible para personas sin formación empresarial previa para identificar oportunidades reales.""",
            
            how_to_guide="""Tiempo estimado: 3 días de observación (15–20 minutos por día)
Materiales: Cuaderno, notas de voz en el celular, o el formulario de la plataforma

Instrucción 1 — Durante 3 días, sal a observar tu comunidad con estas preguntas en mente:

⚠ Puedes escribir, dibujar, grabar una nota de voz o tomar una foto.

Las 5 preguntas del observador:

1. ¿Qué le frustra a la gente de tu comunidad? (quejas frecuentes, discusiones, caras de cansancio)

2. ¿Qué proceso es lento, costoso o difícil de hacer aquí? (comprar ciertos productos, tramitar documentos, transportarse)

3. ¿Qué cosas tienen que hacer las personas que nadie disfruta hacer pero todos tienen que hacer?

4. ¿Qué no existe en tu territorio pero sería muy útil si existiera?

5. ¿Qué hacen muchas personas que hacen mal o con dificultad, y podrían hacerlo mejor con ayuda?

Instrucción 2 — Registra al menos 5 observaciones. Para cada una, completa esta ficha simple:

```
Observación N°___
¿Qué vi o escuché?
¿A quién le pasa?
¿Con qué frecuencia ocurre?
¿Qué tan molesto o importante parece ser para quien lo vive?
```

Instrucción 3 — Al final del día 3, revisa tus observaciones:

- ¿Cuál se repite más veces?
- ¿Cuál le afecta a más personas?
- ¿Cuál tiene que ver con tu Ikigai (Paso 1)?

Ese cruce es el candidato a convertirse en el problema que vas a explorar.

Ejemplo aplicado — Municipio rural, Chocó:

Observaciones registradas por un joven emprendedor:

1. Las mamás de la vereda caminan 1 hora para llevar a sus hijos al puesto de salud más cercano — ocurre cada semana, genera mucho desgaste.

2. Los agricultores tiran la fruta que no pueden vender por falta de compradores — ocurre en temporada de cosecha, genera pérdidas económicas.

3. Los jóvenes que terminan bachillerato no saben qué hacer, no hay donde trabajar — situación permanente, genera frustración y migración.

4. No hay servicio de transporte confiable — todos lo mencionan como queja diaria.

5. Los productos de aseo son muy costosos porque vienen de lejos — afecta a todas las familias.

Problema candidato: Pérdida de fruta por falta de transformación y comercialización (conecta con conocimiento agrícola local + impacto económico colectivo).""",
            
            common_errors="""❌ Registrar solo problemas propios, sin salir a observar a otros

❌ Apresurarse a pensar en soluciones antes de completar las observaciones

❌ Descartar problemas por parecerlos "muy pequeños" — los mejores negocios suelen resolver problemas cotidianos ignorados""",
            
            deliverable_description="""✅ Mínimo 5 observaciones registradas + Problema candidato identificado."""
        )
        
        # Module 3: Empathy
        self.update_module(
            key=Module.EMPATHY,
            why_exists="""El error más costoso en emprendimiento temprano no es falta de dinero ni de tiempo: es construir una solución para un problema que nadie tiene, o que no es tan importante como se creía. El Double Diamond (British Design Council) y el Lean Startup coinciden en que definir correctamente el problema es más valioso que diseñar la solución.

Este paso tiene dos herramientas complementarias: el Mapa de Empatía (para entender profundamente a la persona que vive el problema) y el Enunciado POV (para definir el problema con claridad y precisión).

El Mapa de Empatía es un esquema visual que ayuda a "meterse en los zapatos" de la persona que tiene el problema. No se trata de suponer cómo se siente: se trata de ir a hablar con ella y escucharla.""",
            
            how_to_guide="""Tiempo estimado: 45–60 minutos
Materiales: Guía de entrevista impresa o digital

HERRAMIENTA 3A — MAPA DE EMPATÍA

Paso previo: Escoge una persona real de tu comunidad que vive el problema que identificaste en el Paso 2. Habla con ella 15–20 minutos con estas preguntas:

⚠ Regla de oro de la empatía: Tú hablas 20% del tiempo. La otra persona habla 80%.

Las 6 dimensiones del Mapa de Empatía:

1. ¿Qué PIENSA y SIENTE?
   - ¿Qué es lo que más le preocupa de este problema?
   - ¿Cómo se siente cuando lo vive?
   - Registra: Sus emociones, preocupaciones, aspiraciones profundas

2. ¿Qué VE?
   - ¿Cómo es su entorno? ¿Qué alternativas tiene a su alcance?
   - Registra: Lo que observa en su día a día relacionado con el problema

3. ¿Qué DICE y HACE?
   - ¿Cómo describe el problema con sus propias palabras?
   - ¿Qué hace hoy para resolverlo?
   - Registra: Sus comportamientos reales y el lenguaje que usa

4. ¿Qué ESCUCHA?
   - ¿Qué le dicen sus vecinos, familia o conocidos sobre este problema?
   - Registra: La influencia del entorno social sobre su percepción

5. DOLORES
   - ¿Qué le frustra, qué le da miedo, qué obstáculos enfrenta?
   - Registra: Sus principales fricciones y barreras

6. GANANCIAS
   - ¿Qué sueña lograr? ¿Cómo sería su vida si esto estuviera resuelto?
   - Registra: Sus expectativas, deseos y éxitos esperados

⚠ Tip práctico: Usa las palabras exactas que la persona usó. No las interpretes todavía. Escríbelas entre comillas.

HERRAMIENTA 3B — ENUNCIADO POV (POINT OF VIEW)

¿Qué es? Una frase corta y precisa que resume quién tiene el problema, qué necesita y por qué. Es la definición oficial del problema que vas a resolver.

Estructura del enunciado POV:

"[Descripción de la persona] necesita [necesidad real, expresada como verbo] porque [causa raíz o insight más importante del problema]."

Cómo construirlo:

1. Del Mapa de Empatía, extrae el dolor más importante (el que más angustia genera)
2. Identifica la necesidad subyacente (no el síntoma, sino la raíz)
3. Formula la frase

Ejemplo 1 — Rural:
"Las madres campesinas de veredas alejadas necesitan acceder a atención médica básica sin perder el día de trabajo porque el único puesto de salud está a más de una hora y los horarios no se adaptan a sus jornadas agrícolas."

Ejemplo 2 — Urbano periférico:
"Los jóvenes de comunas populares que terminan el bachillerato necesitan construir una ruta de ingreso económico legal y cercana a su barrio porque la oferta de trabajo formal está concentrada en zonas de la ciudad de difícil acceso y con requisitos que ellos no cumplen."

Prueba de calidad del POV — Hazte estas preguntas:

✓ ¿Hay una persona específica, no una categoría abstracta?
✓ ¿La necesidad es un verbo de acción (acceder, conseguir, transformar), no un adjetivo?
✓ ¿El "porque" explica la causa real, no solo repite el problema?
✓ ¿El enunciado abre posibilidades de solución sin imponer una específica?

Si respondiste sí a todo: tu POV está listo.""",
            
            common_errors="""❌ Construir el mapa de empatía sin hablar con nadie, solo desde supuestos propios

❌ Escribir en el POV la solución en lugar del problema ("necesita un mercado virtual" en vez de "necesita acceder a productos frescos de forma asequible")

❌ Elegir un problema demasiado amplio ("la pobreza") — el POV debe ser concreto y accionable""",
            
            deliverable_description="""✅ Mapa de Empatía completo (6 dimensiones) + Enunciado POV registrado con sus tres partes (persona / necesidad / causa)."""
        )
        
        # Module 4: JTBD
        self.update_module(
            key=Module.JTBD,
            why_exists="""Las personas no compran productos ni servicios. Los "contratan" para lograr un progreso específico en su vida. Clayton Christensen, profesor de Harvard, ilustra esto con un ejemplo clásico: McDonald's descubrió que sus batidos no competían con otros batidos — competían con barras de cereal y bananos. Los conductores los compraban en la mañana para no tener hambre en el trayecto al trabajo sin ensuciar el carro. El trabajo real era "mantenerse ocupado y sin hambre durante el tráfico".

Este paso obliga al emprendedor a ir más allá del problema superficial y encontrar el trabajo real que el cliente necesita completar: su dimensión funcional (qué tarea), social (qué imagen quiere proyectar) y emocional (cómo quiere sentirse). Este entendimiento profundo es lo que diferencia una buena solución de una solución que transforma vidas.""",
            
            how_to_guide="""Tiempo estimado: 20–30 minutos
Materiales: La información del Paso 3 + el formulario de la plataforma

Instrucción 1 — Define el Job Statement (enunciado del trabajo):

El Job Statement describe el trabajo en formato: verbo + objeto + clarificador contextual.

Ejemplos:
- "Conseguir alimentos frescos sin gastar el día entero en transporte"
- "Transformar la cosecha de fruta antes de que se pierda"
- "Encontrar ingresos legales cerca del hogar sin descuidar a los hijos"

Instrucción 2 — Completa el Canvas JTBD de tres dimensiones:

Retoma la persona del Paso 3 y responde:

| Dimensión | Pregunta | Tu respuesta |
|-----------|----------|--------------|
| Funcional | ¿Qué tarea concreta necesita completar esta persona? | (Escribe el Job Statement) |
| Social | ¿Cómo quiere que la vean los demás cuando logre esto? ¿Qué imagen quiere proyectar en su comunidad? | Ej: "Quiero que me vean como una madre responsable que provee bien para su familia" |
| Emocional | ¿Cómo quiere sentirse cuando el trabajo esté hecho? ¿De qué quiere liberarse? | Ej: "Quiero sentir tranquilidad, no tener que preocuparme por si alcanza" |

Instrucción 3 — Descompón el trabajo en etapas (Job Steps):

Pregúntate: ¿qué tiene que hacer la persona, paso a paso, para completar este trabajo hoy? Esto revela exactamente dónde está el dolor más grande y dónde puede intervenir tu solución.

Ejemplo: Trabajo = "Conseguir alimentos frescos"

1. Planear qué necesita comprar
2. Conseguir transporte (pagar o conseguir quien lleve)
3. Viajar al mercado (tiempo y costo)
4. Seleccionar y comprar productos
5. Regresar a casa
6. Almacenar lo comprado

¿Dónde está el mayor dolor? Paso 2 y 3 (transporte: caro, incierto, consume todo el día).

¿Dónde puede intervenir tu solución? Llevar el mercado hasta la vereda, o crear un punto de compra colectivo.

Ejemplo aplicado — Zona PDET, Putumayo:

Trabajo identificado: "Procesar y vender la cosecha de cacao antes de que se deteriore"

| Dimensión | Respuesta |
|-----------|-----------|
| Funcional | Transformar cacao fresco en pasta o chocolate artesanal para vender a mejor precio que el grano bruto |
| Social | Ser reconocido como productor que agrega valor, no solo como cultivador de subsistencia |
| Emocional | Sentir orgullo por vivir dignamente del trabajo propio sin depender de intermediarios |

Job Steps: Cosechar → Fermentar → Secar → Tostar → Moler → Envasar → Distribuir

Mayor dolor: Los pasos de moler, envasar y distribuir (sin equipos ni canales de venta).""",
            
            common_errors="""❌ Quedarse solo en la dimensión funcional e ignorar lo social y emocional

❌ Confundir el trabajo con la solución ("El trabajo es usar una app" — eso es una solución, no un trabajo)

❌ Inventar las dimensiones sin validarlas con la persona real del Paso 3""",
            
            deliverable_description="""✅ Job Statement formulado + Canvas JTBD de tres dimensiones completado + Job Steps identificados con señalamiento del mayor punto de dolor."""
        )
        
        # Module 5: Ideation
        self.update_module(
            key=Module.IDEATION,
            why_exists="""La ideación creativa requiere pensamiento divergente (generar la mayor cantidad posible de ideas, sin juzgar) antes de aplicar pensamiento convergente (filtrar, priorizar y seleccionar). La investigación en creatividad muestra que juzgar las ideas en el momento en que se generan es la principal causa de bloqueo creativo: el miedo a la crítica inhibe las ideas más originales.

SCAMPER es una técnica de ideación sistemática ampliamente validada que activa siete tipos de pensamiento creativo aplicados a un problema o solución existente. Es especialmente útil para comunidades con recursos limitados, porque parte de lo que ya existe en el territorio y propone transformarlo.""",
            
            how_to_guide="""Tiempo estimado: 45-60 minutos
Materiales: Papel grande, post-its, lapiceros de colores (o el formulario digital)

PASO PREVIO: RECUERDA TU IKIGAI (5 MINUTOS)

Antes de generar ideas, revisa tus respuestas del Paso 1 (Ikigai). Las mejores ideas conectan el problema que identificaste con lo que tu amas hacer y en lo que eres bueno.

1. Que amas hacer:
Revisa las actividades que escribiste en el Paso 1. Las soluciones que disfrutes implementar tienen mas probabilidad de sostenerse en el tiempo.

2. En que eres bueno:
Revisa tus fortalezas. Las ideas mas factibles son las que aprovechan habilidades que ya tienes o que puedes desarrollar facilmente.

3. Conexion con el problema:
Preguntate: Como puedo usar lo que amo hacer y lo que se hacer bien para resolver el problema que identifique en los pasos anteriores?

ETAPA 1: BRAINSTORMING LIBRE (15 MINUTOS)

Reglas del brainstorming:
1. No juzgar ni criticar ninguna idea (ni las propias ni las de otros)
2. Cantidad antes que calidad
3. Las ideas locas son bienvenidas, pueden contener la semilla de algo valioso
4. Construir sobre las ideas de otros (y si a esa idea le anadimos...)

Instruccion: Escribe todas las posibles soluciones al problema definido en el Paso 3. Minimo 10 ideas en 15 minutos. No te detengas a evaluar ninguna.

ETAPA 2: SCAMPER (30 MINUTOS)

Toma el problema o una solucion preliminar y aplica las 7 preguntas del SCAMPER:

S - Sustituir
Que parte del proceso o del producto actual podrias reemplazar por algo mas accesible, barato o local?
Ejemplo: En vez de transporte a la ciudad, sustituir con una ruta colectiva semanal

C - Combinar
Podrias unir dos necesidades del territorio en una sola solucion?
Ejemplo: Combinar transporte de personas y de productos en un mismo servicio

A - Adaptar
Hay una solucion que funciona en otro lugar o sector que podrias adaptar a tu contexto?
Ejemplo: Adaptar el modelo de tiendas comunitarias que funcionan en otras veredas

M - Modificar
Que pasaria si cambiaras el tamano, el precio, el horario o la forma de entrega?
Ejemplo: Y si el servicio fuera a domicilio, en lugar de que la persona vaya al servicio

P - Otro uso
Hay algun recurso del territorio que ya existe pero podria usarse de una forma diferente?
Ejemplo: Usar el cultivo de platano no solo para venta de fruta sino para producir harina

E - Eliminar
Que parte del proceso actual es innecesaria o podria quitarse para hacerlo mas simple?
Ejemplo: Eliminar intermediarios vendiendo directamente a restaurantes de la ciudad

R - Reorganizar
Que pasaria si cambiaras el orden del proceso, o lo volcaras al reves?
Ejemplo: Y si el cliente decide el pedido antes de la cosecha (venta anticipada)

ETAPA 3: SELECCION DE LAS 3 MEJORES IDEAS (15 MINUTOS)

Revisa todas las ideas generadas. Para cada una aplica este filtro rapido:

Relevancia
Resuelve directamente el problema definido en el POV? (Puntaje 1-3)

Factibilidad
Es posible hacerla con los recursos actuales del emprendedor y del territorio? (Puntaje 1-3)

Impacto
Beneficia a mas personas ademas del emprendedor? Genera transformacion territorial? (Puntaje 1-3)

Conexion personal
Conecta con las fortalezas e intereses del emprendedor (Ikigai del Paso 1)? (Puntaje 1-3)

Las 3 ideas con mayor puntaje total pasan al Paso 6.

Ejemplo aplicado - Municipio PDET, Norte de Santander:

Problema: Agricultores pierden el 40% de su produccion de tomate por falta de compradores y de refrigeracion.

Ideas generadas con SCAMPER:
- S: Sustituir bodega propia por espacio colectivo compartido entre 5 familias
- C: Combinar produccion de tomate con fabricacion de salsas y conservas artesanales
- A: Adaptar modelo de CSA (agricultura apoyada por la comunidad) donde compradores urbanos pagan antes de la cosecha
- M: Modificar el momento de venta: ofrecer paquetes semanales en lugar de ventas por kilo
- P: Usar el excedente de tomate para producir compost y venderlo a otros agricultores
- E: Eliminar el intermediario conectando directamente con restaurantes de la ciudad
- R: Invertir la logica: que el consumidor final adopte una planta y reciba su produccion

Top 3 seleccionadas: Salsas y conservas artesanales / Venta directa a restaurantes / Modelo de canasta semanal prepagada""",
            
            common_errors="""Evaluar ideas mientras se generan - esto mata la creatividad antes de que nazca

Quedarse con la primera idea buena sin explorar las demas

Seleccionar solo por rentabilidad percibida, ignorando el criterio de impacto territorial""",
            
            deliverable_description="""Lista de al menos 10 ideas + SCAMPER completado + Top 3 ideas seleccionadas con puntaje de criterios."""
        )
        
        # Module 6: Value Proposition
        self.update_module(
            key=Module.VALUE_PROP,
            why_exists="""El Value Proposition Canvas (VPC) de Alexander Osterwalder es la herramienta más citada en la literatura académica para asegurar que el producto o servicio esté diseñado desde las necesidades reales del cliente, no desde las suposiciones del emprendedor. El ajuste (fit) ocurre cuando cada dolor del cliente tiene un aliviador concreto y cada ganancia esperada tiene un creador específico.

En el contexto de Suluhisho, el VPC simplificado tiene un propósito doble: asegurar que la solución sea pertinente, y producir el texto base con el que el emprendimiento quedará registrado en la plataforma.""",
            
            how_to_guide="""Tiempo estimado: 40–60 minutos
Información necesaria: Resultados del Paso 3 (Mapa de Empatía), Paso 4 (JTBD) y Paso 5 (Top 3 ideas)

El VPC tiene dos caras: el perfil del cliente (lo que ya conoces) y el mapa de la propuesta de valor (lo que vas a ofrecer).

CARA 1 — PERFIL DEL CLIENTE

Retoma la información del Mapa de Empatía y el JTBD. Completa:

Customer Jobs (Tareas del cliente):
Lista las 3 tareas principales que el cliente intenta completar (funcionales, sociales y emocionales, tal como las descubriste en el Paso 4).
- Tarea 1 (funcional): __________
- Tarea 2 (social): __________
- Tarea 3 (emocional): __________

Pains (Dolores):
Del Mapa de Empatía, extrae los 3 dolores más importantes — los que más frustración, costo o esfuerzo generan.
- Dolor 1 (el más urgente): __________
- Dolor 2: __________
- Dolor 3: __________

Gains (Ganancias):
¿Qué resultados o beneficios espera el cliente? ¿Qué haría que su vida fuera notablemente mejor?
- Ganancia 1 (la más deseada): __________
- Ganancia 2: __________
- Ganancia 3: __________

CARA 2 — MAPA DE LA PROPUESTA DE VALOR

Tomando la idea mejor evaluada del Paso 5, completa:

Productos y Servicios:
¿Qué ofrece exactamente el emprendimiento? Sé específico.
- Producto/servicio principal: __________
- Producto/servicio complementario (si aplica): __________

Pain Relievers (Aliviadores de dolores):
Por cada dolor del cliente, ¿cómo tu solución lo alivia, reduce o elimina?
- Aliviador del Dolor 1: __________
- Aliviador del Dolor 2: __________
- Aliviador del Dolor 3: __________

Gain Creators (Creadores de ganancias):
Por cada ganancia esperada, ¿cómo tu solución la genera o potencia?
- Creador de Ganancia 1: __________
- Creador de Ganancia 2: __________
- Creador de Ganancia 3: __________

EL AJUSTE (FIT)

Verifica que hay correspondencia entre ambas caras. Marca con ✓ cada dolor que tiene un aliviador y cada ganancia que tiene un creador. Si hay dolores o ganancias sin respuesta → tu propuesta tiene brechas que ajustar antes de avanzar.

FRASE SÍNTESIS DE LA PROPUESTA DE VALOR

Completa:

"Mi emprendimiento ofrece [producto/servicio] para [tipo de persona] que necesita [resolver este problema], a diferencia de [lo que hacen hoy], porque [diferenciador clave que genera más valor]."

Ejemplo — Conservas artesanales, Putumayo:

"Mi emprendimiento ofrece salsas y conservas de tomate artesanales para familias de la ciudad que quieren productos naturales y locales, a diferencia de las salsas industriales del supermercado, porque están hechas con tomates frescos del campo sin conservantes, con identidad territorial y con pedido semanal directo al productor.""",
            
            common_errors="""❌ Llenar el VPC "al revés": empezar por la propuesta de valor y luego "encajar" el cliente — siempre se empieza por el perfil del cliente

❌ Escribir lo que crees que el cliente quiere, no lo que él mismo expresó

❌ Dejar dolores o ganancias sin respuesta en el mapa — esas brechas son señales de alerta antes de lanzar""",
            
            deliverable_description="""✅ Value Proposition Canvas simplificado completo + Verificación de ajuste (fit) + Frase síntesis de propuesta de valor."""
        )
        
        # Module 7: Validation
        self.update_module(
            key=Module.VALIDATION,
            why_exists="""Hasta este punto, el emprendedor ha construido una hipótesis bien estructurada. Pero sigue siendo una hipótesis. El Customer Development (Steve Blank) y el Lean Startup (Eric Ries) son unánimes: la única forma de saber si el problema es real y si la solución tiene sentido es salir a hablar con personas reales — antes de construir nada.

Este paso no es una encuesta ni una presentación. Es una conversación de escucha. El objetivo no es convencer a nadie de que la idea es buena: es aprender si el problema existe, cuán urgente es y si la solución propuesta tiene lógica para quien la viviría.""",
            
            how_to_guide="""Tiempo estimado: 1 semana (5–10 conversaciones de 20–30 minutos cada una)

¿Con quién hablar? Con personas que correspondan al perfil del cliente definido en el Paso 3. No con familiares cercanos (sesgo de cortesía) ni con amigos (sesgo de amistad).

ANTES DE LA ENTREVISTA

Prepara estas anotaciones:
- Nombre (opcional): __________
- Perfil (¿coincide con el cliente del POV?): __________
- Fecha y lugar: __________

⚠ Regla de oro: Nunca menciones tu solución hasta el final. Primero escucha.

GUÍA DE PREGUNTAS PARA LA ENTREVISTA

Apertura (romper el hielo):
- "¿Me puedes contar cómo es un día típico tuyo cuando [contexto del problema]?"
- "¿Cuáles son las cosas que más te complican en [área del problema]?"

Profundización (explorar el problema):
- "¿Cuándo fue la última vez que viviste ese problema? ¿Qué pasó exactamente?"
- "¿Con qué frecuencia te ocurre?"
- "¿Qué tan importante es esto para ti, del 1 al 10? ¿Por qué ese número?"
- "¿Qué pasa si nadie lo resuelve? ¿Qué consecuencias tiene para ti o tu familia?"

Soluciones actuales (entender la competencia real):
- "¿Qué haces hoy para resolver esto?"
- "¿Estás contento/a con esa solución? ¿Qué le mejorarías?"
- "¿Has intentado otras alternativas? ¿Por qué las dejaste?"

Validación final (opcional, si el problema quedó confirmado):
- "Estoy pensando en una idea para resolver esto. Te cuento en un minuto y me dices qué tan útil te parece..."
- Describe la propuesta en máximo 2 frases
- "¿Qué le cambiarías?"

CRITERIOS DE ANÁLISIS POST-ENTREVISTA

Para cada entrevista, marca:

| Señal | ¿Apareció? |
|-------|------------|
| La persona confirmó que el problema existe en su vida | ✓ / ✗ |
| Lo calificó con urgencia ≥ 7/10 | ✓ / ✗ |
| No tiene una solución actual satisfactoria | ✓ / ✗ |
| Mostró interés espontáneo en la solución propuesta | ✓ / ✗ |
| Sugirió mejoras útiles a la idea | ✓ / ✗ |

Criterio de avance: Si 7 de 10 personas confirman al menos 3 de estas 5 señales → el problema es real y la idea tiene tracción suficiente para avanzar a la etapa de formulación.

Si los resultados no son suficientes: No es un fracaso — es aprendizaje. Revisa el POV del Paso 3, ajusta el perfil del cliente o elige otro problema del Paso 2. El pivote en esta etapa es barato; el pivote después de haber invertido dinero y meses de trabajo no lo es.

Ejemplo aplicado — Entrevista con agricultora, Córdoba:

Entrevistadora (emprendedora): "Doña Martha, ¿cuándo fue la última vez que perdió parte de su cosecha?"

Doña Martha: "La semana pasada. Se me dañaron casi 3 arrobas de plátano porque el camión del comprador no llegó."

Entrevistadora: "¿Y qué hizo?"

Doña Martha: "Nada. Tocó tirarlo. A veces se lo damos a los marranos pero igual es pérdida."

Entrevistadora: "¿Qué tan seguido le pasa eso?"

Doña Martha: "Casi cada dos semanas en temporada. Ya uno se acostumbra pero igual es plata que se va."

→ Señal confirmada: problema real, frecuente, con consecuencia económica directa, sin solución actual. Puntaje: 4/5.**""",
            
            common_errors="""❌ Preguntar "¿Usarías mi producto?" — las personas dicen que sí por cortesía; lo que importa es su comportamiento actual

❌ Hablar más que escuchar — viola la regla 20/80 y sesga los resultados

❌ Entrevistar solo a familiares o amigos — confirmarán la idea por afecto, no por criterio real

❌ Rendirse si las primeras 2–3 entrevistas no confirman la idea — se necesitan al menos 7–10 para tener señal suficiente""",
            
            deliverable_description="""✅ Registro de 7–10 entrevistas + Tabla de señales completada + Conclusión de validación + Decisión documentada: ¿Avanzo con esta idea o pivoto?"""
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Successfully populated all 7 modules with instructional content'))

    def update_module(self, key, why_exists, how_to_guide, common_errors, deliverable_description):
        """Update a module with its instructional content"""
        try:
            module = Module.objects.get(key=key)
            module.why_exists = why_exists
            module.how_to_guide = how_to_guide
            module.common_errors = common_errors
            module.deliverable_description = deliverable_description
            module.save()
            self.stdout.write(f'  ✓ Updated {module.title}')
        except Module.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'  ✗ Module {key} not found'))

