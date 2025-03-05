import statsbomb as sb

events =  sb.Events(event_id='3943077')
df = events.get_dataframe(event_types=["shot", "pass", "ball recovery", "block", "dribble", "foul committed", "foul won", "injury stoppage", "substitution", "miscontrol", "clearance", "duel", "50/50",  "interception", "bad behaviour"])
 # present in events but problematic: "ball receipt", "goal keeper"
 # missing from events: tactical
 
print(df)


