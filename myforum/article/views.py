# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from block.models import Block
from comment.models import Comment
from models import Article



def article_list(request,block_id): #block_id从url取到
	block_id=int(block_id)
	block=Block.objects.get(id=block_id) #get 返回有且只有一个板块
	articles=Article.objects.filter(block=block).order_by("-last_update_timestamp")
	
	return render_to_response("article_list.html",
		{"articles":articles,"b":block,},
		context_instance=RequestContext(request))


def create_article(request,block_id):
	block_id=int(block_id)
	block=Block.objects.get(id=block_id)
	if request.method=="GET":  #提交表单的后台处理
		return render_to_response("article_create.html",{"b":block},
			context_instance=RequestContext(request))
	else: # request.method=="POST"
	    title=request.POST["title"].strip()
	    content=request.POST["content"].strip()
	    if not title or not content:
	    	messages.add_message(request,messages.ERROR,u'标题和内容均不能为空')
	    	return render_to_response("article_create.html",
	    		{"b":block,"title":title,"content":content},
	    		context_instance=RequestContext(request))
	    owner=User.objects.all()[0] # TODO:
	    new_article=Article(block=block,owner=owner,title=title,content=content)
	    new_article.save()
	    messages.add_message(request,messages.INFO,u'成功发布文章.')	
	    return redirect(reverse("article_list",args=[block.id]))

def article_detail(request,article_id):
	article_id=int(article_id)
	article=Article.objects.get(id=article_id)
	return render_to_response("article_detail.html",{"article":article},context_instance=RequestContext(request))

