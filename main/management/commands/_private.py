from main.models import Channel, Content
from statistics import mean

# Method to find all children of parent channel
def find_all_child_channels(channel_title):
    query = '''
    WITH RECURSIVE cte_channel AS (
    	SELECT main_channel.*, 0 AS level FROM main_channel where main_channel.title = %s
    	UNION ALL
    	SELECT main_channel.*, cte_channel.level+1 FROM main_channel, cte_channel WHERE main_channel.parent_channel_id = cte_channel.id
    )
    select id, title, parent_channel_id, level from cte_channel;
    '''
    return Channel.objects.raw(query, [channel_title])


# Receive channel, find all child channels, then loop through their contents to calculate an average rating per channel
def calcAvgRatings(chan):
    channelratings = []
    # for each channel, return all it's children (as well as itself)
    childchans = find_all_child_channels(chan.title)

    # now gather ratings for all channels in group
    for ch in childchans:
        # retrieve content for each channel in "channel-group"
        content = Content.objects.filter(channel__exact=ch.id).all()
        for con in content:
            # add ratings to "parent" channel
            channelratings.append(con.rating)

    # now we have a list of ratings for the channel, so calculate the average and return it
    return None if not channelratings else mean(channelratings)
