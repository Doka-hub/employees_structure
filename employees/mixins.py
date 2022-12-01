from django.http import JsonResponse

from typing import Optional


class AjaxViewMixin:
    response = {}

    def ajax_response(self, data: Optional[dict] = None, **kwargs):
        if data is None:
            data = self.response

        return JsonResponse(
            data,
            safe=False,
            **kwargs
        )
