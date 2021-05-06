import amino
from colorama import init, Fore, Back, Style
init(autoreset=True)
print("")
print(Fore.LIGHTCYAN_EX + "??? by obee")
print("")
client = amino.Client()
email = input("Email: ")
email2 = input("Password: ")
client.login(email, email2)
(Fore.LIGHTYELLOW_EX + "Зашёл на аккаунт...")
print("")
print(Fore.LIGHTYELLOW_EX + "ваши сообщества:")
print("")
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
	print (name, id) 
print("")
wcm = input("введите айди сообщества - ")
sub_client = amino.SubClient(comId=wcm, profile=client.profile)
print("")
print(Fore.LIGHTRED_EX + "Начинаю получать чаты...")
for name, id in zip(sub_client.get_chat_threads().title, sub_client.get_chat_threads().chatId):
	print(name, id)
	print("")
	
chat = input("ChatId: ")
print(Fore.LIGHTMAGENTA_EX + "starting...")
with open("yamete.mp3", "rb") as file:
	sub_client.send_message(chatId=chat, file=file, fileType="audio")
	while True:
	    sub_client.send_message(chatId=chat, message="Im gay")
	    sub_client.edit_profile(content="♂️gay♂️")
	    print("Good spam")