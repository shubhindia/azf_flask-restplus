import logging
import importlib
import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi
from ..restplus.listing import app



def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AzureFunctionsWsgi(app).main(req, context)
