import discord
from discord.ext import commands

class prefix_commands(commands.Cog):
    def __init__(self, bot) ->None:
        self.bot = bot

    @commands.command(aliases=["yasakla", "uçur"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx : commands.Context, user : discord.Member, *reasion):
        reasion = " ".join(reasion)

        try:
            await user.ban(reason=reasion)
            await ctx.send(
                embed=discord.Embed(
                    title="KULLANICI YASAKLANDI!",
                    description=f"{user.mention}, {reasion} sebebi ile yasaklandı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await ctx.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını banlamak için yetkim yok!",
                    color=0xFF0000
                )
            )

    @commands.command(aliases=["at", "fırlat"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx : commands.Context, user : discord.Member, *reason):
        reason = " ".join(reason)

        try:
            await user.kick(reason=reason)
            await ctx.send(
                embed=discord.Embed(
                    title="KULLANICI ATILDI!",
                    description=f"{user.mention}, {reason} sebebi ile atıldı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await ctx.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını atmak için yetkim yok!",
                    color=0xFF0000
                )
            )

async def setup(bot : commands.Bot) ->None:
    await bot.add_cog(prefix_commands(bot))