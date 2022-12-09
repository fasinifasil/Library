from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksForm
# Create your views here.
def homepage(request):
    book=Books.objects.all()
    context={
        'book_list':book
    }
    return render(request,'homepage.html',context)
def detail(request,book_id):
    books=Books.objects.get(id=book_id)
    return render(request,'detail.html',{'books':books})

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        author=request.POST.get('author',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        image=request.FILES['image']
        movie=Books(name=name,author=author,desc=desc,year=year,image=image)
        movie.save();
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    book=Books.objects.get(id=id)
    form = BooksForm(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'book':book})
def delete(request,id):
    if request.method=='POST':
        movie=Books.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


