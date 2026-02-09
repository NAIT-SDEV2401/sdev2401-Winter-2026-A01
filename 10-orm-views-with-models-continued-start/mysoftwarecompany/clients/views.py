from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.
from .models import Company, Employee


def list_companies(request):
    # fetching data from the database and passing it to the template
    companies = Company.objects.all()

    return render(request, 'clients/companies_list.html', {'companies': companies})

# let's create a detail view.
# we're going to use the id of the company in the detail view
def company_detail(request, company_id):
    # get the object or 404 which does what it says.
    company = get_object_or_404(
        Company, # the model to fetch from.
        id=company_id # id is the field on the db,
        # company_id is part of the path.
    )
    # under the hood this is doing Company.objects.get(id=company_id)
    # id is generated as primary key for each model.
    return render(
        request,
        'clients/company_detail.html',
        {'company': company}
    )

# is we're going to create a employee search results page.

def employees_search_results(request, company_id):

    # select the specific company.
    company = get_object_or_404(Company, id=company_id)
    # let's get a query parameter from the request object.
    query = request.GET.get('q') # the value or None

    # check if the query exists
    employees = None
    if query:
        # let's first search by the first name using icontains
        # field look up docs here: https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups
        # remember that company.employees is queryset (many rows of instances)
        # that we can filter the first name if it contains any part of the query.
        # note Q objects are ORM specific which all you to do
        # OR is |,  AND is &, or NOT is ~
        # docs here: https://docs.djangoproject.com/en/5.2/topics/db/queries/#complex-lookups-with-q-objects
        employees = company.employees.filter(
            Q(first_name__icontains=query) | # only one pipe
            Q(last_name__icontains=query)
        )
        # so the above is going to search for the first name OR the last name
        # in sql
        # SELECT * FROM clients_employees WHERE first_name LIKE '%query%' OR last_name LIKE '%query%'
    else: # there's no query
        # if there's no query you can just provide an empty queryset
        employees = Employee.objects.none()


    return render(
        request,
        'clients/employees_search_results.html',
        {'company': company, 'employees': employees, 'query': query }
    )