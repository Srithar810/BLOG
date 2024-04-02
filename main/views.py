from django.shortcuts import render,redirect
from .models import Blog, BlogComment,Contact
from .forms import ContactForm,CreateBlogForm,UpdateBlogForm,CommentBlogForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     all_blogs = Blog.objects.all()
#     context = {
#         'blogs':all_blogs
#     }
#     return render(request,'main/blog_home.html',context)

class home(generic.ListView):
    model = Blog
    template_name = 'main/blog_home.html'

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    all_comments = BlogComment.objects.filter(blog = blog.id)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]
    
    form = CommentBlogForm()
    if request.method =='POST':
        form = CommentBlogForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Comment on this blog has been posted')
            return redirect('/blog_detail/'+blog.slug)
    else:
        form =CommentBlogForm()        
        
    context = {
        'blog':blog,
        'all_blogs':all_blogs,
        'form': form,
        'all_comments': all_comments
    }
    print(context)
    return render(request,'main/blog_detail.html',context)

# class blog_detail(generic.DetailView):
#     model = Blog
#     template_name = 'main/blog_detail.html'



# def contactUs(request):
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     e_mail = request.POST['e_mail']
    #     phone_number = request.POST['phone_number']
    #     contact_message = request.POST['contact_message']
        
    #     if len(first_name) < 2 or len(last_name) < 2 or len(e_mail) < 5 or len(phone_number) < 9 or len(contact_message) < 5:
    #         return redirect('home')
    #     else: 
    #         save_data = Contact(first_name=first_name, last_name=last_name, e_mail=e_mail, phone_number=phone_number, contact_message=contact_message)
    #         save_data.save()
           
    #         return redirect('contact_us')
    
    # form = ContactForm()
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,'Your form is submitted succesfully')
    # else:
    #     form = ContactForm()
    #     #messages.error(request,'please fill the form properly')
    # return render(request,'main/contact_us.html',{'form':form})
    
class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = 'main/contact_us.html'
    success_url = '/'
    success_message = 'your query has been submited  successfully, we will contact you soon'
    
    def form_invalid(self,form):
        messages.add_message(self.request, messages.ERROR, 'Please submit the form carefully')
        return redirect('home')
    
class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    login_url = 'login'
    template_name = 'main/create_blog.html'
    success_url = '/'
    success_message = "your blog has been created"
    
class UpdateBlogView(LoginRequiredMixin,SuccessMessageMixin, generic.UpdateView):
    model = Blog
    form_class = UpdateBlogForm
    template_name = 'main/update_blog.html'
    login_url = 'login'
    success_url = '/'
    success_message = "your blog has been updated"
    
    def form_valid(self, form):
        print("Form is valid. Saving...")
        return super().form_valid(form)
    

class DeleteBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Blog
    template_name = 'main/delete_blog.html'
    login_url = 'login'
    success_url = '/'
    success_message = "your blog has been deleted"
    