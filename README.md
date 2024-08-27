<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Автоматизированный запуск Tailwind CSS и ASP.NET проекта</title>
</head>
<body>
    <h1>Автоматизированный запуск Tailwind CSS и ASP.NET проекта</h1>

    <p>Чтобы Tailwind CSS автоматически запускался перед запуском вашего проекта ASP.NET, можно настроить пакетный скрипт (batch script) или PowerShell скрипт, который сначала запустит сборку CSS с помощью Tailwind, а затем запустит проект ASP.NET.</p>
    
    <h2>1. Создание автоматизированного скрипта для запуска проекта с Tailwind</h2>
    <p>Создайте файл <code>run-project.ps1</code> в корне вашего проекта с таким содержимым:</p>
    <pre><code># 1. Запуск сборки CSS с помощью Tailwind CSS
npm run build:css

# 2. Запуск наблюдателя для Tailwind CSS в отдельном процессе
Start-Process powershell -ArgumentList "-NoExit", "-Command", "npm run watch:css"

# 3. Запуск проекта ASP.NET
dotnet run
    </code></pre>

    <h2>2. Настройка проекта</h2>
    <h3>Обновление <code>package.json</code> для добавления команд сборки и наблюдения:</h3>
    <p>Убедитесь, что у вас есть следующие скрипты в <code>package.json</code>:</p>
    <pre><code>"scripts": {
  "build:css": "npx tailwindcss -i ./src/styles.css -o ./wwwroot/css/styles.css --minify",
  "watch:css": "npx tailwindcss -i ./src/styles.css -o ./wwwroot/css/styles.css --watch"
}
    </code></pre>

    <h2>3. Запуск автоматизированного процесса</h2>
    <p>Для запуска скрипта откройте PowerShell и выполните:</p>
    <pre><code>.\run-project.ps1
    </code></pre>

    <h2>4. Дополнительно: Создание одной команды для всех процессов</h2>
    <p>Чтобы сделать процесс еще проще, вы можете добавить сценарий для запуска <code>run-project.ps1</code> в <code>package.json</code>. Это позволит запускать все с помощью одной команды <code>npm</code>.</p>
    <p>В <code>package.json</code> добавьте следующий скрипт:</p>
    <pre><code>"scripts": {
  "start": "powershell -ExecutionPolicy Bypass -File ./run-project.ps1"
}
    </code></pre>
    <p>Теперь, чтобы собрать стили и запустить проект, вы можете использовать одну команду:</p>
    <pre><code>npm start
    </code></pre>

    <h2>5. Запуск проекта</h2>
    <p>Запуск команды <code>npm start</code> выполнит следующие действия:</p>
    <ul>
        <li>Сначала сгенерирует CSS с использованием Tailwind.</li>
        <li>Затем запустит процесс наблюдения за файлами CSS.</li>
        <li>И наконец, запустит ASP.NET проект.</li>
    </ul>
    <p>Этот подход автоматизирует весь процесс, и вам не нужно беспокоиться о сборке CSS перед запуском ASP.NET проекта — всё произойдет автоматически.</p>
</body>
</html>
