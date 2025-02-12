message_map = {
    "]()]|_]|_]][-]|-|]": "hello",
    "{|^{|{{|_{]3{": "blip",
    "..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..": "die stupid people",
    "'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''": "your brain looks delicious",
    "}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}": "try to find duplicated kata"
}
hello="]()]|_]|_]][-]|-|]"
hel="hello"
blip="{|^{|{{|_{]3{"
bli="blip"
die="..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|).."
di= "diestupidpeople"
brain="'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''"
brai="yourbrainlooksdelicious"
kata="}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}"
kat="trytofindduplicatedkata"
def decode(m):
    result = ""
    for i in range(0,len("hello")):
        hello[i::(len(hello)/len("hello"))]=hel[i]
    for i in range(0,len("blip")):
        blip[i::(len(blip)/len("blip"))]=bli[i]
    for i in range(0,len("diestupidpeople")):
        die[i::(len(die)/len("diestupidpeople"))]=di[i]
    for i in range(0,len("yourbrainlooksdelicious")):
        brain[i::(len(brain)/len("yourbrainlooksdelicious"))]=brai[i]
    for i in range(0,len("trytofindduplicatedkata")):
        kata[i::(len(kata)/len("trytofindduplicatedkata"))]=kat[i]
    for i in range(0,len(m)):
        result+=message_map[m[i]]
    return m

#debugg the code and find the flag

    
