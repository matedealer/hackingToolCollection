from collections import OrderedDict
import hashlib
import CSAW_15_crypto50_whiter0ser
import binascii

trans_table = str.maketrans(dict(C="E",
                                 Z="T",
                                 E="A",
                                 W="W"))


file="/home/joti/Dokumente/hacking/hDa_CTF/CSAW_2015/crypto_whiter0se/eps1.7_wh1ter0se_2b007cf0ba9881d954e85eb475d0d5e4.m4v"
chiper = "IWC ECTCC OPK WNQV SI AKGBRU TVZZ EAH JIZ ENEG CFY BMZ"

#chiper = open(file, "r").read()

md5 = hashlib.md5()
#print(chiper)
#cipher="SaWr IrasgZalt \n B hust ZasgdlaZ W Ymmj jmdm bmr tfa Lwgss cyXar Ltmrk RssmYgWtgml. IjaWsa bglZ gt WttWYfaZ tm tfgs akWgj.\n B alYryntaZ gt wgtf RpL usgld W 128-Xgt iay dalarWtaZ usgld tfa rWlZ() bulYtgml mb tfa c stWlZWrZ jgXrWry. \n Gmta tfWt B YmkngjaZ tfa iay tmZWy Wt 12:00Wk.\n\nBl WZZgtgml tm tfgs jmdm, B WZZaZ Wl WrtgYja WXmut Wl gltarastgld Yryntm-Wjdmrgtfk.\nAmwavar, gl mrZar tm raWZ tfa WrtgYja (gt gs WnnrmxgkWtajy 3500 YfWrWYtars jmld), ymu laaZ \n tm ravarsa wfWt B ZgZ tm fgZa gt's Ymltalt brmk ymu. B dgva ymu W fglt: Umu'jj laaZ tfa fajn mb W bWkmus rmkWl aknarmr. cfaars, RjgYa"


cleartext = (chiper.translate(trans_table)).upper()
print(cleartext)
md5.update(cleartext.encode("utf8"))

print(md5.hexdigest())