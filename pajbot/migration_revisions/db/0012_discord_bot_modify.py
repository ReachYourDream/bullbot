import logging

log = logging.getLogger("pajbot")


def up(cursor, bot):
    # new: tier record
    cursor.execute('ALTER TABLE "user" ADD COLUMN tier INTEGER DEFAULT NULL')

    # new: last_pair record
    cursor.execute('ALTER TABLE "user" ADD COLUMN last_pair TIMESTAMPTZ DEFAULT NULL')

    cursor.execute(
        """
    CREATE TABLE user_connections (
        twitch_id INT COLLATE pg_catalog."default" NOT NULL,
        discord_user_id TEXT COLLATE pg_catalog."default",
        steam_id TEXT COLLATE pg_catalog."default",
        disord_username TEXT COLLATE pg_catalog."default",
        CONSTRAINT user_connections_pkey PRIMARY KEY (twitch_id),
        CONSTRAINT user_connections_discord_user_id_key UNIQUE (discord_user_id),
        CONSTRAINT user_connections_steam_id_key UNIQUE (steam_id)
    )
    """
    )
