# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .models import person
from django.views.decorators.csrf import csrf_exempt
import json
#from .models import Person  # Assuming you have a model named 'Person'

def index(request):
    return render(request, 'index.html')

# Implemente as views para detalhes, novo dado, editar dado e excluir dado

def list_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM person ORDER BY fullname ASC LIMIT 25")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(data, safe=False)

'''
def remove_data(request):
    if request.method == 'GET':
        full_name = request.GET.get('fullName', '')

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM person WHERE fullname LIKE %s", [f'{full_name}%'])

        return JsonResponse({'message': 'Data removed successfully'})
'''
def remove_data(request):
    if request.method == 'GET':
        full_name = request.GET.get('fullName', '')

        with connection.cursor() as cursor:
            # Fetch the record before deleting it
            cursor.execute("SELECT * FROM person WHERE fullname LIKE %s", [f'{full_name}%'])
            columns = [col[0] for col in cursor.description]
            removed_data = [dict(zip(columns, row)) for row in cursor.fetchall()]

            # Delete the record
            cursor.execute("DELETE FROM person WHERE fullname LIKE %s", [f'{full_name}%'])

        return JsonResponse({'message': 'Data removed successfully', 'removed_data': removed_data})
    
# views.py
from django.http import JsonResponse

def create_data(request):
    if request.method == 'POST':
        # Parse the JSON data from the request
        data = json.loads(request.body)

        # Extract data from the JSON
        full_name = data.get('fullName', '')
        email = data.get('email', '')
        phone_number = data.get('phoneNumber', '')
        bank_balance = data.get('bankBalance', '')
        is_student = data.get('isStudent', False)

        # Perform the database insertion
        person_to_be_created = person.objects.create(
            fullname=full_name,
            email=email,
            phonenumber=phone_number,
            bankbalance=bank_balance,
            isstudent=is_student
        )

        # You can customize the response as needed
        response_data = {
            'message': 'Data inserted successfully',
            'inserted_data': {
                'person_id': person_to_be_created.id,
                'fullname': person_to_be_created.fullname,
                'email': person_to_be_created.email,
                'phonenumber': person_to_be_created.phonenumber,
                'bankbalance': person_to_be_created.bankbalance,
                'isstudent': person_to_be_created.isstudent,
            }
        }

        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'message': 'Invalid method'}, status=405)
    
def update_data(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)

            # Extract data from the JSON
            updated_full_name = data.get('updatedFullName', '')
            updated_email = data.get('updatedEmail', '')
            updated_phone_number = data.get('updatedPhoneNumber', '')
            updated_bank_balance = data.get('updatedBankBalance', '')
            updated_is_student = data.get('updatedIsStudent', False)

            # Get the person to update
            person_to_update = person.objects.get(fullname=request.GET.get('fullNameToUpdate'))

            # Update the data
            person_to_update.fullname = updated_full_name
            person_to_update.email = updated_email
            person_to_update.phonenumber = updated_phone_number
            person_to_update.bankbalance = updated_bank_balance
            person_to_update.isstudent = updated_is_student

            # Save the changes
            person_to_update.save()

            # You can customize the response as needed
            response_data = {
                'message': 'Data updated successfully',
                'updated_data': {
                    'person_id': person_to_update.id,
                    'fullname': person_to_update.fullname,
                    'email': person_to_update.email,
                    'phonenumber': person_to_update.phonenumber,
                    'bankbalance': person_to_update.bankbalance,
                    'isstudent': person_to_update.isstudent,
                }
            }

            return JsonResponse(response_data)
        except person.DoesNotExist:
            return JsonResponse({'message': 'Person not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error_message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid method'}, status=405)