from pypresence import Presence
from time import time
import config

RPC = Presence(config.settings[app_id])
btns = [
	{
		"label": "Discord",
		"url": "https://discord.com"
	},
	{
		"label": "YouTube",
		"url": "https://youtube.com"
	}
]

RPC.connect()
RPC.update(
	state=config.settings[state],
	details=config.settings[det],
	start=time(),
	buttons=btns,
	large_image=config.settings[large_image],
	small_image=config.settings[small_image],
	large_text=config.settings[text1],
	small_text=config.settings[text2]
)

input() # Чтобы программа резко не закрывалась.
