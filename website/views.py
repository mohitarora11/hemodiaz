from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Category, Subcategory, Product , Aboutus


def show_category(request):
    cat = Category.objects.filter(status=1)
    subcat = Subcategory.objects.filter(status=1).order_by('sortorder')
    subcat_list = {}
    for c in cat:
        for sub in subcat:
            if sub.category == c:
                subcat_list[c.id] = (sub.id, sub.c_name)
                break
            
    return render_to_response('website/categories.html',{'cat':cat,'subcat':subcat_list},context_instance = RequestContext(request))
    
    
def show_product(request,catname,subcatname,catid,subcatid):
    selecat = Category.objects.filter(status=1,id=catid)
    cat = Category.objects.filter(status=1).order_by('sortorder')
    catdic = {}
    subcatdic = {}
    for cat_obj in cat:
        catdic[cat_obj.id] = [cat_obj.c_name]
        catdic[cat_obj.id].append([{subcat_obj.id:subcat_obj.c_name} for subcat_obj in Subcategory.objects.filter(category__id=cat_obj.id,status=1).order_by('sortorder')])
    subc = Subcategory.objects.filter(id=subcatid)

    items  = Product.objects.filter(status=1,subcategory__id=subcatid)
    #return render_to_response('website/product.html',{'selsubcat':selsubcat,'subcat':subcat,'items':items,'catdic':catdic,'selcat':selcat},context_instance = RequestContext(request))
    return render_to_response('bootstrap/website/product.html',{'selecat':selecat,'items':items,'catdic':catdic,'subcatid':int(subcatid),'subc':subc[0].c_name},context_instance = RequestContext(request))
    
def show_aboutus(request):
    abt = Aboutus.objects.all()
    return render_to_response('bootstrap/static/aboutus.html',{'abt':abt},context_instance = RequestContext(request))

def management(request):    
    return render_to_response('bootstrap/static/management.html',context_instance = RequestContext(request))
