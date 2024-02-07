from events.prof_pick_animative_event import ProfPickAnimativeEvent
from events.pick_animative_event import PickAnimativeEvent
from events.mom_greeting_event import MomGreetingEvent

def handle_prof_event(game, player, npc):
    if len(player.animatives) != 0:
        return
    event = ProfPickAnimativeEvent(game.screen, game, player)
    game.event = event

def handle_mom_event(game, player, npc):
    if len(player.animatives) != 0:
        return
    event = MomGreetingEvent(game.screen, game, player)
    game.event = event

def handle_pick_animative_event(game, player, npc):
    if len(player.animatives) != 0:
        return
    event = PickAnimativeEvent(game.screen, game, player, npc)
    game.event = event

def handle(game, player, npc):
    player.position = player.last_position
    #Decide which npc is being talked too and use that event.
    if npc.name == "prof":
        handle_prof_event(game, player, npc)

    if npc.name.startswith("animative"):
        handle_pick_animative_event(game, player, npc)

    if npc.name == "mom":
        handle_mom_event(game, player, npc)

    pass
