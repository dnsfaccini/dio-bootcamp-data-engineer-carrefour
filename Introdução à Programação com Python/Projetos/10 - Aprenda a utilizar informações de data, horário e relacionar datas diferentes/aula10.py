from datetime import date, time, datetime, timedelta


def trabalhando_com_date():
    # Obtem a data atual
    data_atual = date.today()

    # Formata no padrão brasileiro
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%d-%m-%Y'))
    print(data_atual.strftime('%d %m %Y'))
    print(data_atual.strftime('%A-%B-%Y'))

def trabalhando_com_time():
    #cria um horario
    horario = time(hour = 15, minute = 18, second = 30)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)

    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.date())
    print(data_atual.month)
    print(data_atual.weekday())

    # Obter dia da semana em portugues
    tupla = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom')
    print(tupla[data_atual.weekday()])

    # Criar data
    data_criada = datetime(2018, 6, 20 ,15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    # Converter data em String para datetime
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))

    # Subtração e soma de datas
    nova_data_subtraida = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data_subtraida)
    nova_data_somada = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data_somada)

##########################################################

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()

