from django.http import HttpResponseForbidden


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        recipe = self.get_object()
        if recipe.author != request.user:
            return HttpResponseForbidden("Вы не являетесь автором этого рецепта.")
        return super().dispatch(request, *args, **kwargs)
