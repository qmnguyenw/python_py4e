CPU Scheduling in Operating Systems using priority queue with gantt chart



Prerequisite: CPU Scheduling in Operating Systems  
 **Different Scheduling Algorithms:**

  1.  **First Come First Serve CPU Scheduling:**  
Simplest scheduling algorithm that schedules according to arrival times of
processes. First come first serve scheduling algorithm states that the process
that requests the CPU first is allocated the CPU first. It is implemented by
using the FIFO queue. When a process enters the ready queue, its PCB is linked
onto the tail of the queue. When the CPU is free, it is allocated to the
process at the head of the queue. The running process is then removed from the
queue. FCFS is a non-preemptive scheduling algorithm.

  2.  **Shortest Job First(Preemptive):**  
In Preemptive Shortest Job First Scheduling, jobs are put into the ready queue
as they arrive, but as a process with short burst time arrives, the existing
process is preempted or removed from execution, and the shorter job is
executed first.

  3.  **Shortest Job First(Non-Preemptive):**  
In Non-Preemptive Shortest Job First, a process which has the shortest burst
time is scheduled first. If two processes have the same bust time then FCFS is
used to break the tie.

  4.  **Longest Job First(Preemptive):**  
It is similar to an SJF scheduling algorithm. But, in this scheduling
algorithm, we give priority to the process having the largest burst time
remaining.

  5.  **Longest Job First(Non-Preemptive):**  
It is similar to an SJF scheduling algorithm. But, in this scheduling
algorithm, we give priority to the process having the longest burst time. This
is non-preemptive in nature i.e., when any process starts executing, can’t be
interrupted before complete execution.

  6.  **Round Robin Scheduling:**  
To implement Round Robin scheduling, we keep the ready queue as a FIFO queue
of processes. New processes are added to the tail of the ready queue. The CPU
scheduler picks the first process from the ready queue, sets a timer to
interrupt after 1-time quantum, and dispatches the process. One of two things
will then happen. The process may have a CPU burst of less than 1-time
quantum. In this case, the process itself will release the CPU voluntarily.
The scheduler will then proceed to the next process in the ready queue.
Otherwise, if the CPU burst of the currently running process is longer than
1-time quantum, the timer will go off and will cause an interrupt to the
operating system. A context switch will be executed, and the process will be
put at the tail of the ready queue. The CPU scheduler will then select the
next process in the ready queue.

  7.  **Priority Based(Preemptive) Scheduling:**  
In Preemptive Priority Scheduling, at the time of arrival of a process in the
ready queue, its priority is compared with the priority of the other processes
present in the ready queue as well as with the one which is being executed by
the CPU at that point of time. The One with the highest priority among all the
available processes will be given the CPU next. In this program, we have both
options, whether to consider highest number as highest priority or lowest
number as highest priority.

  8.  **Priority Based(Non-Preemptive) Scheduling:**  
In the Non Preemptive Priority scheduling, The Processes are scheduled
according to the priority number assigned to them. Once the process gets
scheduled, it will run till the completion. Generally, the lower the priority
number, the higher is the priority of the process. The people might get
confused with the priority numbers, hence in the GATE, there clearly mention
which one is the highest priority and which one is the lowest one. In this
program, we have both options, whether to consider highest number as highest
priority or lowest number as highest priority.

  9.  **Highest Response Ratio Next(HRRN) Scheduling:**  
Highest Response Ratio Next (HRRN) is one of the most optimal scheduling
algorithms. This is a non-preemptive algorithm in which, the scheduling is
done on the basis of an extra parameter called Response Ratio. A Response
Ratio is calculated for each of the available jobs and the Job with the
highest response ratio is given priority over the others.

Consider the following table:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200403214436/Screenshot-2820.png)

Below is the implementation of the above algorithms using a priority queue:  

## FCFS

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the FCFS algorithm

#include <cstdlib>

#include <iostream>

#include <queue>

using namespace std;

 

class process {

public:

 pid_t p_no = 0;

 time_t start_AT = 0, AT = 0,

 BT_left = 0, BT = 0, temp_BT = 0,

 CT = 0, TAT = 0, WT = 0, RT = 0;

 int priority = 0;

 

 // Function for completion time

 void set_CT(time_t time)

 {

 CT = time;

 set_TAT();

 set_WT();

 }

 

 // Function for Turn Around Time

 void set_TAT()

 {

 TAT = CT - start_AT;

 }

 

 // Function for Waiting Time

 void set_WT()

 {

 WT = TAT - BT;

 }

 // Function to set starting Arrival Time

 // Because arrival time gets updated

 // when you push process in ready queue again

 // in preemptive algorithms

 void P_set()

 {

 start_AT = AT;

 BT_left = BT;

 }

 // Function to set Response Time

 void set_RT(time_t time)

 {

 RT = time - start_AT;

 }

 

 // Overload operator '<' w.r.t arrival

 // time because arrival time is the

 // first priority even greater than

 // priority of process and priority_queue

 // pops out the greatest value first

 // so we need to replace '<' with '>' inorder

 // to pop out smallest value

 friend bool operator<(const process& a, const process& b)

 {

 return a.AT > b.AT;

 }

};

 

// Function to implement FCFS algorithm

priority_queue<process> FCFS_run(priority_queue<process> ready_queue,

 queue<process>* gantt)

{

 priority_queue<process> completion_queue;

 process p;

 time_t clock = 0;

 

 // Till ready queue is not empty

 while (!ready_queue.empty()) {

 

 // While clock is less than

 // Arrival Time

 while (clock < ready_queue.top().AT) {

 p.temp_BT++;

 clock++;

 }

 if (p.temp_BT > 0) {

 p.p_no = -1;

 p.CT = clock;

 (*gantt).push(p);

 }

 p = ready_queue.top();

 ready_queue.pop();

 p.set_RT(clock);

 while (p.BT_left > 0) {

 p.temp_BT++;

 p.BT_left--;

 clock++;

 }

 p.set_CT(clock);

 

 // Update the Gantt Chart

 (*gantt).push(p);

 p.temp_BT = 0;

 

 // Update the completion time to

 // the queue

 completion_queue.push(p);

 }

 return completion_queue;

}

 

// Set data on the basis of given table

priority_queue<process> set_sample_data()

{

 priority_queue<process> ready_queue;

 process temp;

 temp.AT = 0;

 temp.BT = 4;

 temp.priority = 2;

 temp.p_no = 1;

 temp.P_set();

 ready_queue.push(temp);

 temp.AT = 1;

 temp.BT = 2;

 temp.priority = 4;

 temp.p_no = 2;

 temp.P_set();

 ready_queue.push(temp);

 temp.AT = 2;

 temp.BT = 3;

 temp.priority = 6;

 temp.p_no = 3;

 temp.P_set();

 ready_queue.push(temp);

 temp.AT = 3;

 temp.BT = 5;

 temp.priority = 10;

 temp.p_no = 4;

 temp.P_set();

 ready_queue.push(temp);

 temp.AT = 4;

 temp.BT = 1;

 temp.priority = 8;

 temp.p_no = 5;

 temp.P_set();

 ready_queue.push(temp);

 temp.AT = 5;

 temp.BT = 4;

 temp.priority = 12;

 temp.p_no = 6;

 temp.P_set();

 ready_queue.push(temp);

 temp.AT = 6;

 temp.BT = 6;

 temp.priority = 9;

 temp.p_no = 7;

 temp.P_set();

 ready_queue.push(temp);

 return ready_queue;

}

 

// Function to get total Waiting Time

double get_total_WT(priority_queue<process> processes)

{

 double total = 0;

 while (!processes.empty()) {

 total += processes.top().WT;

 processes.pop();

 }

 return total;

}

 

// Function to get total Turn Around Time

double get_total_TAT(priority_queue<process> processes)

{

 double total = 0;

 while (!processes.empty()) {

 total += processes.top().TAT;

 processes.pop();

 }

 return total;

}

 

// Function to get total Completion Time

double get_total_CT(priority_queue<process> processes)

{

 double total = 0;

 while (!processes.empty()) {

 total += processes.top().CT;

 processes.pop();

 }

 return total;

}

 

// Function to get total Response Time

double get_total_RT(priority_queue<process> processes)

{

 double total = 0;

 while (!processes.empty()) {

 total += processes.top().RT;

 processes.pop();

 }

 return total;

}

 

// Function to display Completion Queue and

// all the time

void disp(priority_queue<process> main_queue, bool high)

{

 int i = 0, temp, size = main_queue.size();

 priority_queue<process> tempq = main_queue;

 double temp1;

 cout << "+-------------+--------------";

 cout << "+------------+-----------------";

 cout << "+-----------------+--------------+---------------+";

 if (high == true)

 cout << "----------+" << endl;

 else

 cout << endl;

 cout << "| Process No. | Arrival Time ";

 cout << "| Burst Time | Completion Time ";

 cout << "| Turnaround Time | Waiting Time | Response Time |";

 if (high == true)

 cout << " Priority |" << endl;

 else

 cout << endl;

 cout << "+-------------+--------------";

 cout << "+------------+-----------------";

 cout << "+-----------------+--------------+---------------+";

 if (high == true)

 cout << "----------+" << endl;

 else

 cout << endl;

 while (!main_queue.empty()) {

 temp = to_string(main_queue.top().p_no).length();

 cout << '|' << string(6 - temp / 2 - temp % 2, ' ')

 << main_queue.top().p_no << string(7 - temp / 2, ' ');

 temp = to_string(main_queue.top().start_AT).length();

 cout << '|' << string(7 - temp / 2 - temp % 2, ' ')

 << main_queue.top().start_AT << string(7 - temp / 2, ' ');

 temp = to_string(main_queue.top().BT).length();

 cout << '|' << string(6 - temp / 2 - temp % 2, ' ')

 << main_queue.top().BT << string(6 - temp / 2, ' ');

 temp = to_string(main_queue.top().CT).length();

 cout << '|' << string(8 - temp / 2 - temp % 2, ' ')

 << main_queue.top().CT << string(9 - temp / 2, ' ');

 temp = to_string(main_queue.top().TAT).length();

 cout << '|' << string(8 - temp / 2 - temp % 2, ' ')

 << main_queue.top().TAT << string(9 - temp / 2, ' ');

 temp = to_string(main_queue.top().WT).length();

 cout << '|' << string(7 - temp / 2 - temp % 2, ' ')

 << main_queue.top().WT << string(7 - temp / 2, ' ');

 temp = to_string(main_queue.top().RT).length();

 cout << '|' << string(7 - temp / 2 - temp % 2, ' ')

 << main_queue.top().RT << string(8 - temp / 2, ' ');

 if (high == true) {

 temp = to_string(main_queue.top().priority).length();

 cout << '|' << string(5 - temp / 2 - temp % 2, ' ')

 << main_queue.top().priority << string(5 - temp / 2, ' ');

 }

 cout << "|\n";

 main_queue.pop();

 }

 cout << "+-------------+--------------";

 cout << "+------------+-----------------";

 cout << "+-----------------+--------------+---------------+";

 if (high == true)

 cout << "----------+";

 cout << endl;

 temp1 = get_total_CT(tempq);

 cout << "\nTotal completion time :- " << temp1

 << endl;

 cout << "Average completion time :- " << temp1 / size

 << endl;

 temp1 = get_total_TAT(tempq);

 cout << "\nTotal turnaround time :- " << temp1

 << endl;

 cout << "Average turnaround time :- " << temp1 / size

 << endl;

 temp1 = get_total_WT(tempq);

 cout << "\nTotal waiting time :- " << temp1

 << endl;

 cout << "Average waiting time :- " << temp1 / size

 << endl;

 temp1 = get_total_RT(tempq);

 cout << "\nTotal response time :- " << temp1

 << endl;

 cout << "Average response time :- " << temp1 / size

 << endl;

}

 

// Function to display Gantt Chart

void disp_gantt_chart(queue<process> gantt)

{

 int temp, prev = 0;

 queue<process> spaces = gantt;

 cout << "\n\nGantt Chart (IS indicates ideal state) :- \n\n+";

 

 // For 1st row of gantt chart

 while (!spaces.empty()) {

 cout << string(to_string(spaces.front().p_no).length()

 + (spaces.front().p_no != -1)

 + 2 * spaces.front().temp_BT,

 '-')

 << "+";

 spaces.pop();

 }

 cout << "\n|";

 spaces = gantt;

 

 // For process no. in 2nd row

 while (!spaces.empty()) {

 cout << string(spaces.front().temp_BT, ' ');

 if (spaces.front().p_no == -1)

 cout << "IS" << string(spaces.front().temp_BT, ' ') << '|';

 else

 cout << "P" << spaces.front().p_no

 << string(spaces.front().temp_BT, ' ') << '|';

 spaces.pop();

 }

 spaces = gantt;

 cout << "\n+";

 

 while (!spaces.empty()) {

 cout << (string(to_string(spaces.front().p_no).length()

 + (spaces.front().p_no != -1)

 + 2 * spaces.front().temp_BT,

 '-'))

 << "+";

 spaces.pop();

 }

 spaces = gantt;

 cout << "\n0";

//For 3rd row of gantt chart

 while (!spaces.empty()) {

 temp = to_string(spaces.front().CT).length();

 cout << (string(to_string(spaces.front().p_no).length()

 + (spaces.front().p_no != -1)

 + 2 * spaces.front().temp_BT - temp / 2 - prev,

 ' '))

 << spaces.front().CT;

 prev = temp / 2 - temp % 2 == 0;

 spaces.pop();

 }

 cout << "\n\n";

}

 

// Driver Code

int main()

{

 // Initialise Ready and Completion Queue

 priority_queue<process> ready_queue;

 priority_queue<process> completion_queue;

 

 // queue for Gantt Chart

 queue<process> gantt;

 ready_queue = set_sample_data();

 

 // Function call for completion data

 completion_queue = FCFS_run(ready_queue, &gantt;);

 

 // Display Completion Queue

 disp(completion_queue, false);

 

 // Display Gantt Chart

 disp_gantt_chart(gantt);

 return 0;

}  
  
---  
  
 __

 __

 **OUTPUT :-**

    
    
    +-------------+--------------+------------+-----------------+-----------------+--------------+---------------+
    | Process No. | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time | Response Time |
    +-------------+--------------+------------+-----------------+-----------------+--------------+---------------+
    |     1       |      0       |     4      |       4         |       4         |      0       |      0        |
    |     2       |      1       |     2      |       6         |       5         |      3       |      3        |
    |     3       |      2       |     3      |       9         |       7         |      4       |      4        |
    |     4       |      3       |     5      |       14        |       11        |      6       |      6        |
    |     5       |      4       |     1      |       15        |       11        |      10      |      10       |
    |     6       |      5       |     4      |       19        |       14        |      10      |      10       |
    |     7       |      6       |     6      |       25        |       19        |      13      |      13       |
    +-------------+--------------+------------+-----------------+-----------------+--------------+---------------+
    
    Total completion time :- 92
    Average completion time :- 13.1429
    
    Total turnaround time :- 71
    Average turnaround time :- 10.1429
    
    Total waiting time :- 46
    Average waiting time :- 6.57143
    
    Total response time :- 46
    Average response time :- 6.57143
    
    
    Gantt Chart (IS indicates ideal state) :- 
    
    +----------+------+--------+------------+----+----------+--------------+
    |    P1    |  P2  |   P3   |     P4     | P5 |    P6    |      P7      |
    +----------+------+--------+------------+----+----------+--------------+
    0          4      6        9           14   15         19             25
    
    
    
    

