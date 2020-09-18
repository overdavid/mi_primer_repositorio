from django.shortcuts import render,HttpResponse
import psycopg2

def insert(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    # 1 return HttpResponse('Funciona!')

    # 2 with open("debug.log", "a+") as debug_file:
    # 2    print("Funciona!", file=debug_file)
    # 2 return HttpResponse('Funciona!')

    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp VALUES ('7364','HUGO','OFICINISTA', \
            '7903',date '1980-12-17','800.00',NULL,'20');")
    # 3 return HttpResponse('Registro insertado')

    # 4 cursor.execute("select * from emp")
    # 4 return HttpResponse(cursor.fetchall())

    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse("Insertado")

def select(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    # 5 return HttpResponse(cursor.fetchall())

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return HttpResponse(result)

def delete(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("delete from emp;")
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse("borrado")





