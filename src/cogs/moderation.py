import discord
from discord.ext import commands
import youtube_dl

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("moderation.py success")

#   Code for role on join, allow owner to set role id per server first.
#   @commands.Cog.listener()
#   async def on_member_join(self, member):
#       role = discord.utils.get(member.server.roles, id='')
#       await self.client.add_roles(member, role)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        async with ctx.typing():
            if reason == None:
                reason == "No Reason Provided."
            message = f"You have been banned from {ctx.guild.name} for {reason}"
            await member.send(message)
            await ctx.guild.ban(member, reason = reason)
            await ctx.channel.send(f'{ctx.message.author.mention} has Banned {member.mention} for {reason}')

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        async with ctx.typing():
            if reason == None:
                reason == "No Reason Provided."
            message = f"You have been kicked from {ctx.guild.name} for {reason}"
            await member.send(message)
            await ctx.guild.kick(member, reason = reason)
            await ctx.channel.send(f'{ctx.message.author.mention} has kicked {member.mention} for {reason}')
    
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, count):
             async with ctx.typing():
                await ctx.channel.purge(limit = int(count) + 1)
                await ctx.send(f"Purged {count} messages!")

    



async def setup(client):
    await client.add_cog(Moderation(client))