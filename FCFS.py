class Process:
	def __init__(self, pid, arrival_time, burst_time):
		self.pid = pid
		self.arrival_time = arrival_time
		self.burst_time = burst_time
		self.start_time = None
		self.finish_time = None
		self.response_time = None
		self.waiting_time = 0
		self.turnaround_time = 0

def fcfs(processes):
	processes.sort(key=lambda p: p.arrival_time)
	time = 0
	gantt = []
	for p in processes:
		if time < p.arrival_time:
			time = p.arrival_time
		p.start_time = time
		p.response_time = p.start_time - p.arrival_time
		gantt.append(f"[{p.pid}:{time}–{time + p.burst_time}]")
		time += p.burst_time
		p.finish_time = time
		p.turnaround_time = p.finish_time - p.arrival_time
		p.waiting_time = p.turnaround_time - p.burst_time
	return gantt, processes

def print_metrics(gantt, processes):
	print("Gantt:", "".join(gantt))
	print("Per-process (W / T / R):")
	w_sum = t_sum = r_sum = 0
	for p in processes:
		print(f"{p.pid}: {p.waiting_time} / {p.turnaround_time} / {p.response_time}")
		w_sum += p.waiting_time
		t_sum += p.turnaround_time
		r_sum += p.response_time
	n = len(processes)
	print(f"Averages: Waiting {w_sum/n:.1f}, Turnaround {t_sum/n:.1f}, Response {r_sum/n:.1f}")

if __name__ == "__main__":
	processes = [
		Process("P1", 0, 7),
		Process("P2", 2, 4),
		Process("P3", 4, 1),
		Process("P4", 5, 4),
		Process("P5", 7, 3),
	]
	gantt, procs = fcfs(processes)
	print_metrics(gantt, procs)
