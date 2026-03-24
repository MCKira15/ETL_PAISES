# ETL_PAISES
Este proyecto es un proceso ETL de países de América que automatiza la obtención de datos geográficos y demográficos utilizando API's y MySQL.

ETL_PAISES/
├── tasks/           # Módulos de la lógica ETL
│   ├── extract.py   # Conexión con la API
│   ├── transform.py # Limpieza de datos (Data Wrangling)
│   └── load.py      # Operaciones con SQL
├── main.py          # Punto de entrada del programa
├── .gitignore       # Archivos excluidos de Git
└── README.md        # Documentación