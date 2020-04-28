import evfl
import mmh3
import json
import os
import sys

seen_actors = {}

def collect_names(path):
	ev = evfl.EventFlow()
	ev.read(open(path, 'rb').read())
	for actor in ev.flowchart.actors:
		try:
			ac_dict = seen_actors[str(actor.identifier)]
		except KeyError:
			ac_dict = {'queries': {}, 'actions': {}}
			seen_actors[str(actor.identifier)] = ac_dict
		for query in actor.queries:
			query = str(query)
			ac_dict['queries'][query] = mmh3.hash(query.encode('utf-8')) & 0xFFFFFFFF
		for action in actor.actions:
			action = str(action)
			ac_dict['actions'][action] = mmh3.hash(action.encode('utf-8')) & 0xFFFFFFFF


in_path = sys.argv[1]
for name in os.listdir(in_path):
	if name.endswith('.bfevfl'):
		collect_names(in_path + '/' + name)

with open('eventflow_actor_info.json', 'w') as f:
	json.dump(seen_actors, f, indent=4, sort_keys=True)

