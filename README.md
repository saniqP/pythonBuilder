# PythonBuilder 🐍

Автоматический настройщик Python проектов, который упрощает начальную настройку и стандартизирует структуру ваших проектов.

## 📦 Установка

```bash
git clone https://github.com/saniqP/pythonBuilder.git
cd PythonBuilder
chmod +x install.sh
./install.sh
```

После установки у вас появится глобальная команда `pybuild`

## 🚀 Использование

1. Создайте конфигурационный файл

В корне вашего проекта создайте файл `pythonBuild.jsonc`:

{
  "venv_name": ".venv",           // Имя виртуального окружения
  
  "libraries": [                  // Список библиотек для установки
    "requests",
    "numpy", 
    "pillow"
  ],
  
  "default_folders": {            // Автоматическое создание структуры папок
    "enable": true,
    "folders": [
      "src",
      "tests",
      "docs",
      "data"
    ]
  },
  
  "start_file": {                 // Создание скрипта для запуска
    "enable": true,
    "main_file": "src/main.py"    // Главный файл вашего проекта
  }
}
