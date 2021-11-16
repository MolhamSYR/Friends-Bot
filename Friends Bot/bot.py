import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, MissingPermissions
import os


TOKEN = "EXAMPLE TOKEN"

client = commands.Bot(command_prefix = '>')


@client.event
async def on_ready():
    print("The Bot Is Running And Being Used!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(">help"))




@client.command()
async def setrules(ctx,*,RuleMessage):
    ctx.send("**Rules Has Been Updated!**")

RuleMessage="Start Making a New Rule Page By >setrules \"Your Rules\""

@client.command(aliases=["rl"])
async def rules(ctx):
    await ctx.send(RuleMessage)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! The Ping Of The Bot is {round(client.latency * 1000)}ms")


@client.command(aliases =["8ball","8b"])
async def _8ball(ctx,*, question):
    respones = ["Yeah It Is Certain", "It is decidedly so.", "Without a doubt", "Yes, Definitely.", "You May Rely On It", "As I See It.. Yes.", "Most Likely", "Outlook Good.", "Yes.", "signs point to yes..", "Reply hazy, try again.", "Ask Again Later.", "Better not tell you now.", "Cannot predict now.","Dont count on it.", "My reply is no", "My Sources say no","Outlook not so good", "very doubtful", "probably not..", "No."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(respones)}")


@commands.has_permissions(manage_messages=True)
@client.command(aliases = ["c"])
async def clear(ctx, amount=5):
    await ctx.send(f"**Deleted {amount} Messages!**")
    await ctx.channel.purge(limit=amount + 2)

@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f"{member.mention} has been Kicked :airplane:! Reason: {reason}")
    await member.kick(reason=reason)


@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):

       await ctx.send(f"{member.mention} **has been Banned** :airplane:! **Reason**: **{reason}**")
       await member.ban(reason=reason)

@client.command(aliases=["lr"])
async def loverate(ctx,*, Lover):
    LOVE_RATE = random.randrange(0, 101)
    await ctx.send(f"**Person:** " + Lover + "\n**Love Rate:** " + LOVE_RATE + "%")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_disc):
            await ctx.send(f"**Unbanned {user.mention}**")
            await ctx.guild.unban(user)
            return
        else:
            ctx.send("**User Is Not Banned!**")




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")



client.run(TOKEN)

