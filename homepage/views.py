from django.shortcuts import render
from .test import cat1_tsne, cat2_tsne, cat3_tsne, getData1, getData2, getData3

coord1 = []
text1 = []
for i in range(len(getData1())):
	coord1.append(getData1()[i]['coordinates'])
	text1.append(getData1()[i]['text'])
coord2 = []
text2 = []
for i in range(len(getData2())):
	coord2.append(getData2()[i]['coordinates'])
	text2.append(getData2()[i]['text'])
coord3 = []
text3 = []
for i in range(len(getData3())):
	coord3.append(getData3()[i]['coordinates'])
	text3.append(getData3()[i]['text'])

def index(request):
	templates = 'index.html'

	context = {
			'coord1': coord1,
			'coord2': coord2,
			'coord3': coord3,
			'text1' : text1,
			'text2' : text2,
			'text3' : text3,

		}
	return render(request, templates, context)
	