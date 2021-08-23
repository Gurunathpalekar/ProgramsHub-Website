"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_website import views
urlpatterns = [
    path('admin/', admin.site.urls),
path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('java',views.java,name='java'),
    path('jv',views.jv,name='jv'),
    path('cplus',views.cplus,name='cplus'),
    path('c',views.c,name='c'),
    path('py',views.py,name='py'),
    path('python',views.python,name='python'),
    path('projects',views.projects,name='projects'),
    path('first',views.first,name='first'),
    path('addnum',views.addnum,name='addnum'),
    path('ascii', views.ascii, name='ascii'),
    path('prime', views.prime, name='prime'),
    path('primeno', views.primeno, name='primeno'),
    path('swap', views.swap, name='swap'),
    path('randomnum', views.randomnum, name='randomnum'),
    path('divi', views.divi, name='divi'),
    path('factno', views.factno, name='factno'),
    path('contactus', views.contactus, name='contactus'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('add', views.add, name='add'),
    path('alphabet', views.alphabet, name='alphabet'),
    path('asciino', views.asciino, name='asciino'),
    path('evenodd', views.evenodd, name='evenodd'),
    path('fact', views.fact, name='fact'),
    path('mul', views.mul, name='mul'),
    path('positive', views.positive, name='positive'),
    path('swapnum', views.swapnum, name='swapnum'),
    path('vowel', views.vowel, name='vowel'),
    path('alph',views.alph,name='alph'),
    path('countno',views.countno,name='countno'),
    path('fibo',views.fib,name='fibo'),
    path('gcd',views.gcd,name='gcd'),
    path('larnum',views.larnum,name='larnum'),
    path('lcm',views.lcm,name='lcm'),
    path('leapy',views.leapy,name='leapy'),
    path('multab',views.multab,name='multab'),
    path('palin',views.palin,name='palin'),
    path('roots',views.roots,name='roots'),
    path('sumnatnum',views.sumnatnum,name='sumnatnum'),


    path('cc',views.cc, name='cc'),
    path('cadd',views.cadd, name='cadd'),
    path('cascii',views.cascii, name='cascii'),
    path('cfactno',views.cfactno, name='cfactno'),
    path('cpower',views.cpower, name='cpower'),
    path('cprime',views.cprime, name='cprime'),
    path('cprint',views.cprint, name='cprint'),
    path('creverse',views.creverse, name='creverse'),
    path('cswap',views.cswap, name='cswap'),
    path('cleap',views.cleap, name='cleap'),
    path('ceveorodd', views.ceveorodd, name='ceveorodd'),
    path('cfibo', views.cfibo, name='cfibo'),
    path('cgcd', views.cgcd, name='cgcd'),
    path('clarnum', views.clarnum, name='clarnum'),
    path('clcm', views.clcm, name='clcm'),
    path('cmultable', views.cmultable, name='cmultable'),
    path('cpal', views.cpal, name='cpal'),
    path('cposorneg', views.cposorneg, name='cposorneg'),
    path('croot', views.croot, name='croot'),
    path('csumnatnum', views.csumnatnum, name='csumnatnum'),
    path('cvoworcon', views.cvoworcon, name='cvoworcon'),



    path('cp',views.cp,name='cp'),
    path('cpadd',views.cpadd, name='cpadd'),
    path('cpascii',views.cpascii, name='cpascii'),
    path('cpfact',views.cpfact, name='cpfact'),
    path('cpleap',views.cpleap, name='cpleap'),
    path('cpmul',views.cpmul, name='cpmul'),
    path('cpnum',views.cpnum, name='cpnum'),
    path('cpprime',views.cpprime, name='cpprime'),
    path('cppyramid',views.cppyramid, name='cppyramid'),
    path('cpswap',views.cpswap, name='cpswap'),
    path('cparmst',views.cparmst, name='cparmst'),
    path('cpeveorodd',views.cpeveorodd, name='cpeveorodd'),
    path('cpfibo',views.cpfibo, name='cpfibo'),
    path('cpgcd',views.cpgcd, name='cpgcd'),
    path('cplarnum',views.cplarnum, name='cplarm'),
    path('cplcm',views.cplcm, name='cplcm'),
    path('cplus',views.cplus, name='cplus'),
    path('cpmultab',views.cpmultab, name='cpmultab'),
    path('cpnatnum',views.cpnatnum, name='cpnatnum'),
    path('cprevnum,',views.cprevnum, name='cprevnum'),
    path('cproot',views.cproot, name='cproot'),
    path('cpvoworcon',views.cpvoworcon, name='cpvoworcon'),

    path('areatri', views.areatri,name='areatri'),
    path('armstrongnum', views.armstrongnum,name='armstrongnum'),
    path('fib', views.fib,name='fib'),
    path('fpyramid', views.fpyramid,name='fpyramid'),
    path('hpyramid', views.hpyramid,name='hpyramid'),
    path('kmtomi', views.kmtomi,name='kmtomi'),
    path('oddeven', views.oddeven,name='oddeven'),
    path('palindrome', views.palindrome,name='palindrome'),
    path('celsius', views.celsius,name='celsius'),
    path('sortwords', views.sortwords,name='sortwords'),
    path('dectobin',views.dectobin,name='dectobin')




]
