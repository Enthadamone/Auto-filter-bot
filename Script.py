class script(object):
    START_TXT = """<b>Hi π {},</b>
<b>My Name is <a href='https://t.me/filterbetterbot'>Samantha</a>, \nπΈ can provide movies in your Group, \nJust add me to your group and i will do my work π.....</b>"""
    HELP_TXT = """Hei π³ {}
<b>Here is the help for my COMMANDs.</b>"""
    ABOUT_TXT = """β― <b>My Name: Samantha </b>
β― <b>Creator: <a href='https://t.me/rahulp_r'>This Person</a> </b> 
β― <b>Library: Pyrogram</b>
β― <b>Language: Python 3</b>
β― <b>Data Base: MONGO DB</b>
β― <b>Server: HEROKU</b>
β― <b>Build Status: v1.7.0 [BETA]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>- Last Updated on 11-08-2022 at 8.00pm [IST]. </b>
<b>- Join @CP_Archivedmovies to be updated with me. </b>
<b>- Support files More than 2GB π³</b>
<b>- Now you can request movie in my pm tooπ..</b>
<b>- Updated pyrogram π</b>
<b>- Thankz to @rahulp_r for maintaining me.</b>
<b>- I can only work in @cinemapedikagroup and @cinemapedika, If u want to add me to your group contact my master. </b>
<b>- My Best Friend : <a href='tg://settings'>This Person</a> </b> π"""
    MANUELFILTER_TXT = """HELP: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and I will respond whenever a keyword is found in the message.... 

<b>NOTE:</b>
1. In order to work I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """HELP: <b>Buttons</b>

- Iam Supportable to both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Samantha supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format. 

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/CP_Archivedmovies)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:Type Your Alert Message)</code>"""
    AUTOFILTER_TXT = """HELP: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db π."""
    CONNECTION_TXT = """HELP: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """HELP: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Me. 

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """HELP : <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins π. 

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
π Group = {}(<code>{}</code>)
π¨βπ§βπ¦ Total Members = <code>{}</code>
π¨βπ§ Added By - {}
"""
    LOG_TEXT_P = """ #NEW_USER
   ID - <code>{}</code>
   Name - {}
   """

