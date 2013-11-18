def index():
    # make a link to show form
    # load all list via ajax.
    link = A('Makeform', _href=URL('form.load'), _id='afrm', cid='frm')
    
    #A('linked page',_href='http://example.com',cid=request.cid)

    return dict(link=link)

def processor():
    rows = db(db.item).select(orderby=db.item.id)
    
    #return response.render('default/list.ajax.html', dict(retact=retact, rows=rows))
    return dict(rows=rows)
    
def form():
    form = SQLFORM(db.item, _id='myform')
    if form.accepts(request, formname='default'):
        response.flash = T('Success')
        response.js = '$("%s").load("%s");' % ('#list', URL('processor'))
        #response.headers['web2py-component-command']='$(%s).load(%s);' % ('#list', URL('processor'))
        #response.js = 'alert("submitted");'
    elif form.errors:
        response.flash = T('Failed')
        #response.js = 'alert("fialed");'
        #response.js = 'alert("%s" + " " + "%s");' % ('#list', URL('processor'))
    else:
        response.flash = T('Please fill out the form')
    #return response.render('default/form.ajax.html', dict(form=form));
    return dict(form=form)

def regular():
    form = SQLFORM(db.item)
    
    if form.accepts(request, session, formname='default'):
        response.flash = T('Success')
    else:
        response.flash = T('Failed')
    
    return dict(form=form)

def formholder():
    form = SQLFORM(db.item, _id="formid")
    if form.accepts(request, session, formname='default'):
        response.flash = T('Success')
    else:
        response.flash = T('Failed')
    
    return dict(form=form)
    
def formtaker():
    link = A(T('openform'), _href="#", _id="openform")
    return dict(link=link)

