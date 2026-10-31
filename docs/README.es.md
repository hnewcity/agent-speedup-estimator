<div align="center">

# Agent Speedup Estimator

**¿Cuánto aceleraría un ordenador nuevo a tu agente de programación?**

Estima el efecto de una mejora de hardware a partir del historial local de Claude Code y Codex.

[![Tests](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml/badge.svg)](https://github.com/hnewcity/agent-speedup-estimator/actions/workflows/tests.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](#inicio-rápido)
[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

[![English](https://img.shields.io/badge/English-555555?style=for-the-badge)](../README.md)
[![简体中文](https://img.shields.io/badge/简体中文-555555?style=for-the-badge)](README.zh-CN.md)
[![日本語](https://img.shields.io/badge/日本語-555555?style=for-the-badge)](README.ja.md)
[![Español](https://img.shields.io/badge/Español-selected-1f6feb?style=for-the-badge)](README.es.md)

[Inicio rápido](#inicio-rápido) · [Instalar como skill](#instalar-como-skill) · [Informe de ejemplo](example/report.md) · [Referencia completa en inglés](../README.md)

</div>

## Por qué existe

Un ordenador nuevo puede acelerar las compilaciones y las pruebas, pero no un modelo que se ejecuta en un servidor remoto. Esta herramienta estima la diferencia para **tu carga de trabajo real** usando registros de tiempo existentes.

Por ejemplo, si una tarea dedica 80 segundos al modelo remoto y 20 a herramientas locales, duplicar la velocidad de todo el trabajo local reduce el total de 100 a 90 segundos: **1,11× en conjunto**. La estimación real también considera las partes del tiempo de herramientas que no dependen del hardware.

> Es una estimación, no un benchmark. Los escenarios conservador, esperado y optimista muestran distintos supuestos; no son intervalos estadísticos de confianza ni recomendaciones de compra.

## Qué ofrece

- Desglose de tiempo del modelo, herramientas, respuestas humanas, inactividad y otras actividades.
- Clasificación de compilaciones, pruebas, instalaciones, scripts, Git y operaciones con archivos.
- Comparaciones con puntuaciones de referencia de Geekbench 6, cuatro gamas predeterminadas o valores propios.
- Aceleración total, aceleración de herramientas y ahorro estimado en tres escenarios.
- Informes en Markdown, HTML interactivo sin conexión y JSON.
- Uso como skill de un agente o como comando de Python.

El análisis básico utiliza solo la biblioteca estándar, no hace peticiones de red ni ejecuta comandos del historial. **Los informes están disponibles en inglés y chino simplificado**. Los botones superiores cambian el idioma del README.

## Inicio rápido

Necesitas **Python 3.9+**, Git para clonar el repositorio e historial local con datos de tiempo compatibles.

```bash
git clone https://github.com/hnewcity/agent-speedup-estimator.git
cd agent-speedup-estimator
python skills/agent-speedup-estimator/scripts/agent_speedup.py --lang en --out ./agent-speedup-report
```

Si `python` no está disponible, usa `py -3` en Windows o `python3` en macOS/Linux. Abre `agent-speedup-report/report.html` en el navegador al terminar.

| Archivo | Uso |
| --- | --- |
| `report.md` | Leer el resumen |
| `report.html` | Cambiar de ordenador, consultar gráficos y tablas sin conexión |
| `summary.json` | Reutilizar los datos agregados |

Los archivos comprimidos de Codex (`.jsonl.zst`) necesitan **Python 3.14+** o este paquete opcional en versiones anteriores:

```bash
python -m pip install zstandard
```

Se informa del número de archivos comprimidos que no se pueden leer. Si no hay datos de tiempo utilizables, el comando devuelve el código `2`. Puedes indicar carpetas con `--claude-dir` y `--codex-dir`.

## Instalar como skill

Copia la carpeta completa [`skills/agent-speedup-estimator`](../skills/agent-speedup-estimator), incluidos `scripts/` y `data/`.

| Agente | Directorio personal | Directorio del proyecto |
| --- | --- | --- |
| Codex | `~/.agents/skills/agent-speedup-estimator/` | `.agents/skills/agent-speedup-estimator/` |
| Claude Code | `~/.claude/skills/agent-speedup-estimator/` | `.claude/skills/agent-speedup-estimator/` |

La [guía de instalación en inglés](../README.md#install-as-a-skill) incluye comandos para macOS/Linux y PowerShell. Reinicia Codex si no detecta la instalación. Después, pide al agente:

> Usa agent-speedup-estimator para comprobar si mi ordenador limita a mis agentes de programación. Compáralo con un Apple M4 Pro y explica los supuestos.

La detección automática de entradas y las instrucciones del agente están en [SKILL.md](../skills/agent-speedup-estimator/SKILL.md).

## Ejemplos

Ejecuta los comandos desde la raíz del repositorio:

```bash
# Últimos 30 días y una CPU concreta
python skills/agent-speedup-estimator/scripts/agent_speedup.py --days 30 --target "Apple M4 Pro" --lang en

# Varios objetivos
python skills/agent-speedup-estimator/scripts/agent_speedup.py --target "Apple M4" --target "AMD Ryzen 9 9950X"

# Puntuaciones propias; estos números solo ilustran los argumentos
python skills/agent-speedup-estimator/scripts/agent_speedup.py --current-gb6 1500 6000 --custom-target "Mi próximo ordenador" 3000 15000

python skills/agent-speedup-estimator/scripts/agent_speedup.py --list-cpus
python skills/agent-speedup-estimator/scripts/agent_speedup.py --help
```

Se buscan registros en `~/.claude/projects`, `~/.codex/sessions` y `~/.codex/archived_sessions`, respetando `CLAUDE_CONFIG_DIR` y `CODEX_HOME`. Usa `--agents` para elegir agentes, `--current-disk` / `--target-disk` para el disco y `--sensitivity` para tus supuestos. Consulta la [lista completa de opciones](../README.md#more-examples).

Se sobrescriben los informes del mismo nombre en la carpeta de salida. Un objetivo desconocido genera un aviso; si ninguno coincide, se usan las gamas predeterminadas. `--days` selecciona por la fecha de finalización del registro o turno y no recorta tareas que cruzan el límite del período.

## Cómo funciona

Lee tiempos y duraciones, y clasifica comandos en memoria. Reparte el tiempo solapado entre llamadas paralelas dentro de cada sesión. De forma predeterminada, la parte de un comando que supera 300 segundos permanece fija en los escenarios conservador y esperado; el optimista también aplica la mejora a esa parte.

```text
projected_time = original_time × ((1 − cpu_share − disk_share)
                                + cpu_share / cpu_speed_ratio
                                + disk_share / disk_speed_ratio)
overall_speedup = (model_time + original_tool_time)
                 / (model_time + projected_tool_time)
```

La velocidad de CPU combina las razones entre puntuaciones de un núcleo y varios núcleos, con pesos por categoría. El disco utiliza una heurística. Las proporciones están entre 0 y 1 y la suma de CPU y disco no puede superar 1. La base se obtiene de una coincidencia en la tabla, un sustituto documentado o una aproximación por número de hilos. Las aproximaciones se señalan y amplían el rango. `--current-gb6` permite usar mediciones propias.

## Datos y limitaciones

[`data/`](../skills/agent-speedup-estimator/data) contiene fuentes de puntuaciones, gamas, sustitutos y supuestos de sensibilidad.

- Se asumen modelos remotos y herramientas locales. No se modelan LLM locales, compilación remota, mejoras de GPU o falta de memoria.
- El tiempo del modelo se infiere de intervalos que pueden incluir red y coordinación. Las esperas de aprobación pueden contarse como herramientas.
- Codex necesita campos de tiempo en `item_completed` o límites de tareas con tiempos. Otros formatos pueden no aportar datos utilizables.
- Las sesiones simultáneas se suman. El ahorro representa tiempo acumulado de agentes, no tiempo transcurrido de calendario.
- Las puntuaciones no reflejan por completo compiladores, refrigeración o ancho de banda de memoria. Windows/Linux eligen la clase de disco más rápida detectada; macOS asume NVMe. Puedes sobrescribirla.
- Las puntuaciones son referencias fechadas de páginas públicas, no medias oficiales de Geekbench ni recomendaciones actuales de productos.

## Privacidad

Los registros JSON se analizan localmente en memoria. El informe incluye tiempos agregados, categorías, familias de comandos permitidas, fechas de actividad y hardware. Excluye prompts, respuestas, comandos completos, rutas de historiales e identificadores de sesión. La CLI no sube historiales, llama a API ni ejecuta comandos del historial. Instalar el paquete opcional es una operación de red independiente.

Revisa los informes antes de compartirlos: pueden revelar tu configuración y hábitos de trabajo. Git ignora informes personales e historiales. El [ejemplo público](example/report.md) utiliza exclusivamente tiempos sintéticos y hardware ficticio, creados por el [generador](../examples/generate_demo.py).

## Desarrollo y licencia

```bash
python -m unittest discover -s skills/agent-speedup-estimator/tests -v
python examples/generate_demo.py
```

Las pruebas cubren clasificación, atribución, compresión, puntuaciones, límites, validación y privacidad en ambos adaptadores. GitHub Actions utiliza Linux, Windows y macOS con Python 3.9 y 3.14. Lee [CONTRIBUTING.md](../CONTRIBUTING.md) para contribuir código, datos o traducciones, siempre con ejemplos sintéticos.

[MIT](../LICENSE) © 2026 hnewcity. Proyecto independiente, sin afiliación con OpenAI, Anthropic ni Primate Labs.
