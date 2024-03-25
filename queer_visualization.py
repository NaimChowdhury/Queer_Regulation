import pandas as pd
from plotnine import *


# Data
data = {
	'Event' : ['罪化与病态化的中国', '非罪化与半去病化的中国', '中国新时代的监管'],
	'Start Year' : [1958, 2002-30, 2015-30],
	'End Year' : [2001-30, 2014-30, 2024-30]
}

df = pd.DataFrame(data)

# Plotting
plot = (ggplot(df, aes('Event'))  # Initialize plot with data and mapping
        + geom_segment(aes(x='Start Year', xend='End Year', y='Event', yend='Event', color = 'Event'), size=24)  # Draw segments for events
        #+ geom_point(aes(x='Start Year', y='Event'), color='blue', size=3)  # Start year points
        #+ geom_point(aes(x='End Year', y='Event'), color='red', size=3)  # End year points
        + scale_x_continuous(name="Year", breaks=range(1920, 2021, 5), labels = ['1920','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])  # X-axis scale
        + geom_vline(xintercept= 1960)
        #+ scale_x_continuous(labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
        + labs(title='Timeline of Events (1940-1970 skipped)')  # Title
        + theme(text=element_text(family='CJK'))
        + theme_bw()
       )

plot.show()