from django.shortcuts import render
from.models import about,career
from django.forms import ModelForm
# Create your views here.


class PostsForm(ModelForm):
    class Meta:
        model = career
        fields = ['Username','email','pdf']
def home(request):
	a=about.objects.all()
	return render(request, 'home.html',{'a':a})

def career(request,template_name ='career.html'):
	form = PostsForm(request.POST or None)
	if form.is_valid():
		form.save()
		# return redirect('contect')
	return render(request, template_name, {'form': form})		
		