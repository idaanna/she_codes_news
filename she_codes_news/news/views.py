from typing import Any
from django.db import models
from django.views import generic
# is below required as it was not for createview?
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from django.shortcuts import get_object_or_404


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
# ida adding edit view
class EditView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/editView.html'
    success_url = reverse_lazy('news:index')

class DeleteView(generic.DeleteView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/deleteView.html'
    success_url = reverse_lazy('news:index')

    def DeleteView(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)



# ida adding detailview for author search
# with Bernardo
# class AuthorView(generic.DetailView):
#     template_name = 'news/authorView.html'
#     model = CustomUser

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['stories'] = NewsStory.objects.filter(author= self.object.id )
#         return context

# detailview from Rebecca's class
class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'news/authorView.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser,
        username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.filter(author__id=self.object.id)
        return context