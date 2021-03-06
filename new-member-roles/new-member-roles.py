import discord
import typing
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class NewMemberRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="newmember", aliases=["nmr"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def newmember(self, ctx):
        member = ctx.guild.get_member(ctx.thread.recipient.id)
        pend = ctx.guild.get_role(324658636574162945)
        nego = ctx.guild.get_role(732405243299495968)
        madrid = ctx.guild.get_role(305440616354152450)
        await member.add_roles(nego, madrid)
        await member.remove_roles(pend)
        
        await ctx.send("This member has been successfully approved!")
        
        config = await self.db.find_one({"_id": "config"})

def setup(bot):
    bot.add_cog(NewMemberRoles(bot))
