from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Список событий в деловой программе выставки
program = [
    {
        'time': '10:00 - 11:00',
        'event': 'Открытие выставки',
        'place': 'Главный зал'
    },
    {
        'time': '11:00 - 12:00',
        'event': 'Семинар «Новые технологии в племенном разведении»',
        'place': 'Конференц-зал'
    },
    {
        'time': '12:00 - 14:00',
        'event': 'Обед',
        'place': 'Ресторан'
    },
    {
        'time': '14:00 - 15:00',
        'event': 'Конкурс лучшего барана',
        'place': 'Главный зал'
    },
    {
        'time': '15:00 - 16:00',
        'event': 'Семинар «Современные методы кормления племенного скота»',
        'place': 'Конференц-зал'
    },
    {
        'time': '16:00 - 17:00',
        'event': 'Церемония награждения',
        'place': 'Главный зал'
    }
]

# Ссылка на файл программы в формате pdf
program_file = 'static/program.pdf'

@app.route('/program')
def program_page():
    return render_template('program.html', program=program)

@app.route('/download_program')
def download_program():
    return send_file(program_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
