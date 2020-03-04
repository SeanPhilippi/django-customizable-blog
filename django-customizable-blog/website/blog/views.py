from django.views import generic
from .models import Post, Setting
# kwargs is key word arguments
# ** syntax is spreading the dictionary
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    def get_context_data(self, **kwargs): # overwriting a built in function
        settings = Setting.objects.all().first()
        context = {
            'background_image' : settings.background_image,
            'text_color' : str(settings.color_palettes.text_color),
            'button_color' : str(settings.color_palettes.button_color),
            'navbar_color' : str(settings.color_palettes.navbar_color),
            'font_type' : str(settings.font_type),
            'post_list' : self.queryset
        }

        for key in kwargs.keys():
            context[key] = kwargs[key]

        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        settings = Setting.objects.all().first()
        context = {
            'background_image' : settings.background_image,
            'text_color' : str(settings.color_palettes.text_color),
            'button_color' : str(settings.color_palettes.button_color),
            'navbar_color' : str(settings.color_palettes.navbar_color),
            'font_type' : str(settings.font_type),
        }
        for key in kwargs.keys():
            context[key] = kwargs[key]

        return context