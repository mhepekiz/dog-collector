from django.shortcuts import render

# Add the following import
from django.http import HttpResponse



class Dog:
    def __init__(self, name, breed, description, age, color):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        self.color = color

dogs = [
    Dog('Lolo', 'tabby', 'foul little demon', 3, 'Brown'),
    Dog('Smoky', 'Flat Coated Retriever', 'Sleepy dog', 6, 'Black'),
    Dog('Oddie', 'Terrier', 'Doesn\'t like Smoky', 3, 'White'),
]


# Define the home view
def home(request):
  return HttpResponse('<h1>kkjkjjk</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })