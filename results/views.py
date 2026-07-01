from django.shortcuts import render, redirect, get_object_or_404
from .models import Result
from .forms import ResultForm


def result_list(request):
    results = Result.objects.all()
    return render(request, "results/result_list.html", {"results": results})


def add_result(request):

    if request.method == "POST":
        form = ResultForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("result_list")

    else:
        form = ResultForm()

    return render(request, "results/add_result.html", {"form": form})


def edit_result(request, id):

    result = get_object_or_404(Result, id=id)

    if request.method == "POST":

        form = ResultForm(request.POST, instance=result)

        if form.is_valid():
            form.save()
            return redirect("result_list")

    else:
        form = ResultForm(instance=result)

    return render(request, "results/edit_result.html", {"form": form})


def delete_result(request, id):

    result = get_object_or_404(Result, id=id)

    result.delete()

    return redirect("result_list")