# FraudIQ - Sistema de Detección de Fraude

## Descripción del Proyecto

FraudIQ es una solución de machine learning diseñada para detectar transacciones fraudulentas en tiempo real. Utilizando algoritmos avanzados de aprendizaje automático, nuestro sistema analiza patrones de transacciones para identificar actividades sospechosas con alta precisión.

## Características Principales

- **Múltiples Modelos ML**: Implementación de diversos algoritmos (Random Forest, LightGBM, SVM, etc.)
- **API REST**: Endpoints para predicciones en tiempo real
- **Interfaz Web**: Dashboard interactivo para pruebas y visualización
- **Pipeline de Preprocesamiento**: Transformación automática de datos de entrada
- **Logging Detallado**: Sistema de registro para monitoreo y debugging

## ecnologías Utilizadas

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn
- **Frontend**: HTML5, Bootstrap 5
- **Datos**: pandas, NumPy
- **Serialización**: joblib

## Requisitos Previos

```bash
Python 3.11+
pip (última versión)
Entorno virtual (venv)
```

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/FraudIQ.git
cd FraudIQ
```

2. **Crear y activar entorno virtual**
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
python app.py
```

## Estructura del Proyecto

```
FraudIQ/
├── app.py                  # Aplicación principal Flask
├── ml_engineering/        
│   ├── data_processing/   # Scripts de procesamiento de datos
│   └── model_training/    # Modelos entrenados y notebooks
├── static/                # Recursos estáticos
├── templates/             # Plantillas HTML
└── requirements.txt       # Dependencias del proyecto
```

## Uso del Sistema

1. Acceder a la interfaz web (http://localhost:5000)
2. Ingresar los datos de la transacción
3. Seleccionar el modelo a utilizar
4. Obtener la predicción y probabilidad de fraude

## Rendimiento de los Modelos

| Modelo | Precisión | Recall | F1-Score |
|--------|-----------|--------|----------|
| Random Forest | 98.12% | 94.70% | 96.37% |
| Neural Network | 96.54% | 93.82% | 95.16% |
| SVM | 97.60% | 95.06% | 77.74% |

## Equipo de Desarrollo

- **Deybby Rosario** - Desarrollador Web - [@deybby](https://www.linkedin.com/in/deybby-rosario/)
- **Sarah Peña** - Ingeniera ML - [@sarah](https://www.linkedin.com/in/sarah-v-pena/)

