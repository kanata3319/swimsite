import logging
from django.shortcuts import render

logger = logging.getLogger('access')


class AccessLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info('[user:{}]{}'.format(request.user, request.path))
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error('[user:{}]{}'.format(request.user, exception), exc_info=True)
        return render(request, '500error.html')
