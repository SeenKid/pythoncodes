#coding:utf-8

import discord
from discord.ext import commands
import asyncio
from discord import embeds
import random


bot = commands.Bot(command_prefix = "+", self_bot = True)
bot.remove_command('help')

@bot.event
async def on_ready():
	print("SelfBot ON !  by Sortgenji edited by SeenKid")



# EMBEDS :

@bot.command(pass_context=True)
async def help(ctx):
	channel = ctx.message.channel
	embed = discord.Embed(
		title = "Commandes du LostSelfBot",
		description = (" "),
		color = discord.Color.dark_red()

	)

	embed.set_footer(text="by Sortgenji edited by SeenKid")
	embed.set_image(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_thumbnail(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_author(name=" ")
	icon_url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640"
	embed.add_field(name="Commandes :", value="Liste des commandes : ", inline=False)
	embed.add_field(name="+help", value="Ce message.", inline=False)
	embed.add_field(name="+fun", value="Affiche la liste des commandes amusantes.", inline=False)
	embed.add_field(name="+raid", value="Affiche les commandes de raid.", inline=False)
	embed.add_field(name="+mod", value="Affiche les commandes de modération.(discord)")


	await ctx.send(embed=embed)



@bot.command(pass_context=True)
async def fun(ctx):
	channel = ctx.message.channel
	embed = discord.Embed(
		title = "Commandes fun :",
		description = (" "),
		color = discord.Color.dark_red()

	)

	embed.set_footer(text="by Sortgenji edited by SeenKid")
	embed.set_image(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_thumbnail(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_author(name=" ")
	icon_url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640"
	embed.add_field(name="+help", value="Afficher ce message.", inline=False)
	embed.add_field(name="+tg", value="Dire à quelqu'un de fermer sa gueule. \n+tg (@user)", inline=False)
	embed.add_field(name="+gpalu", value="G PA LU ! (MEME)", inline=False)
	embed.add_field(name="+sueur", value="(@user) en SUEUR !\n +sueur(@user)", inline=False)
	embed.add_field(name="+debite (@mention)", value="Pour débiter un sale clochard, et lui montrer que t'es supérieur.", inline=False)
	embed.add_field(name="+play", value="Met en statue : Joue a (message)\nPour enlever l'activité il faut fermer le selfbot.", inline=False)
	embed.add_field(name="+chut", value="Chut bagra\n +chut (@user)", inline=False)
	embed.add_field(name="+stonks", value="STONKS ! (MEME) 'o'", inline=False)
	embed.add_field(name="+tehc", value="TEHC ! (MEME)", inline=False)
	embed.add_field(name="+question", value="Poser une question.\n+question (question)", inline=False)

	await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def raid(ctx):
	channel = ctx.message.channel
	embed = discord.Embed(
		title = "Commandes de raid.",
		description = ("Liste des commandes de raid : "),
		color = discord.Color.dark_red()

	)

	embed.set_footer(text="by Sortgenji edited by SeenKid")
	embed.set_image(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_thumbnail(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_author(name=" ")
	icon_url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640"
	embed.add_field(name="+spam", value="Spam un message sans espaces. +spam (message) (nombre)", inline=False)
	embed.add_field(name="+clear", value="Clear les message. Necessite la permission de supprimer les messages. +clear (nombres)", inline=False)
	embed.add_field(name="+cchannel", value="Crée des salons textuels.\n+cchannel (nom du channel) (nombre de salons)")

	await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def mod(ctx):
	channel = ctx.message.channel
	embed = discord.Embed(
		title = "Commandes de modération.",
		description = ("Liste des commandes de modération : "),
		color = discord.Color.dark_red()

	)

	embed.set_footer(text="by Sortgenji edited by SeenKid")
	embed.set_image(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_thumbnail(url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640")
	embed.set_author(name=" ")
	icon_url="https://cdn110.picsart.com/216591336002202.gif?to=min&r=640"
	embed.add_field(name="+mute", value="Mute la personne indiquée. \nVeillez à mettre le role Muted en haut dans la liste des roles \n+mute (@user)", inline=False)
	embed.add_field(name="+unmute", value="Unmute la personne indiquée. \n+mute (@user)", inline=False)
	embed.add_field(name="+clear", value="Clear les message. Nécessite la permission de supprimer les messages. \n+clear (nombres)", inline=False)
	embed.add_field(name="+ban", value="Ban la personne indiquée. \n+ban (@user)", inline=False)
	embed.add_field(name="+kick", value="Kick la personne indiquée. \n+kick (@user)", inline=False)

	await ctx.send(embed=embed)

#COMMANDES FUN


@bot.command()
async def tg(ctx, member : discord.Member, *, reason = "Ferme ta gueule, fils."):
	await ctx.send(f"{member.mention} Couche toi et dors fils. \nhttps://tenor.com/view/ta-gueule-ferme-chut-netflix-gif-12266922")


@bot.command()
async def gpalu(ctx):
	await ctx.send("G PA LU !\nhttps://risibank.fr/cache/stickers/d532/53225-full.png")


@bot.command()
async def sueur(ctx, member : discord.Member, *, reason = "sueur"):
	await ctx.send(f"{member.mention} en sueur !\nhttps://tenor.com/view/sweating-hot-sweat-sweaty-nervous-gif-5794196")

@bot.command()
async def debite(ctx, member : discord.Member, *, reason = "debite"):
	await ctx.send(f"{member.mention} **Fils de trisomiques nés dans un gang bang gay scatophile. Ta vie est gênante, espèce de fausse couche va, t'as réssuscité. J'te mets des coups de réglisse **")


@bot.command()
async def play(ctx, message):
    await bot.change_presence(activity=discord.Game(name=(message)))

@bot.command()
async def juif(ctx, member : discord.Member, *, reason="juif"):
	await ctx.send(f"{member.mention} GET JUIFED !\n https://media.tenor.com/images/59dd129b01e520a19f31a5cc7e714dd7/tenor.gif")


@bot.command()
async def stonks(ctx):
	await ctx.send("STONKS\nhttps://i.kym-cdn.com/entries/icons/mobile/000/029/959/Screen_Shot_2019-06-05_at_1.26.32_PM.jpg")

@bot.command()
async def chut(ctx, member : discord.Member, *, reason="chut"):
	await ctx.send(f"{member.mention} Tu peux la fermer ta gueule, stp ?\nhttps://cdn.discordapp.com/attachments/724234886885671004/752122704454221844/chut_.PNG")

@bot.command()
async def blc(ctx):
		await ctx.send("https://media.makeameme.org/created/tu-vois-le-dd6969.jpg")

@bot.command()
async def pasdrole(ctx):
	await ctx.send("https://wir.skyrock.net/wir/v1/resize/?c=isi&im=%2F5645%2F91095645%2Fpics%2F3231404497_1_2_eZgV0OMe.png&w=600")

@bot.command()
async def con(ctx):
	await ctx.send("https://cdn.discordapp.com/attachments/602092721468866560/752497709071728640/mais-tes-con-ou-tu-fait-expres-.jpg")

@bot.command()
async def tehc(ctx):
	await ctx.send("https://i.kym-cdn.com/entries/icons/original/000/032/379/Screen_Shot_2020-01-09_at_2.22.56_PM.png")


@bot.command()
async def question(ctx):
	responses = ["C'est certain.",
	"Ouais.",
	"Bah non.",
	"Bah oui.",
	"Je pense que oui..",
	"Je pense que non.",
	"C'est très probable.",
	"Possiblement.",
	"N'y pense même pas.",
	"J'ai pas envie de répondre",
	"J'ai pas bien comrpis, tu peux répéter ?",
	"Je sais pas.",
	"MENFOU",
	"ok",
	"J'suis pas là, rappelle plus tard"]
	await ctx.send(f"{random.choice(responses)}")




# COMMANDES DE RAID :

@bot.command()
async def spam(ctx, message, number : int):
	for i in range (number):
		await ctx.send(message)


@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()

@bot.command()
async def cchannel(ctx, channelname, number : int):
	for i in range(number):
		guild = ctx.message.guild
		await guild.create_text_channel(channelname)



# COMMANDES DE MODÉRATION :

async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
async def mute(ctx, member : discord.Member, *, reason = "raison manquante"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} Viens de se faire mute.")

@bot.command()
async def unmute(ctx, member : discord.Member, *, reason = "raison manquante"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute.")

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)





token = ""

bot.run(token, bot = False)


