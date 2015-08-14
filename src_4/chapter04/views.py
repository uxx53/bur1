from django.views import generic
from django.http import HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from braces.views import JSONResponseMixin
from posts.models import Post, PostForm
from chapter04 import models
from vanilla.model_views import CreateView, ListView, DeleteView, UpdateView
# from chapter04 import forms


def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))


class HelloView(View):
    def get(self, request, name="World"):
        return HttpResponse("Hello {}!".format(name))


class GreetView(View):
    greeting = "Hello {}!"
    default_name = "World"

    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))


class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"


class FeedMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feed"] = Post.objects.viewable_posts(self.request.user)
        return context


class LoginRequiredMixin:
    def dispatch(request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class MyFeed(FeedMixin, generic.CreateView):
    form_class = PostForm
    model = Post
    template_name = "myfeed.html"
  #  fields = ['privacy']
    success_url = reverse_lazy("home")


class PublicPostJSONView(JSONResponseMixin, generic.View):

    def get(self, request, *args, **kwargs):
        msgs = models.Post.objects.public_posts().values(
            "posted_by_id", "message")[:5]
        return self.render_json_response(list(msgs))

class AutorCreate(CreateView):
    form_class = models.AuthorForm
    model = models.Author
    #   form_class = forms.AuthorForm
    # fields = ['name','title']
    # template_name = "myfeed.html"
    success_url = reverse_lazy('list_notes')


class AutorList(ListView):
    model = models.Author
    # success_url = reverse_lazy("my_feed")


class AutorEdit(UpdateView):
    form_class = models.AuthorForm
    model = models.Author
    success_url = reverse_lazy('list_notes')


class AutorDelete(DeleteView):
    model = models.Author
    success_url = reverse_lazy('list_notes')
