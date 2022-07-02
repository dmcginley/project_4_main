from django.shortcuts import render

# Create your views here.


posts = [
    {
        'auther': 'me',
        'title': 'First post',
        'content': 'We use a subset of all colors to create a smaller color palette for generating color schemes, also available as Sass variables.',
        'date_posted': 'aug 27 2022'
    },
    {
        'auther': 'me',
        'title': 'Second post',
        'content': 'Bootstrap is supported by an extensive color system that themes our styles and components. This enables more comprehensive customization and extension for any project.',
        'date_posted': 'aug 32 2022'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
