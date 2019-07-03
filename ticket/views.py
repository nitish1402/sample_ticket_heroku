from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from ticket.models import *
from datetime import datetime, date, time
from datetime import timedelta
import os
from ticket_booking import settings
from django.db.models import Max

def index(request):
    template = loader.get_template('index.html')
    context = {'mess': ''}
    request.session.flush()
    context['ureg'] = ureg = Ureg.objects.all()
    treg = Treg.objects.all()
    mreg = Movie.objects.all()
    c = 0
    for m in mreg:
        c = 0
        for t in treg:
            if m.mname == t.tmorn_name or m.mname == t.tafter_name or m.mname == t.teve_name:
                if m.mcity == t.tcity:
                    c = 1
        if c == 0:
            m.delete()

    if request.method == 'POST':
        umail = request.POST.get('umail')
        upass = request.POST.get('upass')

        for x in ureg:
            if x.umail == umail and x.upass == upass:
                request.session['umail'] = umail
                request.session['urole'] = x.urole
                context['mess'] = 'Successfully Login in'

                if x.urole == 'customer':
                    return redirect('custhome')

                if x.urole == 'theatre':
                    return redirect('thehome')

        if context['mess'] == '':
            context['mess'] = 'Incorrect mail id or password'

    return HttpResponse(template.render(context,request))

def reg(request):
    template = loader.get_template('register.html')
    context = {'mess': ''}
    request.session.flush()
    if request.method == 'POST':
        uname = request.POST.get('uname')
        umail = request.POST.get('umail')
        upass = request.POST.get('upass')
        upass1 = request.POST.get('upass1')
        uaddr = request.POST.get('uaddr')
        uphone = request.POST.get('uphone')
        urole = request.POST.get('urole')

        if upass != upass1:
            context['mess'] = ' Password mismatch '

        try:
            uphone == int(uphone)
        except:
            context['mess'] += ' number in-correctly '

        if context['mess'] == '':
            for x in Ureg.objects.all():
                if x.umail == umail:
                    context['mess'] = 'mail id is already registered'

            if context['mess'] != 'mail id is already registered':
                ucobj = Ureg.objects.create(
                    uname=uname,
                    umail=umail,
                    upass=upass,
                    uaddr=uaddr,
                    urole=urole,
                    uphone=uphone
                )
                ucobj.save()
                context['mess'] = 'Registration Successful'
                if ucobj.urole == 'theatre':
                    tobj = Treg.objects.create(tmail=ucobj.umail)
                    tobj.save()

    return HttpResponse(template.render(context,request))

def forgot(request):
    template = loader.get_template('forgot.html')
    context = {'mess': ''}
    if request.method == 'POST':
        sname = request.POST.get('uname')
        smail = request.POST.get('umail')
        spass = request.POST.get('upass')

        uobj = Ureg.objects.all()

        for x in uobj:
            if x.umail == smail and x.uname == sname:
                x.upass = spass
                context['mess'] = 'Successfully Password Changed'
                x.save()

        if context['mess'] != 'Successfully Password Changed':
            context['mess'] = 'username or email not found'
    return HttpResponse(template.render(context,request))

def logout(request):
    template = loader.get_template('logout.html')
    context = {'mess': ''}
    request.session.flush()
    return redirect('index')

def sample(request):
    template = loader.get_template('sample.html')
    context = {'mess': ''}
    context['mobj'] = mobj = Movie.objects.all()

    if request.method == 'POST':
        selopt = request.POST.get('selopt')
        context['mess'] = selopt


    return HttpResponse(template.render(context,request))

# --------------------- Customer -------------------

def custhome(request):
    template = loader.get_template('customer/cust_home.html')
    context = {'mess': 'Please update'}
    context['umail'] = umail = request.session['umail']
    context['mobj'] = mobj = Movie.objects.all()
    sobj = Slot.objects.all()
    context['obj'] = obj = Treg.objects.values('tcity').distinct()

    for x in sobj:
        if x.sstat == 'no':
            x.delete()

    return HttpResponse(template.render(context,request))

def custmovie(request):
    template = loader.get_template('customer/cust_movie.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    context['mobj'] = mobj = Movie.objects.all()

    context['selopt'] = selopt = request.session['selopt'] = request.POST.get('selopt')
    context['tobj'] = tobj = Treg.objects.all()

    sobj = Slot.objects.create()
    sobj.sumail = umail
    sobj.scity = selopt
    sobj.save()
    request.session['sid'] = sobj.id

    return HttpResponse(template.render(context,request))

def custloc(request, prod_id):
    template = loader.get_template('customer/cust_loc.html')
    context = {'mess': '', 'mshow':'', 'ashow':'', 'eshow':'', 'dis':''}
    context['umail'] = umail = request.session['umail']
    context['mobj'] = mobj = Movie.objects.get(id=prod_id)

    context['tobj'] = tobj = Treg.objects.all()
    sid = request.session['sid']
    context['sobj'] = sobj = Slot.objects.get(id=sid)
    context['today_c'] = today_c = 0
    check = 0
    ptime = (datetime.now()).time()
    pdate = (datetime.now()).date()

    if request.method == 'POST':
        context['mess'] = ''
        context['dis'] = ''
        seldate1 = request.POST.get('seldate')

        format_str = '%Y-%m-%d'
        seldate = cd = datetime.strptime(seldate1, format_str)
        cd_day = cd.day
        cd_month = cd.month
        cd_year = cd.year

        if cd_year >= pdate.year:
            if cd_month == pdate.month:
                if cd_day >= pdate.day:
                    context['mess'] = ''

                else:
                    context['mess'] = 'Enter a proper Date'
            elif cd_month > pdate.month:
                if cd_day <= pdate.day:
                    context['mess'] = ''
                else:
                    context['mess'] = 'Enter a proper Date'
            else:
                context['mess'] = 'Enter a proper Date'
        else:
            context['mess'] = 'Enter a proper Date'

        if context['mess'] == '':

            if cd_year == pdate.year:
                if cd_month == pdate.month:
                    if cd_day == pdate.day:
                        context['today_c'] = today_c = 1
                        context['dis'] = 'y'
                        if ptime.hour >= 9:
                            context['mshow'] = 'No Show'

                        if ptime.hour >= 13:
                            context['ashow'] = 'No Show'

                        if ptime.hour >= 18:
                            context['eshow'] = 'No Show'
                    else:
                        today_c = 0
                else:
                    today_c = 0
            else:
                today_c = 0

            if today_c == 0:
                sobj.stdate = seldate
                sobj.sshowname = mobj.mname
                sobj.save()
                for x in tobj:
                    if x.tname != 'Please update' and x.tcity == mobj.mcity:
                        if x.tmorn_name == mobj.mname or x.tafter_name == mobj.mname or x.teve_name == mobj.mname:
                            if sobj.stdate.year <= x.tdate.year:
                                if x.tdate.month == sobj.stdate.month:
                                    if sobj.stdate.day <= x.tdate.day:
                                        context['mess'] = ''
                                        context['dis'] = 'y'
                                        check = 1
                                if sobj.stdate.month < x.tdate.month:
                                        context['mess'] = ''
                                        context['dis'] = 'y'
                                        check = 1

                if context['mess'] == '' and context['dis'] == 'y' and check == 1:
                    context['dis'] = 'y'
                    sobj.save()
                elif check == 0:
                    context['mess'] = 'Enter Valid Date'

    return HttpResponse(template.render(context, request))

def custloc2(request):
    template = loader.get_template('customer/cust_loc_2.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    context['tobj'] = tobj = Treg.objects.all()
    context['mobj'] = mobj = Movie.objects.all()

    val = []
    sradio = str(request.POST.get('sradio'))
    sp = sradio.split()
    for x in sp:
        val.append(x)

    val[0] = str(val[0])
    val[1] = int(val[1])
    tobj = Treg.objects.get(id=val[1])

    sid = request.session['sid']
    context['sobj'] = sobj = Slot.objects.get(id=sid)

    sobj.sid = tobj.id
    sobj.stname = tobj.tname

    if val[0] == 'morn':
        sobj.sshowtype = context['dstype'] = 'morn'

    if val[0] == 'after':
        sobj.sshowtype = context['dstype'] = 'after'

    if val[0] == 'eve':
        sobj.sshowtype = context['dstype'] = 'eve'

    sobj.save()

    return redirect('custslot')

def custslot(request):
    template = loader.get_template('customer/cust_slot.html')
    context = {'mess': '','dis':''}
    list = []
    tlist = []
    for x in range(1, 51):
        tlist.append(x)
    context['tlist'] = tlist

    sid = request.session['sid']

    context['sobj'] = sobj = Slot.objects.get(id=sid)
    context['tobj'] = tobj = Treg.objects.get(id=sobj.sid)
    context['slots'] = slots = Slot.objects.all()

    cdate = sobj.stdate
    if context['mess'] == '':
        sobj.stcost = int(tobj.tcost)
        for x in slots:
            if x.sstat == 'yes' and x.stdate != None:
                d = x.stdate
                sty = d.year
                stm = d.month
                std = d.day

                cty = sobj.stdate.year
                ctm = sobj.stdate.month
                ctd = sobj.stdate.day

                if (std == ctd and stm == ctm and cty == sty) and x.stname == sobj.stname and x.sshowname == sobj.sshowname and x.sshowtype == sobj.sshowtype:
                    list.append(int(x.sslot))

        context['dis'] = 'yes'
        context['list'] = list
        sobj.save()

    return HttpResponse(template.render(context,request))

def custconfirm(request):
    template = loader.get_template('customer/cust_confirm.html')
    context = {'mess': ''}

    context['umail'] = umail = request.session['umail']
    context['mobj'] = mobj = Movie.objects.all()
    sid = request.session['sid']
    context['sobj'] = sobj = Slot.objects.get(id=sid)
    context['tobj'] = tobj = Treg.objects.get(id=sobj.sid)
    cslots = request.POST.getlist('checks')
    if not cslots:
        request.session['res'] = 'empty'
    else:
        request.session['res'] = 'y'
    for x in cslots:
        obj = Slot.objects.create(
            sumail=sobj.sumail,
            stname=sobj.stname,
            sid=sobj.id,
            stdate=sobj.stdate,
            sshowname=sobj.sshowname,
            sshowtype=sobj.sshowtype,
            sslot=int(x),
            stcost=int(sobj.stcost)
        )
        obj.save()

    return redirect('custack')

def custack(request):
    template = loader.get_template('customer/cust_ack.html')
    context = {'mess': ''}
    context['sid'] = sid = request.session['sid']
    context['sobj'] = sobj = Slot.objects.all()
    cost = 0
    slots = ''
    context['res'] = res = request.session['res']

    for x in sobj:
        if x.sid == sid:
            context['mail'] = x.sumail
            context['name'] = x.stname
            context['date'] = x.stdate
            context['sname'] = x.sshowname
            cost += int(x.stcost)
            context['stcost'] = cost
            slots += (" " + str(x.sslot))
            context['sslot'] = slots
            if x.sshowtype == 'morn':
                context['stype'] = '09:00 AM'

            if x.sshowtype == 'after':
                context['stype'] = '01:00 PM'

            if x.sshowtype == 'eve':
                context['stype'] = '06:00 PM'

    if request.method == 'POST':
        tcard = request.POST.get('tcard')
        tcvv = request.POST.get('tcvv')

        try:
            tcard = int(tcard)
            tcvv = int(tcvv)
        except:
            context['mess'] = ' Enter Card Details Correctly '

        if context['mess'] == '':
            for x in sobj:
                if x.sid == sid:
                    x.sstat = 'yes'
                    x.save()

            context['mess'] = 'Booked Successfully'

    return HttpResponse(template.render(context,request))

def custprofile(request):
    template = loader.get_template('customer/cust_porfile.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    context['ureg'] = ureg = Ureg.objects.get(umail=umail)

    if request.method == 'POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        uaddr = request.POST.get('uaddr')
        uphone = request.POST.get('uphone')

        try:
            uphone == int(uphone)
        except:
            context['mess'] = ' number in-correctly '

        if context['mess'] == '':

            ureg.uname = uname
            ureg.upass = upass
            ureg.uphone = uphone
            ureg.uaddr = uaddr

            ureg.save()

            context['mess'] = 'Updated Successful'

    return HttpResponse(template.render(context,request))

def custnoti(request):
    template = loader.get_template('customer/cust_noti.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    tid = Ureg.objects.get(umail=umail)
    context['tid'] = tid.umail
    context['sobj'] = sobj = Slot.objects.all()

    return HttpResponse(template.render(context,request))

def custcancel(request):
    template = loader.get_template('customer/cust_cancel.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    tid = Ureg.objects.get(umail=umail)
    context['tid'] = tid.umail
    context['sobj'] = sobj = Slot.objects.all()

    if request.method == 'POST':
        scancel = request.POST.get('scancel')
        obj = Slot.objects.get(id=scancel)
        obj.delete()
        context['mess'] = 'Successfully seat Deleted'

    return HttpResponse(template.render(context, request))

# --------------------- Theatre ---------------------

def thehome(request):
    template = loader.get_template('theatre/the_home.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    context['tdreg'] = tdreg = Treg.objects.get(tmail=umail)

    return HttpResponse(template.render(context,request))

def theprofile(request):
    template = loader.get_template('theatre/the_profile.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    context['ureg'] = ureg = Ureg.objects.get(umail=umail)
    context['treg'] = treg = Treg.objects.get(tmail=umail)
    tn=treg.tname

    if request.method == 'POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        uaddr = request.POST.get('uaddr')
        uphone = request.POST.get('uphone')
        tname = str(request.POST.get('tname')).title()
        tloc = str(request.POST.get('tloc')).title()
        tcity = str(request.POST.get('tcity')).title()
        c = 0
        try:
            uphone == int(uphone)
        except:
            context['mess'] += ' number in-correctly '

        if context['mess'] == '':
            for x in Treg.objects.all():
                if x.tname == tname and tname != tn:
                    context['mess'] = 'Theatre already registered'

            if context['mess'] == '':
                ureg.uname = uname
                ureg.upass = upass
                ureg.uphone = uphone
                ureg.uaddr = uaddr
                treg.tloc = str(tloc).title()
                treg.tname = str(tname).title()
                treg.tcity = str(tcity).title()
                treg.save()
                ureg.save()

                context['mess'] = 'Updated Successful'

    return HttpResponse(template.render(context,request))

def theaddmovies(request):
    template = loader.get_template('theatre/the_add.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    context['treg'] = treg = Treg.objects.get(tmail=umail)
    context['mreg'] = mreg = Movie.objects.all()
    c = 0
    if request.method == 'POST':
        tdate = request.POST.get('tdate')
        tshow = str(request.POST.get('tshow'))
        tshowname = str(request.POST.get('tshowname')).title()
        tshowimg = request.FILES['tshowimg']
        treg.tdate = tdate

        if str(tshow) == 'ms':
            treg.tmorn_name = tshowname
            treg.tmorn_img = tshowimg

        if str(tshow) == 'as':
            treg.tafter_name = tshowname
            treg.tafter_img = tshowimg

        if str(tshow) == 'es':
            treg.teve_name = tshowname
            treg.teve_img = tshowimg

        treg.save()

        for x in mreg:
            if str(x.mname) == str(tshowname) and str(x.mcity) == treg.tcity:
                c = 1

        if c == 0:
            obj = Movie.objects.create(
                mname=tshowname,
                mimg=tshowimg,
                mcity=treg.tcity
            )
            obj.save()

        context['mess'] = 'Movies added or Updated'

    return HttpResponse(template.render(context,request))

def thecusthis(request):
    template = loader.get_template('theatre/the_cust_his.html')
    context = {'mess': ''}
    context['umail'] = umail = request.session['umail']
    tid = Treg.objects.get(tmail=umail)
    context['tid'] = tid.tname
    context['sobj'] = sobj = Slot.objects.all()

    return HttpResponse(template.render(context,request))



