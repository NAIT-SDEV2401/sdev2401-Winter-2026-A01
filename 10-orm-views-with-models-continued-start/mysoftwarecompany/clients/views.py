from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Company


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
    query = request.GET.get('q', '')

    breakpoint()

    return render(
        request,
        'clients/employees_search_results.html'
    )