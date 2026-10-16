from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render,  get_object_or_404
from expenses import data
from expenses.forms import ContactForm, ExpenseForm
from expenses.models import Expense, Category
from django.contrib.auth.decorators import login_required

def index(request: HttpRequest):

    return render(request, 'expenses/home.html')


def about(request: HttpRequest):

    return render(request, 'expenses/about.html')



def contact(request: HttpRequest):
    form = ContactForm()
    return render(request, 'expenses/contact.html', {'form': form})


@login_required
def expenses_view_list(request: HttpRequest) -> HttpResponse:

    
    expenses = Expense.objects.filter(author=request.user)
    return render(request, 'expenses/expenses_list.html', {'expenses': expenses})


@login_required
def expenses_detail (request: HttpRequest, expense_id: int) -> HttpResponse:


    expense = get_object_or_404(Expense.objects.select_related('author', "category"), pk=expense_id)
  
    if expense.author != request.user:

        return HttpResponseForbidden("You can only see expenses owned by yourself")
    
    return render(request, 'expenses/expense_detail.html', {'expense': expense})


@login_required
def expenses_create (
        request: HttpRequest
) -> HttpResponse:
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.author = request.user
            expense.save()
            form.save_m2m()
            messages.success(request, "Expense created")            
            return redirect('expenses:expenses_detail', expense_id=expense.pk)
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_create.html', {'form': form})


@login_required
def expenses_update(
        request: HttpRequest,
        expense_id: int
) -> HttpResponse:
    expense = get_object_or_404(Expense, pk=expense_id)
   
    if expense.author != request.user:
    
        return HttpResponseForbidden("You can only edit expenses owned by yourself")
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated")
            return redirect ('expenses:expenses_detail', expense_id=expense.pk)
      
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_create.html', {'form': form})

            


@login_required
def expenses_delete (

    request: HttpRequest,
    expense_id: int
) -> HttpResponse:
    expense = get_object_or_404(Expense, pk=expense_id)
    if expense.author != request.user:
    
        return HttpResponseForbidden("You can only delete expenses owned by yourself")

    if request.method == 'POST':
        expense.delete()
        messages.success(request, "Expense deleted")
        return redirect('expenses:expenses_list')
    return render(request, 'expenses/expense_delete.html', {'expense': expense})



# def register_view(request):
#     user = User.objects.create_user(

        
#     )

#     login(request, user)
#     messages.success