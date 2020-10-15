def song_decoder(song):
    song="WUB"+song+"WUB"
    j=""
    s=""
    for i in song:
        j+=i
        if j=="WUB":
            j=""
        elif j.find("WUB") != -1:
            s+=(j[:j.find("WUB")]+" ")
            j=""
    return s.strip()
