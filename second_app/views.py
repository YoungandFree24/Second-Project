# from django.shortcuts import HttpResponse, redirect
# from django.http import JsonResponse

# # Create your views here.
# # Responses Go here!!!!!!

# # def index(request):
# #     return render(request,'index.html')
#     # Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.

# # def another_route(request):
# #     return render("/root")

# # def redirected_method(request):
# #     return JsonResponse({"response": "JSON Response from redirected_method", "status": True})

# def root(request):
#     return redirect("/blogs")

# def index(request):
#     return JsonResponse({"responce": "placeholder to later display a list of all blogs with a method named index"})

# def new(request):
#     return JsonResponse({"responce": "placeholder to display a new form to create a new blog"})

# def create(request):
#     return redirect("/blogs")

# def show(request):
#     return JsonResponse({"response": "placeholder to display blog number", "status": True})

# def edit(request):
#     return JsonResponse({"response": "placeholder to edit blog number", "status": True})
    
# def destroy(request):
#     return redirect("/blogs")


# ---------------------------------------------------
from django.shortcuts   import render # notice the import!
def root(request):
    return render(request, "index.html")

# def root(request):
#     return render(request, "")