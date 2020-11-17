from django.shortcuts import render
from .test import cat1_tsne, cat2_tsne, cat3_tsne, get_text_category1, get_text_category2, get_text_category3

def index(request):
	templates = 'index.html'

	text1 = get_text_category1()
	text2 = get_text_category2()
	text3 = get_text_category3()



	context = {
			'qwe': cat1_tsne(),
			'asd': cat2_tsne(),
			'zxc': cat3_tsne(),
			'text1' : text1,
			'text2' : text2,
			'text3' : text3,
		}
	return render(request, templates, context)
	