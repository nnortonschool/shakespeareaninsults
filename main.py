import random

prompt1 = [""]
prompt2 = []
prompt3 = []

stringf = "artless base-court apple-john bawdy bat-fowling baggage beslubbering beef-witted barnacle bootless beetle-headed bladder churlish boil-brained boar-pig cockered clapper-clawed bugbear clouted clay-brained bum-bailey craven common-kissing canker-blossom currish crook-pated clack-dish dankish dismal-dreaming clotpole dissembling dizzy-eyed coxcomb droning doghearted codpiece errant dread-bolted death-token fawning earth-vexing dewberry fobbing elf-skinned flap-dragon froward fat-kidneyed flax-wench frothy fen-sucked flirt-gill gleeking flap-mouthed foot-licker goatish fly-bitten fustilarian gorbellied folly-fallen giglet impertinent fool-born gudgeon infectious full-gorged haggard jarring guts-griping harpy loggerheaded half-faced hedge-pig lumpish hasty-witted horn-beast mammering hedge-born hugger-mugger mangled hell-hated joithead mewling idle-headed lewdster paunchy ill-breeding lout pribbling ill-nurtured maggot-pie puking knotty-pated malt-worm puny milk-livered mammet qualling motley-minded measle rank onion-eyed minnow reeky plume-plucked miscreant roguish pottle-deep moldwarp ruttish pox-marked mumble-news saucy reeling-ripe nut-hook spleeny rough-hewn pigeon-egg spongy rude-growing pignut surly rump-fed puttock tottering shard-borne pumpion unmuzzled sheep-biting ratsbane vain spur-galled scut venomed swag-bellied skainsmate villainous tardy-gaited strumpet warped tickle-brained varlot wayward toad-spotted vassal weedy unchin-snouted whey-face yeasty weather-bitten wagtail"

cols = []
current = []
count = 0
for word in stringf.split():
    if count >= 3:
        cols.append(current)
        current = []
        count = 1
        current.append(word)
    else:
        current.append(word)
        count += 1
        
#dumb workaround manual stupid stink
cols.append(['yeasty', 'weather-bitten', 'wagtail'])
        
for row in cols:
    prompt1.append(row[0])
    prompt2.append(row[1])
    prompt3.append(row[2])
    
for _ in range(10):
    print('Thou art a {} {} {}'.format(random.choice(prompt1), random.choice(prompt2), random.choice(prompt3)))
