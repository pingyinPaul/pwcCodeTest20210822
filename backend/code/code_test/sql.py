#from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
#settings.configure()
from itertools import *

from django.db import connection

from rest_framework.views import APIView

# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]

# def custom_sql(query_str, params = []):
#     with connection.cursor() as cursor:
#         cursor.execute(query_str, params)
#         row = dictfetchall(cursor)

#     return row

# class test_test(APIView):
#     def get(self, request):
#         # print(User.objects.model._meta.db_table)
#         row = custom_sql("""SELECT Q.dob FROM code_test_patient P, code_test_questionnaire Q
#                             WHERE P.id=Q.patient_id
#                             LIMIT 1""")
#         print(row)
#         content = {"result": row}
#         return JsonResponse(content)