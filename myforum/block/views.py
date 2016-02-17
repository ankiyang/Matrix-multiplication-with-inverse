from django.shortcuts import render_to_response
from models import Block

# Create your views here.
def block_list(request):
	blocks=Block.objects.all().order_by("-id")
	return render_to_response("block_list.html",{"blocks":blocks})