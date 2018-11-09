# saannd 

### Dependencies
```bash
$ pip install pyinstaller
$ wget https://raw.githubusercontent.com/aniruddha0pandey/dotfiles/master/.scripts/ydaami.c
```
### Build
```bash
$ ./buildapp.sh                      # build application
$ ./ydaami -rm! saannd/ README.md # (optional) build project-structure markdown
$ # tree >> README.md # (otherwise)
```
### Rebuild / Clean
```bash
$ ./cleanapp.sh
```  
<sub><code>chmod u+x</code> to access build scripts as executables and <code>make</code> for making <code>ydaami</code> binaries.</sub>
  
### File Structure
```
saannd/
├── build/
│   └── setup/
├── buildApp.sh
├── cleanApp.sh
├── dist/
│   └── setup/
|       └── ./setup
├── .gitignore
├── logs/
│   └── day:month:year-hour:min:sec.log
├── packages/
│   └── menuBar/
├── __pycache__/
│   └── setup.cpython-37.pyc
├── README.md
├── setup.py
├── setup.spec
└── TODOs
```

```
.
├── build
│   └── setup
│       ├── Analysis-00.toc
│       ├── base_library.zip
│       ├── COLLECT-00.toc
│       ├── EXE-00.toc
│       ├── PKG-00.pkg
│       ├── PKG-00.toc
│       ├── PYZ-00.pyz
│       ├── PYZ-00.toc
│       ├── setup
│       ├── Tree-00.toc
│       ├── Tree-01.toc
│       ├── warn-setup.txt
│       └── xref-setup.html
├── buildapp.sh
├── cleanapp.sh
├── dist
│   └── setup
│       ├── base_library.zip
│       ├── binascii.cpython-37m-x86_64-linux-gnu.so
│       ├── _bisect.cpython-37m-x86_64-linux-gnu.so
│       ├── _blake2.cpython-37m-x86_64-linux-gnu.so
│       ├── _bz2.cpython-37m-x86_64-linux-gnu.so
│       ├── _codecs_cn.cpython-37m-x86_64-linux-gnu.so
│       ├── _codecs_hk.cpython-37m-x86_64-linux-gnu.so
│       ├── _codecs_iso2022.cpython-37m-x86_64-linux-gnu.so
│       ├── _codecs_jp.cpython-37m-x86_64-linux-gnu.so
│       ├── _codecs_kr.cpython-37m-x86_64-linux-gnu.so
│       ├── _codecs_tw.cpython-37m-x86_64-linux-gnu.so
│       ├── _datetime.cpython-37m-x86_64-linux-gnu.so
│       ├── grp.cpython-37m-x86_64-linux-gnu.so
│       ├── _hashlib.cpython-37m-x86_64-linux-gnu.so
│       ├── _heapq.cpython-37m-x86_64-linux-gnu.so
│       ├── ld-linux-x86-64.so.2
│       ├── libcrypto.so.1.0.0
│       ├── liblzma.so.5
│       ├── libpython3.7m.so.1.0
│       ├── libreadline.so.7
│       ├── libssl.so.1.0.0
│       ├── libtcl8.6.so
│       ├── libtinfow.so.6
│       ├── libtk8.6.so
│       ├── libX11.so.6
│       ├── libXau.so.6
│       ├── libXdmcp.so.6
│       ├── libz.so.1
│       ├── _lzma.cpython-37m-x86_64-linux-gnu.so
│       ├── math.cpython-37m-x86_64-linux-gnu.so
│       ├── _md5.cpython-37m-x86_64-linux-gnu.so
│       ├── _multibytecodec.cpython-37m-x86_64-linux-gnu.so
│       ├── _opcode.cpython-37m-x86_64-linux-gnu.so
│       ├── _pickle.cpython-37m-x86_64-linux-gnu.so
│       ├── _posixsubprocess.cpython-37m-x86_64-linux-gnu.so
│       ├── pyexpat.cpython-37m-x86_64-linux-gnu.so
│       ├── _random.cpython-37m-x86_64-linux-gnu.so
│       ├── readline.cpython-37m-x86_64-linux-gnu.so
│       ├── resource.cpython-37m-x86_64-linux-gnu.so
│       ├── select.cpython-37m-x86_64-linux-gnu.so
│       ├── setup
│       ├── _sha1.cpython-37m-x86_64-linux-gnu.so
│       ├── _sha256.cpython-37m-x86_64-linux-gnu.so
│       ├── _sha3.cpython-37m-x86_64-linux-gnu.so
│       ├── _sha512.cpython-37m-x86_64-linux-gnu.so
│       ├── _socket.cpython-37m-x86_64-linux-gnu.so
│       ├── _ssl.cpython-37m-x86_64-linux-gnu.so
│       ├── _struct
│       │   └── cpython-37m-x86_64-linux-gnu
│       │       └── sotruct.cpython-37m-x86_64-linux-gnu.so
│       ├── _struct.cpython-37m-x86_64-linux-gnu.so
│       ├── tcl
│       │   ├── auto.tcl
│       │   ├── clock.tcl
│       │   ├── encoding
│       │   │   ├── ascii.enc
│       │   │   ├── big5.enc
│       │   │   ├── cp1250.enc
│       │   │   ├── cp1251.enc
│       │   │   ├── cp1252.enc
│       │   │   ├── cp1253.enc
│       │   │   ├── cp1254.enc
│       │   │   ├── cp1255.enc
│       │   │   ├── cp1256.enc
│       │   │   ├── cp1257.enc
│       │   │   ├── cp1258.enc
│       │   │   ├── cp437.enc
│       │   │   ├── cp737.enc
│       │   │   ├── cp775.enc
│       │   │   ├── cp850.enc
│       │   │   ├── cp852.enc
│       │   │   ├── cp855.enc
│       │   │   ├── cp857.enc
│       │   │   ├── cp860.enc
│       │   │   ├── cp861.enc
│       │   │   ├── cp862.enc
│       │   │   ├── cp863.enc
│       │   │   ├── cp864.enc
│       │   │   ├── cp865.enc
│       │   │   ├── cp866.enc
│       │   │   ├── cp869.enc
│       │   │   ├── cp874.enc
│       │   │   ├── cp932.enc
│       │   │   ├── cp936.enc
│       │   │   ├── cp949.enc
│       │   │   ├── cp950.enc
│       │   │   ├── dingbats.enc
│       │   │   ├── ebcdic.enc
│       │   │   ├── euc-cn.enc
│       │   │   ├── euc-jp.enc
│       │   │   ├── euc-kr.enc
│       │   │   ├── gb12345.enc
│       │   │   ├── gb1988.enc
│       │   │   ├── gb2312.enc
│       │   │   ├── gb2312-raw.enc
│       │   │   ├── iso2022.enc
│       │   │   ├── iso2022-jp.enc
│       │   │   ├── iso2022-kr.enc
│       │   │   ├── iso8859-10.enc
│       │   │   ├── iso8859-13.enc
│       │   │   ├── iso8859-14.enc
│       │   │   ├── iso8859-15.enc
│       │   │   ├── iso8859-16.enc
│       │   │   ├── iso8859-1.enc
│       │   │   ├── iso8859-2.enc
│       │   │   ├── iso8859-3.enc
│       │   │   ├── iso8859-4.enc
│       │   │   ├── iso8859-5.enc
│       │   │   ├── iso8859-6.enc
│       │   │   ├── iso8859-7.enc
│       │   │   ├── iso8859-8.enc
│       │   │   ├── iso8859-9.enc
│       │   │   ├── jis0201.enc
│       │   │   ├── jis0208.enc
│       │   │   ├── jis0212.enc
│       │   │   ├── koi8-r.enc
│       │   │   ├── koi8-u.enc
│       │   │   ├── ksc5601.enc
│       │   │   ├── macCentEuro.enc
│       │   │   ├── macCroatian.enc
│       │   │   ├── macCyrillic.enc
│       │   │   ├── macDingbats.enc
│       │   │   ├── macGreek.enc
│       │   │   ├── macIceland.enc
│       │   │   ├── macJapan.enc
│       │   │   ├── macRoman.enc
│       │   │   ├── macRomania.enc
│       │   │   ├── macThai.enc
│       │   │   ├── macTurkish.enc
│       │   │   ├── macUkraine.enc
│       │   │   ├── shiftjis.enc
│       │   │   ├── symbol.enc
│       │   │   └── tis-620.enc
│       │   ├── history.tcl
│       │   ├── http1.0
│       │   │   ├── http.tcl
│       │   │   └── pkgIndex.tcl
│       │   ├── init.tcl
│       │   ├── msgs
│       │   │   ├── af.msg
│       │   │   ├── af_za.msg
│       │   │   ├── ar_in.msg
│       │   │   ├── ar_jo.msg
│       │   │   ├── ar_lb.msg
│       │   │   ├── ar.msg
│       │   │   ├── ar_sy.msg
│       │   │   ├── be.msg
│       │   │   ├── bg.msg
│       │   │   ├── bn_in.msg
│       │   │   ├── bn.msg
│       │   │   ├── ca.msg
│       │   │   ├── cs.msg
│       │   │   ├── da.msg
│       │   │   ├── de_at.msg
│       │   │   ├── de_be.msg
│       │   │   ├── de.msg
│       │   │   ├── el.msg
│       │   │   ├── en_au.msg
│       │   │   ├── en_be.msg
│       │   │   ├── en_bw.msg
│       │   │   ├── en_ca.msg
│       │   │   ├── en_gb.msg
│       │   │   ├── en_hk.msg
│       │   │   ├── en_ie.msg
│       │   │   ├── en_in.msg
│       │   │   ├── en_nz.msg
│       │   │   ├── en_ph.msg
│       │   │   ├── en_sg.msg
│       │   │   ├── en_za.msg
│       │   │   ├── en_zw.msg
│       │   │   ├── eo.msg
│       │   │   ├── es_ar.msg
│       │   │   ├── es_bo.msg
│       │   │   ├── es_cl.msg
│       │   │   ├── es_co.msg
│       │   │   ├── es_cr.msg
│       │   │   ├── es_do.msg
│       │   │   ├── es_ec.msg
│       │   │   ├── es_gt.msg
│       │   │   ├── es_hn.msg
│       │   │   ├── es.msg
│       │   │   ├── es_mx.msg
│       │   │   ├── es_ni.msg
│       │   │   ├── es_pa.msg
│       │   │   ├── es_pe.msg
│       │   │   ├── es_pr.msg
│       │   │   ├── es_py.msg
│       │   │   ├── es_sv.msg
│       │   │   ├── es_uy.msg
│       │   │   ├── es_ve.msg
│       │   │   ├── et.msg
│       │   │   ├── eu_es.msg
│       │   │   ├── eu.msg
│       │   │   ├── fa_in.msg
│       │   │   ├── fa_ir.msg
│       │   │   ├── fa.msg
│       │   │   ├── fi.msg
│       │   │   ├── fo_fo.msg
│       │   │   ├── fo.msg
│       │   │   ├── fr_be.msg
│       │   │   ├── fr_ca.msg
│       │   │   ├── fr_ch.msg
│       │   │   ├── fr.msg
│       │   │   ├── ga_ie.msg
│       │   │   ├── ga.msg
│       │   │   ├── gl_es.msg
│       │   │   ├── gl.msg
│       │   │   ├── gv_gb.msg
│       │   │   ├── gv.msg
│       │   │   ├── he.msg
│       │   │   ├── hi_in.msg
│       │   │   ├── hi.msg
│       │   │   ├── hr.msg
│       │   │   ├── hu.msg
│       │   │   ├── id_id.msg
│       │   │   ├── id.msg
│       │   │   ├── is.msg
│       │   │   ├── it_ch.msg
│       │   │   ├── it.msg
│       │   │   ├── ja.msg
│       │   │   ├── kl_gl.msg
│       │   │   ├── kl.msg
│       │   │   ├── kok_in.msg
│       │   │   ├── kok.msg
│       │   │   ├── ko_kr.msg
│       │   │   ├── ko.msg
│       │   │   ├── kw_gb.msg
│       │   │   ├── kw.msg
│       │   │   ├── lt.msg
│       │   │   ├── lv.msg
│       │   │   ├── mk.msg
│       │   │   ├── mr_in.msg
│       │   │   ├── mr.msg
│       │   │   ├── ms.msg
│       │   │   ├── ms_my.msg
│       │   │   ├── mt.msg
│       │   │   ├── nb.msg
│       │   │   ├── nl_be.msg
│       │   │   ├── nl.msg
│       │   │   ├── nn.msg
│       │   │   ├── pl.msg
│       │   │   ├── pt_br.msg
│       │   │   ├── pt.msg
│       │   │   ├── ro.msg
│       │   │   ├── ru.msg
│       │   │   ├── ru_ua.msg
│       │   │   ├── sh.msg
│       │   │   ├── sk.msg
│       │   │   ├── sl.msg
│       │   │   ├── sq.msg
│       │   │   ├── sr.msg
│       │   │   ├── sv.msg
│       │   │   ├── sw.msg
│       │   │   ├── ta_in.msg
│       │   │   ├── ta.msg
│       │   │   ├── te_in.msg
│       │   │   ├── te.msg
│       │   │   ├── th.msg
│       │   │   ├── tr.msg
│       │   │   ├── uk.msg
│       │   │   ├── vi.msg
│       │   │   ├── zh_cn.msg
│       │   │   ├── zh_hk.msg
│       │   │   ├── zh.msg
│       │   │   ├── zh_sg.msg
│       │   │   └── zh_tw.msg
│       │   ├── opt0.4
│       │   │   ├── optparse.tcl
│       │   │   └── pkgIndex.tcl
│       │   ├── package.tcl
│       │   ├── parray.tcl
│       │   ├── safe.tcl
│       │   ├── tclAppInit.c
│       │   ├── tclIndex
│       │   ├── tm.tcl
│       │   └── word.tcl
│       ├── termios.cpython-37m-x86_64-linux-gnu.so
│       ├── tk
│       │   ├── bgerror.tcl
│       │   ├── button.tcl
│       │   ├── choosedir.tcl
│       │   ├── clrpick.tcl
│       │   ├── comdlg.tcl
│       │   ├── console.tcl
│       │   ├── dialog.tcl
│       │   ├── entry.tcl
│       │   ├── focus.tcl
│       │   ├── fontchooser.tcl
│       │   ├── iconlist.tcl
│       │   ├── icons.tcl
│       │   ├── images
│       │   │   ├── logo100.gif
│       │   │   ├── logo64.gif
│       │   │   ├── logo.eps
│       │   │   ├── logoLarge.gif
│       │   │   ├── logoMed.gif
│       │   │   ├── pwrdLogo100.gif
│       │   │   ├── pwrdLogo150.gif
│       │   │   ├── pwrdLogo175.gif
│       │   │   ├── pwrdLogo200.gif
│       │   │   ├── pwrdLogo75.gif
│       │   │   ├── pwrdLogo.eps
│       │   │   ├── README
│       │   │   └── tai-ku.gif
│       │   ├── listbox.tcl
│       │   ├── megawidget.tcl
│       │   ├── menu.tcl
│       │   ├── mkpsenc.tcl
│       │   ├── msgbox.tcl
│       │   ├── msgs
│       │   │   ├── cs.msg
│       │   │   ├── da.msg
│       │   │   ├── de.msg
│       │   │   ├── el.msg
│       │   │   ├── en_gb.msg
│       │   │   ├── en.msg
│       │   │   ├── eo.msg
│       │   │   ├── es.msg
│       │   │   ├── fr.msg
│       │   │   ├── hu.msg
│       │   │   ├── it.msg
│       │   │   ├── nl.msg
│       │   │   ├── pl.msg
│       │   │   ├── pt.msg
│       │   │   ├── ru.msg
│       │   │   └── sv.msg
│       │   ├── obsolete.tcl
│       │   ├── optMenu.tcl
│       │   ├── palette.tcl
│       │   ├── panedwindow.tcl
│       │   ├── pkgIndex.tcl
│       │   ├── safetk.tcl
│       │   ├── scale.tcl
│       │   ├── scrlbar.tcl
│       │   ├── spinbox.tcl
│       │   ├── tclIndex
│       │   ├── tearoff.tcl
│       │   ├── text.tcl
│       │   ├── tkAppInit.c
│       │   ├── tkfbox.tcl
│       │   ├── tk.tcl
│       │   ├── ttk
│       │   │   ├── altTheme.tcl
│       │   │   ├── aquaTheme.tcl
│       │   │   ├── button.tcl
│       │   │   ├── clamTheme.tcl
│       │   │   ├── classicTheme.tcl
│       │   │   ├── combobox.tcl
│       │   │   ├── cursors.tcl
│       │   │   ├── defaults.tcl
│       │   │   ├── entry.tcl
│       │   │   ├── fonts.tcl
│       │   │   ├── menubutton.tcl
│       │   │   ├── notebook.tcl
│       │   │   ├── panedwindow.tcl
│       │   │   ├── progress.tcl
│       │   │   ├── scale.tcl
│       │   │   ├── scrollbar.tcl
│       │   │   ├── sizegrip.tcl
│       │   │   ├── spinbox.tcl
│       │   │   ├── treeview.tcl
│       │   │   ├── ttk.tcl
│       │   │   ├── utils.tcl
│       │   │   ├── vistaTheme.tcl
│       │   │   ├── winTheme.tcl
│       │   │   └── xpTheme.tcl
│       │   ├── unsupported.tcl
│       │   └── xmfbox.tcl
│       ├── _tkinter.cpython-37m-x86_64-linux-gnu.so
│       ├── unicodedata.cpython-37m-x86_64-linux-gnu.so
│       ├── zlib
│       │   └── cpython-37m-x86_64-linux-gnu
│       │       └── soib.cpython-37m-x86_64-linux-gnu.so
│       └── zlib.cpython-37m-x86_64-linux-gnu.so
├── logs
│   ├── 08:11:2018-19:57:13.log
│   ├── 08:11:2018-19:57:39.log
│   ├── 08:11:2018-19:58:43.log
│   ├── 08:11:2018-19:59:01.log
│   ├── 08-11-2018@20-03-06.log
│   ├── 08-11-2018@20-06-48.log
│   ├── 08-11-2018@20-10-40.log
│   ├── 09-11-2018@22-51-00.log
│   ├── 25:10:2018-20:02:32.log
│   └── 25:10:2018-20:16:31.log
├── packages
│   ├── __init__.py
│   ├── menuBar.py
│   └── __pycache__
│       ├── __init__.cpython-37.pyc
│       └── menuBar.cpython-37.pyc
├── __pycache__
│   └── setup.cpython-37.pyc
├── README.md
├── saanndPresentation.pptx
├── setup.py
├── setup.spec
└── TODOs

21 directories, 397 files

```
