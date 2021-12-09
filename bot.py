import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "!", description = "Bot de secret santa", case_insensitive="True")
@bot.event
async def on_ready():
    print("Your Bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Bonjour !")

@bot.command(brief="inscription pour le secret Santa",help=f"Le Krampouz viendra vous parler en privé. Répondez à ses questions.")
async def Lutin(ctx):
    await ctx.author.send("Do you like Sushi ?")

@bot.event
async def on_message(self, message):
    if message.content.startswith('$dm'):
        msg = "you called me ?"
        await message.author.send(msg)

bot.run("ODM3NjEwOTk3NjQ3NjcxMzE3.YIvEBw.tugYP9-63UNGnDAP1JExW979gWY")
