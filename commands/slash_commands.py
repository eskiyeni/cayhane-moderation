import discord
from discord.ext import commands

class slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(
        name="ban",
        description="Kullanıcıyı sunucudan yasaklar."
    )
    @commands.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        await interaction.response.defer()

        try:
            await user.ban(reason=reason)
            await interaction.followup.send(
                embed=discord.Embed(
                    title="KULLANICI YASAKLANDI!",
                    description=f"{user.mention}, {reason} sebebi ile yasaklandı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını yasaklamak için yetkim yok!",
                    color=0xFF0000
                )
            )
        except discord.HTTPException:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description="Bir hata oluştu, işlem gerçekleştirilemedi!",
                    color=0xFF0000
                )
            )

    @discord.app_commands.command(
        name="kick",
        description="Kullanıcıyı sunucudan atar."
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        await interaction.response.defer()

        try:
            await user.kick(reason=reason)
            await interaction.followup.send(
                embed=discord.Embed(
                    title="KULLANICI ATILDI!",
                    description=f"{user.mention}, {reason} sebebi ile atıldı!",
                    color=0xFF0000
                ).set_footer(text="Kurallara dikkat ediniz!")
            )
        except discord.Forbidden:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description=f"{user.mention} kullanıcısını atmak için yetkim yok!",
                    color=0xFF0000
                )
            )
        except discord.HTTPException:
            await interaction.followup.send(
                embed=discord.Embed(
                    title="HATA!",
                    description="Bir hata oluştu, işlem gerçekleştirilemedi!",
                    color=0xFF0000
                )
            )

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(slash_commands(bot))