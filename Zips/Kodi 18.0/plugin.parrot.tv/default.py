import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin


def CATEGORIES():
   addDir3('SK Channels','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/SK%20Channels.txt',3,'https://i.ibb.co/2cH2kVB/SK.jpg','','')
   addDir3('CZ Channels','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/CZ%20Channels.txt',4,'https://i.ibb.co/mb6Q81H/CZ.jpg','','')
   addDir3('DE Channels','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/DE%20Channels.txt',5,'https://i.ibb.co/6W5CN1r/DE.jpg','','')
   addDir3('CA Channels','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/CA%20Channels.txt',6,'https://i.ibb.co/1b4HVfQ/CA.png','','')
   addDir3('US Channels','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/US%20Channels.txt',7,'https://i.ibb.co/N3NqB1n/US.jpg','','')
   addDir3('UK Channels','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/UK%20Channels.txt',8,'https://i.ibb.co/gmzNmJt/UK.png','','')
   addDir3('Pluto TV','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/Pluto%20TV/Pluto%20TV.txt',9,'https://i.ibb.co/kg6vQHS/Pluto-TV.png','','')   
   addDir3('The Simpsons','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/TV%20Shows/TV%20Shows/The%20Simpsons/The%20Simpsons.txt',10,'https://i.ibb.co/61cKZcf/The-Simpsons.jpg','','')
   addDir3('Futurama','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/TV%20Shows/TV%20Shows/Futurama/Futurama.txt',11,'https://i.ibb.co/SBkYJ3m/Futurama.jpg','','')
   addDir3('TV Shows','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/TV%20Shows/TV%20Shows.txt',12,'https://i.ibb.co/pdgH08k/TV-Shows.png','','')
   addDir3('Movies','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/Movies/Movies.txt',13,'https://i.ibb.co/zbt3KHp/Movies.png','','')  
   addDir3('Check For Updates','https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Updates/8.0.0/CheckForUpdate.txt',14,'https://i.ibb.co/GHdh2Pm/Check-For-Updates.png','','')


#################################################################################################################
 
#                                            Definitions 


def SK_Channels():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/SK%20Channels.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
	 
def CZ_Channels():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/CZ%20Channels.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def DE_Channels():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/DE%20Channels.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def CA_Channels():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/CA%20Channels.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def US_Channels():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/US%20Channels.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def UK_Channels():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Channels/UK%20Channels.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def Pluto_TV():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/Pluto%20TV/Pluto%20TV.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def The_Simpsons():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/TV%20Shows/TV%20Shows/The%20Simpsons/The%20Simpsons.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
        
def Futurama():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/TV%20Shows/TV%20Shows/Futurama/Futurama.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def TV_Shows():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/TV%20Shows/TV%20Shows.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
 
def Movies():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Special/Movies/Movies.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     
def Check_For_Updates():
   r = requests.get('https://raw.githubusercontent.com/ParrotDevelopers/Parrot-TV-Kodi/main/Updates/8.0.0/CheckForUpdate.txt')
   match = re.compile('name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.content)
   for name,link, logo in match:
     addLink(name,link,logo,'','')
     


	 
def addLink(name,url,image,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       
#################################################################################################################

#                               NEED BELOW CHANGED

  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
     
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
elif mode==3:
        SK_Channels()
elif mode==4:
        CZ_Channels()
elif mode==5:
        DE_Channels()
elif mode==6:
        CA_Channels()
elif mode==7:
        US_Channels()
elif mode==8:
        UK_Channels()
elif mode==9:
        Pluto_TV()
elif mode==10:
        The_Simpsons()
elif mode==11:
        Futurama()
elif mode==12:
        TV_Shows()
elif mode==13:
        Movies()
elif mode==14:
        Check_For_Updates()

        


xbmcplugin.endOfDirectory(int(sys.argv[1]))

