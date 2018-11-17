# w11c33

## Objectives

Objectives for class today are to help you install your application on our Linux server, and some of the basic concepts and commands related to doing this.


## Basic "deamon"ing

To start your server as a background process that will be disassociated with the terminal you started it from (will not be killed when the terminal is killed)
```
$ nohup <<command>> &
```

This command does two things: 1) the & character tells Linux that you want this to be started as a background process, 2) The nohup says that you want the process to ignore kill signal 1 (NOHUP). Every process in Linux can send or receive kill signals. Signals are a limited/basic form of inter-process communication that is used in all Unix, and Unix-like operating systems (e.g. Linux).

When starting a program, We can indicate that we want certain signals to be ignored for that process. By nohup, we indicate that our new process should ignore any nohup signals. nohup signals are sent to all child processes of a terminal when you close the terminal. Under normal circumstances, this means that each program that you start within your terminal session will be automatically stopped (aka killed) for you (behavior that you would naturally expect). But, there are occasions where we want to override the default behavior - such is the case with our ChatBot code.

By disassociating our ChatBot program from the terminal (nohup) and sending it to the background - we've created what in Unix lingo is called "daemon process" (that is a background process that usually acts as some sort of server for other processes on the same machine, or processes on other machines).

## "Killing" processes

There are a number of signals that we can use to terminate a process that has be "daemonized"

```
Signal     Value     Action   Comment
──────────────────────────────────────────────────────────────────────
SIGHUP        1       Term    Hangup detected on controlling terminal
                              or death of controlling process
SIGINT        2       Term    Interrupt from keyboard
SIGQUIT       3       Core    Quit from keyboard
SIGILL        4       Core    Illegal Instruction
SIGABRT       6       Core    Abort signal from abort(3)
SIGFPE        8       Core    Floating point exception
SIGKILL       9       Term    Kill signal
SIGSEGV      11       Core    Invalid memory reference
SIGPIPE      13       Term    Broken pipe: write to pipe with no
                              readers
SIGALRM      14       Term    Timer signal from alarm(2)
SIGTERM      15       Term    Termination signal
SIGUSR1   30,10,16    Term    User-defined signal 1
SIGUSR2   31,12,17    Term    User-defined signal 2
SIGCHLD   20,17,18    Ign     Child stopped or terminated
SIGCONT   19,18,25    Cont    Continue if stopped
SIGSTOP   17,19,23    Stop    Stop process
SIGTSTP   18,20,24    Stop    Stop typed at terminal
SIGTTIN   21,21,26    Stop    Terminal input for background process
SIGTTOU   22,22,27    Stop    Terminal output for background process
```

To see a list of signals that we can send using kill command
```
kill -l
```

```
tim@mis407:~$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

To send a process a signal, we must first find the PID (process ID):
```
$ ps

  PID TTY          TIME CMD
24106 pts/0    00:00:00 bash
24530 pts/0    00:00:00 python3
24533 pts/0    00:00:00 ps

```

Then we send the signal

```
$ kill -SIGINT 24530
```

NOTE: We can also use the number instead of the word associated with it...
```
$ kill -2 24530
```

The three kill signals you should  know :  2, 9 and 15 (SIGINT, SIGKILL, SIGTERM). The most "gentle" way to terminate a process is by sending the SIGINT signal. The most aggressive way to terminate is to send SIGKILL. So, if you're attempting to kill a process, start with SIGINT, then SIGTERM, and if it still won't "die" then use SIGKILL (even the worst hung processes will still terminate under a SIGKILL signal)

### Redirecting output

Now, often, even when we start our program as a "deamon", we may still be expecting a terminal to write output (eg print statements). Also, system errors may also be attempted to be displayed to the terminal. In either case, since there is (or may not be) a terminal to display to (or we don't want the deamon writing annoying messages to our screen while we are doing other word), we should include information on where to "redirect" this output.

```
./test.py > test_std.out 2> test_std.err &
```

NOTE: In Linux (and Unix OS's such as mac) we can set our py files to be directly executable.

```
#!/usr/bin/env python3
```

Then we change the attributes of the file to be executable

```
$ chmod 770  test.py
```

NOTE: If we SIGKILL or SIGTERM a process, any output that still resides in a buffer and that has not yet been written to disk will be lost. The best way to terminate a process is with SIGINT. This will allow for the most graceful exit for the process, and allow any keys to be flushed before the program is terminated.

### Crontab

Linux (and all Unix's that I've come across) have a built in job scheduler called cron. Cron reads a file called a crontab that provides instructions on when to start and run certain jobs.

To view, and edit "cron jobs", we edit the crontab file.  This can be done using the following command.

```
$ crontab -e
```

NOTE: The header for this file provides all the instructions you'll need to set up your "cron job"

## Methods to create a Daemon that will be periodically checked and restarted when necessary

One method is to have your programm periodically called from cron. Then, in your program, when it runs the first time, create a lock file that contains it's PID -- a file to indicate that the process is running, and that no more should be run.

Create a __main__ method that reads the lock file to find the PID. If it can't find the file, or a running PID equal to that PID stored in the file -- store the current PID of the program, and let the program run, otherwise let the program finish with running any other code.


### Finding PID's

To find if there any running processes with the PID found in the file...

```
os.kill(pid, 0)
```

To get the PID of the current running program...
```
os.getpid()
```

### "Flushing" output stream

If your program is writing output to the screen (for diagnostics or other reason) and is running as a daemon, to ensure you have you output saved to the file periodically you should "flush" standard output (NOTE: Only with the 'gentlest' of signals will this be flushed (SIGINT)... also, there are times when you might want to be monitoring this output file (e.g. ```$ tail -F std_out.txt```))
```
print("something")
sys.stdout.flush()
```
