from django.shortcuts import render, redirect
from .models import Objective
from .form import ObjectiveForm

def objective(request):
    objectives = Objective.objects.all()
    context = {'objectives': objectives}
    return render(request, 'objectives/objective.html', context)

def objective_details(request, pk):
    objective_Obj = Objective.objects.get(objective_id=pk)
    context = {'objective':objective_Obj}
    return render(request, "objectives/objective_detail.html", context)

def create_objective(request):
    form = ObjectiveForm

    if request.method == "POST":
        form = ObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('objective')
        
    context = {'form':form}
    return render(request, 'objectives/objective_form.html', context)

def update_objective(request, pk):
    objective = Objective.objects.get(objective_id=pk)
    form = ObjectiveForm(instance=objective)

    if request.method == "POST":
        form = ObjectiveForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            return redirect('objectives')
        
    context = {'form':form}
    return render(request, 'objectives/objective_form.html', context)

def delete_objective(request,pk):
    objective = Objective.objects.get(objective_id=pk)

    if request.method == "POST":
        objective.delete()
        return redirect(objective)

    return render(request, 'objectives/delete_template.html, context')