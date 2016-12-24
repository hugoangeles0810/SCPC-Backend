import logging

from scpc.utils import setallattr
from scpc_core.models.managers import get_now

logger = logging.getLogger('scpc.middleware.RequestModelMiddleware')

class RequestModelMiddleware(object):

  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    
    self.process_request(request)

    response = self.get_response(request)

    self.process_response(request, response)

    return response


  def process_request(self, request):
    logger.info("Starting request ... ")
    
    from scpc_core.models import Request, User
    user = None
    if hasattr(request, 'user') and request.user and isinstance(request.user, User):
      user = request.user
    headers = str(request.META)
    ip_address = request.META.get('REMOTE_ADDR')
    request.core_request = Request.objects.create(
      user=user, ip_address=ip_address, url=request.path, method=request.method, 
      request_headers=headers, started_at=get_now()
    )

  def process_response(self, request, response):
    if hasattr(request, 'core_request') and request.core_request:
      status_code =response.status_code
      validation_errors = None
      if int(status_code/100) == 4:
        validation_errors = response.content
      setallattr(
        request.core_request, response_status=status_code, 
        validation_errors=validation_errors, finished_at=get_now()
      )
      request.core_request.save()
    logger.info("Finishing request ... ")