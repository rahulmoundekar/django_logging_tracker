from django.shortcuts import render
import logging


# Create your views here.

def viewWelcome(request):
    logging.debug("Your debug warning message is here")
    logging.warning("Your log warning message is here")
    logging.info("Your log info message is here")
    logging.exception("Something bad happened")
    return render(request, 'index.html')


def viewHome(request):
    logging.info("Your log info message is here")
    return render(request, 'home.html')
