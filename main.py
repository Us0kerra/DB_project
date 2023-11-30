import psycopg2
from prettytable import PrettyTable

dbname = input("Введите название базы данных: ")
user = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
def connect(dbname, user, password):
    conn = psycopg2.connect(dbname=dbname, host="localhost", user=user, password=password, port="5432")
    cursor = conn.cursor()
    conn.autocommit = True
    return conn, cursor

def select(table_name):
    while True:
        table = PrettyTable()
        conn, cursor = connect()
        match table_name:
            case 'orders':
                table.field_names = ["Номер приказа", "Дата"]
                cursor.execute("SELECT * FROM orders")
            case "points":
                table.field_names = ["снилс", "сумма баллов"]
                cursor.execute("SELECT * FROM points")
            case "contests":
                table.field_names = ["код конкурса", "вид конкурса", "форма обучения", "уровень подготовки"]
                cursor.execute("SELECT * FROM contests")
            case "positions":
                table.field_names = ["код должности", "название должности"]
                cursor.execute("SELECT * FROM positions")
            case "staff":
                table.field_names = ["код сотрудника", "сотрудник", "код должности"]
                cursor.execute("SELECT * FROM staff")
            case "programs":
                table.field_names = ["код направления", "название направления"]
                cursor.execute("SELECT * FROM programs")
            case "applicants":
                table.field_names = ["рег. номер", "снилс"]
                cursor.execute("SELECT * FROM applicants")
            case "accountings":
                table.field_names = ["рег. номер", "код направления", "код конкурса", "номер приказа", "код сотрудника"]
                cursor.execute("SELECT * FROM accountings")
            case _:
                print("Неизвестное название таблицы.")
                break

        for row in cursor.fetchall():
            table.add_row([row[element] for element in range(len(row))])
        print(table)
        cursor.close()
        conn.close()
        break

def insert():
    while True:
        table_name = input("Введите название таблицы, в которую хотите добавить данные: ")
        conn, cursor = connect()
        match table_name:
            case 'orders':
                ord_date = input("Введите дату зачисления абитуриента('year-month-day')")
                cursor.execute(f"INSERT INTO orders(ord_date) "
                               f"VALUES (\'{ord_date}\')")
            case 'points':
                snils = input("Введите снилс абитуриента: ")
                sum_points = input("Введите сумму баллов абитуриента:")
                if len(snils) == 14:
                    cursor.execute(f"INSERT INTO points(snils, sum_points) "
                                   f"VALUES (\'{snils}\',\'{sum_points}\')")
                else:
                    print("Неверный формат снилса.")
                    break
            case 'applicants':
                snils = input("Введите снилс абитуриента: ")
                if len(snils) == 14:
                    cursor.execute(f"INSERT INTO applicants(snils) "
                                   f"VALUES (\'{snils}\')")
                else:
                    print("Неверный формат снилс:")
                    break
            case 'contests':
                cont_type = input("Введите тип конкурса: ")
                form_of_study = input("Введите форму обучения: ")
                lvl_education = input("Введите уровень подготовки(бакалавр, специалитет и т.д.): ")
                cursor.execute(f"INSERT INTO contests(cont_type, form_of_study, lvl_education) "
                               f"VALUES (\'{cont_type}\',\'{form_of_study}\',\'{lvl_education}\')")
            case 'positions':
                position_name = input("Введите должность: ")
                cursor.execute(f"INSERT INTO positions "
                               f"VALUES (\'{position_name}\')")
            case 'staff':
                staff_name = input("Введите ФИО работника: ")
                position_id = input("Введите код должности работника: ")
                cursor.execute(f"INSERT INTO staff(staff_name, position_id) "
                               f"VALUES (\'{staff_name}\',\'{position_id}\')")
            case 'programs':
                program_name = input("Введите название направления: ")
                cursor.execute(f"INSERT INTO programs(program_name) "
                               f"VALUES (\'{program_name}\')")
            case 'accountings':
                reg_num = input("Введите регистрационный номер абитуриента: ")
                program_id = input("Введите код направления: ")
                cont_id = input("Введите код конкурса: ")
                ord_num = input("Введите номер приказа: ")
                staff_id = input("Введите код работника: ")
                cursor.execute(f"INSERT INTO accountings(reg_num, program_id, cont_id, ord_num, staff_id) "
                               f"VALUES(\'{reg_num}\',\'{program_id}\',\'{cont_id}\',\'{ord_num}\',\'{staff_id}\')")
            case _:
                print("Неизвестное название таблицы.")
        cursor.close()
        conn.close()
        break

def delete(table_name):
    while True:
        conn, cursor = connect()
        match table_name:
            case 'orders':
                ord_num = input("Введите номер приказа: ")
                cursor.execute(f"DELETE FROM orders "
                               f"WHERE book_id = \'{ord_num}\'")
            case 'points':
                snils = input("Введите номер снилса: ")
                if len(snils) == 14:
                    cursor.execute(f"DELETE FROM points "
                                   f"WHERE snils = \'{snils}\'")
                else:
                    print("Неверный формат снилса.")
                    break
            case 'applicants':
                reg_num = input("Введите регистрационный номер абитуриента: ")
                cursor.execute(f"DELETE FROM applicants "
                               f"WHERE reg_num = \'{reg_num}\'")
            case 'contests':
                cont_id = input("Введите код конкурса: ")
                cursor.execute(f"DELETE FROM contests "
                               f"WHERE cont_id = \'{cont_id}\'")
            case 'positions':
                position_id = input("Введите код должности: ")
                cursor.execute(f"DELETE FROM positions "
                               f"WHERE position_id = \'{position_id}\'")
            case 'staff':
                staff_id = input("Введите код работника: ")
                cursor.execute(f"DELETE FROM staff "
                               f"WHERE staff_id = \'{staff_id}\'")
            case 'programs':
                program_id = input("Введите код направления: ")
                cursor.execute(f"DELETE FROM programs "
                               f"WHERE program_id = \'{program_id}\'")
            case 'accountings':
                reg_num = input("Введите регистрационный номер: ")
                program_id = input("Введите код направления: ")
                cursor.execute(f"DELETE FROM accountings "
                               f"WHERE reg_num =\'{reg_num}\' AND program_id = \'{program_id}\'")
            case _:
                print("Неизвестное название таблицы: ")
                break
        cursor.close()
        conn.close()
        break

def update(table_name):
    while True:
        conn, cursor = connect()
        match table_name:
            case 'orders':
                ord_num = input("Введите номер приказа, данные которого хотите изменить: ")
                ord_date = input("Введите новую дату приказа(year-month-day): ")
                cursor.execute(
                    f"UPDATE orders "
                    f"SET ord_date = \'{ord_date}\' "
                    f"WHERE ord_num = {ord_num}")
            case 'points':
                snils = input("Введите снилс абитуриента, информацию о баллах которого вы хотите изменить: ")
                if len(snils) == 14:
                    sum_points = input("Введите новое количество баллов абитуриента")
                    cursor.execute(f"UPDATE points "
                                   f"SET sum_points = \'{sum_points}\' "
                                   f"WHERE snils = \'{snils}\'")
                else:
                    print("Введен неверный формат снилса.")
                    break
            case 'applicants':
                reg_num = input("Введите номер приказа, информацию которого хотите изменить: ")
                snils = input("Введите новый снилс абитуриента: ")
                if len(snils) == 14:
                    cursor.execute(f"UPDATE applicants "
                                   f"SET snils = \'{snils}\' "
                                   f"WHERE reg_num = \'{reg_num}\'")
            case 'contests':
                cont_id = input("Введите код конкурса, информацию которого хотите изменить: ")
                cont_type = input("Введите новый вид конкурса: ")
                form_of_study = input("Введите новую форму обучения: ")
                lvl_education = input("Введите новый уровень подготовки: ")
                cursor.execute(f"UPDATE contests "
                               f"SET cont_type = \'{cont_type}\', form_of_study = \'{form_of_study}\', lvl_education = \'{lvl_education}\' "
                               f"WHERE cont_id = \'{cont_id}\'")
            case 'positions':
                position_id = input("Введите код должности, информацию которого хотите изменить: ")
                position_name = input("Введите новое название должности: ")
                cursor.execute(f"UPDATE positions "
                               f"SET position_name = \'{position_name}\' "
                               f"WHERE position_id = \'{position_id}\'")
            case 'staff':
                staff_id = input("Введите код работника, информацию о котором хотите изменить: ")
                staff_name = input("Введите новое ФИО работника: ")
                position_id = input("Введите новый код должности: ")
                cursor.execute(f"UPDATE staff "
                               f"SET staff_name = \'{staff_name}\', position_id = \'{position_id}\' "
                               f"WHERE staff_id = \'{staff_id}\'")
            case 'programs':
                program_id = input("Введите код направления, информацию которого хотите изменить: ")
                program_name = input("Введите новое название направления: ")
                cursor.execute(f"UPDATE programs "
                               f"SET program_name = \'{program_name}\' "
                               f"WHERE program_id = \'{program_id}\'")
            case 'accountings':
                reg_num = input("Введите регистрационый номер абитуриента: ")
                program_id = input("Введите код направления, информацию которого хотите изменить:")
                cont_id = input("Введите новый код конкурса: ")
                ord_num = input("Введите новый номер приказа:  ")
                staff_id = input("Введите новый код сотрудника: ")
                cursor.execute(f"UPDATE accountings "
                               f"SET cont_id = \'{cont_id}\', ord_num = \'{ord_num}\', staff_id = \'{staff_id}\' "
                               f"WHERE reg_num = \'{reg_num}\' AND program_id = \'{program_id}\'")
            case _:
                print("Неизвестное название таблицы.")
                break
        cursor.close()
        conn.close()
        break

def print_report():
    while True:
        con, cursor = connect()
        print("Доступно 5 видов отчета:\n"
              "1 - средний балл абитуриентов поступивших на \"Направление\"\n"
              "2 - Количество приказов подписанных \"Сотрудник\"\n"
              "3 - Количество приказов подписанных \"Дата\" числа\n"
              "4 - Количество абитуриентов поступивших на \"Направление\"\n"
              "5 - Количество работников с должностью \"Должность\"\n")
        type_report = input("Выберите тип отчета: ")
        table = PrettyTable()
        match type_report:
            case '1':
                select("programs")
                program = input("Введите название направления: ")
                cursor.execute(f"SELECT program_name, avg(sum_points) as Average FROM accountings "
                               f"JOIN programs on accountings.program_id = programs.program_id "
                               f"JOIN applicants on accountings.reg_num = applicants.reg_num "
                               f"JOIN points on applicants.snils = points.snils "
                               f"WHERE programs.program_name = \'{program}\' "
                               f"GROUP by program_name")
                table.field_names = ["Название направления", "Средний балл"]

            case '2':
                select("staff")
                staff = input("Введите код сотрудника: ")
                cursor.execute(f"SELECT staff_name, COUNT(ord_num) FROM accountings "
                               f"JOIN staff on staff.staff_id = accountings.staff_id "
                               f"WHERE staff.staff_id = '{staff}' "
                               f"GROUP BY staff_name")
                table.field_names = ["Сотрудник", "Количество подписанных приказов"]
            case '3':
                ord_date = input("Введите дату(year-month-day): ")
                cursor.execute(f"SELECT ord_date, count(orders.ord_num) FROM accountings "
                               f"JOIN orders on orders.ord_num = accountings.ord_num "
                               f"WHERE ord_date = '{ord_date}' "
                               f"GROUP BY ord_date")
                table.field_names = ["Дата", "Количество приказов"]
            case '4':
                select("programs")
                program = input("Введите название направления: ")
                cursor.execute(f"SELECT program_name, count(accountings.reg_num) FROM accountings "
                               f"JOIN programs on programs.program_id = accountings.program_id "
                               f"JOIN applicants on applicants.reg_num = accountings.reg_num "
                               f"WHERE program_name = '{program}' "
                               f"GROUP BY program_name")
                table.field_names = ["Название направления", "количество абитуриентов"]
            case '5':
                select("positions")
                position_name = input("Введите должность: ")
                cursor.execute(f"SELECT position_name, count(staff.position_id) FROM staff "
                               f"JOIN positions on positions.position_id = staff.position_id "
                               f"WHERE positions.position_name = '{position_name}' "
                               f"GROUP BY position_name")
                table.field_names = ["Должность", "Количество сотрудников"]
            case _:
                print("Неизвестная команда!")
                break
        for row in cursor.fetchall():
            table.add_row([row[0], int(row[1])])
        print(table)
        cursor.close()
        con.close()
        break

table = PrettyTable()
table.add_column("Название таблицы",[
    "Приказы",
    "Баллы",
    "Абитуриенты",
    "Конкурсы",
    "Должности",
    "Работники",
    "Направления",
    "Учет",
])
table.add_column("требуемый ввод",["orders","points","applicants",'contests','positions','staff','programs','accountings'])
print('Добро пожаловать в программу "учет поступления абитуриентов"!\n'
      'Программа работает со следующими таблицами:\n',
      table)

input("Нажмите \"Enter\" Для продолжения!")

print("1 - вывод таблицы на экран\n"
      "2 - добавить запись в таблицу\n"
      "3 - удалить запись из таблицы\n"
      "4 - редактировать запись в таблице\n"
      "5 - Вывод отчетов\n"
      "0 - выход из программы\n")

while True:
    menu_item = input("Выберите пункт меню: ")
    if (menu_item == '1'):
        table_name = input("Введите название таблицы, данные которой нужно вывести: ")
        select(table_name)
    elif (menu_item == '2'):
        insert()
    elif (menu_item == '3'):
        table_name = input("Введите название таблицы, данные которой нужно вывести: ")
        select(table_name)
        delete(table_name)
    elif (menu_item == '4'):
        table_name = input("Введите название таблицы, данные которой нужно вывести: ")
        select(table_name)
        update(table_name)
    elif (menu_item == '5'):
        print_report()
    elif (menu_item == '0'):
        break
    else: print("Неизвестная команда!")
    input('Нажмите "Enter" чтобы продолжить')