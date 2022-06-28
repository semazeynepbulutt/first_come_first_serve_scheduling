import pandas as pd
def sort_by_arrival_time(processes):
    processes.sort(key=lambda x: x[1])
    return processes
def create_service_time(processes):
    st = list(map(lambda x: sum(processes[:processes.index(x)][i][2] for i in range(processes.index(x))) if (processes.index(x) - 1 >= 0) else 0, processes))
    p = list(map(lambda x: processes[processes.index(x)]+(st[processes.index(x)],),processes))
    return p
def create_waiting_time(processes):
    wt = list(map(lambda x: processes[processes.index(x)][3]-processes[processes.index(x)][1] if (processes.index(x) - 1 >= 0) else 0, processes))
    p = list(map(lambda x: processes[processes.index(x)] + (wt[processes.index(x)],), processes))
    return p
def create_turn_around_time(processes):
    tat = list(map(lambda x: processes[processes.index(x)][3]+processes[processes.index(x)][2]-processes[processes.index(x)][1] , processes))
    p = list(map(lambda x: processes[processes.index(x)] + (tat[processes.index(x)],), processes))
    df = pd.DataFrame(p,columns=['index of process','arrival time','execution time','service time','waiting time','turn around time'])
    return df
def read_txt(filename):
    queue_fcfs = []
    with open(filename) as f:
        for index,line in enumerate(f.readlines()):
            line = list(map(int, line.replace("\n","").split()))
            line.insert(0,index)
            line = (*line, )
            queue_fcfs.append(line)
    return queue_fcfs
def main():
    data = create_turn_around_time(create_waiting_time(create_service_time(sort_by_arrival_time(read_txt('fcfs_data.txt')))))
    print(data)
if __name__=="__main__":
    main()
