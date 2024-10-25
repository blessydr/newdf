from django.shortcuts import render,redirect,get_object_or_404
from.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import BlogForm
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import UserRegistration
from myaccounts.models import Post
from django.contrib.auth import logout
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request,*args,**kwargs):
    image=post.objects
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        breakpoint()
        if form.is_valid():
            post = form.save(commit=False) 
            # post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = BlogForm()
    context={
        'form': form,
        'image':image
    }
    return render(request, 'create_post.html')

def blog_list(request):
    blog = Post.objects.all().order_by('-date_posted')
    print(blog)
    search_query = request.GET.get('search', '')  # Get the search query from the request, or set it to an empty string
    if search_query:
        # Filter posts by the search query (case-insensitive search using `icontains`)
        blogs = Post.objects.filter(title__icontains=search_query)
    else:
        blogs = Post.objects.all().order_by('-date_posted')  # Show all posts if no search query
    
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'search_query': search_query})




def blog_detail(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def blog_create(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form=BlogForm()
        return render(request,'blog/blog_form.html',{'form':form})

def blog_edit(request,pk):
        blog = get_object_or_404(Post, pk=pk)
        if request.method=='POST':
           form=BlogForm(request.POST,instance=blog)
           if form.is_valid():
               form.save()
               return redirect('blog_detail',pk=pk)
        else:
            form= BlogForm(instance=blog)
        return render(request,'blog/blog_form.html',{'form':form})

def blog_delete(request,pk):
    blog = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
            blog.delete()
            return redirect('blog_list')
    return render(request,'blog/blog_confirm_delete.html',{'blog':blog})

   
def logout_view(request):
    logout(request) 
    return redirect('home') 

def home(request):
     return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        
        user = auth.authenticate(username=user_name, password=pass_word)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect('blog_list') 
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  
    else:
        return render(request, 'login.html')
def register(request):
     
     if request.method == 'POST':
        firstname= request.POST['first_name']
        lastname= request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
               user = User.objects.create_user(username=username, password=password1, email=email)
               user.save()
               new_user = UserRegistration(
               first_name=firstname,
               last_name=lastname,
               username=username,
               email=email,
               password=password1,  # This will be hashed in the save method
          )
               new_user.save()
               messages.success(request, "You have registered successfully!")
               return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
     return render(request, 'register.html')

def index(request):
     return render(request,'blog_index.html')
 
