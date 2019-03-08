from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_update(request, pk):
	post = Post.objects.filter(pk=pk)
	if len(post) == 0 :
		return redirect("/")
	else :
		return render(request, 'blog/post_write.html', {'post': post[0]})
	
def post_write(request):
	return render(request, 'blog/post_write.html', {})
	
def post_save(request):
	pk = request.POST.get("pk", '')
	try :
		user = User.objects.get(username=request.POST.get("writter"))
		if pk == '' :			
			Post.objects.create(author=user, title=request.POST.get("title", ''), text=request.POST.get("text", ''))
		else :			
			post = Post.objects.get(author=user, pk=request.POST.get("pk", ''))
			post.title = request.POST.get("title", '')
			post.text = request.POST.get("text", '')
			post.save()
	except :
		print("Post Svae Error:" + request.POST.get("writter") + "^" + request.POST.get("pk", ''))
	
	return redirect("/")
	
def post_del(request, id, pk):
	try :
		user = User.objects.get(username=id)
		post = Post.objects.get(author=user, pk=pk)
		post.delete()
	except Exception  as ex:
		print("delete error:" + id + "^" + pk)

	return redirect("/")