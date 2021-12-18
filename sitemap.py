#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Dec 25, 2020 09:21:58 PM +0700  platform: Windows NT

# Автор : Алексей Черемных
# Официальный сайт : https://xn--90abhbolvbbfgb9aje4m.xn--p1ai/
# license : GNU GPL v2
# version : 1.0

# Планируется:
# - проверить приоритеты на других сайтах
# - скрол дергается
# - добавить в игнор gif

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ui_support
import requests
from lxml import html
from urllib.parse import urljoin, urlparse
from datetime import datetime
import sys, time, threading, re
from tkinter import messagebox, IntVar
import os
import concurrent.futures
import urllib.robotparser

# Язык системы
import locale
try:
    LanguageSystem = locale.getdefaultlocale()[0]
except:
    LanguageSystem = 'Неизвестно'

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    top = Toplevel1 (root)
    ui_support.init(root, top)
    StartApp() #запускаем процесс создания карты сайта
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    ui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("601x439+279+240")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        # root.iconbitmap('data\\LicenseChecker.ico')
        # top.iconbitmap('ico.ico')
        if LanguageSystem == 'ru_RU':
            top.title("XmlSitemapGenerator от КонтинентСвободы.рф")
        else:
            top.title("XmlSitemapGenerator version 1.1")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.212, relwidth=0.607)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.055, rely=0.43, height=20, relwidth=0.751)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.822, rely=0.43, height=24, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        if LanguageSystem == 'ru_RU':
            self.Button1.configure(text='''Начать''')
        else:
            self.Button1.configure(text='''Start''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.082, rely=0.086, height=17, width=294)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        if LanguageSystem == 'ru_RU':
            self.Label1.configure(text='''Укажите адрес сайта и нажмите кнопку "Начать"''')
        else:
            self.Label1.configure(text='''Enter the website address and click "Start"''')

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.599, rely=0.0, relheight=0.189, relwidth=0.408)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(self.Frame3)
        self.Labelframe1.place(relx=0.041, rely=0.0, relheight=0.916
                , relwidth=0.898)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        if LanguageSystem == 'ru_RU':
            self.Labelframe1.configure(text='''Статистика:''')
        else:
            self.Labelframe1.configure(text='''Statistics:''')

        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.091, rely=0.237, height=19, width=124
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        if LanguageSystem == 'ru_RU':
            self.Label2.configure(text='''Обработано ссылок:''')
        else:
            self.Label2.configure(text='''Processed links:''')

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.091, rely=0.474, height=19, width=114
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        if LanguageSystem == 'ru_RU':
            self.Label3.configure(text='''Добавлено в карту:''')
        else:
            self.Label3.configure(text='''Added to sitemap:''')

        self.lObnStr = tk.Label(self.Labelframe1)
        self.lObnStr.place(relx=0.682, rely=0.237, height=19, width=34
                , bordermode='ignore')
        self.lObnStr.configure(activebackground="#f9f9f9")
        self.lObnStr.configure(activeforeground="black")
        self.lObnStr.configure(background="#d9d9d9")
        self.lObnStr.configure(disabledforeground="#a3a3a3")
        self.lObnStr.configure(foreground="#000000")
        self.lObnStr.configure(highlightbackground="#d9d9d9")
        self.lObnStr.configure(highlightcolor="black")
        self.lObnStr.configure(text='''0''')

        self.lDobMap = tk.Label(self.Labelframe1)
        self.lDobMap.place(relx=0.682, rely=0.474, height=19, width=34
                , bordermode='ignore')
        self.lDobMap.configure(activebackground="#f9f9f9")
        self.lDobMap.configure(activeforeground="black")
        self.lDobMap.configure(background="#d9d9d9")
        self.lDobMap.configure(disabledforeground="#a3a3a3")
        self.lDobMap.configure(foreground="#000000")
        self.lDobMap.configure(highlightbackground="#d9d9d9")
        self.lDobMap.configure(highlightcolor="black")
        self.lDobMap.configure(text='''0''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.182, relheight=0.811, relwidth=1.008)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Scrolledtext1 = ScrolledText(self.Frame2)
        self.Scrolledtext1.place(relx=0.0, rely=0.0, relheight=0.997
                , relwidth=0.997)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="blue")
        self.Scrolledtext1.configure(selectforeground="white")
        self.Scrolledtext1.configure(wrap="none")

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

def StartApp():
    global top, root
    provar = IntVar()
    provar.set(0)
    spisok = []
    ignore = ['.jpg', '.png', '/user?id=', 'login', 'logout', 'redirect.php',
              '.exe', '.zip', '.msi',
              '.JPG', '.PNG', 'comment-', 'component', 'users', '.tar.bz2']
    #top.Scrolledtext1.insert(1.0, 'https://www.mrkaban.ru/')
    top.Entry1.insert(0, 'https://www.mrkaban.ru/')

    # top.configure(title="Идёт поиск веб-страниц")
    def ClickedStart():
        if LanguageSystem == 'ru_RU':
            root.title("Идёт поиск веб-страниц...")
        else:
            root.title("The web pages are being searched...")

        # global s1
        # Веб-сайт начиная с http:// или https://
        start_url = top.Entry1.get()
        # Домен с www или без
        domain = start_url
        # domain = root.leDomain.text()
        domain = domain.replace('http://', '')
        domain = domain.replace('https://', '')
        domain = domain.replace('/', '')
        # root.leDomain.setText(domain)
        # root.textBrowser.setText('Поиск начат...')

        # начинаем парсить роботс
        rp = urllib.robotparser.RobotFileParser()
        d = start_url + "robots.txt"
        rp.set_url(d)
        rp.read()
        rrate = rp.request_rate("*")
        rp.crawl_delay("*")

        # Путь к карте сайта в системе
        # sitemap_path = root.lePath.text()
        sitemap_path = 'sitemap.xml'
        # Частота изменения
        # frequency = 'Daily'
        # Приоритет
        # priority = 'None'
        # Список игнорируемых страниц
        # ignore1 = [str(root.lwIgnore.item(i).text()) for i in
        #            range(root.lwIgnore.count())]
        ignore1 = ignore
        # root.tableView.clear()
        # Список посещенных ссылок, чтобы игнорировать их позже
        visted_links = []
        # Открыть файл для записи
        sitemap_file = open(sitemap_path, "w", encoding='utf8')

        # s1 = ''
        global cifra
        cifra = 0
        global cifra2
        cifra2 = 0
        def download(url):
            global cifra
            cifra += 1
            top.lObnStr.configure(text=str(cifra))
            top.lObnStr.update()
            if not url in visted_links:
                visted_links.append(url)
                # print("[", str(datetime.now().time()), "] Crawling : ", url)
                sitemap_file.write('<url>\n')
                try:
                    if s == '':
                        s = url + '\n'
                    else:
                        s = s + url + '\n'
                except:
                    s = url + '\n'
                spisok.append(url)
                # print(s)
                sitemap_file.write('<loc>' + url + '</loc>\n')

                ### Из спкрипта для сайта
                # беру дату со страницы
                request1 = requests.get(url, allow_redirects=False)
                k = request1.text
                k = k.replace(' января ', '.01.')
                k = k.replace(' февраля ', '.02.')
                k = k.replace(' марта ', '.03.')
                k = k.replace(' апреля ', '.04.')
                k = k.replace(' мая ', '.05.')
                k = k.replace(' июня ', '.06.')
                k = k.replace(' июля ', '.07.')
                k = k.replace(' августа ', '.08.')
                k = k.replace(' сентября ', '.09.')
                k = k.replace(' октября ', '.10.')
                k = k.replace(' ноября ', '.11.')
                k = k.replace(' декабря ', '.12.')
                k = k.replace(' Jan ', '.01.') 
                k = k.replace(' Feb ', '.02.') 
                k = k.replace(' Mar ', '.03.') 
                k = k.replace(' APR ', '.04.') 
                k = k.replace(' may ', '.05.') 
                k = k.replace(' Jun ', '.06.') 
                k = k.replace(' Jul ', '.07.') 
                k = k.replace(' Aug ', '.08.') 
                k = k.replace(' Sep ', '.09.') 
                k = k.replace(' Oct ', '.10.') 
                k = k.replace(' Nov ', '.11.') 
                k = k.replace(' Dec ', '.12.')
                
                k = k.replace(' January ', '.01.') 
                k = k.replace(' February ', '.02.') 
                k = k.replace(' March  ', '.03.') 
                k = k.replace(' April ', '.04.') 
                k = k.replace(' May ', '.05.') 
                k = k.replace(' June  ', '.06.') 
                k = k.replace(' July ', '.07.') 
                k = k.replace(' August ', '.08.') 
                k = k.replace(' September ', '.09.') 
                k = k.replace(' October ', '.10.') 
                k = k.replace(' November ', '.11.') 
                k = k.replace(' December ', '.12.')
                g = re.search(r'([Обновлено: ]|[Опубликовано: ]|[Создано: ])+\d{2}[.]+\d{2}[.]+\d{4}', k)
                g = re.search(r'([Updated: ]|[Published: ]|[Created: ])+\d{2}[.]+\d{2}[.]+\d{4}', k)
                
                # g = re.search(r'[Обновлено: ]+\d{2}[.]+\d{2}[.]+\d{4}', k)

                if g is None:
                    pass
                else:
                    j = g.group()
                    j = j.replace('.', '-')
                    j = j.replace('Обновлено: ', '')
                    j = j.replace('Опубликовано: ', '')
                    j = j.replace('Создано: ', '')
                    j = j.replace('Updated: ', '')
                    j = j.replace('Published: ', '')
                    j = j.replace('Created: ', '')
                    j = j.replace(' ', '')
                    sitemap_file.write('<lastmod>' + j + '</lastmod>\n')

                # пробую заполнить приоритет
                h1 = re.findall('/', url)
                if len(h1) <= 3:
                    sitemap_file.write('<priority>' + '1.0' + '</priority>\n')
                    sitemap_file.write(
                        '<changefreq>' + 'Daily' + '</changefreq>\n')
                elif 'post' in url:
                    sitemap_file.write('<priority>' + '0.5' + '</priority>\n')
                    sitemap_file.write(
                        '<changefreq>' + 'monthly' + '</changefreq>\n')
                elif len(h1) >= 5:
                    sitemap_file.write('<priority>' + '0.5' + '</priority>\n')
                    sitemap_file.write(
                        '<changefreq>' + 'monthly' + '</changefreq>\n')
                else:
                    sitemap_file.write('<priority>' + '0.9' + '</priority>\n')
                    sitemap_file.write(
                        '<changefreq>' + 'Daily' + '</changefreq>\n')

                # s = s + '<loc>'+url+'</loc>\n'
                # sitemap_file.write('<changefreq>' + frequency + '</changefreq>\n')
                # s = s + '<changefreq>'+frequency+'</changefreq>\n'
                # sitemap_file.write('<priority>' + priority + '</priority>\n')
                # s = s + '<priority>'+priority+'</priority>\n'
                sitemap_file.write('</url>\n')
                # s = s + '</url>\n'
                request = requests.get(url, allow_redirects=False)
                content = html.fromstring(bytes(request.text, encoding='utf8'))
                # content = html.fromstring(request.text)
                links = content.xpath('//a/@href')
                links = filter(links)
                # root.textBrowser.setText(s)
                # TextChange(s)
                # f1 = tpe.submit(TextChange, s)
                for link in links:
                    if not link in visted_links:
                        for url in link:
                            if rp.can_fetch("*", url):
                                pass
                            else:
                                continue
                            try:
                                download(url)
                                h = url + '\n'
                                top.Scrolledtext1.insert(1.0, h)
                                root.update()
                                root.after(25, provar.set(25))
                                top.Scrolledtext1.update()
                                # root.after(2000, provar.set(45))
                                top.Scrolledtext1.update()
                                global cifra2
                                cifra2 += 1
                                top.lDobMap.configure(text=str(cifra2))
                                top.lDobMap.update()
                            except:
                                continue
            # h = url + '\n'
            # text.insert(1.0, h)
            # root.update()
            # root.after(500, provar.set(25))
            # text.update()
            # #root.after(2000, provar.set(45))
            # text.update()
            return s

        def filter(urls):
            links = []
            urls = map(lambda s: urljoin(start_url, s), urls)
            for url in urls:
                ignore_flag = False
                for word in ignore1:
                    if word in url:
                        ignore_flag = True
                if domain == urlparse(
                        url).hostname and ignore_flag is False and not url in visted_links:
                    links.extend([url])
            yield links

        # Заголовок карты сайта
        sitemap_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        sitemap_file.write(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        # запуск функции сбора урлов
        s2 = download(start_url)
        # f = tpe.submit(download, start_url)
        # Нижняя часть файла
        sitemap_file.write('</urlset>')
        sitemap_file.close()
        return s2

    def startButton():
        # text.insert(1.0, 'Поиск начат...')
        # s = ClickedStart()
        # f = concurrent.futures.wait(f1, timeout=60, return_when='ALL_COMPLETED')
        # f = tpe.submit(ClickedStart)
        # f.wait(f1)
        # s1 = f.result()
        s1 = ClickedStart()
        sk = ''
        for u in spisok:
            sk = sk + u + '\n'
        # print('список: ', sk)
        # global s1
        # root.textBrowser.setText(sk)
        # text.insert(1.0, sk)
        # tpe.shutdown()
        if LanguageSystem == 'ru_RU':
            root.title("Карта сайта создана - XmlSitemapGenerator от КонтинентСвободы.рф")
            messagebox.showinfo("Карта сайта создана",
                             "Карта сайта создана и сохранена в директории с "
                             "программой.")
        else:
            root.title("Site map created - Xml Sitemap Generator")
            messagebox.showinfo("Site map created",
            "Site map created and saved in the directory with the program.")
        



    # top.Entry1.bind('<Return>', startButton)
    top.Button1.configure(command=startButton)
    #btnPoisk = Button(frame, text="Поиск", command=startButton)
    #btnPoisk.pack(side=LEFT, expand=True)
    root.update()

if __name__ == '__main__':
    vp_start_gui()






