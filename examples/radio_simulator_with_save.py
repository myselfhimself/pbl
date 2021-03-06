from pbl import *

'''
    this cynical radio simulator plays today's top hits with the twist
    that every fourth song is by either katy perry or sia
'''

if __name__ == '__main__':
    gold = Concatenate([ArtistTopTracks('Sia'), ArtistTopTracks('Katy Perry')])
    norm = PlaylistSource("Today's Top Hits")
    radio = Alternate([norm, norm, norm, Shuffler(gold)])
    radio = PlaylistSave(radio, 'cynical radio', 'plamere', max_size=40)
    show_source(radio)
