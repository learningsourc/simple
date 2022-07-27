U
    /��bn(  �                   @   s&  d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dlm	Z	 d dl
mZ d dl
mZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl Z edd� e	d dd�Z!e!�"�  ze�#d� W n   Y nX dej$� dej$� dej$� dej$� dej$� dej$� dej$� dej$� dej%� d�Z&e'e&� ej(� d�� dZ)d d!d"d#d$d%d&d'd(d)d*d+d,d-d.d/d0d1d2d3d4d5d6gZ*ej+Z,ej-Z.ej/Z0ej1Z2d7Z3d8e,e.e0e2f Z4d@d9d:�Z5d;d<� Z6d=d>� Z7e8d?k�r"z
e7�  W n  e9k
�r    dZ)e:�  Y nX dS )A�    N)�ThreadPoolExecutor)�Display)�Fore)�init)�BeautifulSoup)�	webdriver)�By)�Keys)�ActionChains)�WebDriverWait)�expected_conditions)�Options)�TimeoutExceptionT)Z	autoreset)i   i�  )Zvisible�size�resultz      
z,         ) (       )              (        
z,   (  ( /( )\ ) ( /(   (    (     )\ )     
z,   )\ )\()|()/( )\())( )\   )\   (()/((    
z, (((_|(_)\ /(_)|(_)\ )((_|(((_)(  /(_))\   
z, )\___ ((_|_))  _((_|(_)_ )\ _ )\(_))((_)  
z,((/ __/ _ \_ _|| \| || _ )(_)_\(_) __| __| 
z, | (_| (_) | | | .` || _ \ / _ \ \__ \ _|  
zX  \___\___/___||_|\_||___//_/ \_\|___/___| 
                                           
z"                VALIDATOR CLI    
z-===========================================

FzoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.44zcMozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36zjMozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36zeMozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.11 Safari/537.36zSMozilla/5.0 (Macintosh; Intel Mac OS X 12.4; rv:102.0) Gecko/20100101 Firefox/102.0z�Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.44z~Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36/R4hVluVB-29zrMozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36z~Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Vivaldi/4.3zrMozilla/5.0 (Linux; Android 10; MI 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36ziMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.20 Safari/537.36zuMozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36zuMozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36zrMozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15ztMozilla/5.0 (Linux; Android 12; SM-X706B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36zsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.20 Safari/537.36ztMozilla/5.0 (Linux; Android 9; RMX1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36z}Mozilla/5.0 (iPad; CPU OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C114 Safari/604.1z�Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15A5341f Safari/605.1.15zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ao  
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
aP  
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["foobar.com"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
c              	   C   s�   t � }| r�d}t�|d��}|�dt� |�dt� W 5 Q R X |�|� |�ddg� |�dd� |�d	� |�d
� |�d� t	j
|d�}|S )Nzproxy_auth_plugin.zip�wzmanifest.jsonzbackground.jsZexcludeSwitcheszenable-automationZuseAutomationExtensionFzdisable-infobarszwindow-size=1280,800z---disable-blink-features=AutomationControlled)Zoptions)r   �zipfileZZipFileZwritestr�manifest_json�background_js�add_extensionZadd_experimental_option�add_argumentr   ZChrome)�	use_proxyZoptZ
pluginfileZzp�driver� r   �coinbase.py�get_chromedriver�   s    



r   c           	      C   s*  t �s&t�t�}tdd�}|�dd|i� |�d� �z~|�d� |�d� t	|d��
t�tjd	f��}|�tjd
���  |�tjd
��| � t�d� |��  z�t	|d��
t�tjdf��}t�d� |��  ttj� dtj� dtj� dtj� d| � tj� d�� tdd�}|�d� |�| � |��  |� �  W �nz   z�|�tjd�}|�d�}t|d�}|� � }d|k�r�ttj� dtj!� dtj� dtj� d| � tj� d�� tdd�}|�d� |�| � |��  |� �  nbttj� dtj"� dtj� dtj� d| � tj� d�� tdd�}|�d� |�| � |��  |� �  W nn   ttj� dtj"� dtj� dtj� d| � tj� d�� tdd�}|�d� |�| � |��  |� �  Y nX Y nX W q    ttj� dtj"� dtj� d tj� d| � tj� d�� tdd�}|�d� |�| � |��  |� �  Y q X q d S )!NT)r   zNetwork.setUserAgentOverrideZ	userAgentzEObject.defineProperty(navigator, 'webdriver', {get: () => undefined})�   zhttps://login.coinbase.com/�   z,.cds-item-izghyk0 > .cds-transparent-tlx9nbbZEmail�   �   ZPassword�   z[#]z Validz =� z ~ CB Validatorzresult/valid.txtza+�
z.cds-column-c1lezl4sZ	innerHTMLzhtml.parserz[No Coinbase account exists for this email. Please check your spelling or create an account.z Diezresult/die.txtz Captchazresult/proxy.txtz Bad Proxy �=)#�quit�randomZchoice�userr   Zexecute_cdp_cmdZexecute_scriptZimplicitly_wait�getr   Zuntil�ECZelement_to_be_clickabler   ZCSS_SELECTORZfind_elementZIDZclickZ	send_keys�time�sleep�printr   �LIGHTWHITE_EX�LIGHTCYAN_EX�LIGHTGREEN_EX�open�write�
writelines�closeZget_attributer   Zget_text�LIGHTRED_EX�LIGHTYELLOW_EX)	ZemailsZuar   �elementZpasswZtx�textZhtmlZreadyr   r   r   �login�   sp    






4





4



4


4


4


r7   c                  C   s  g } t td��}|�� �� }t|�}|D ]}| �|� q(ttd��}tdtj	� dtj
� dtj	� dtj� |� tj� �
� ttj	� dtj
� dtj	� dtj� |� tj� �	� tdtj	� dtj� d	�� t|d
��}|�t| � W 5 Q R X tdtj� dtj
� dtj� dtj
� d�	� d S )NzInput Your List: zSet Your Thread: r"   z=>z Total your list z= z Your Thread �>z Wait a second......
)Zmax_workersz

z=> zCheking Completed...!
zCheck on folder result)r/   �input�read�
splitlines�len�append�intr+   r   r,   ZLIGHTBLUE_EXZLIGHTMAGENTA_EX�RESETr4   r   �mapr7   r3   )ZemailistZmailistZlimeZtot�lineZworkZexecutorr   r   r   �main�   s    20rB   �__main__)F);�sys�osr   r)   r%   �confZconcurrent.futuresr   Zpyvirtualdisplayr   Zcoloramar   r   Zbs4r   Zseleniumr   Zselenium.webdriver.common.byr   Zselenium.webdriver.common.keysr	   Z'selenium.webdriver.common.action_chainsr
   Zselenium.webdriver.support.waitr   Zselenium.webdriver.supportr   r(   Z!selenium.webdriver.chrome.optionsr   Zselenium.common.exceptionsr   Zchromedriver_binaryZdisplay�start�mkdirr.   r-   �cbr+   r?   r$   r&   ZhostZ
PROXY_HOSTZportZ
PROXY_PORTZusernameZ
PROXY_USERZpasswordZ
PROXY_PASSr   r   r   r7   rB   �__name__�KeyboardInterrupt�exitr   r   r   r   �<module>   s�   (
��������
��
� 
>

