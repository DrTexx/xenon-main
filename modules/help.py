import discord_worker as wkr


class Help(wkr.Module):
    @wkr.Module.command()
    async def help(self, ctx, *, command=None):
        if command is None:
            cmd = ctx.bot

        else:
            _, cmd = ctx.bot.find_command(command.split(" "))

        prefix = ctx.bot.prefix
        embed = {
            "fields": [],
            "footer": {
                "text": "Use '%shelp [command]' to get more information about a specific command." % prefix
            }
        }
        if isinstance(cmd, wkr.Command):
            embed["title"] = prefix + cmd.usage
            embed["description"] = cmd.description.format(b=ctx.bot)

        if len(cmd.commands) > 0:
            embed["fields"].append({
                "name": "Commands",
                "value": "\n".join([
                    "**{p}{c.usage:\u2002<15}** {c.brief}".format(p=prefix, c=sub_cmd)
                    for sub_cmd in cmd.commands
                ])
            })

        await ctx.send(embed=embed)
