from django.shortcuts import render

# import the company model
from .models import Company

def list_companies(request):

    # I want you to get all of the companies
    companies = Company.objects.all()


    return render(
        request,
        "clients/companies_list.html",
        {
            # the line below we're passing the query values (rows from table)
            # to the template
            "companies": companies
        }
    )