# 


class AbstractEvent:

	def __init__(self, name, code):
		self.name = name
		self.code = code


class Command(AbstractEvent):
	pass


class Event(AbstractEvent):
	pass


class State:

	def __init__(self, name):
		self.name = name
		self.actions = []
		self.transitions = {}

	def add_transition(self, event, target_state):
		assert target_state
		self.transitions[event.code] = Transition(self, event, target_state)

	def get_all_targets(self):
		result = []
		for key in self.transitions:
			result.append(self.transitions[key].target)
		return result


class Transition:

	def __init__(self, source, trigger, target):
		self.source = source
		self.trigger = trigger
		self.target = target

	def get_event_code(self):
		return self.trigger.code


class StateMachine:

	def __init__(self, start):
		self.start = start

	def get_states(self):
		result = []
		self.collect_states(result, self.start)
		return result

	def collect_states(self, result, start):
		if start in result:
			return
		result.append(start)
		for next_ in start.get_all_targets():
			self.collect_states(result, next_)

	def add_reset_events(self, events):
		for e in events:
			self.reset_events.append(e)


if __name__ == '__main__':
	print('Hello')
